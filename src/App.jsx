import { useEffect, useState } from "react";
import {
  AppConfig,
  UserSession,
  showConnect,
  openContractCall,
} from "@stacks/connect";
import { StacksMocknet } from "@stacks/network";
import { uintCV, principalCV } from "@stacks/transactions";

function App() {
  const [userData1, setUserData1] = useState("");
  const [userData2, setUserData2] = useState("");
  const [bet, setBet] = useState("");

  const appConfig = new AppConfig(["store_write"]);
  const userSession1 = new UserSession({ appConfig });
  const userSession2 = new UserSession({ appConfig });
  const appDetails = {
    name: "Hello Stacks",
    icon: "https://freesvg.org/img/1541103084.png",
  };

  useEffect(() => {
    if (userSession1.isSignInPending()) {
      userSession1.handlePendingSignIn().then((userData) => {
        setUserData1(userData);
      }); 
    } else if (userSession1.isUserSignedIn()) {
      setUserData1(userSession1.loadUserData());
    }

    if (userSession2.isSignInPending()) {
      userSession2.handlePendingSignIn().then((userData) => {
        setUserData2(userData);
      }); 
    } else if (userSession2.isUserSignedIn()) {
      setUserData2(userSession2.loadUserData());
    }
  }, []);

  console.log(userData1);
  console.log(userData2);

  const connectWallet1 = () => {
    showConnect({
      appDetails,
      onFinish: () => {
        if (userSession1.isUserSignedIn()) {
          setUserData1(userSession1.loadUserData());
        }
        //window.location.reload();
      },
      userSession: userSession1,
    });
  };
  
  const connectWallet2 = () => {
    showConnect({
      appDetails,
      onFinish: () => {
        if (userSession2.isUserSignedIn()) {
          setUserData2(userSession2.loadUserData());
        }
        //window.location.reload();
      },
      userSession: userSession2,
    });
  };

  const handleBetChange = (bet) => {
    setBet(bet.target.value);
  };

  const submitTransaction = async (from, to, bet) => {

    const network = new StacksMocknet();

    const options = {
      contractAddress: from,
      contractName: "h_n_t",
      functionName: "safe-transfer",
      functionArgs: [principalCV(from), principalCV(to), uintCV(bet)],
      network,
      appDetails,
      onFinish: ({ txId }) => console.log(txId),
    };

    await openContractCall(options);
  };

  const flipCoin = () => {

    if (!userData1 || !userData2) {
      console.error("Both users must be signed in to flip the coin");
      return;
    }

    console.log("user data:", userData1);

    var r = Math.random();

    console.log(r);
    console.log("Bet: ", bet);

    if (r <= 0.5) {
      submitTransaction(userData1.profile.stxAddress.testnet, userData2.profile.stxAddress.testnet, bet);
    } else {
      submitTransaction(userData2.profile.stxAddress.testnet, userData1.profile.stxAddress.testnet, bet);
    }

  }

  return (
    <div className="flex flex-col justify-center items-center h-screen gap-8">
      {(
        <button
          className="p-4 bg-indigo-500 rounded text-white"
          onClick={connectWallet1}
        >
          Connect Wallet 1
        </button>
      )}
      {(
        <button
          className="p-4 bg-indigo-500 rounded text-white"
          onClick={connectWallet2}
        >
          Connect Wallet 2
        </button>
      )}
      <div className="flex gap-4">
          <input
            className="p-4 border border-indigo-500 rounded"
            placeholder="Bet..."
            onChange={handleBetChange}
            value={bet}
          />
          <button
            className="p-4 bg-indigo-500 rounded text-white"
            onClick={flipCoin}
          >
            Play!
          </button>
        </div>
      {/* ... rest of your component */}
    </div>
  );
}

export default App;
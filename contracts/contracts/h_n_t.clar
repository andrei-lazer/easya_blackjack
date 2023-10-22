(define-public (safe-transfer (from principal) (to principal) (amount uint))
  (ok (stx-transfer? amount tx-sender to))
)

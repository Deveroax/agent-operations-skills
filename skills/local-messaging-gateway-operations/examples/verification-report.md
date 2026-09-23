# Synthetic verification report

**Fictional observations only. No real bridge, credential, account or messaging API was exercised.** Example integration: Cedar Relay and an agent gateway on one host. Identities and correlation labels below are invented.

| Layer | Fictional scenario result | Bounded fictional evidence | Actual pack operational test |
| --- | --- | --- | --- |
| Service/listener | pass | Expected process owns the configured loopback listener | not executed |
| Authenticated API | pass | Status-only authenticated health succeeds | not executed |
| Adapter | pass | Expected adapter reports connected | not executed |
| Callback registration | pass | One expected callback with required event types | not executed |
| Outbound send | pass | Synthetic receipt `send-example-1` | not executed |
| Destination readback | pass | Exact test text in approved conversation | not executed |
| Fresh inbound dispatch | fail | Reply present in source app, no gateway session event | not executed |
| Authorization | incomplete | Intended sender configured; denied/unauthenticated paths not checked | not executed |
| Restart persistence | not executed | Restart not approved in the fictional scope | not executed |

Fictional conclusion: outbound delivery verified in the imagined scenario; two-way integration unproven. Next separately approved diagnostic: compare automatic callback transport with listener receipt and routing evidence, without replaying production content. Do not claim that registration alone proves delivery or that an inbound failure invalidates independent outbound evidence.

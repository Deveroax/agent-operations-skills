# Approval-required transition rules

**Precedence:** `publication-unverified` and confirmed `published` facts override feedback, editing, expiry and reapproval transitions below. An uncertain send is not known to be unpublished. Keep attempt evidence and record feedback/expiry separately; unresolved attempts block any new send of the candidate or a replacement revision. The ordinary draft/review/approval transitions apply only to known-unpublished items with no unresolved attempt.

| Starting state/event | Result | Required evidence |
| --- | --- | --- |
| New draft | draft, then approval-required | Complete identity, source and target; dedupe/freshness review |
| Definite named rejection | rejected | Exact ID/revision and scoped reason |
| Ambiguous feedback on a known-unpublished item with no unresolved attempt | review-required | Record identity uncertainty; invalidate prior approval |
| Feedback, edits, expiry or reapproval during an unresolved send | publication-unverified retained | Preserve attempt evidence; record feedback/expiry separately; no new send, including replacement revisions |
| Clarification resolves review | approval-required or rejected | Exact selection and decision; never infer approval |
| Narrow preference, no content change | Existing disposition retained | Scope recorded; preference alone cannot approve |
| Any edit to an approved item | approval-required | New revision; prior approval invalidated |
| Exact approval of eligible current revision | approved-to-publish | Approver, content revision, target/account and validity interval |
| Expiry or stale source | expired | Reason, time and historical annotation |
| Send attempted without verified readback | publication-unverified | Retain all available attempt evidence; explicitly note missing receipts; no blind resend |
| Reconciliation confirms nonpublication | Applicable review-required, rejected, expired or approval-required disposition | Reliable outcome evidence retained; any retry needs resolved prior-attempt status and valid bounded authorization |
| Exact destination readback | published | Matching content/target and durable URL or receipt |

A timeout, missing receipt or absent result from an incomplete search does not establish nonpublication. If reconciliation remains inconclusive, the hold remains. If it confirms publication, preserve `published` and separately review any proposed correction/follow-up; a new revision or approval cannot erase that fact.

A revoked rejection stays in history as a superseded decision, not a rewritten past. If an item was already published, preserve that fact; uncertain feedback triggers review of any proposed follow-up, not a fiction that the publication never happened. Never delete or edit a live post without separate authorization.

An approval record is not authenticated merely because a file names an approver. A future automated executor must establish trusted approval at its mutation boundary; this pack supplies no executor.

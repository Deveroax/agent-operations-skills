---
name: social-content-candidate-operations
description: "Reconcile draft queues and feedback without accidental publication."
version: "0.1.0"
platforms: ["macos", "linux", "windows"]
---
# Social content candidate operations

## When to use

A draft queue has definite rejection, a narrow preference, or feedback that may refer to the wrong item. Keep candidate identity, disposition and style scope separate.

## When not to use

This is not permission to publish, browse accounts, optimize account strategy or alter global voice rules after one ambiguous correction. It is not an autonomous publishing system.

## Prerequisites

A configured queue root, stable candidate IDs, immutable content revision/digest, target identity, status, expiry, approval record and history. A filesystem or note editor is sufficient; no platform credentials are needed for queue maintenance.

## Safety boundaries

Read-only: inspect candidate, feedback, current summary and dedupe history. Local mutations: change exact candidate state, append historical annotation, repair moved links and update summary, within the authorized queue. Publishing is a separate external mutation requiring exact-item approval; default state is approval-required, never autonomous-ready.

## Workflow

**Publication-state precedence:** `publication-unverified` means a send may already have published, not that the item is unpublished. Keep that state and all attempt evidence until reconciliation establishes the outcome. Record feedback/review disposition, edits and expiry separately; rejection, ambiguity, dedupe, edits, expiry and reapproval cannot clear this hold. Neither this candidate nor a replacement revision may be sent while any prior attempt is unresolved. A timeout, missing receipt or absence from an incomplete search is not proof of nonpublication. If reconciliation confirms publication, preserve `published` and review any correction/follow-up separately. If reliable evidence confirms nonpublication, retain that evidence and return through the applicable feedback/freshness gates; any retry still requires valid bounded authorization.

1. Read the exact candidate ID and revision, target, machine-readable state and current history. If identity is unresolved, hold all plausibly affected items in review rather than selecting by row position.
2. Classify feedback: definite rejection affects only the named candidate; a narrow style preference updates only that preference; global voice changes require explicit generalization or confirmed repeated evidence, not extrapolation.
3. For mistaken selection or ambiguity, invalidate any approval and record a `review-required` feedback disposition. Set the main state to `review-required` only for a known-unpublished item with no unresolved send; otherwise preserve its publication state. Annotate the previous decision as superseded without erasing its history. Restore the item to review if archived. This is not an approval or definitive rejection.
4. Dedupe exact content and target IDs, then review semantic/topic overlap against active, rejected and published history. Record expiry with a reason; set `expired` only when no unresolved send or published fact takes precedence, and retain the audit trail. Dedupe never revives rejected or uncertain candidates.
5. Apply only supported state changes using the [transition rules](references/approval-state.md). Repair current links and recompute counts from actual states, not prose. Verify each item exists once.
6. After clarification and resolution of all prior send attempts, move a known-unpublished eligible revision only to `approval-required`. Exact approval binds content revision, target/account, timing/expiry and approver. Editing any bound field invalidates approval.
7. If publication is separately authorized later, recheck resolved prior-attempt status, approval, expiry and duplicates immediately before sending, including for replacement revisions. An uncertain send becomes `publication-unverified`; reconcile before retry. Only exact destination readback plus durable URL/receipt permits `published`.

## Verification checklist

- [ ] Identity and revision match feedback; uncertainty retains a review-required feedback disposition without overriding publication state.
- [ ] Unresolved sends retain publication-unverified and attempt evidence across edits, expiry and reapproval; no candidate or replacement retry bypasses reconciliation.
- [ ] No narrow correction was expanded into a global ban.
- [ ] Rejected, expired and uncertain items cannot enter approved-to-publish.
- [ ] Every move leaves one canonical item and valid current links.
- [ ] Summary counts agree with machine-readable states; history remains annotated.
- [ ] Exact-item approval is fresh and invalidated on content/target edits.
- [ ] No platform action is implied by local queue maintenance.

## Synthetic worked example

[Feedback cases](examples/feedback-cases.md) covers rejection, narrow preference, mistaken selection and ambiguous feedback after an uncertain send. It is illustrative, not an executed state machine.

## Known limitations

These rules are human/agent procedures, not enforcement code. Semantic dedupe and ambiguous language require review. The validator checks documents, not queue transitions or publication authorization. See [attribution](../../ATTRIBUTION.md) and the [MIT License](../../LICENSE).

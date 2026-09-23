# Synthetic feedback cases

**All candidates and feedback below are fictional. Illustrative only; no posts, queue mutations or platform calls were executed.** Publisher: `@example_editor`. Default: approval-required.

| Candidate | Initial state | Fictional feedback | Expected current state and scope |
| --- | --- | --- | --- |
| draft-a, revision 1 | approval-required | “Reject draft-a; it sounds unlike me.” | rejected; annotate that revision only; no global voice rewrite |
| draft-b, revision 1 | approval-required | “I rarely use exclamation marks.” | approval-required; record an uncommon punctuation preference, not a ban on enthusiasm or short sentences |
| draft-c, revision 2 | rejected | “I may have selected the wrong draft.” | review-required; restore to review, invalidate any approval, preserve the earlier rejection as superseded |

The current fictional queue has one rejected, one approval-required and one review-required item; none is publishable. If another item may have been intended in the last case, hold it too until identity is resolved.

After clarification, draft-c can return to approval-required, not directly to approved-to-publish. Expiry moves it to expired even if its writing improves. A duplicate is linked to the retained canonical item without erasing its own historical decisions. Publication requires a later exact revision/target approval and destination readback; this example supplies neither.

## Fictional uncertain-send case

Separately, draft-d revision 1 times out during a send; no receipt returns. Its state stays `publication-unverified`, with the attempt and missing receipt recorded. The editor says “I may have selected the wrong draft,” then proposes revision 2. Record `review-required` feedback separately and invalidate approval; do not clear the unresolved-send hold. Expiry or a new approval cannot make revision 1 or 2 eligible to send. An incomplete destination search finding nothing does not resolve the attempt. If reliable reconciliation confirms publication, preserve `published` and separately review revision 2 as a proposed correction/follow-up. If it confirms nonpublication, retain the evidence and require resolved feedback, freshness and valid bounded retry authorization. Otherwise keep the hold. This is an illustrative rule, not an executed queue test.


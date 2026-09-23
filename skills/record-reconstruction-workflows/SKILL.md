---
name: record-reconstruction-workflows
description: "Reconstruct project history while separating recorded decisions, present observations and inference."
version: "0.1.0"
platforms: ["macos", "linux", "windows"]
---

# Record reconstruction workflows

Covered by the [MIT License](../../LICENSE); see [attribution](../../ATTRIBUTION.md).

## When to use

Answer: **What happened, what evidence supports it, and what is true now?** Use when notes, conversation exports, repositories and current systems disagree or leave gaps.

## When not to use

Not for recovering vanished bytes, unrestricted conversation mining, changing governance records, or deciding what to publish. For that last question use [portfolio auditing](../developer-portfolio-auditing/SKILL.md).

## Prerequisites

Agree on the project, allowed roots/systems, time range, read-only access and discovery budget. A file reader, text search and optionally read-only repository/system tools suffice; no agent-specific session API is required. Keep private evidence and source locators in the authorized private report.

## Safety boundaries

Do not mutate sources, lift pauses, contact customers or interpret implementation as authorization. Do not read credential stores or unrelated conversations. Copy exact permitted evidence locators, not private payloads, into the report. Public derivatives need a separate sanitization pass. Stop at the agreed search bound and label inaccessible evidence.

## Workflow

1. Inventory permitted notes, conversation exports, repository states and systems. Read the project anchor and decision log before expanding discovery. Search exact names, dates and IDs, then only authorized related terms. Read surrounding context; search snippets are leads, not conclusions.
2. Recover earliest relevant intent and latest relevant decisions separately. Deduplicate copied messages and continuations using source IDs and unique content. A limited result set cannot establish that no later decision exists.
3. Use a **claim-specific hierarchy**: explicit dated decisions support historical authorization; durable project records support the recorded plan; contemporaneous conversations clarify intent; direct current reads support current implementation state. Later recollections and inferred links are weaker evidence. A current repository does not supersede a pause decision. Preserve conflicting sources and explain which claim each can support.
4. Build the [event ledger](references/evidence-ledger.md). Label **Recorded fact**, **Current observation**, **Inference**, or **Durable-record gap**. Store event date separately from observation date, precise source location and evidence cutoff. An observation of a file is not proof that its assertions are true.
5. Resolve aliases only with explicit identity evidence. Keep similar names as a possible relationship when continuity is unproven. Distinguish umbrella ideas, delivery variants and components from independently evidenced projects; retain retired items in history rather than active totals.
6. Inspect present state read-only where permitted. Distinguish working files, committed code, remote state, deployment and actual use. State exactly which layer was inspected. Recheck volatile sources near the cutoff or mark them stale/unavailable.
7. Synthesize chronology, current technical state, last evidenced authorization and record gaps separately. A built artifact is internal implementation evidence, not customer validation, payment or demand. Scope absence claims to the inspected corpus. Recommend reconciliation without performing it.

## Verification checklist

- Every material claim has an exact source locator and evidence label.
- Decision date and observation cutoff are distinct; contradictory evidence is retained.
- Alias merges are supported, and uncertain continuity remains inference.
- Implementation, permission and customer evidence are reported separately.
- Search bounds, unread sources and inaccessible present-state layers are disclosed.
- No record was rewritten and no paused work was reactivated.

## Synthetic worked example

[Lantern project reconstruction](examples/lantern-history.md) contains fictional records, a sample ledger and a synthesis preserving an active note, later pause and subsequent implementation.

## Known limitations

This is a documentation workflow, not executable state enforcement or an exhaustive archive search. Platform labels describe intended document use, not tested runtime compatibility. Source dates, identities and completeness may themselves be disputed. No live research, deployment or agent loading is demonstrated by the example.

# Evidence ledger and synthesis template

Covered by the [MIT License](../../../LICENSE); see [attribution](../../../ATTRIBUTION.md).

Use one row per supported event or observation. Do not merge contradictory rows.

| Event date | Observed at | Claim | Label | Exact locator | Scope / limits |
|---|---|---|---|---|---|
| Recorded date or unknown | Read cutoff | Narrow statement | Recorded fact / Current observation / Inference / Durable-record gap | File plus section/lines, message ID, or repository revision plus file | Unread, conflicting or inaccessible evidence |

A historical decision can remain authoritative for permission while a current read establishes later implementation. Prefer an explicit decision over an inferred change of direction. If decisions conflict and authority is unresolved, report both; do not choose by recency alone.

For a mutable file, record a version or content identity when available. For a conversation, preserve the retrieval system's exact locator and resolve it before citing; do not fabricate links. Tool-neutral exports with stable message IDs are sufficient. Never describe a saved historical receipt as a fresh execution.

## Compact final report

- Scope, permitted corpus, searches, exclusions and cutoff.
- Chronology with the evidence ledger.
- Current state by layer: working tree, commit, remote, deployment, use.
- Last evidenced authorization, separately from technical state.
- Alias register: names, identity evidence, merge or unresolved relation.
- Customer evidence, or a bounded statement that none was inspected.
- Inferences and durable-record gaps, including conflicting sources.
- Remaining questions and read-only reconciliation recommendations.

Keep this private when locators or facts identify private work. Publishing the report is a different authorization.

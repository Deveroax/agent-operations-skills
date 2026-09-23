# Synthetic worked example: Lantern

**Every record, date, identifier and observation below is fictional and synthetic.** These are authored teaching fixtures, not real files, tool receipts, repository checks or customer evidence. The identifiers below locate records within this document only.

## Synthetic source records

### N1 — project note, 2025-02-03

Record ID: N1; section: Status. Project ID: lantern-01. Name: Lantern. Status: active. Goal: build an offline note index. The note calls “Lamp index” an earlier name for the same project.

### D1 — decision log, 2025-02-18

Record ID: D1; section: Decision. Project ID: lantern-01. The fictional project owner pauses Lantern pending a privacy review. No restart authorization is recorded here.

### R1 — repository observation, 2025-03-06

Record ID: R1; section: Observed tree. A synthetic read-only repository inspection at the fictional cutoff 2025-03-06T10:00:00Z observes a README identifying lantern-01, an indexer implementation, and a recorded implementation change dated 2025-03-01. This fixture says nothing about test success, deployment or customer use. The inspected project note still contains N1's active status. The permitted corpus is exactly N1, D1 and R1; no other decisions or systems were inspected.

## Sample event ledger — synthetic

| Event date | Observed at | Claim | Label | Exact evidence | Limit |
|---|---|---|---|---|---|
| 2025-02-03 | Synthetic cutoff above | Note described Lantern as active | Recorded fact | [N1, Status](#n1--project-note-2025-02-03) | Historical assertion, not current authorization |
| 2025-02-18 | Synthetic cutoff above | Owner paused lantern-01 pending privacy review | Recorded fact | [D1, Decision](#d1--decision-log-2025-02-18) | Latest decision in this bounded corpus |
| 2025-03-01 | 2025-03-06T10:00:00Z | Repository records later implementation work | Current observation | [R1, Observed tree](#r1--repository-observation-2025-03-06) | Synthetic observation of repository evidence, not a restart decision |
| Unknown update date | 2025-03-06T10:00:00Z | Project note still says active despite D1 | Durable-record gap | N1 + D1 + R1 above | Does not establish whether other records were updated |

## Final synthesis — synthetic

**Recorded facts:** N1 described active work; D1 later paused it. **Current observation (synthetic):** R1 shows subsequent implementation and an unchanged active note. Preserve all three facts: the technical state advanced after the pause, while the last evidenced authorization remains paused. No renewed authorization was found in the three-record corpus; this is not a claim that none exists elsewhere.

**Identity:** N1 explicitly identifies Lamp index as an earlier name, and R1 identifies the same project ID. Count one project with an alias, not two opportunities. Similar names alone would not justify this merge.

**Inference:** the later work may have been exploratory preparation; its purpose and permission are unknown. Do not conclude that it violated the pause or that it lifted the pause.

**Durable-record gap:** the active note was not reconciled with D1 at the fictional cutoff. Recommend asking the owner to reconcile the record; do not edit the note or activate tasks during reconstruction.

**Validation boundary:** code exists in this fixture. Test success, remote parity, deployment, actual use, customer demand and paid commitment are not evidenced. No live checks occurred.

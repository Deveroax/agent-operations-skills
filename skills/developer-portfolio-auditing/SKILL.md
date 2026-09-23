---
name: developer-portfolio-auditing
description: "Find reusable public components in private work without conflating value, provenance and release readiness."
version: "0.1.0"
platforms: ["macos", "linux", "windows"]
---

# Developer portfolio auditing

Covered by the [MIT License](../../LICENSE); see [attribution](../../ATTRIBUTION.md).

## When to use

Answer: **What can we responsibly extract and share?** Use for a bounded inventory of utilities, workflows, tests and lessons inside authorized private repositories or skill collections.

## When not to use

Not permission to open a private workspace, publish, inspect secrets or make legal determinations. For disputed chronology or project identity, use [record reconstruction](../record-reconstruction-workflows/SKILL.md) rather than guessing history here.

## Prerequisites

Agree on allowed roots, exclusions, discovery depth, read-only scope and report destination. Use file inventory, source readers and available project-native tests. Keep findings private by default. Do not install tools or execute unfamiliar project code without permission.

## Safety boundaries

Discovery does not authorize extraction; extraction does not authorize publication. Keep unrelated files, source history, customer records, logs and credentials out of the edition. Report sensitive categories rather than matched values. Local installation, agent metadata and personalization do not establish ownership or redistribution authority. Rewording source material does not clear rights.

## Workflow

1. Inventory only approved roots. Prune dependency, cache, archive and generated trees unless explicitly in scope. Distinguish local work, upstream checkouts, forks, worktrees and non-repository projects. Deduplicate worktrees and active/archived skill copies. State coverage instead of claiming an unbounded “all.”
2. Identify a narrow reusable component and its audience. Tie value to an actual inspected receipt, or label it unverified. Track **public value** separately from **publication readiness**; useful work can still be unready.
3. Record exact consulted files and evidence for locally authored work, upstream dependencies, adaptations and unresolved origin. Read notices and explicit import leads first. Use bounded follow-ups, not an exhaustive hunt. Metadata is a declaration, not a recovered creation history. Do not invent an upstream owner because provenance is incomplete.
4. Fill the [inventory template](references/inventory-template.md). For upstream work, credit its authors and recommend a contribution or clearly identified adaptation rather than an originality claim. Preserve applicable notices. Withhold unresolved components independently; do not block unrelated candidates with established evidence.
5. If extraction is authorized, build a narrow clean edition without inherited private history. Select files explicitly; generalize identifiers and configuration, replace production examples with clearly synthetic fixtures, and preserve source-dependent attribution. Confirm rights and intended license before assigning a grant. Otherwise retain a local review draft with a precise missing-decision note.
6. Inspect both content and filenames, including parent and diagnostic paths. Check credential shapes, personal paths, account/customer identifiers, private links, runtime data and metadata. Keep private marker dictionaries outside the edition. Redact unsafe diagnostics at the shared result boundary so CLI and structured callers cannot leak paths; preserve useful safe relative names. Generate adverse fixtures only in automatically cleaned temporary storage.
7. Exercise permitted tests against the extracted artifact, check referenced files and review examples manually. Record exact commands, outcomes, file membership and hashes privately. A heuristic scan is limited evidence, not certification; before release, inspect the proposed history, metadata and assets with suitable scanning plus manual review.
8. Hand off eligible components, exclusions, notices, uncertainties and the exact proposed release scope for approval. Repository creation, pushes, visibility changes and social posting require separate explicit authorization. Local completion is not independent review or publication.

## Verification checklist

- Roots, exclusions, consulted files and evidence coverage are recorded.
- Value, readiness, provenance and evidence quality remain separate.
- Upstream/adapted work has accurate credit; uncertainty is component-specific.
- Synthetic fixtures replace private data; filenames and diagnostic paths were checked.
- Tests were actually run where authorized; failures and unexecuted checks remain visible.
- No blanket rights claim covers unresolved additions; publication remains permissioned.

## Synthetic worked example

[Four-component fictional portfolio](examples/fictional-portfolio.md) demonstrates independent extraction, upstream attribution, sanitization and exclusion decisions without confidence scores.

## Known limitations

This procedure does not certify legal status, secrecy or operational safety. Platform labels describe intended document use, not runtime tests. Commercial analysis is optional: distinguish internal implementation from customer evidence or payment, and avoid treating technical maturity as demand. No monetization framework is required.

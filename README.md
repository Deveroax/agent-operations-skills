# agent-operations-skills

Practical playbooks for agents and their operators: diagnose a service, review a
draft, or verify a messaging bridge without mistaking a successful check for
permission to act. Start with a fictional example, then use the checklist for your
own bounded task. This is a documentation pack, not an automation framework.

## When would I use this?

Your agent appears to be running twice. Before stopping anything, identify which
service is healthy, distinguish observation from a proposed change, and record
what would prove recovery. The [duplicate-service example](skills/macos-service-maintenance/examples/duplicate-service.md)
walks through that decision with fictional evidence; it does not touch your Mac.

| Your task | Start with this fictional example | Boundary to preserve |
| --- | --- | --- |
| Maintain a Mac agent | [Duplicate service](skills/macos-service-maintenance/examples/duplicate-service.md) | Diagnosis is not approval to stop a service |
| Review social drafts | [Feedback cases](skills/social-content-candidate-operations/examples/feedback-cases.md) | A promising draft is not permission to post |
| Verify a message bridge | [Verification report](skills/local-messaging-gateway-operations/examples/verification-report.md) | Outbound delivery is not two-way integration |
| Reconstruct project history | [History example](skills/record-reconstruction-workflows/examples/lantern-history.md) | Recoverable bytes are not authority to restore them |
| Prepare public portfolio work | [Portfolio example](skills/developer-portfolio-auditing/examples/fictional-portfolio.md) | Useful material is not automatically publishable |

## Five-minute start: validate, don't operate

With Python 3.9+ installed, run from the pack root:

```sh
python3 -B scripts/validate_public_pack.py .
python3 -B -m unittest discover -s tests -v
```

These commands validate the documents and exercise the validator with temporary
fixtures. They do not run service maintenance, send messages, or publish drafts.
Then read one example above and its linked procedure. No agent installation is
required for this first pass; runtime compatibility remains untested.

## The five procedures

- [macOS service maintenance](skills/macos-service-maintenance/SKILL.md): diagnose duplicate services and crash loops without stopping the healthy survivor.
- [Social candidate operations](skills/social-content-candidate-operations/SKILL.md): reconcile draft feedback without turning uncertainty into publication permission.
- [Local messaging gateways](skills/local-messaging-gateway-operations/SKILL.md): distinguish delivery from verified two-way integration.

- [Record reconstruction](skills/record-reconstruction-workflows/SKILL.md): recover history without confusing implementation with authorization.
- [Developer portfolio auditing](skills/developer-portfolio-auditing/SKILL.md): identify responsible public extractions.

## Status and rights

All five skills, documentation, synthetic examples, validator and tests, including the additions and integration changes, are covered by the existing [MIT License](LICENSE). See [ATTRIBUTION.md](ATTRIBUTION.md) for maintainer-confirmed local origin and documentation credits.

Deveroax — prepared with Hermes Agent assistance.

## Use and prerequisites

Read each `SKILL.md`, then its linked reference and synthetic example. Set your own maintenance directory, queue root, service labels, bridge endpoint and test destinations; no host-specific configuration is bundled. macOS operations require launchd knowledge and application-native health tools. Queue maintenance needs a filesystem or note editor. Messaging requires the chosen bridge, gateway and separately approved accounts. Validation needs Python 3.9+ with the standard library; no packages are installed.

These are Markdown procedure documents with a small YAML-compatible frontmatter subset. The [Hermes skills documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) documents this directory pattern. This candidate was not installed or load-tested in any agent runtime. It has no automatic discovery, registry or cross-runtime compatibility guarantee. Do not replace existing skills with this candidate.

Read-only diagnosis does not authorize service changes, credential access, account provisioning, publishing, or sending messages. Every operational mutation needs its own bounded approval. Examples are fictional, illustrative records—not live operational results or executable service recipes.

## Local validation

From the pack root:

```sh
python3 -B -m unittest discover -s tests -v
python3 -B scripts/validate_public_pack.py .
```

The [validator](scripts/validate_public_pack.py) checks the five intended skill identities, required metadata and sections, a nonempty root LICENSE, local Markdown links and literal backtick file references, plus heuristic path/credential patterns. It accepts an optional `--markers-file` pointing to a private JSON array of forbidden source identifiers. Keep that file outside this tree. The default run cannot know private source markers. The exact approved maintainer-credit line is exempt only from matching that maintainer name as a private marker in the root README and attribution; the name elsewhere, other markers and all credential patterns remain checked. LICENSE content is scanned normally; license wording is verified separately, not interpreted by this validator. Findings retain ordinary safe relative filenames; paths matching the same sensitive-pattern or private-marker checks are replaced by opaque per-run labels across all categories, including in structured results. No reverse mapping or path hash is emitted. Argument errors are deliberately generic to avoid echoing input values. This remains heuristic redaction, not a guarantee against unrecognized secrets.

The [tests](tests/test_validate_public_pack.py) generate temporary adversarial fixtures and check clean input, broken references, private paths/markers, metadata failures, and credential detection without value disclosure. They exercise documentation tooling only. They do not prove secret-free content, legal clearance, launchd behavior, queue enforcement, secure authentication, message delivery, restart persistence or runtime compatibility. Markdown link checks support this pack's inline/reference links and file references, not every Markdown extension; external URLs are not fetched by the validator. Human privacy and rights review remain required.

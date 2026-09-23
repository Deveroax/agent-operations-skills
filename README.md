# agent-operations-skills — local release candidate

Three focused operating procedures, not an automation framework:

- [macOS service maintenance](skills/macos-service-maintenance/SKILL.md): diagnose duplicate services and crash loops without stopping the healthy survivor.
- [Social candidate operations](skills/social-content-candidate-operations/SKILL.md): reconcile draft feedback without turning uncertainty into publication permission.
- [Local messaging gateways](skills/local-messaging-gateway-operations/SKILL.md): distinguish delivery from verified two-way integration.

## Status and rights

This three-skill pack is licensed under the [MIT License](LICENSE). The maintainer confirms that its workflows and supporting notes were developed locally with Hermes assistance. See [ATTRIBUTION.md](ATTRIBUTION.md) for attribution and documentation credits.

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

The [validator](scripts/validate_public_pack.py) checks the three skill identities, required metadata and sections, a nonempty root LICENSE, local Markdown links and literal backtick file references, plus heuristic path/credential patterns. It accepts an optional `--markers-file` pointing to a private JSON array of forbidden source identifiers. Keep that file outside this tree. The default run cannot know private source markers. The exact approved maintainer-credit line is exempt only from matching that maintainer name as a private marker in the root README and attribution; the name elsewhere, other markers and all credential patterns remain checked. LICENSE content is scanned normally; license wording is verified separately, not interpreted by this validator. Findings retain ordinary safe relative filenames; paths matching the same sensitive-pattern or private-marker checks are replaced by opaque per-run labels across all categories, including in structured results. No reverse mapping or path hash is emitted. Argument errors are deliberately generic to avoid echoing input values. This remains heuristic redaction, not a guarantee against unrecognized secrets.

The [tests](tests/test_validate_public_pack.py) generate temporary adversarial fixtures and check clean input, broken references, private paths/markers, metadata failures, and credential detection without value disclosure. They exercise documentation tooling only. They do not prove secret-free content, legal clearance, launchd behavior, queue enforcement, secure authentication, message delivery, restart persistence or runtime compatibility. Markdown link checks support this pack's inline/reference links and file references, not every Markdown extension; external URLs are not fetched by the validator. Human privacy and rights review remain required.

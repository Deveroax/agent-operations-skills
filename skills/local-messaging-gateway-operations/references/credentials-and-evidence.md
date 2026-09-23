# Credential handling and evidence boundaries

The current [Hermes BlueBubbles documentation](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/bluebubbles) documents the local `hermes gateway setup` wizard and environment-backed credentials. Setup is a mutation, not a diagnostic. In a separately approved setup, the operator enters the secret locally using the supported wizard or product UI; agents do not collect it in chat or invent a generic vault API. Check that the selected input surface conceals the value before entering it; if secure input is unavailable, stop for a supported manual procedure.

The docs describe credential storage in the profile environment file, not an encrypted secret vault. Protect that store with owner-only access, keep it out of source control and diagnostics, and resolve the active profile through documented configuration rather than assuming a home path. Do not read an existing secret store just to verify setup. No clipboard transfer or disposable secret-file bridge is recommended here.

The documented BlueBubbles callback authenticates through a query parameter because its registration API lacks custom-header support. Therefore an authenticated callback URL is itself a secret. Inspect only credential-free endpoint components, subscription names and counts. Do not use shell command-line URLs containing secrets or dump HTTP client exceptions/logs. A provider accepting bearer headers elsewhere does not imply this callback does. If no reviewed secret-safe diagnostic is available, mark authenticated checks not executed rather than improvising.

A configured explicit adapter disable can override stored credentials; wizard success alone does not prove enablement. The gateway registers callbacks during connection. Starting it can register callbacks and deliver queued or startup messages, so it is not read-only.

If a credential is exposed, stop affected automation under separate approval, revoke/rotate the value, update approved consumers and verify the replacement without revealing it. Preserve the incident record; log remediation and retention require their own authorization. Never silently erase logs or merely redact a display while leaving an exposed credential active.

For live evidence, retain only bounded status, correlation identifiers safe for the review audience and explicit dispositions. A callback HTTP success does not alone establish session creation, model execution or a delivered reply. A restart receipt does not establish persistence. Do not store real conversations in a public example.

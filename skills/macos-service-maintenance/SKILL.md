---
name: macos-service-maintenance
description: "Diagnose duplicate launchd services and stabilize crash loops."
version: "0.1.0"
platforms: ["macos"]
---
# macOS service maintenance

## When to use

A stale service repeatedly exits while another installation appears healthy, or two services compete for a listener. Use this workflow to establish identity and stabilize only the approved failing service.

## When not to use

Not for deleting installations, migrating databases, provisioning accounts, changing credentials, or repairing privileged launch transports. Defer those to separately reviewed procedures. Unknown ownership is a reason to pause mutation, not guess the survivor.

## Prerequisites

macOS with launchd, authorized read access to the specific job definition, a native application readiness check, and an operator-selected protected maintenance directory. Read the local `launchctl` manual for the installed OS before preparing an exact command. Service commands here are concepts, not tested invocation recipes.

## Safety boundaries

Read-only: bounded inventory, sanitized plist structure, listener/process ownership and readiness observations. Avoid raw arguments, environment dumps and full logs, which may expose credentials.

State-changing: rollback creation, disable/unload, restore/re-enable, restart, permission changes and cleanup. Obtain approval naming the exact label, domain, survivor, rollback plan and change. Administrator authority is a separate boundary. Never bypass an approval guard or blindly retry a timed-out mutation.

## Workflow

1. Inventory both installations before mutation: domain, label, plist, executable, data directory, state, PID, run count, exit status, listeners and bounded log size/mtime. Save observations incrementally; errors and unexecuted checks stay explicit.
2. Identify the intended survivor by executable, data ownership, listener ownership and native readiness, not product name alone. Capture baseline health through each required socket or network route.
3. Distinguish a login-session LaunchAgent (`gui/<uid>/<label>`) from a LaunchDaemon (`system/<label>`). Agents can also use other launchd domains; determine the actual loaded domain rather than deriving it from a filename. See the [domain reference](references/domain-and-rollback.md).
4. Prepare protected rollback material: only reviewed non-secret configuration, original enabled state, owner/mode facts and restoration procedure. A redacted copy is not necessarily restorable; if secrets are needed, retain the protected original and stop for a separate custody decision.
5. After narrow approval and fresh identity checks, persist the disabled override and unload only the failing job in its actual domain. Preserve its plist, data and logs. Record partial execution; a timeout leaves execution unknown until reconciled.
6. Verify the disabled state, absence of the job and attributed process, and survivor readiness. Observe bounded run-count and log-growth stability over a declared interval; static logs alone are not proof.
7. Stop at stabilization. Deletion, log truncation, compression and data migration require a separate cleanup decision.

## Verification checklist

- [ ] Exact failed label/domain and survivor identified before the change.
- [ ] Protected rollback plan/material and baseline health recorded.
- [ ] Approved failing job disabled and unloaded; no attributed process remains.
- [ ] Survivor and dependent readiness checks pass before and after.
- [ ] Observation interval and repeated run-count/log evidence recorded.
- [ ] Partial/unknown execution reconciled before any retry.
- [ ] Data, credentials and unapproved services untouched; cleanup deferred.

## Synthetic worked example

[Duplicate-service worksheet](examples/duplicate-service.md) is illustrative, not a live host test.

## Known limitations

Native health commands and launchd behavior vary by OS/application. PID disappearance or one green health response is insufficient. This procedure does not qualify privileged code, secure service accounts, ACLs, credential ABIs or restart helpers. See [attribution](../../ATTRIBUTION.md) and the [MIT License](../../LICENSE).

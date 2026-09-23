# Domain and rollback decision sheet

| Job type | Typical definition location | Loaded service target | Scope |
| --- | --- | --- | --- |
| Login-session LaunchAgent | `$HOME/Library/LaunchAgents` or `/Library/LaunchAgents` | `gui/<uid>/<label>` | The identified user's GUI session |
| LaunchDaemon | `/Library/LaunchDaemons` | `system/<label>` | System-wide; separate administrator approval |

A plist can exist without being loaded. Other user domains exist; inspect the actual registration. Do not equate a missing GUI session with a failed daemon.

Use an operator-selected private maintenance directory, ordinarily mode 0700, and non-secret files ordinarily mode 0600; directories need traversal permission, so 0600 is not a suitable directory mode. Do not change existing directories or copy secret-bearing plists just to satisfy a checklist. Record original enabled state, configuration identity and ownership as bounded facts. Preserve protected originals where sanitized copies cannot restore functionality.

Rollback itself is a mutation: name the exact previously loaded domain/configuration, restore only the approved job/state, then recheck listener collisions and survivor health. A reviewed rollback plan does not authorize an automatic restore if the current state differs from assumptions. Stop and reconcile unknown partial changes.

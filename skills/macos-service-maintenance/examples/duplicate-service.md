# Synthetic duplicate-service worksheet

**Fictional, illustrative only. No launchd commands were executed.**

Operator Rowan is reviewing `org.example.indexer.legacy` and `org.example.indexer.current` in the same identified GUI domain. Paths are configured as `LEGACY_PLIST`, `CURRENT_PLIST`, `DATA_ROOT` and `MAINTENANCE_DIR`; they are not literal shell commands.

| Stage | Fictional observation | Decision |
| --- | --- | --- |
| Baseline | Legacy run count rises between two observations; current owns the intended listener and passes native readiness. | Select current as survivor after owner confirmation. |
| Approval | Exact legacy label/domain and disable/unload scope approved; cleanup not approved. | Preserve non-secret rollback material privately. |
| Stabilization | Legacy is absent, disabled and has no attributed process. | Do not delete its plist or data. |
| Recheck | Current remains healthy; no legacy respawn or log growth during the chosen observation window. | Mark stabilization complete for this fictional scenario only. |
| Cleanup | Legacy logs remain large. | Defer deletion pending separate approval. |

If readiness failed, preserve the failure and investigate without stopping the survivor or retrying mutations. Actual operational status for this pack: **not executed**.

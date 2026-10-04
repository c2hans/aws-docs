---
name: task-rds-oracle-commondbatasks
description: RDS-for-Oracle Common DBA Tasks hub (~50 child pages) attack-research plan — rdsadmin.* managed-admin packages, DBA-role privesc, host-file/RCE, egress/SSRF, RDS↔S3 confused deputy, audit evasion
metadata:
  type: project
---

Security-questionbuilder plan for the **Oracle CommonDBATasks hub**
(`Appendix.Oracle.CommonDBATasks`) + children, `Oracle.Concepts.ONA.md`,
`oracle-s3-integration.md`, `PermissionsNonMasters.md`. Mirrors the SQL Server analog
[[task-rds-sqlserver-commondbatasks]] in shape.

**Why:** documentation-derived research plan; RDS Oracle is single-tenant per instance → cross-account
IDOR N/A. Live boundaries = **intra-instance DBA→SYS/rdsadmin privesc**, **host filesystem/RCE**,
**outbound egress/SSRF**, **RDS↔S3/KMS confused deputy**, **audit evasion**.

**How to apply:** crown leads, priority order —
1. **F-2 native `CREATE [ANY] DIRECTORY` (Critical):** master holds Oracle DBA role; if native dir-create
   not revoked, bypass `rdsadmin_util.create_directory` allowlist → map any host path. Gates F-1/F-3.
2. **F-1 external-table `PREPROCESSOR` (Critical, host RCE):** External_Tables page; Oracle-native OS-exec;
   RDS gate undocumented → sandbox escape.
3. **G-1 IMDS/control-plane reach from UTL_HTTP/UTL_TCP/DB-link (Critical/HARD-STOP, doc-gap):** no page
   mentions 169.254.169.254 denylist; **live test only**; fleet cred → STOP+disclose.
4. **E-1 `grant_sys_object` no blocklist (Critical):** grant DBMS_SYS_SQL/UTL_FILE/DBMS_SCHEDULER to low-priv
   schema WITH GRANT OPTION; contrast SQL Server's rds_changedbowner blocklist.
5. **E-2 `ALTER PROFILE RDSADMIN … PASSWORD_VERIFY_FUNCTION` (Critical-if-true, HARD-STOP, weakest evidence):**
   capture hidden rdsadmin cleartext pw on next rotation; verify profile fence first.
6. **B-1 RDS→S3 confused deputy (Critical):** `rds.amazonaws.com` trust w/ no documented aws:SourceArn/Account;
   +B-2 console wildcard-all-buckets; +B-3 (C11) RMAN-backup→upload_to_s3 self-exfil chain.
7. **E-3 `create_passthrough_verify_fcn` (High):** arbitrary PL/SQL + cleartext pw on every password change.
8. **A-2 `create_sys_x$_view` (High):** cross-session SGA/X$ leak, WITH GRANT OPTION.
9. **F-3 `rds_file_util.read_text_file` + caller-nameable `dump_directory` (High):** read retained host files;
   AWR/ADRCI write there. **AWR `p_tag` injection REFUTED** (charset [a-zA-Z0-9_.-] enforced).
10. **O-1 `noaudit_all_sys_aud_table` (High):** single-call audit kill-switch; +O-3 `set_no_commit_flag` async
    job = exec-and-erase; +O-2 enable FGR$AUTOPURGE_JOB; traditional-vs-unified/FGA asymmetry; rdsadmin PL/SQL
    calls not documented as CloudTrail-logged.

**Session mgmt (directly analyzed):** `rdsadmin_util.kill(sid,serial,method)` — sid/serial# from V$SESSION are
enumerable, **no documented ownership check** → any-session DoS (A-1).

**Pivot variable that re-ranks half the plan:** is EXECUTE on `RDSADMIN.*` grantable to non-master users?
`PermissionsNonMasters.md` covers SYS objects only, NOT RDSADMIN schema → doc-gap. If yes, scheduler/system-
event/file leads jump a tier (scoped-user → instance-wide).

Master user = **Oracle DBA role, NOT SYSDBA**; hidden identities `rdsadmin`, `SYS`. Null hypotheses: cross-account
IDOR N/A (single-tenant), Lens C session-vending N/A, custom-DNS-as-SQL-SSRF refuted (it's VPC DHCP, ec2:*DhcpOptions).
Unread pages to tighten: `Appendix.Oracle.Options.SSL.md` (DB-link TLS default for G-2). Two HARD-STOP tripwires:
G-1 IMDS cred, E-2 real rdsadmin cred → preserve+disclose. Plan file:
skill-agent_docs.aws.amazon.com_AmazonRDS_latest_UserGuide_Appendix.Oracle.CommonDBATasks.html.md

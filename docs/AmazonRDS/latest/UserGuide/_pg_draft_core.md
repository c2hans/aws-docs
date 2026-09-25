# RDS DB Parameter Groups — Attack Research Plan (CORE DRAFT)

Source of leads: docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html and its child pages (parameter-groups-overview, USER_ParamValuesRef "Specifying DB parameters", USER_WorkingWithParamGroups.{Creating,Associating,Modifying,Resetting,Copying,CreatingCluster}, USER_WorkingWithDBClusterParamGroups), offline mirror /work/aws-docs/docs/AmazonRDS/latest/UserGuide/, RDS API Reference, and RDS service-authorization reference. Cross-referenced with prior RDS notes /work/aws-docs/_rds_sub_creds_params_zeroetl.md and /work/aws-docs/_rds_plan_skeleton.md. **Status: documentation-derived hypotheses only; nothing tested against a live account.**

## 1. Pentest Objectives (boundary-breach goals)
1. Via a parameter value written into the engine's on-host config, set a parameter RDS does not expose / restricts — reaching a config directive that grants file access, native code load, or superuser (→ engine escape toward AWS host, HARD STOP if it reaches fleet identity).
2. Via the server-side parameter **formula/expression/log parser** (`{DBInstanceClassMemory/…}`, `log()`, `IF/GREATEST/LEAST/SUM`, boolean exprs) reach a parser fault, resource issue, or value the evaluator should reject — the evaluator runs on RDS-managed compute.
3. Modify or reset a parameter group so a **security-hardening parameter** (rds.force_ssl, audit logging, password restriction, allowed-extensions allowlist) is silently weakened across **all associated instances**, immediately (dynamic) and without a reboot.
4. Use control-plane param-group actions (Modify/Reset/Associate/Copy) to affect a DB instance/cluster the caller does not own within-account (blast radius) or across account/region (Copy).
5. Confirm no cross-tenant read/enumeration via Describe*Parameters / DescribeEngineDefaultParameters.

## 2. Components, Assets, and Design

**What a parameter group is.** A *DB parameter group* is an account-scoped container of engine configuration values applied to one or more DB instances; a *DB cluster parameter group* applies to Multi-AZ DB clusters (and, for the default, the per-instance DB parameter group is still used). Each **default** group carries "database engine defaults **and Amazon RDS system defaults** based on the engine, compute class, and allocated storage" (parameter-groups-overview.md). Defaults are **not modifiable**; the customer creates a custom group, edits it, then associates it.

**Resource identity.**
- Named by a customer string: 1–255 letters/numbers/hyphens, first char a letter, no trailing hyphen, no `--`. Custom names **cannot contain a period**; default names **can** (`default.mysql8.0`, `default.mysql5.7`) — so the `default.` + `.`-bearing namespace is reserved to RDS-managed defaults (a namespace boundary). (Creating.md / CreatingCluster.md)
- ARN forms `arn:aws:rds:<region>:<acct>:pg:<name>` (DB parameter group) and `:cpg:<name>` (cluster parameter group) (USER_Tagging.ARN.md, prior notes). Account-scoped.
- Group is tied to a **family** (`MySQL8.0`, `mysql8.0`, …) chosen at create; family fixes the valid parameter set/engine version.

**Where parameter values live and execute.** A parameter is `ParameterName=…,ParameterValue=…,ApplyMethod={immediate|pending-reboot}`. Values may be literals, or **formulas/expressions/functions** (see §5 Area P). Static params require a manual reboot to take effect; dynamic params apply **immediately without a reboot**. The console forces `pending-reboot` for static and `immediate` for dynamic; the CLI/API let you choose (with an engine exception: `pending-reboot` on SQL Server dynamic params errors). The resolved value is materialized into the engine's configuration on the **AWS-managed DB host** — i.e., customer-supplied strings/formulas are transformed and written into engine config by RDS automation. That transform is the primary injection seam.

**Blast radius.** "If you update parameters within a DB parameter group, the changes apply to **all DB instances that are associated with that parameter group**." Dynamic changes apply immediately. Associating a new group with an instance happens immediately, but its static/dynamic params take effect only on reboot; later dynamic edits to that group apply immediately. Reset (`reset-db-parameter-group`, optionally `--reset-all-parameters`) reverts values to defaults across all associated instances.

**Trust zones.** Customer control-plane IAM principal → RDS control plane (SigV4). RDS control plane / host automation → engine config file on the AWS-managed host (RDS service account). DB engine process (non-superuser master; hidden `rdsadmin` owns the box) → host OS / IMDS / control-ENI / storage plane (all AWS-owned, the hard-stop line). Parameter groups sit at the **first** seam (customer input → engine config on AWS host) and are the lever that changes what the engine can do at the **second** seam.

```
customer IAM ──SigV4──> RDS control plane ──materialize param value/formula──> engine config file
                                                        (on AWS-managed host, RDS svc acct)      │
                                                                                                  ▼
                                     master user (non-superuser) ──engine features toggled by params──> ??? host OS / IMDS / storage
                                                                                        (HARD STOP if reached)
```

## 3. API / Interface Inventory

| Name | Mutating | Facing | Functionality | Authorized callers | Notes / lead |
|---|---|---|---|---|---|
| CreateDBParameterGroup / CreateDBClusterParameterGroup | yes | external | create custom group in family | IAM `rds:CreateDBParameterGroup` (+ tag-on-create keys?) | name/description are customer strings; family enum |
| ModifyDBParameterGroup / ModifyDBClusterParameterGroup | yes | external | set ParameterName/Value/ApplyMethod | IAM `rds:ModifyDBParameterGroup` | **the value/formula injection + hardening-downgrade surface**; dynamic = immediate, all associated instances |
| ResetDBParameterGroup / ResetDBClusterParameterGroup | yes | external | revert params to default (or all) | IAM `rds:ResetDBParameterGroup` | silently undoes a hardening param across all associated instances |
| CopyDBParameterGroup / CopyDBClusterParameterGroup | yes | external | duplicate a group | IAM `rds:CopyDBParameterGroup` | cross-region/cross-account source? (Lens A/AA) |
| DeleteDBParameterGroup / … | yes | external | delete group | IAM | can't delete a group in use / default |
| ModifyDBInstance / ModifyDBCluster (DBParameterGroupName) | yes | external | associate group with instance/cluster | IAM `rds:ModifyDBInstance` | association immediate; params on reboot; can trigger reboot/failover (availability) |
| DescribeDBParameters / DescribeDBClusterParameters | no | external | list a group's params | IAM Describe* | cross-tenant leak check (likely null) |
| DescribeEngineDefaultParameters / …ClusterParameters | no | external | engine default values | IAM Describe* | shared/global defaults — enumeration only |
| DescribeDBParameterGroups / …Listing | no | external | list groups | IAM | account-scoped |

Undocumented-knob sweep target: does `ModifyDBParameterGroup` accept ApplyMethod / parameter names or values the console never surfaces (e.g. a restricted `rds.*` param settable via API but hidden in console)? Cross-check API/SDK model vs console. (Step 3 discipline.)

## 5 (partial) — Areas I own

### Area P — Server-side parameter formula / expression / log-function parser
Background: `USER_ParamValuesRef.md` ("Specifying DB parameters") defines a real grammar RDS evaluates server-side: brace formulas `{FormulaVariable}`, `{FormulaVariable*Integer/Integer}`; operators `*` and `/` (integer, truncating); variables `AllocatedStorage`, `DBInstanceClassMemory`, `DBInstanceVCPU`, `EndPointPort`, `TrueIfReplica`, `DBInstanceClassHugePagesDefault`; functions `IF`, `GREATEST`, `LEAST`, `SUM` (case-insensitive, ≥1 arg, no empty members); PostgreSQL-only boolean expressions `"expr > expr"` (also `>= => <= =<`); and log expressions `{log(DBInstanceClassMemory/8187281418)*1000}` (log base 2). Variable names are case-sensitive.

Security Concern: this is a customer-controlled expression evaluated by RDS-managed code, per instance, at apply time (variables like `DBInstanceClassMemory` are host-specific → evaluated on/for the host). Parsers that accept nesting, division, and functions are classic fault surfaces.

High-level Test Scenarios (falsifiable):
- **Claim:** the evaluator does not safely handle division by zero / degenerate formulas. **Mechanism:** `/` "Divides the dividend by the divisor" with no documented zero guard; truncation only. **Oracle:** `ParameterValue={DBInstanceClassMemory/0}` (or `{X/ (Y-Y)}` via SUM) → does Modify accept it, and what happens at apply/reboot — validation error (fail-closed, good), instance stuck in a bad apply state, or a control-plane 5xx (fault)? Severity: Med (self-DoS/instance-unavailable); higher only if it perturbs shared automation. **Stop** at first 5xx/host-side error signal; do not iterate.
- **Claim:** nesting / arg-count is unbounded → parser resource issue. **Mechanism:** `SUM/GREATEST/LEAST` take an n-ary comma list; formulas compose. **Oracle:** deeply nested `SUM(SUM(SUM(…)))` or a very long arg list in a ParameterValue → Modify latency/size limit vs accepted-then-faults-at-apply. Severity: Low–Med (single-tenant).
- **Claim:** log/formula overflow. **Mechanism:** `{log(DBInstanceClassMemory/8187281418)*1000}`, integer multiply. **Oracle:** values forcing huge/negative integers (`{AllocatedStorage*<2^31>}`) — truncation/overflow into an out-of-range engine setting silently accepted. Severity: Low.
- Lens mapping: **F** (parser) + **L** (DoS). Not cross-tenant on its face → keep severity honest; escalate only with evidence of shared-automation impact (then HARD STOP toward service plane).

### Area V — Parameter-VALUE → engine-config injection (the sharpest lead)
Background: RDS materializes the customer `ParameterValue` string into the engine's native configuration on the AWS-managed host. The docs constrain the *name* to a known parameter set (family) and *type* (Integer/Boolean/String/…), but a **String** value's content is customer-controlled.

Security Concern: if the value is written into a line-oriented config file (e.g. PostgreSQL `postgresql.conf`, `key = value`) without strict escaping, a value containing a **newline + a second `key = value`** could set a *different* parameter that RDS deliberately withholds (e.g. one enabling native extension load, an untrusted procedural language, a file/log path, or superuser-adjacent behavior). This is the parameter-group analogue of config injection.

High-level Test Scenarios:
- **Claim:** a String parameter value permits injection of a second directive RDS does not expose. **Mechanism:** value type "String" (USER_ParamValuesRef.md); values written to engine config by RDS automation (parameter-groups-overview.md "engine configuration values that are applied to … DB instances"). **Oracle:** set a benign String param to `legit\n<restricted_directive> = <value>` (also try `#` comment breakout, quotes, `\r`), reboot, then from the master user query `SHOW <restricted_directive>` / `current_setting()` (PostgreSQL) or `@@<var>` (MySQL) — if the restricted directive took effect, escaping is broken. Severity: **High–Critical** if the injected directive grants file/native-code/superuser reach (then HARD STOP the moment host/fleet identity is reachable). **Stop** at proof the restricted directive is set; do not exercise the resulting capability against the host.
- Lens mapping: **F** (injection into a downstream config language) → chains into **E/G/T** (whatever the smuggled directive enables). Compose the kill chain: value-injection → load native extension / enable `local_infile`/`UTL_HTTP` → file read or SSRF under engine/host identity.

### Area L — Lifecycle integrity: reset / associate / apply-method as a silent-downgrade + blast-radius surface
Background: Reset reverts params to defaults across **all associated instances**; dynamic edits apply **immediately without reboot**; a shared custom group is edited once and hits every associated instance; associating/modifying can trigger reboot/failover.

Security Concern & Scenarios:
- **Claim:** a principal with only `rds:ResetDBParameterGroup` (or `Modify…`) can neutralize a security control (rds.force_ssl, audit logging, `rds.restrict_password_commands`, `rds.allowed_extensions`) on production DBs it does not administer, immediately and quietly. **Mechanism:** Resetting.md / Modifying.md "changes … applied to **all DB instances that are associated**"; dynamic = immediate. **Oracle:** with a scoped test role holding only the param action, reset/modify a group associated with a second instance and confirm the control dropped on that instance (transport allows non-TLS, audit stops, extension allowlist widens). Severity: **High** if it silences transport/audit on a DB the caller can't otherwise touch (intra-account cross-workload); Medium as a self-inflicted footgun. **Distinguish** AWS-managed-policy over-grant (reportable, Tier 2) from a customer-authored policy (out of scope).
- **Claim:** modifying/associating a group is an availability lever (forces reboot/failover). **Mechanism:** overview "RDS automatically reboots … as part of the startup process"; SQL Server AlwaysOn/Mirroring "a failover is expected." **Oracle:** confirm a param action induces reboot on associated instances. Severity: Med (cross-workload availability), Low (self).
- Lens mapping: **O/U/AA** (control weakening + revoke/reset completeness) + **A** (blast radius / cross-workload within account).

### Copy / cross-account (Lens A/AA) — see IAM subagent; keep as open lead
`CopyDBParameterGroup` source-identifier shape and any cross-account/cross-region reach — deferred to control-plane authz subagent.

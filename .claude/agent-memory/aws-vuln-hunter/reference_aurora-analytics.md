---
name: aurora-analytics
description: Aurora PostgreSQL analytics (embedded DuckDB, foreign tables over S3/Iceberg) — test methods, cluster substrate, and refuted/confirmed boundary results
metadata:
  type: reference
---

Aurora PostgreSQL **analytics**: embedded DuckDB in-process in the PG server reads Iceberg/Parquet from S3/Glue/S3Tables using a cluster-wide IAM role attached via `rds add-role-to-db-cluster --feature-name AuroraAnalytics`. Feature gated to engine versions with `AuroraAnalytics` in `describe_db_engine_versions` SupportedFeatureNames — **17.11 and 18.6** (us-east-1, both test accts). Run 2026-10-08-1.

## Cheap substrate (no bastion)
- Serverless v2 cluster: `create_db_cluster(Engine=aurora-postgresql, EngineVersion=17.11, ManageMasterUserPassword=True, EnableHttpEndpoint=True, ServerlessV2ScalingConfiguration={Min:0.5,Max:2}, DBClusterParameterGroupName=<custom aurora-postgresql17 pg with aurora_analytics.enabled=true>)` + `create_db_instance(DBInstanceClass=db.serverless)`. ~11 min to available. << $1 for ~20 min.
- SQL via **RDS Data API** (`rds-data execute_statement`, resourceArn=cluster ARN, secretArn=managed master secret, database=postgres). Scoped DB-user test: `begin_transaction` → `SET ROLE analyst` → probes → `rollback` (each stmt separate; use a transaction so SET ROLE/DDL persist and roll back clean).
- Need default-VPC S3 **gateway endpoint** (free) on the main route table so the cluster reaches S3. Default VPC present in A (vpc-09fa3e439befb5f32).
- `CREATE EXTENSION aurora_analytics` needs rds_superuser (master user has it). Foreign server `aurora_analytics_server` auto-created.

## Results (all boundary tests REFUTED except H4)
- **H1 PassRole on AddRoleToDBCluster: ENFORCED.** Scoped principal w/o `iam:PassRole` → 403 `AccessDenied ... not authorized to perform: iam:PassRole on resource:<role> because no identity-based policy allows the iam:PassRole action`, and it fires BEFORE the cluster-existence check. Add scoped PassRole (`iam:PassedToService=rds.amazonaws.com`) → reaches `DBClusterNotFoundFault`. PassRole is the sole gate. Not a privesc.
- **H2 engine SSRF: validation COMPLETE, no service-plane egress.** `location`/`region` reject http/file/MRAP/URL-region (`invalid location; must be an S3 path, a Glue ARN, or an S3 Tables ARN`, SQLState 22023). Iceberg `manifest-list` in an attacker-controlled metadata.json: an absolute non-s3 URL is treated as a **relative path under the S3 base** and composition fails (`Could not create full path from Iceberg Path (...) and the relative path (http://169.254.169.254/...)`) — never followed as an outbound fetch. `s3://169.254.169.254/...` is rendered to `169.254.169.254.s3.us-east-1.amazonaws.com` (S3 virtual-host) — SSRF-to-IMDS via s3:// is structurally impossible. Absolute `s3://other-bucket/...` manifest-lists ARE followed but only through the S3 endpoint, bounded by cluster-role IAM (HTTP 403 cross-acct). No hard-stop; no disclosure candidate.
- **H3(a) cross-acct role attach: BLOCKED.** `AddRoleToDBCluster(RoleArn=<acctB role>)` → 403 `AccessDenied: Cross-account pass role is not allowed` (before cluster lookup).
- **H3(b) consent-free cross-acct read: both-sides ENFORCED.** Cluster role GetObject on foreign bucket w/o bucket policy → 403; add bucket policy granting the role → engine SELECT returns rows. Standard S3 cross-acct; boundary held.
- **H4 CONFIRMED misconfiguration / AWS guidance defect (Medium).** `aurora-analytics-prerequisites.md:81` recommends `AmazonS3ReadOnlyAccess`/`AWSGlueConsoleFullAccess` for the cluster-wide role. No per-location IAM check in the DB, so ANY foreign-table-capable DB user (non-superuser, no AWS identity) reads account-wide S3. Demonstrated: scoped `analyst` SELECT'ed real rows from an unrelated same-account bucket. Routing: aws-security guidance hardening, not a service-plane bug.

**Why:** avoids re-provisioning + re-deriving the analytics attack surface; all four live boundaries already refuted.
**How to apply:** reuse the Serverless-v2+DataAPI substrate for any RDS/Aurora data-plane hunt. For new analytics surface, the unexplored low-prio leads are H5 (blue/green `TargetKmsKeyId` cross-acct) and H6 (Lake Formation `GetDataAccess` vending / Glue federated catalog). See [[env-sessions]].

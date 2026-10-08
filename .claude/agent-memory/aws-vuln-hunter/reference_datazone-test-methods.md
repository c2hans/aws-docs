---
name: datazone-test-methods
description: DataZone cheap test substrate (custom blueprint, no CFN), subscription-target account-level-authz CONFIRMED finding, setup gotchas
metadata:
  type: reference
---

Reusable facts for Amazon DataZone (datazone client, us-east-1) hunts.

## Cheap substrate (no CloudFormation / S3 / LakeFormation / EC2)
- `CreateDomain(domainVersion="V1", domainExecutionRole=<role trusting datazone.amazonaws.com w/ AmazonDataZoneDomainExecutionRolePolicy>)` → AVAILABLE instantly.
- **DefaultDataLake env FAILS** with `VALIDATION_FAILED: Invalid S3 path provided null` unless the blueprint regional config supplies an S3 location — skip it.
- **Use the `CustomAwsService` blueprint instead** (`ListEnvironmentBlueprints(managed=True)` → name `CustomAwsService`). `PutEnvironmentBlueprintConfiguration(enabledRegions=['us-east-1'])` (no roles needed). Provisioning is "manual", no userParameters.
- `CreateEnvironment` for custom blueprint needs **environmentBlueprintIdentifier + environmentAccountIdentifier + environmentAccountRegion** (all three, else ValidationException "without a profile"), + an env role in userParameters `[{'name':'environmentRoleArn','value':<arn>}]`. Env comes up status **DISABLED** — that's fine, subscription targets still work.
- `CreateSubscriptionTarget` does **NOT** validate Glue DB existence nor require env ACTIVE — the target object is stored regardless. Good for pure authz tests. Type `GlueSubscriptionTargetType`, config `[{'formName':'GlueSubscriptionTargetConfigForm','content':json.dumps({'databaseName': <any>})}]`, needs `manageAccessRole` (triggers iam:PassRole check) + `applicableAssetTypes=['GlueTableAssetType']`.
- Can't create two targets with the same `databaseName` in one env (Conflict/ValidationException) — vary the db name.
- Teardown order: targets → environment → env-profile → project(skipDeletionCheck=True) → blueprint configs → domain(skipDeletionCheck=True) → glue dbs → IAM roles. delete_domain cascades but explicit order is cleaner. Domain delete is fast.

## CONFIRMED finding — subscription-target APIs are ACCOUNT-level authorized
Doc: `use-your-own-role.md` line 66. `Create/Update/DeleteSubscriptionTarget` ignore DataZone project ownership/contributorship; authorized at account level; **cannot be scoped below `Resource:"*"`**.
- Verified 2026-10-08: a scoped IAM role holding ONLY the 5 `datazone:*SubscriptionTarget`+Get/List actions, **member of no project**, could `List`/`Get`/`Update`(hijack authorizedPrincipals)/`Delete` another project's target in the same domain. Boundary crossed = project↔project (tenant↔tenant in-account). Sink shape WHOLE (write lands on their record) + WHO (owner read from request).
- **CREATE is additionally gated by `iam:PassRole`** on the manageAccessRole (orthogonal IAM control, not a membership check). UPDATE needs no PassRole (body fields optional) → the hijack of an existing victim target needs zero extra privilege.
- **Account↔Account IS enforced**: `authorizedPrincipals` with a foreign-account ARN → `ValidationException: Authorized principal is not in the same account as the environment account`. Finding is strictly intra-account.
- Scoped principal with only the 5 actions is denied `ListEnvironments`/`ListProjects` → must learn victim env/target id from another channel (mild mitigating factor; ids aren't secret).
- Classification: boundary-dependent / intended-behavior-as-AWS-documents + genuine least-privilege design gap. Routing account-operator (no AWS service-plane crossing). Severity Medium.

**Why:** avoids re-deriving the whole DataZone provisioning dance; the custom-blueprint substrate is the cheap path for any future subscription-target / data-source / grant hunt. See [[env-sessions]].
**How to apply:** reuse the CustomAwsService substrate for DataZone authz tests; this subscription-target lead is CONFIRMED+torn-down — do not re-tread, only extend (Redshift DB-role-name + RedshiftDbRoles tag path, and full-fulfilment grant-landing, remain untested).

---
name: width-sweep-0928-facts
description: Live-tested facts for the 2026-09-28 width-sweep leads (DataZone RoleArn/Designation, SSM RAM doc sharing, DataSync shared-subnet, EventBridge ManagedBy) — all crossings INSUFFICIENT/REFUTED
metadata:
  type: project
---

Run vh-run-id=2026-09-28-A (2026-09-29), accounts A 183174222929 / B 289531347876, us-east-1.
Plan: left-right-width-sweep-attack-research-plan.md. No confirmed crossing; no hard-stop.

**SDK-vs-CFN gaps (botocore 1.43.95):** several 2026-09-28-push CFN/doc fields are NOT in the service SDK:
- DataZone `Connection` `IamPropertiesInput.RoleArn` — CFN has it (pattern `\d{12}`, no SourceArn/SourceAccount
  guidance) but `datazone.CreateConnection props.iamProperties` exposes ONLY `glueLineageSyncEnabled`. No live
  confused-deputy assume path via SDK. RoleArn cross-acct-permissive pattern = hardening-gap observation only.
- EventBridge `DescribeEventBus` output has NO `ManagedBy` member; only `default` bus in A and B → no managed-bus
  write-posture surface to test.
- DataZone `CreateProjectMembership.designation` STILL models the closed 5-value enum in SDK; the CFN free-form
  `^[a-zA-Z0-9_-]{1,36}$` loosening is most likely a schema-regen artifact. (enum is client-informational only.)

**DataZone authz is application-layer, not pure IAM:** `iam:SimulatePrincipalPolicy` says research-admin is
ALLOWED datazone:CreateProjectMembership/CreateConnection, but the live service returns 403 AccessDeniedException
("User is not permitted to perform operation") — DataZone enforces its own domain-membership authz on top of IAM.
So DataZone over-grant tests need real domain membership, not just IAM allow. No DataZone domains exist in A or B.

**SSM document sharing (fully live in A/B, docs are free):**
- Legacy `ssm:ModifyDocumentPermission` A→B works; B `get_document` on full ARN returns content (intended, NOT a
  finding). Revocation is COMPLETE: after AccountIdsToRemove, B gets 400 InvalidDocument "does not exist" (IDOR-safe).
- `ssm:Document` IS a RAM-shareable type w/ default managed permission `AWSRAMPermissionSsmDocument` (broad: incl.
  StartAutomationExecution, SendCommand, StartSession, CreateAssociation — but doc-resource-scoped). HOWEVER RAM
  resource association of a Command ssm:Document to foreign acct B **immediately FAILS** (statusMessage null),
  with or without legacy present, with explicit permissionArns — create_resource_share returns ACTIVE shell but
  list_resources is empty, B never gets access. Generalized-RAM-doc-sharing crossing NOT reproducible here.
  (public-sharing setting = Enable both accts; org unreadable as research-admin so couldn't confirm in/out-of-org.)
- JITNA auto-DENY fail-open untested (needs managed nodes + JITNA config; none present).

**DataSync CreateAgent:** subnetArns/securityGroupArns regex admits any `[0-9]{12}` account (config-plane accepts
cross-acct ARNs, consistent w/ documented shared-subnet support); real ownership check is past ActivationKey
validation which needs a live agent appliance (compute). Interception is inherent VPC-sharing → out of plan scope.

**Residual not-mine in A:** pre-existing SSM doc `vh-run` + RAM share `vh-backupap-lag-share` (tag
vh-backupap-20260814) from an August run — leftover, operator cleanup.

Result file: /work/aws-docs/findings/result-datazone-ssm-2026-09-28-A.md

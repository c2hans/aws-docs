---
name: crosstenant-p3p4p5-facts
description: Observed live cross-tenant isolation behavior for Connect Customer Profiles, GuardDuty/RAM/LakeFormation, EC2 AMI-snapshot/IPAM-token/StackSets (run 2026-09-10-1, all REFUTED)
metadata:
  type: project
---

Run 2026-09-10-1 executed `/work/cross-tenant-research-plan.md` P3/P4/P5 (fresh; P1/P2 already covered — see [[agent-registry-service-facts]]). Accounts A=183174222929, B=289531347876. **All P3/P4/P5 hypotheses REFUTED — no findings.** Controls that HELD (don't re-report without new evidence):

## P3 Amazon Connect Customer Profiles (REFUTED)
- **DomainName is a per-account namespace.** A naming B's domain on GetDomain/SearchProfiles/BatchPutProfileObject/GetProfileRecommendations/ListProfileObjectTypes => 404 ResourceNotFoundException, msg literally "DomainName X is not found in account 183174222929". Request resolves in caller's account; never reaches B's data. [OWNER-FROM-REQ]/[WRITE-LANDS]/[SECOND-KEY] all dead — domain check fires before ProfileId check.
- **CreateEventStream** Uri must be same region+account => 400 "must belong to same region and account" (confused-deputy REFUTED).
- **AssociateStreamForSegments** (newest route, NOT in SDK 1.43.73; raw SigV4 POST /domains/{d}/segment-streams, service `profile`, host profile.us-east-1.amazonaws.com): takes DestinationArn+DestinationRoleArn; cross-account stream => 400 "not a valid Kinesis Data Stream ARN"; A naming B domain => 404 "Domain could not be found". Same per-account enforcement.
- SDK customer-profiles model 2020-08-15 HAS BatchPutProfileObject/GetProfileRecommendations/CreateRecommender/CreateSegmentDefinition etc.; LACKS Associate/Disassociate/Subscription routes (raw SigV4).

## P4 aggregation cluster (REFUTED / partly blocked)
- **GuardDuty [FIRST-ID-ONLY]:** unconsented member is dead. A CreateMembers(B) => member status "Created"; GetMemberDetectors(B)/UpdateMemberDetectors(B) => UnprocessedAccounts "not an associated member". Mutual consent (AcceptInvitation) required; naming B confers zero read/write. B ListInvitations empty (CreateMembers alone sends nothing).
- **Lake Formation [SECOND-KEY]:** A GrantPermissions/GetTable with CatalogId=B => resource ARN resolves in B's acct (arn:...:289531347876:catalog:289531347876), 400 AccessDenied "no resource-based policy allows". Granter's own catalog never confused with named CatalogId.
- **RAM [LOOSE-MATCH]/[SECOND-KEY]:** AssociateResourceShare of a B-owned ARN => "cannot share resources owned by other accounts" (ownership = exact ARN-account match); look-alike principal "289531347876extra" => "Principal ID is malformed" (strict format, no prefix/contains).
- **[HEADER]/[SIG-NOT-YOU] sourceAccount/sourceArn:** derived from signed context, no caller-body path. Org delegated-admin (GuardDuty org, LF org) BLOCKED — both accts lack organizations:DescribeOrganization; no management account creds.

## P5 EC2 sharing / IPAM token / StackSets (REFUTED)
- **AMI/snapshot [WRITE-LANDS]:** A ModifySnapshotAttribute/DescribeSnapshots/CreateVolume on B's snap-id => InvalidSnapshot.NotFound (per-account). NOTE: **CopySnapshot returns HTTP 200 synchronously for ANY source id** then resolves async and errors "Source snapshot is not found" (state=error) — the 200 is optimistic request-accept, NOT a cross-tenant read. Don't be fooled by the 200.
- **Encrypted↔readable boundary HOLDS:** A shares encrypted snap to B (createVolumePermission) WITHOUT sharing CMK => KMS list_grants stays [] (no auto-grant); B CopySnapshot => async state=error "Given key ID is not accessible"; B CreateVolume from it fails same. B sees metadata only (enc=True, kms=A-key-ARN, owner=A).
- **IPAM ExternalResourceVerificationToken [SIG-NOT-YOU]:** TokenValue is opaque UUID; ARN account-scoped (arn:aws:ec2::ACCT:ipam-external-resource-verification-token/...). B cannot see A's token (empty list), describe A's token id (NotFound), or create token under A's IpamId (InvalidIpamId.NotFound). Not replayable cross-account. CreateIpam Tier='free' works standalone (no org).
- **StackSets self-managed [FIRST-ID-ONLY]:** A (with AWSCloudFormationStackSetAdministrationRole) CreateStackInstances into B => instance FAILED "Account B should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to ...AdministrationRole". Target-account trust required & STS-enforced; no admin-relationship-alone confused deputy. Teardown gotcha: delete_stack_set 409 StackSetNotEmpty even on FAILED deploy — must delete_stack_instances (RetainStacks=False) first.

## P3 re-verify + deepened 2026-10-02-1 (CustomerProfiles full attack plan, still ALL REFUTED)
Ran `/work/aws-docs/CustomerProfiles-attack-research-plan.md`. SDK botocore 1.43.95 NOW MODELS Associate/Disassociate/PutSegmentSubscription/GetProfileHistoryRecord/CreateSegmentSnapshot/CreateUploadJob/GetUploadJobPath (were raw-SigV4-only before) — use SDK.
- **IDOR-1/2/3 REFUTED (reconfirmed):** B naming A's domain on BatchGetProfile/SearchProfiles/MergeProfiles/ListProfileObjects => 404 "DomainName vhcpA is not found in account 289531347876" (msg interpolates CALLER acct). Foreign-real vs nonexistent domain = IDENTICAL 404 (no existence oracle, no 403/404 split).
- **MergeProfiles path-domain-scoped:** A merging pA3 (lives in domain vhcpA2) via path-domain vhcpA => 400 BadRequest "Unknown profile IDs". No cross-domain merge even intra-account. Each ProfileId validated against path domain.
- **SS-1 confused-deputy REFUTED on 3 INDEPENDENT controls:** (1) cross-acct DestinationArn Kinesis => 400 "not a valid Kinesis Data Stream ARN" (stream pinned to domain acct); (2) cross-acct DestinationRoleArn => 403 "Cross-account pass role is not allowed" (same hard guard as Bedrock CreateConsentPortal); (3) iam:PassRole IS ENFORCED same-acct — scoped principal with explicit deny iam:PassRole => 403 "not authorized to perform: iam:PassRole ... explicit deny", EVEN THOUGH list_customer-profiles.md authz map OMITS iam:PassRole for profile:AssociateStreamForSegments (DOC GAP, fails-closed, no sec impact). Same cross-acct-passrole 403 on CreateSegmentSnapshot. Baseline same-acct assoc needs role w/ kinesis:*+kms:* (stream default-encryption KMS) else 403 "role does not have permission to access the Kinesis Data Stream".
- **KMS-1 REFUTED:** UpdateDomain cross-acct DefaultEncryptionKey => 400 "Failed to grant access to key" (service kms:CreateGrant on foreign key fails w/o owner consent); same-acct key => 200.
- **DLQ-1 REFUTED:** UpdateDomain cross-acct DeadLetterQueueUrl => 400 "Error queue URL does not belong to your account ID".
- **CreateEventStream** cross-acct Uri => 400 "must belong to same region and account" (reconfirmed).
- **INT-1 PutIntegration:** cross-acct source S3 bucket consent-gated (AppFlow demands bucket policy granting appflow.amazonaws.com s3:ListBucket/GetObject before proceeding); cross-acct RoleArn isolation AMBIGUOUS (AppFlow object-type-mapping validation fires first; needs full object-type setup to reach). Not a confirmed path.
No findings. All cross-tenant/confused-deputy paths account-pinned server-side.

## P1/P2 re-verify 2026-09-10 (still HELD)
- P1 CreateConsentPortal (raw SigV4 POST /identities/CreateConsentPortal, service bedrock-agentcore, host bedrock-agentcore-control.us-east-1.amazonaws.com) cross-account executionRoleArn => 403 "Cross-account pass role is not allowed" (server-side confused-deputy guard). Body req: name, executionRoleArn, idpConfig{audience,credentialProviderArn}, sources[{type:agentcore-gateway,identifier}].
- P2 registry record body uses `descriptors` (plural, document-typed shape — not plain list/dict); provenance forgery already REFUTED prior (see [[agent-registry-service-facts]]).

## Residual (NOT mine): RAM share `vh-backupap-lag-share` in acct A (sibling actor) — left intact.

---
name: acxd-sagemaker-hyperpod-facts
description: Observed facts for Connect Agentic CX Designer (ACXD) reachability + SageMaker HyperPod AttachClusterNodeVolume/TrainingPlanArns cross-tenant tests (run 2026-09-13-1, all REFUTED/BLOCKED)
metadata:
  type: project
---

Run 2026-09-13-1 executed the docs-diff plan `/tmp/.../aws-docs-diff-leads.md` (P1 ACXD, P2 SageMaker HyperPod). Accounts A=183174222929, B=289531347876. See [[aws-env-setup]]. **No findings.**

## PRIORITY 1 — Amazon Connect ACXD (Agentic CX Designer): BLOCKED (not reachable), all 7 tests
**Why blocked (precondition, not skipped):** ACXD is NOT an AWS SigV4/IAM service. It is a feature *inside "Amazon Connect Customer"* (a distinct product from classic Amazon Connect 2017-08-08). Auth = opaque API key `acxd_live_<20charPrefix>.<secret>` + `workspaceId`, via its own JS SDK `amazon-connect-acxd-sdk` (`new AgenticCXDesignerClient({apiKey, workspaceId})`). No SigV4, no signing name, no documented base endpoint host.
- Docs mirror: 66 `acxd-*` files under `docs/connect/latest/{adminguide,devguide}/`. API surface is a Command-pattern JS SDK (DataRequest/Secret/KnowledgeBase/Flow/Workspace/ProgrammaticUser/ApiToken ops). Getting an `acxd_live_` token requires: Connect Customer instance -> Admin Hub -> create workspace -> CreateProgrammaticUser -> CreateApiToken. All console/instance-gated.
- **Environment ground truth:** `connect list-instances` = EMPTY in BOTH A and B. No Connect (classic) instance, and no "Connect Customer" instance-creation API in the connect botocore model (only classic `CreateInstance/DescribeInstance/ReplicateInstance`). classic CreateInstance builds a DIFFERENT product, not an ACXD tenant.
- **No live endpoint:** DNS NXDOMAIN for acxd.us-east-1.amazonaws.com, acxd.connect.*, api.acxd.*, connect-customer.*, agentic-cx-designer.*, acxd.studio. Service plane not resolvable in this sandbox.
- **Verdict:** all ACXD tests (1 External SSRF, 2 Send-context exfil, 3 MCP SSRF+injection chain, 4 Secret TOCTOU/cross-ws, 5 cross-workspace IDOR, 6 KB Documents parser/injection, 7 stored XSS) = BLOCKED. **Unblock requires:** a provisioned Connect Customer instance with ACXD enabled + issued `acxd_live_` API tokens for two workspaces (and a successful application build — the Debugger/test-mode oracle needs a build). None obtainable from IAM creds. If a live ACXD tenant is ever provisioned, the plan's battery is well-scoped and worth running (docs: `acxd-data-requests.md`, `acxd-secrets.md`, `acxd-live-sync.md`, `acxd-knowledge-base-documents.md`, `acxd-testing.md` Debugger, `acxd-audit.md` = control-plane Write/Delete only, no runtime fetch logging).

## PRIORITY 2 — SageMaker HyperPod (both SigV4-reachable, botocore 1.43.73): REFUTED
research-admin in BOTH accts simulate-allowed: AttachClusterNodeVolume, DetachClusterNodeVolume, CreateCluster, ec2:CreateVolume/DescribeVolumes/DeleteVolume.

### Test 8 — AttachClusterNodeVolume / Detach twin cross-tenant EBS: REFUTED
New APIs live (in SDK model). Endpoint api.sagemaker.us-east-1.amazonaws.com. Body {ClusterArn, NodeId=i-, VolumeId=vol-}. **VolumeId is resolved in the CALLER's own account** — cross-account volume is invisible. Crisp discriminator (all from A against a well-formed but nonexistent A-cluster ARN):
- A's OWN available vol + fake cluster => `ResourceNotFound / ClusterNotExistsException: Specified cluster not found` (volume check PASSED, advanced to cluster check).
- B's real available vol + fake cluster => `ValidationException / HyperPod - Client Error: InvalidVolume.NotFound: The volume 'vol-...' does not exist.` (volume resolved in A, B's vol invisible).
- nonexistent-in-A well-formed vol => IDENTICAL InvalidVolume.NotFound msg as B's real vol => **no cross-account existence oracle.**
- cross-account cluster ARN (B's acct) => `AccessDeniedException: not authorized ... on this resource`.
- Detach twin identical behavior. **No HyperPod-EKS cluster needed** — isolation enforced at the EC2 volume-resolution layer before the cluster matters. Encrypted↔readable & account↔account boundaries HOLD.

### Test 9 — InstancePreference.TrainingPlanArns / ResourceConfig.TrainingPlanArn cross-tenant reserved capacity: REFUTED
SDK has job-level `ResourceConfig.TrainingPlanArn` (singular); newer per-preference `ResourceConfig.InstancePreferences[].TrainingPlanArns` (Array, 1 item) NOT in SDK 1.43.73 but LIVE service understands it (raw SigV4 X-Amz-Target SageMaker.CreateTrainingJob). Both paths identical:
- B-account training-plan ARN => `AccessDeniedException: Access to the requested training plan is denied`.
- **Same-account NONEXISTENT plan ARN => IDENTICAL AccessDeniedException** (fail-closed; no cross-account vs not-found distinction => no enumeration oracle).
- No plan => advances to role validation (`ValidationException: Could not assume role`). So training-plan authz fires BEFORE role/passrole validation. No capacity theft, no accept.
- Training-plan ARN pattern `arn:aws:sagemaker:<region>:<acct>:training-plan/.*` (min len 50). CreateTrainingJob min body: TrainingJobName, AlgorithmSpecification{TrainingImage,TrainingInputMode}, RoleArn, OutputDataConfig{S3OutputPath}, ResourceConfig, StoppingCondition.

**Teardown:** created 2 gp3 1GiB volumes (A vol-0bf1b4d0cc65e5883, B vol-01ccb5bb40c0e44a0), both deleted + tag-sweep verified empty. No training jobs/clusters created (all attempts failed at validation). Note: `vh-2026-08-08-1-imds-*` training jobs pre-exist in A (prior run, not this session).

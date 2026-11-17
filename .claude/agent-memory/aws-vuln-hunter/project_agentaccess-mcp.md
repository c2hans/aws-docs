---
name: agentaccess-mcp
description: Live facts about the agentaccess-mcp (WorkSpaces Applications Agent Access MCP) service + how to drive/test it
metadata:
  type: project
---

**agentaccess-mcp** is a LIVE, deployed AWS service (observed 2026-11-17): AI agents remote-control an
AppStream/WorkSpaces-Applications streaming desktop via MCP (Streamable HTTP, JSON-RPC). Endpoint
`https://agentaccess-mcp.{region}.api.aws/mcp`. NOT a modeled botocore service — raw SigV4 (service name
`agentaccess-mcp`) over HTTP. AppStream control plane IS modeled: `CreateStack`/`CreateImageBuilder`/
`UpdateImageBuilder` take `AgentAccessConfig` (Settings COMPUTER_VISION|COMPUTER_INPUT|FORWARD_MCP_TOOLS,
ScreenResolution W_1280xH_720, ScreenImageFormat PNG|JPEG, S3BucketArn, ScreenshotsUploadEnabled,
ReplaySessionEnabled, KmsKeyArn, UserControlMode VIEW_ONLY|VIEW_STOP|DISABLED).

**How to test (env has NO boto3/CLI in system python):** use venv `/work/.vhvenv` (boto3/botocore 1.44.3).
SigV4-sign with botocore SigV4Auth(service="agentaccess-mcp"). MCP sequence: POST initialize -> capture
`Mcp-Session-Id` response header -> POST notifications/initialized (carry Mcp-Session-Id) -> tools/list ->
tools/call. Tool names are prefixed `agentaccess___` (e.g. `agentaccess___get_current_user`,
`agentaccess___switch_user`, `agentaccess___screenshot`, `agentaccess___get_session_info`). End session via
HTTP DELETE (carry Mcp-Session-Id + headers). Reusable helpers were at /work/aam-hunt/{mcp,seq,live}.py.

**Connect headers.** NDJ fleet/stack: `x-amzn-agentaccess-workspaces-applications-stack` (name OR ARN) +
optional `-user-id`. Image builder: `-image-builder-name` (NAME) + REQUIRED `x-amzn-agentaccess-local-user`
(ADMINISTRATOR|TEMPLATE_USER|TEST_USER). Or streaming-URL header. Needs a RUNNING fleet / RUNNING image
builder to bind a desktop (stack alone -> "No fleet associated"; stopped fleet -> "fleet not running").

**Security controls OBSERVED TO HOLD (2026-11-17 sweep, accounts A=183174222929/B=289531347876):**
- StackArn bound to signing account: cross-account ARN -> 403 "ARN does not belong to caller's account".
  Bare name / uppercase-or-malformed ARN -> synthesized into CALLER's account (benign). (H1/H2 refuted.)
- Mcp-Session-Id bound PER-PRINCIPAL: cross-account AND same-account cross-principal reuse -> 404
  "Session not found". (H4 refuted.)
- Image-builder connect: InvokeMcp REQUIRES a valid local-user (can't omit). local-user validated
  case-INSENSITIVELY ("Administrator" accepted, "root" rejected) — possible deny-policy case bypass (T-NEW).
- LocalUser gate: fresh connect HONORS requested local-user (TEST_USER-scoped agent -> get_current_user
  TEST_USER even if admin was last user); switch_user->ADMINISTRATOR under TEST_USER policy -> 403.
  Live get_current_user desc: reconnect "as the account the session was using, fails if IAM no longer allows
  InvokeMcp for that account" => reconnect re-checks InvokeMcp per-account. H3 end-to-end REFUTED despite a
  latent simulate fail-open (StringEqualsIfExists + unconditioned desktop actions in AWS's recommended policy).
- user-id vs SourceIdentity: mismatch -> 400 "UserId header conflicts with authenticated identity
  (aws:SourceIdentity)". Enforced only when SourceIdentity present; bare principal picks any user-id (no
  condition key) — H5 boundary-dependent (victim home folder needs running fleet + home folders, untested).
- Replay screenshot S3 bucket must be same-account: cross-account bucket -> InvalidParameterValueException.

**Gotchas.** CreateFleet/CreateImageBuilder need IAM role `AmazonAppStreamServiceAccess` (/service-role/,
managed policy same name) — absent by default; create it. Image builders only ONE agent connection at a
time (stale MCP sessions hold the slot ~13min -> CONNECTION_LIMIT_REACHED; DELETE them). Newest Windows
public base image was 2026-09-22 yet agent access enabled fine on Aug-2026 base (no IncompatibleImageException).
Image builder bills while RUNNING — stop/delete promptly. See [[aws-test-environment]].

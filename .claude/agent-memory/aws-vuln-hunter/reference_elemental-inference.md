---
name: elemental-inference
description: AWS Elemental Inference (elemental-inference) live-test facts — regions, data-plane IDOR oracle, feed-policy validation bypass, accessRoleArn/PassRole behavior
metadata:
  type: reference
---

AWS Elemental Inference (`elementalinference` in botocore 1.43+). GA, observed live 2026-10-06 (run 20261006-eleminf). See [[agentcore-env]] for the two in-scope accounts.

**Regions:** live in us-east-1, us-west-2, eu-west-1, ap-southeast-2 (ListFeeds 200). NOT us-east-2/eu-central-1/ap-northeast-1 (EndpointConnectionError). `get_available_regions('elementalinference')` returns [] — use region_name explicitly.

**Control vs data plane:**
- Control plane client ops: Create/Get/List/Delete/Update/Associate/Disassociate Feed; *Dictionary; Put/Get/Delete FeedPolicy; SearchFixtures; GetFixture; Tag/Untag/ListTags. `accessRoleArn` IS in the live CreateFeed/UpdateFeed model (despite plan claiming absent).
- `GetMetadata` and `PutMedia` are DATA PLANE only (NOT in botocore client). Data endpoint host is SHARED/multi-tenant: both accounts' feeds returned the same host `<10hex>.elemental-inference-data.<region>.api.aws` — per-feed isolation is by feed-id in the URL path, not hostname.

**Data-plane GetMetadata oracle (sign SigV4 service name `elemental-inference`):**
POST `https://<host>/v1/feed/<feed-id>/input/0/metadata` body `{"outputName":..,"timeSpecification":{"ptsBased":{"startPts":0,"endPts":5000,"timescale":1000}},"parameters":{"contextualMetadata":{}}}`.
- own feed, no data: HTTP 404 "No metadata was found" (= authorized)
- foreign feed: HTTP 403 "Access Denied" — IDENTICAL to bogus id => clean ownership enforcement, NO existence oracle. Cross-tenant data-plane IDOR REFUTED.

**CONFIRMED VULN — PutFeedPolicy wildcard-Principal validation bypass:** feed-policies-requirements.md documents "Principal cannot be a wildcard (*)" and "only action = GetMetadata". Service REJECTS extra actions, NotPrincipal, missing Sid, oversize>2048 — but ACCEPTS `Principal:"*"` AND enforces it (foreign account GetMetadata goes 403->404 after attaching). Also accepts `Action:"*"` (cosmetic; data plane only honors GetMetadata). AWS-side validator defect; makes a feed's contextual metadata (transcripts, on-screen text, scene summaries, brands) world-readable despite the documented guardrail. Exploit requires owner to author the wildcard, so Medium (guardrail gap), not attacker-initiated.

**accessRoleArn / PassRole (L1 confused-deputy):** EI defines NO service-specific condition keys (only aws:RequestTag/ResourceTag/TagKeys). CreateFeed/UpdateFeed enforce SAME-ACCOUNT PassRole — a cross-account role ARN => `AccessDeniedException "Cross-account pass role is not allowed"`. So cross-account confused-deputy via accessRoleArn is NOT reachable. CreateFeed does NOT validate role existence/trust at create (nonexistent role & role not trusting EI both accepted; failure deferred to media time). Template read is DEFERRED to media-processing time (feed reaches AVAILABLE regardless) — no role-assume observable without AssociateFeed+PutMedia (CMAF, heavy).

**templateUris SSRF (L5): REFUTED.** CreateFeed enforces s3://-only regex at API layer — http/https/file/gopher and `http://169.254.169.254` all REJECTED ValidationException. s3:// to any bucket accepted (read deferred, uses same-account access role).

**Other:** SearchFixtures = shared reference data (identical fixtureIds across accounts, not tenant-scoped). Dictionary/Feed control-plane cross-account reads = ResourceNotFoundException (clean, no oracle). ABAC self-widen (unconditioned TagResource lets a scoped principal tag a feed into its own team) works but is the generic avoidable footgun, not an EI bug. ElementalInferencePlaygroundServiceRole is console-created only (absent unless console used) — L2/L3 blocked:precondition in a scripted run.

**Cheap substrate:** a feed with a single `contextualMetadata` output (no accessRoleArn, no S3) is the minimal resource for FeedPolicy/data-plane tests. Feeds reach AVAILABLE in ~a few seconds.

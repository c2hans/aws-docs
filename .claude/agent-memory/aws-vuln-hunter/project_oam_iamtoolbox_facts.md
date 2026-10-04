---
name: oam-iamtoolbox-facts
description: Live facts for OAM + iam-toolbox disclosure cluster (run 2026-10-03-1) — iam-toolbox cross-org disclosure CONFIRMED, OAM IDOR REFUTED
metadata:
  type: project
---

Run 2026-10-03-1. Both services SDK-modeled (botocore 1.43.95): `oam` (2022-06-10), `iam-toolbox` (2018-05-10), us-east-1 endpoints live in A and B.

**CONFIRMED — iam-toolbox `GetRequestAuthorizationDetails` intra-org cross-account disclosure (High, routing: aws-security).**
- The id is emitted inside the AccessDenied message of a NARROW subset of IAM denials: `iam:GetUser` and `iam:GetRole` emit a 25-char base36 `authorizationId` + console URL; `iam:ListUsers`, s3/sts/logs/ec2/kms/dynamodb do NOT. Standard non-IAM AccessDenied has no id.
- To generate: assume a role (not GetFederationToken — fed-user tokens can't call IAM, give InvalidClientTokenId) whose policy omits iam:GetUser, call get_user → id in message.
- B holding ONLY `iam:GetRequestAuthorizationDetails` (no grant from A) reads A's full record: requestContext (principalARN, aws:UserId sess name, real SourceIp, UserAgent, principal tags, org paths) + evaluated policies (types/attachment ARNs) + matched SIDs. Byte-identical to A's self-read. By-design per 404 "same account or organization"; unconditionable (victim owns no resource, no condition key). **L2 facet:** same record leaks mgmt-authored SCP ARN+OU attachment (arn:aws:organizations::532876697804:…/p-r2n826oj @ ou-ja5k-umgi471e) to a plain member. File: /work/findings/iam-toolbox-getrequestauthorizationdetails-intra-org-cross-account-disclosure.md
- **L3 hard-stop tripwire NEVER fired:** all *IsAWSService/Via*Service="false"; only world-known ::aws: managed policies (p-FullAWSAccess, AWSDenyAll). No AWS fleet identity.
- REFUTED: L5 ids high-entropy 25-char base36 (not enumerable); L6 no 404 differential (echoes id). Doc example id `a1b2c3d4e5f6g7h8i9j0` (20ch) is rejected ValidationException — real=25ch. Fresh ids may 404 briefly (ingestion delay).
- BLOCKED: L4 (no out-of-org session), L7 (only IAM denials emit ids → no RESOURCE_BASED_POLICY eval path), L8 (mgmt acct OOS).
- Org facts observed: org `o-pf2hyvtase`, root r-ja5k, OU ou-ja5k-umgi471e, mgmt 532876697804. Custom SCP p-r2n826oj on the OU. (Matches [[sincelastpush-0926-facts]] org topology.)

**REFUTED — OAM cross-account read IDOR (Areas 1 & 2).** A↔B GetSink/GetSinkPolicy/ListAttachedLinks/GetLink/ListTags on counterpart sink ARN all 403 AccessDeniedException "explicit deny in a resource-based policy", both directions. Resource policy evaluated authz-first & ownership-aware; sink policy granting only CreateLink/UpdateLink denies all reads. No 403-vs-404 existence oracle (real-foreign and fabricated-nonexistent sink both identical 403; authz before existence).
- Pre-existing OAM topology (NOT ours, snapshot, never mutate): A sink oam-rev-sink de3d3143 (grants B CreateLink Metric); B sink oam-victim-sink e17a813b (grants A CreateLink/UpdateLink Metric/LogGroup/XRay); bidirectional links already present; labels "m1tz-aws-bb-{1,2}-wearehackerone.com".

**Run 2026-10-03-2 — OAM Areas 3/5/4b/6 (throwaway us-east-2 sink+link, A=mon 183174222929, B=src 289531347876). ALL REFUTED except Area 6 (intended/Low).**
- Setup: A CreateSink us-east-2 + PutSinkPolicy granting B CreateLink/UpdateLink with `ForAllValues:StringEquals oam:ResourceTypes=[Metric]` (single-elem array normalized to scalar). B CreateLink Metric-only. Torn down fully; us-east-2 empty both accts; us-east-1 pre-existing topology untouched.
- **Area 5 twin-parity REFUTED.** UpdateLink IS re-authorized against the SINK resource policy on EVERY call, incl. the oam:ResourceTypes condition. B UpdateLink [Metric,LogGroup] under Metric-only policy = 403 AccessDenied on sink ARN ("no resource-based policy allows oam:UpdateLink"); CreateLink [Metric,LogGroup] = identical 403. No UpdateLink-200/CreateLink-403 split. UpdateLink has NO LabelTemplate member (label immutable post-create); has LinkConfiguration(filter)+ResourceTypes.
- **Area 4b type-intersection REFUTED (enforced server-side).** ForAllValues oam:ResourceTypes=Metric denies any request containing a non-listed type (LogGroup) on both CreateLink & UpdateLink. Vacuous-truth-via-omission NOT reachable: ResourceTypes required 1-50 on both APIs; empty list []=client ParamValidationError min 1. Key always populated → ForAllValues never vacuous.
- **Area 3 revocation-incompleteness REFUTED (control plane).** After A PutSinkPolicy removes B (self-only, no */org): B UpdateLink existing link = 403 immediately AND after 30s (live re-check present, not stale); B fresh CreateLink = 403. B CAN still GetLink+DeleteLink its OWN link (owns resource), and the link OBJECT still shows in A's ListAttachedLinks until B deletes it source-side (matches doc "remove from source acct"; A cannot unilaterally delete B's link). Data-plane telemetry-flow-after-revoke = INCONCLUSIVE (needs pushing telemetry, out of scope). B one link per sink (2nd CreateLink=409 ConflictException).
- **Area 6 label spoofing = INTENDED/Low footgun.** LabelTemplate stored & returned VERBATIM to monitoring acct A via ListAttachedLinks: spoof "prod-payments-111111111111" and HTML `<img src=x onerror=alert(1)>` both unsanitized at API layer; real source acct only in LinkArn, no provenance binding. By-design (source-controlled friendly name). Stored-XSS render-path NOT tested (headless; console render = AWS-side, untested → note not finding).
- No HARD-STOP: no AWS service-plane identity/ARN surfaced in any response.

**OAM Area 4 guardrail — DOWN-RATED to Low footgun.** PutSinkPolicy accepts Principal:"*" with no condition / no BPA / no warning (200, stored). BUT global keys aws:PrincipalOrgID + aws:PrincipalAccount ARE accepted/authorable & IAM-enforced → plan's "unconditionable AWS defect" claim REFUTED. One sink per account per region; use throwaway us-east-2 sinks for policy tests (A's us-east-1 slot already taken).

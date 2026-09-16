---
name: ebs-volume-clones-crossaccount
description: Result of hunting the EBS Volume Clones cross-account feature (RAM ec2:Volume share + ec2:CopyVolumes + KMS re-encrypt) — boundary held, all security hypotheses refuted
metadata:
  type: project
---

Tested the "EBS Volume Clones" cross-account feature (plan: `/work/aws-docs/ebs-volume-clones-cross-account-attack-research-plan.md`). Feature = direct cross-account EBS *volume* share via AWS RAM on `ec2:Volume` + new `ec2:CopyVolumes` API + KMS re-encryption of the clone. API is genuinely live server-side in the two test accounts (Owner A=183174222929, Consumer B=289531347876), not just SDK-model-injected.

**Outcome: cross-account boundary HELD. Zero confirmed vulnerabilities.** All security hypotheses REFUTED with resource-policy denials (the RAM-generated resource-based policy — not IAM — is the real copy-access enforcement layer; both test users are over-privileged research-admins, so a resource-policy denial is the strongest possible refutation since a scoped principal gets the same result).

- CopyVolumes authz (A1/A2/A4/A5): REFUTED — copying an unshared/foreign volume denied.
- Action-family parity (E): REFUTED — consumer cannot attach/modify/delete/snapshot a shared volume, only describe+copy.
- KMS boundary (C1/C3): REFUTED.
- Managed-permission audit (H): REFUTED — AWSRAMDefaultPermissionEBSVolume and AWSRAMPermissionEBSVolumeCopyAccess both tightly scoped.
- Recycle Bin removed-principal re-exposure (D3): REFUTED — after removing B while volume binned then restoring, B's describe returns InvalidVolume.NotFound; removed principal does NOT regain access (matches share-volume.md line 167).
- Copy contention (F): CONFIRMED but DOCUMENTED-INTENDED + availability-only — one copy at a time per shared volume across all accounts (ConcurrentCopyVolumeLimitExceeded); did not pursue sustained DoS (AWS policy).
- Doc bug (G): ebs-copying-volume.md CLI examples show `--encrypted`/`--kms-key-id` but the CopyVolumes API/CLI does not implement them. Documentation inconsistency, not a vuln.

**Phase 2 (run 2026-09-15-2)** re-ran the untested areas + reopened the KMS boundary. Boundary still HOLDS; zero vulns. Key results:
- **CORRECTION to Phase-1's "G doc bug (KmsKeyId/Encrypted rejected)":** the botocore SDK model AND API reference omit `KmsKeyId`/`Encrypted`, but the **live wire API HONORS them.** Phase-1's "rejected" was a CLI/SDK client-side validation artifact (CLI drops params not in the model before they hit the wire). To send them: register `before-call.ec2.CopyVolumes` and inject into `params['body']` (e.g. body['Encrypted']='true'; body['KmsKeyId']=arn). Confirmed: clone came back Encrypted under the injected CMK. Security posture unaffected — all KMS authz still fires. It's a doc/SDK-model gap.
- KMS gate re-tested with real params: C1' (copy encrypted shared vol w/o CMK shared) → AuthFailure ReEncrypt (403), REFUTED. C2 key-steering (disabled/pending/foreign/malformed) all rejected at request time, no fail-open, REFUTED. C5 (unencrypted copy of encrypted source) → UnsupportedOperationException, REFUTED. C4 no standing grant on CMK (ReEncrypt uses key-policy directly, 0 grants). C3' headline re-encryption under B's chosen CMK works cross-account (intended).
- Area I (detection): custom `sharedVolumeCopy` EventBridge event ("EBS Volume Notification", source aws.ec2) delivered to owner carries volume ARN+result+time+request-id but NOT consumer account ID (I1, low). BUT the CloudTrail-backed delivery ("AWS API Call via CloudTrail", recipientAccountId=owner) DOES carry consumer userIdentity.accountId + sourceIP, even on failed AuthFailure copies (I2 refuted). Consumer DescribeVolumes reads are invisible in owner's CloudTrail/EventBridge (I3, low, standard cross-account behavior).
- Area B: both accounts have identical AZ name→ID maps; clone lands in owner's physical AZ ID (use1-az1), consumer can infer it — by-design side-effect of same-AZ copy, AZ IDs non-secret. CopyVolumes has NO AZ input param.
- Area J: RAM validates OU/org existence at share creation (bogus → UnknownResourceException) but does NOT validate account IDs (nonexistent 12-digit acct → ACTIVE share). Platform-wide RAM footgun, owner-chosen principal, not a feature vuln.
- Area K: clone has empty SnapshotId (direct vol-to-vol copy, no lineage handle); consumer can't enumerate owner snapshots (describe_snapshots OwnerIds=[A]=0); K3 positive control PASSED — with owner CMK disabled, consumer snapshotted its clone (under consumer's own key) successfully = fully independent.
- Area L: view-only copy → UnauthorizedOperation (authz before size validation); pre-accept → InvalidVolume.NotFound (short-circuits before size); Size=0 error doesn't disclose exact size. No size/existence oracle. REFUTED.
- Consumer scope nuance: B can DescribeVolumes but DescribeVolumeStatus on shared vol → NotFound (managed perm scoped tighter than "describe").

**Why:** confirms the newly-launched cross-account clone path enforces isolation at the RAM resource-policy layer AND the KMS gate (ReEncrypt on source key) as designed.
**How to apply:** if re-tested or a variant feature appears, the enforcement points are (1) the RAM-generated resource-based policy on the volume, not IAM, and (2) the KMS key-policy ReEncrypt check on the source CMK. To exercise KmsKeyId/Encrypted you MUST inject via before-call hook — CLI/SDK will silently drop them. HARD STOP was never triggered — no AWS service-plane identity encountered.

**Env gotcha:** Recycle Bin ingestion for freshly-deleted volumes is eventually-consistent and flaky — a volume can appear to hard-delete within a 30s poll then be fine on a later attempt. Poll the bin generously (>60s) before concluding a volume didn't enter it. See [[infra-json-race-and-buffering]] for the general consistency caveat.

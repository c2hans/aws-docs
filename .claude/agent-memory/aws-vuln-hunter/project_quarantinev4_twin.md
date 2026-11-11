---
name: project-quarantinev4-twin
description: AWSCompromisedKeyQuarantineV4 BatchGetSecretValue "twin bypass" is REFUTED at the data plane
metadata:
  type: project
---

`AWSCompromisedKeyQuarantineV4` (DefaultVersionId v2, 214 denied actions, Effect Deny on Resource "*") denies `secretsmanager:GetSecretValue` but NOT `secretsmanager:BatchGetSecretValue`. The hypothesis that a quarantined key can still read secrets via the Batch* twin is **REFUTED live**.

**Why:** BatchGetSecretValue re-authorizes `secretsmanager:GetSecretValue` per secret (documented: "you must have secretsmanager:GetSecretValue for each secret"). The quarantine's explicit Deny on GetSecretValue carries through — the secret lands in the per-secret `Errors` array (AccessDeniedException, HTTP 200, 0 SecretValues), never returned. The IAM policy *simulator* shows Batch* as "allowed" because it evaluates only the literal action, not the service-side per-secret re-check — so simulate over-reports exploitability here.

**How to apply:** Do not re-file the SM Batch* twin as a confirmed bypass — always confirm at the data plane. A policy-text deny-list gap visible in `simulate_custom_policy` is NOT proof of data exposure for aggregate actions that re-authorize the primary.

**S3 version twin — CONFIRMED bypass (2026-11-11, account A 183174222929).** The quarantine denies `s3:GetObject` and `s3:ListBucket` but NOT `s3:GetObjectVersion` or `s3:ListBucketVersions`. On a versioned bucket a quarantined key: GetObject(no version) -> AccessDenied, ListObjectsV2 -> AccessDenied, BUT ListObjectVersions -> 200 (via s3:ListBucketVersions) and GetObject(VersionId=...) -> 200 returning the object bytes (via s3:GetObjectVersion). Versioned reads authorize against GetObjectVersion and do NOT re-check GetObject, so the containment is fully bypassed for object bytes. Real data-plane bypass of an AWS-operated containment control -> only AWS can fix the deny list.

STS `AssumeRoleWith{WebIdentity,SAML}` are NOT meaningful twins: those calls authenticate with an external OIDC/SAML token, not the compromised principal's key, so the identity-based quarantine isn't the caller's policy there. Dropped. PoC: `/work/findings/quarantinev4_incomplete_deny.py`.

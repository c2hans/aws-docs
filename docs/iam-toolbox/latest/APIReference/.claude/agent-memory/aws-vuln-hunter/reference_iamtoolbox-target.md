---
name: reference-iamtoolbox-target
description: Stable facts about the iam-toolbox GetRequestAuthorizationDetails target and the two-account test env, so future runs skip settled probes
metadata:
  type: reference
---

Target: `iam-toolbox:GetRequestAuthorizationDetails` (Preview, API 2018-05-10) — the service's ONLY operation. Endpoint `GET https://iam-toolbox.us-east-1.amazonaws.com/authorization-details/{authorizationId}`, SigV4 `signingName=iam`, action `iam:GetRequestAuthorizationDetails`.

Env: A=`183174222929` (profile `default`), B=`289531347876` (profile `awsbb2`), org `o-pf2hyvtase`, mgmt `532876697804` (NO creds — mgmt/RCP branches BLOCKED). Creds at `/work/.aws`; run with `AWS_CONFIG_FILE=/work/.aws/config AWS_SHARED_CREDENTIALS_FILE=/work/.aws/credentials`. boto3 1.43.87 with the model lives in the scratchpad venv (`.../scratchpad/venv`), NOT `/work/.venv`. Teardown ledger: `/work/.vh0903_ledger.md`.

Settled facts (don't re-probe):
- **Single region:** only `iam-toolbox.us-east-1.amazonaws.com` resolves; all other regional + global endpoints NXDOMAIN.
- **authorizationId = uniform random ~128-bit**, base36, canonical (no leading zero), value < 2^128. Validation = canonical-form + magnitude bound, NOT a checksum. Not forgeable/predictable (finding 21/T1).
- **Only account-local IAM *read* actions mint an id** (GetUser/GetRole/ListAccessKeys). Writes and all non-IAM/cross-account service denials do NOT (finding 18/V1).
- **Retrieval scope = "same account OR organization", never same-principal.** Any principal with the one action reads any denial in the account/org. Confirmed cross-account (finding 15/17), intra-account cross-principal (finding 19), and it discloses IDENTITY/SESSION/PERMISSIONS_BOUNDARY/SCP policy ARNs + full org tree + source IP + session tags.
- **Not customer-scopable:** action needs `Resource:"*"` (no resource-level ARN), `aws:ResourceAccount` NOT populated; only caller-side condition keys work. So customers can only deny/restrict WHO holds the action, not WHICH denials are read (finding 21/T6). Fix is AWS's → routing `aws-security` human submission.
- **nextToken** never appears (single-evaluation denials); fabricated tokens are ignored, authId path param is the sole record selector (finding 21/T2).

Confirmed findings: 15 (cross-account), 17 (CloudTrail-sourced id + full org tree), 19 (intra-account cross-principal), 20 (permissions-boundary class). Refuted/blocked/informational: finding 18, finding 21.

---
name: socialmessaging-facts
description: AWS End User Messaging Social (socialmessaging/WhatsApp) live verdicts — MEDIA-1/2/3, EVT-1, signup; validation order + defended controls (run 2026-10-02-1)
metadata:
  type: project
---

Run **2026-10-02-1**, accounts A `183174222929`/B `289531347876`, us-east-1. Plan `/work/aws-docs/SocialMessaging-attack-research-plan.md`. See [[aws-env-setup]], [[sincelastpush-0926-facts]] (prior precheck: both accts 0 WABAs — still true). socialmessaging fully SDK-modeled (botocore 1.43.95), 35 ops. Both A&B have **0 linked WABAs**; cannot onboard (needs Meta consent) — so anything past phone/WABA resolution is BLOCKED.

**Validation ORDER (observed, GetWhatsAppMessageMedia presigned path):** (1) URL regex → ValidationException; (2) phone-ARN partition+region+account match → InvalidParametersException; (3) Content-Type header presence in headers map → InvalidParametersException "Content-Type header is required in S3PresignedUrl"; (4) phone-number-id resolution against CALLER account → 404 ResourceNotFoundException "Origination phone number id not found for account." The Meta-fetch/URL-dereference happens ONLY after (4). **No host-allowlist before (4)** — only URL gate is the regex. destinationS3File (bucket) path skips straight to (4) phone-404.

**MEDIA-3 cross-tenant phone-number-id ARN = REFUTED (settled).** Field accepts bare `phone-number-id-...` AND `arn:...:phone-number-id/...`. Self-account ARN + bare both resolve against caller acct (404 not-found). FOREIGN-account ARN (B 289531347876 or arbitrary 1111...) → 400 InvalidParametersException "Provided parameters are not valid". Also pinned: wrong-region self-ARN (us-west-2) and wrong-partition (aws-cn) both → InvalidParameters. So partition+region+account all bound to caller before resolution. Same for waba ARNs (PutWhatsAppBusinessAccountEventDestinations foreign-waba → InvalidParameters) and PostWhatsAppMessageMedia foreign phone → InvalidParameters. Account-binding is the central defended control, enforced at param layer.

**MEDIA-2 presigned-URL regex = CONFIRMED validation-layer weakness; end-to-end SSRF BLOCKED (Meta onboarding).** Regex `https://(.*)s3(.*).amazonaws.com/(.*)` unanchored, unescaped dots, enforced server-side. ACCEPTS (host attacker-controlled, token in path/query/fragment): `https://attacker.example.com/?x=s3.amazonaws.com/y`, `https://169.254.169.254/?x=s3.amazonaws.com/` (LINK-LOCAL passes!), `https://evil.example/#s3.amazonaws.com/`, `https://evil.example/a?b=s3xamazonaws.com/`. REJECTS (incidentally, regex wants `/` right after `...amazonaws?com`): userinfo `https://s3.amazonaws.com@evil/path`, suffix `https://s3.amazonaws.com.evil/path`, control `https://evil/plain`. Fetch unreachable w/o real phone + real Meta mediaId → could NOT confirm fleet egress; link-local probed once at validation layer only, not iterated (hard-stop discipline). Finding file: `/work/findings/socialmessaging-01-presigned-url-regex-unanchored-ssrf-validator.md` (routing aws-security, medium confidence). Same regex on PostWhatsAppMessageMedia sourceS3PresignedUrl.

**MEDIA-1 cross-account bucket write = BLOCKED.** destinationS3File = {bucketName (just S3 grammar, NO account field), key}. Bucket path hits phone-404 first; owner-validation unreachable w/o real linked phone. Cannot observe whether fleet validates bucket owner.

**EVT-1 cross-account event destination = BLOCKED.** PutWhatsAppBusinessAccountEventDestinations needs real WABA: self synthetic waba + cross-acct SNS → "LinkedWhatsAppBusinessAccountId Not Found" (WABA checked before SNS-arn cross-acct validation; latter unreachable). Foreign-waba ARN → InvalidParameters (account bound).

**Signup/Associate (WABA-1/TOK-1) = BLOCKED by CSRF gate.** AssociateWhatsAppBusinessAccount via SigV4 → **403 AccessDeniedException "CSRF header does not exist"**. Console-only enforced by a CSRF header SigV4 can't supply; callbackUrl/accessToken never processed. Defended control. PutWhatsAppBusinessPublicKey takes `originationPhoneNumberId` (NOT id/waba as plan assumed) — needs phone, BLOCKED.

**No resources created** (every probe rejected pre-execution). Teardown trivially clean (0 WABAs both accts post-run).

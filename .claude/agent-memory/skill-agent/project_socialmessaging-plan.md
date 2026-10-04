---
name: socialmessaging-plan
description: security-questionbuilder attack plan for AWS End User Messaging Social (SocialMessaging/WhatsApp broker); reuse, don't restart.
metadata:
  type: project
---

A boundary-first attack-research plan exists for **AWS End User Messaging Social (service prefix `social-messaging`, the AWS-managed broker to Meta's WhatsApp Cloud API)** at `/work/aws-docs/SocialMessaging-attack-research-plan.md` (~8 leads).

**Why:** Backfill after an earlier 429 lost the plan. The non-obvious structural fact driving the leads: `GetWhatsAppMessageMedia`/`PostWhatsAppMessageMedia` are **NOT iam:PassRole-gated and take no roleArn**, yet the SLR `AWSSocialMessagingServiceRolePolicy` grants ONLY `cloudwatch:PutMetricData` — so the media S3 read/write is done by the service's own fleet identity, making destination handling a confused-deputy question.

**NEW (2026-10-03 leftright):** a SECOND, non-overlapping plan covers the WhatsApp **public-key management + WhatsApp calling** surface at `/work/aws-docs/_change-analysis/plans/2026-10-03-leftright/social-messaging-whatsapp-attack-research-plan.md`. Top 3: (A1) cross-customer key-substitution via `PutWhatsAppBusinessPublicKey` — the one mutating API whose docs OMIT the ownership sentence its sibling `SendWhatsAppCallEvent` states; (A2) cross-account KMS confused-deputy — `managing-flows-dynamic.md` sample grants `kms:GetPublicKey` to `social-messaging.amazonaws.com` with NO SourceAccount, `kmsKeyArn` accepts any 12-digit acct, fleet does the read (SLR = cloudwatch only); (A3) read/settings IDOR on `GetWhatsAppBusinessPublicKey`/`UpdateLinkedWhatsAppBusinessAccountPhoneNumber`/`GetWhatsAppCallPermission` (all omit ownership text, share loose `phone-number-id` regex that accepts foreign-account ARN form).

**How to apply (broker/media plan):** Top leads to hand a hunter: (1) MEDIA-1 confused-deputy write — fleet writes Meta media to caller-supplied `destinationS3File.bucketName`; "same account/region" is prose-only in `managing-media-files-s3.md`, no condition-key enforcement. (2) MEDIA-2 SSRF-write — `S3PresignedUrl.url` validator `https://(.*)s3(.*).amazonaws.com/(.*)` is UNANCHORED with unescaped dots (so `https://attacker.tld/?u=s3.amazonaws.com/` passes); caller also controls the `headers` map. (3) MEDIA-3 cross-tenant media via `originationPhoneNumberId` ARN-form (pattern accepts arbitrary account) + Meta-opaque `mediaId`; `metadataOnly:true` is a cheap existence oracle. Also EVT-1 (cross-account eventDestinationArn), WABA-1 (phone/WABA claim + twoFactorPin brute), TOK-1 (Meta accessToken/callbackUrl). HARD STOP if any write identity/bucket resolves to AWS's own plane. Related: [[customerprofiles-segments-plan]].

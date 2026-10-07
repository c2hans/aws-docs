---
name: end-user-messaging
description: AWS End User Messaging service/client mapping, teardown cascade behavior, and ValidateNotifyCodeVerification status-only oracle (observed 2026-10-06)
metadata:
  type: reference
---

AWS End User Messaging live facts (observed 2026-10-06, both in-scope accounts; see [[agentcore-env]] for account IDs).

**Client / operation mapping (botocore 1.43.x):**
- Brand profiles live in client `endusermessaging` (NOT `pinpoint-sms-voice-v2`): `CreateBrandProfile`, `ListBrandProfiles`, `DeleteBrandProfile`, `list_tags_for_resource(resourceArn=...)` -> `{"tags":[{"key","value"}]}`. Brand profile ARNs are `arn:aws:end-user-messaging:...:brand-profile/bp-...`.
- Registrations live in client `pinpoint-sms-voice-v2`: `CreateRegistration`, `DescribeRegistrations`, `PutRegistrationFieldValue`, `DeleteRegistration`, `DescribeRegistrationFieldValues`, etc. Registration ARNs are `arn:aws:sms-voice:...:registration/registration-...`.
- `socialmessaging` client has none of these.

**Teardown cascade (important):** Required registration field values (e.g. `agentDetails.brandName`, `agentDetails.serviceName`) CANNOT be deleted individually — `DeleteRegistrationFieldValue` returns `ValidationException Reason="REGISTRATION_FIELD_CANNOT_BE_DELETED"`. But `DeleteRegistration` on a DRAFT/CREATED registration succeeds (returns `RegistrationStatus=DELETED`) and cascades away all field values. After delete, `DescribeRegistrations` drops the row entirely (not even a DELETED tombstone) and `ListBrandProfiles` returns empty — clean verification.

**ValidateNotifyCodeVerification oracle (L4 "status-only, no ResourceNotFound"):** input `destinationIdentity` (E.164, required) + `code` (required) + optional `referenceId`; output is `status` only. For a NEVER-SENT (destination, code) tuple it returns HTTP 200 `status=INVALID` — NOT `ResourceNotFoundException`, NOT `AccessDeniedException`. The API does not need an origination identity to submit and does not leak an existence oracle: "no code ever sent" and "wrong code" collapse to the same `INVALID`. Read-only, persists nothing.

---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_StatusRecord.html
---

# StatusRecord
<a name="API_StatusRecord"></a>

An object that contains status information for a reputation entity, including the current status, cause description, and timestamp.

## Contents
<a name="API_StatusRecord_Contents"></a>

 ** Cause **   <a name="SES-Type-StatusRecord-Cause"></a>
A description of the reason for the current status, or null if no specific cause is available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** LastUpdatedTimestamp **   <a name="SES-Type-StatusRecord-LastUpdatedTimestamp"></a>
The timestamp when this status was last updated.
Type: Timestamp
Required: No

 ** Status **   <a name="SES-Type-StatusRecord-Status"></a>
The current sending status. This can be one of the following:
+  `ENABLED` – Sending is allowed.
+  `DISABLED` – Sending is prevented.
+  `REINSTATED` – Sending is allowed even with active reputation findings.
Type: String
Valid Values: `ENABLED | REINSTATED | DISABLED`
Required: No

## See Also
<a name="API_StatusRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/StatusRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/StatusRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/StatusRecord)

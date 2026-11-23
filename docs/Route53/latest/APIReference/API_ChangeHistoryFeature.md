---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeHistoryFeature.html
---

# ChangeHistoryFeature

The status of Change History for the hosted zone.

## Contents
<a name="API_ChangeHistoryFeature_Contents"></a>

 ** RetentionStartsAt **   <a name="Route53-Type-ChangeHistoryFeature-RetentionStartsAt"></a>
The earliest date and time from which you can read the change history of the hosted zone. Route 53 returns this value only when `Status` is `ENABLED`.
Type: Timestamp
Required: No

 ** Status **   <a name="Route53-Type-ChangeHistoryFeature-Status"></a>
Indicates whether Change History is turned on for the hosted zone. Valid values are the following:
+  `ENABLED`: Change History is turned on for the hosted zone.
+  `DISABLED`: Change History is turned off for the hosted zone.
Route 53 turns Change History on or off when the hosted zone moves to or from a tier that includes it.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_ChangeHistoryFeature_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ChangeHistoryFeature)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ChangeHistoryFeature)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ChangeHistoryFeature)

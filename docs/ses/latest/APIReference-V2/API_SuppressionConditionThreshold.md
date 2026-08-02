---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SuppressionConditionThreshold.html
---

# SuppressionConditionThreshold
<a name="API_SuppressionConditionThreshold"></a>

Contains Auto Validation settings, allowing you to suppress sending to specific destination(s) if they do not meet required threshold. For details on Auto Validation, see [Auto Validation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/email-validation.html).

## Contents
<a name="API_SuppressionConditionThreshold_Contents"></a>

 ** ConditionThresholdEnabled **   <a name="SES-Type-SuppressionConditionThreshold-ConditionThresholdEnabled"></a>
Indicates whether Auto Validation is enabled for suppression. Set to `ENABLED` to enable the Auto Validation feature, or set to `DISABLED` to disable it.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** OverallConfidenceThreshold **   <a name="SES-Type-SuppressionConditionThreshold-OverallConfidenceThreshold"></a>
The overall confidence threshold used to determine suppression decisions.
Type: [SuppressionConfidenceThreshold](API_SuppressionConfidenceThreshold.md) object
Required: No

## See Also
<a name="API_SuppressionConditionThreshold_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/SuppressionConditionThreshold)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/SuppressionConditionThreshold)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/SuppressionConditionThreshold)

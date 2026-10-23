---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PerformanceStatusSummary.html
---

# PerformanceStatusSummary
<a name="API_PerformanceStatusSummary"></a>

Provides a summary of the performance status check results for an instance.

## Contents
<a name="API_PerformanceStatusSummary_Contents"></a>

 ** impairedSince **
The date and time when the performance status became impaired.
Type: Timestamp
Required: No

 ** remediation **
The recommended action to remediate the impaired instance, if one is available. This value is returned only when the instance is impaired.
Type: String
Required: No

 ** status **
The current status.
Type: String
Valid Values: `ok | impaired | insufficient-data | not-applicable | initializing`
Required: No

## See Also
<a name="API_PerformanceStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PerformanceStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PerformanceStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PerformanceStatusSummary)

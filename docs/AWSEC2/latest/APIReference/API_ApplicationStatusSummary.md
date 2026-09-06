---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ApplicationStatusSummary.html
---

# ApplicationStatusSummary
<a name="API_ApplicationStatusSummary"></a>

Provides a summary of the application-level health status for an instance.

## Contents
<a name="API_ApplicationStatusSummary_Contents"></a>

 ** impairedSince **
The date and time when the application status became impaired.
Type: Timestamp
Required: No

 ** status **
The current status.
Type: String
Valid Values: `ok | impaired | insufficient-data | not-applicable | initializing`
Required: No

## See Also
<a name="API_ApplicationStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ApplicationStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ApplicationStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ApplicationStatusSummary)

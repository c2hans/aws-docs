---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsStatusSummary.html
---

# EbsStatusSummary
<a name="API_EbsStatusSummary"></a>

Provides a summary of the attached EBS volume status for an instance.

## Contents
<a name="API_EbsStatusSummary_Contents"></a>

 ** Details.N **
Details about the attached EBS status check for an instance.
Type: Array of [EbsStatusDetails](API_EbsStatusDetails.md) objects
Required: No

 ** status **
The current status.
Type: String
Valid Values: `ok | impaired | insufficient-data | not-applicable | initializing`
Required: No

## See Also
<a name="API_EbsStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EbsStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EbsStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EbsStatusSummary)

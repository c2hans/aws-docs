---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceStatusSummary.html
---

# InstanceStatusSummary
<a name="API_InstanceStatusSummary"></a>

Describes the status of an instance.

## Contents
<a name="API_InstanceStatusSummary_Contents"></a>

 ** Details.N **
The system instance health or application instance health.
Type: Array of [InstanceStatusDetails](API_InstanceStatusDetails.md) objects
Required: No

 ** status **
The status.
Type: String
Valid Values: `ok | impaired | insufficient-data | not-applicable | initializing`
Required: No

## See Also
<a name="API_InstanceStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceStatusSummary)

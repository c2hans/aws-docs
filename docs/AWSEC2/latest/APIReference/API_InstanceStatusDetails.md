---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceStatusDetails.html
---

# InstanceStatusDetails
<a name="API_InstanceStatusDetails"></a>

Describes the instance status.

## Contents
<a name="API_InstanceStatusDetails_Contents"></a>

 ** impairedSince **
The time when a status check failed. For an instance that was launched and impaired, this is the time when the instance was launched.
Type: Timestamp
Required: No

 ** name **
The type of instance status.
Type: String
Valid Values: `reachability`
Required: No

 ** status **
The status.
Type: String
Valid Values: `passed | failed | insufficient-data | initializing`
Required: No

## See Also
<a name="API_InstanceStatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceStatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceStatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceStatusDetails)

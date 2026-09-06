---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AwsEc2InstanceViolation.html
---

# AwsEc2InstanceViolation
<a name="API_AwsEc2InstanceViolation"></a>

Violation detail for an EC2 instance resource.

## Contents
<a name="API_AwsEc2InstanceViolation_Contents"></a>

 ** AwsEc2NetworkInterfaceViolations **   <a name="fms-Type-AwsEc2InstanceViolation-AwsEc2NetworkInterfaceViolations"></a>
Violation detail for network interfaces associated with the EC2 instance.
Type: Array of [AwsEc2NetworkInterfaceViolation](API_AwsEc2NetworkInterfaceViolation.md) objects
Required: No

 ** ViolationTarget **   <a name="fms-Type-AwsEc2InstanceViolation-ViolationTarget"></a>
The resource ID of the EC2 instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_AwsEc2InstanceViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/AwsEc2InstanceViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/AwsEc2InstanceViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/AwsEc2InstanceViolation)

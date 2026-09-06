---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceTypeSpecificationRequest.html
---

# InstanceTypeSpecificationRequest
<a name="API_InstanceTypeSpecificationRequest"></a>

The instance type specification for an AMI, which contains lists of supported and unsupported instance types that define which instance types are compatible with the AMI.

## Contents
<a name="API_InstanceTypeSpecificationRequest_Contents"></a>

 ** SupportedInstanceType.N **
The instance types that the AMI supports. You can specify instance type names or use wildcard patterns (for example, `t3.*`).
Constraints: Maximum 100 entries. Each entry must be 1-24 characters and match the pattern `^[A-Za-z0-9_.*-]+$`. Consecutive wildcard characters (`**`) are not allowed. Entries must be unique within each list and across both lists; duplicate entries cause the request to fail.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 24.
Required: No

 ** UnsupportedInstanceType.N **
The instance types that the AMI does not support. You can specify instance type names or use wildcard patterns (for example, `t3.*`).
Constraints: Maximum 100 entries. Each entry must be 1-24 characters and match the pattern `^[A-Za-z0-9_.*-]+$`. Consecutive wildcard characters (`**`) are not allowed. Entries must be unique within each list and across both lists; duplicate entries cause the request to fail.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 24.
Required: No

## See Also
<a name="API_InstanceTypeSpecificationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceTypeSpecificationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceTypeSpecificationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceTypeSpecificationRequest)

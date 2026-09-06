---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_VpcConfigResponse.html
---

# VpcConfigResponse
<a name="API_VpcConfigResponse"></a>

VPC configuration for workflow runs with computed VPC ID.

## Contents
<a name="API_VpcConfigResponse_Contents"></a>

 ** securityGroupIds **   <a name="omics-Type-VpcConfigResponse-securityGroupIds"></a>
List of security group IDs.
Type: Array of strings
Length Constraints: Minimum length of 4. Maximum length of 128.
Pattern: `sg-[0-9a-f]+`
Required: No

 ** subnetIds **   <a name="omics-Type-VpcConfigResponse-subnetIds"></a>
List of subnet IDs.
Type: Array of strings
Length Constraints: Minimum length of 8. Maximum length of 128.
Pattern: `subnet-[0-9a-f]+`
Required: No

 ** vpcId **   <a name="omics-Type-VpcConfigResponse-vpcId"></a>
VPC ID computed from the provided subnet IDs.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 128.
Pattern: `vpc-[0-9a-f]+`
Required: No

## See Also
<a name="API_VpcConfigResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/VpcConfigResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/VpcConfigResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/VpcConfigResponse)

---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_PipelineEndpointVpcOptions.html
---

# PipelineEndpointVpcOptions
<a name="API_osis_PipelineEndpointVpcOptions"></a>

Configuration settings for the VPC endpoint, specifying network access controls.

## Contents
<a name="API_osis_PipelineEndpointVpcOptions_Contents"></a>

 ** SecurityGroupIds **   <a name="opensearchservice-Type-osis_PipelineEndpointVpcOptions-SecurityGroupIds"></a>
A list of security group IDs that control network access to the pipeline endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Length Constraints: Minimum length of 11. Maximum length of 20.
Pattern: `sg-\w{8}(\w{9})?`
Required: No

 ** SubnetIds **   <a name="opensearchservice-Type-osis_PipelineEndpointVpcOptions-SubnetIds"></a>
A list of subnet IDs where the pipeline endpoint network interfaces are created.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `subnet-\w{8}(\w{9})?`
Required: No

## See Also
<a name="API_osis_PipelineEndpointVpcOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/PipelineEndpointVpcOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/PipelineEndpointVpcOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/PipelineEndpointVpcOptions)

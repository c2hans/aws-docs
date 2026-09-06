---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_VpcOptions.html
---

# VpcOptions
<a name="API_osis_VpcOptions"></a>

Options that specify the subnets and security groups for an OpenSearch Ingestion VPC endpoint.

## Contents
<a name="API_osis_VpcOptions_Contents"></a>

 ** SubnetIds **   <a name="opensearchservice-Type-osis_VpcOptions-SubnetIds"></a>
A list of subnet IDs associated with the VPC endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `subnet-\w{8}(\w{9})?`
Required: Yes

 ** SecurityGroupIds **   <a name="opensearchservice-Type-osis_VpcOptions-SecurityGroupIds"></a>
A list of security groups associated with the VPC endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Length Constraints: Minimum length of 11. Maximum length of 20.
Pattern: `sg-\w{8}(\w{9})?`
Required: No

 ** VpcAttachmentOptions **   <a name="opensearchservice-Type-osis_VpcOptions-VpcAttachmentOptions"></a>
Options for attaching a VPC to a pipeline.
Type: [VpcAttachmentOptions](API_osis_VpcAttachmentOptions.md) object
Required: No

 ** VpcEndpointManagement **   <a name="opensearchservice-Type-osis_VpcOptions-VpcEndpointManagement"></a>
Defines whether you or Amazon OpenSearch Ingestion service create and manage the VPC endpoint configured for the pipeline.
Type: String
Valid Values: `CUSTOMER | SERVICE`
Required: No

## See Also
<a name="API_osis_VpcOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/VpcOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/VpcOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/VpcOptions)

---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_PipelineEndpoint.html
---

# PipelineEndpoint
<a name="API_osis_PipelineEndpoint"></a>

Represents a VPC endpoint for an OpenSearch Ingestion pipeline, enabling private connectivity between your VPC and the pipeline.

## Contents
<a name="API_osis_PipelineEndpoint_Contents"></a>

 ** EndpointId **   <a name="opensearchservice-Type-osis_PipelineEndpoint-EndpointId"></a>
The unique identifier for the pipeline endpoint.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 512.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]+$`
Required: No

 ** IngestEndpointUrl **   <a name="opensearchservice-Type-osis_PipelineEndpoint-IngestEndpointUrl"></a>
The URL used to ingest data to the pipeline through the VPC endpoint.
Type: String
Required: No

 ** PipelineArn **   <a name="opensearchservice-Type-osis_PipelineEndpoint-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline associated with this endpoint.
Type: String
Length Constraints: Minimum length of 46. Maximum length of 76.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`
Required: No

 ** Status **   <a name="opensearchservice-Type-osis_PipelineEndpoint-Status"></a>
The current status of the pipeline endpoint.
Type: String
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | DELETING | REVOKING | REVOKED`
Required: No

 ** VpcId **   <a name="opensearchservice-Type-osis_PipelineEndpoint-VpcId"></a>
The ID of the VPC where the pipeline endpoint is created.
Type: String
Required: No

 ** VpcOptions **   <a name="opensearchservice-Type-osis_PipelineEndpoint-VpcOptions"></a>
Configuration options for the VPC endpoint, including subnet and security group settings.
Type: [PipelineEndpointVpcOptions](API_osis_PipelineEndpointVpcOptions.md) object
Required: No

## See Also
<a name="API_osis_PipelineEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/PipelineEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/PipelineEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/PipelineEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

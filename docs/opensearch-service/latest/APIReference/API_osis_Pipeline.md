---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_Pipeline.html
---

# Pipeline
<a name="API_osis_Pipeline"></a>

Information about an existing OpenSearch Ingestion pipeline.

## Contents
<a name="API_osis_Pipeline_Contents"></a>

 ** BufferOptions **   <a name="opensearchservice-Type-osis_Pipeline-BufferOptions"></a>
Options that specify the configuration of a persistent buffer. To configure how OpenSearch Ingestion encrypts this data, set the `EncryptionAtRestOptions`. For more information, see [Persistent buffering](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-features-overview.html#persistent-buffering).
Type: [BufferOptions](API_osis_BufferOptions.md) object
Required: No

 ** CreatedAt **   <a name="opensearchservice-Type-osis_Pipeline-CreatedAt"></a>
The date and time when the pipeline was created.
Type: Timestamp
Required: No

 ** Destinations **   <a name="opensearchservice-Type-osis_Pipeline-Destinations"></a>
Destinations to which the pipeline writes data.
Type: Array of [PipelineDestination](API_osis_PipelineDestination.md) objects
Required: No

 ** EncryptionAtRestOptions **   <a name="opensearchservice-Type-osis_Pipeline-EncryptionAtRestOptions"></a>
Options to control how OpenSearch encrypts buffer data.
Type: [EncryptionAtRestOptions](API_osis_EncryptionAtRestOptions.md) object
Required: No

 ** IngestEndpointUrls **   <a name="opensearchservice-Type-osis_Pipeline-IngestEndpointUrls"></a>
The ingestion endpoints for the pipeline, which you can send data to.
Type: Array of strings
Required: No

 ** LastUpdatedAt **   <a name="opensearchservice-Type-osis_Pipeline-LastUpdatedAt"></a>
The date and time when the pipeline was last updated.
Type: Timestamp
Required: No

 ** LogPublishingOptions **   <a name="opensearchservice-Type-osis_Pipeline-LogPublishingOptions"></a>
Key-value pairs that represent log publishing settings.
Type: [LogPublishingOptions](API_osis_LogPublishingOptions.md) object
Required: No

 ** MaxUnits **   <a name="opensearchservice-Type-osis_Pipeline-MaxUnits"></a>
The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
Type: Integer
Required: No

 ** MinUnits **   <a name="opensearchservice-Type-osis_Pipeline-MinUnits"></a>
The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
Type: Integer
Required: No

 ** PipelineArn **   <a name="opensearchservice-Type-osis_Pipeline-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Required: No

 ** PipelineConfigurationBody **   <a name="opensearchservice-Type-osis_Pipeline-PipelineConfigurationBody"></a>
The Data Prepper pipeline configuration in YAML format.
Type: String
Required: No

 ** PipelineName **   <a name="opensearchservice-Type-osis_Pipeline-PipelineName"></a>
The name of the pipeline.
Type: String
Required: No

 ** PipelineRoleArn **   <a name="opensearchservice-Type-osis_Pipeline-PipelineRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the pipeline uses to access AWS resources.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b|aws\-iso\-e|aws\-iso\-f):iam::[0-9]+:role\/.*$`
Required: No

 ** ServiceVpcEndpoints **   <a name="opensearchservice-Type-osis_Pipeline-ServiceVpcEndpoints"></a>
A list of VPC endpoints that OpenSearch Ingestion has created to other AWS services.
Type: Array of [ServiceVpcEndpoint](API_osis_ServiceVpcEndpoint.md) objects
Required: No

 ** Status **   <a name="opensearchservice-Type-osis_Pipeline-Status"></a>
The current status of the pipeline.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | STARTING | START_FAILED | STOPPING | STOPPED`
Required: No

 ** StatusReason **   <a name="opensearchservice-Type-osis_Pipeline-StatusReason"></a>
The reason for the current status of the pipeline.
Type: [PipelineStatusReason](API_osis_PipelineStatusReason.md) object
Required: No

 ** Tags **   <a name="opensearchservice-Type-osis_Pipeline-Tags"></a>
A list of tags associated with the given pipeline.
Type: Array of [Tag](API_osis_Tag.md) objects
Required: No

 ** VpcEndpoints **   <a name="opensearchservice-Type-osis_Pipeline-VpcEndpoints"></a>
The VPC interface endpoints that have access to the pipeline.
Type: Array of [VpcEndpoint](API_osis_VpcEndpoint.md) objects
Required: No

 ** VpcEndpointService **   <a name="opensearchservice-Type-osis_Pipeline-VpcEndpointService"></a>
The VPC endpoint service name for the pipeline.
Type: String
Required: No

## See Also
<a name="API_osis_Pipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/Pipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/Pipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/Pipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

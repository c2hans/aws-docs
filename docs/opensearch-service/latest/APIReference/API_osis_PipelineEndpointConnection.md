---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_PipelineEndpointConnection.html
---

# PipelineEndpointConnection
<a name="API_osis_PipelineEndpointConnection"></a>

Represents a connection to a pipeline endpoint, containing details about the endpoint association.

## Contents
<a name="API_osis_PipelineEndpointConnection_Contents"></a>

 ** EndpointId **   <a name="opensearchservice-Type-osis_PipelineEndpointConnection-EndpointId"></a>
The unique identifier of the endpoint in the connection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 512.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]+$`
Required: No

 ** PipelineArn **   <a name="opensearchservice-Type-osis_PipelineEndpointConnection-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline in the endpoint connection.
Type: String
Length Constraints: Minimum length of 46. Maximum length of 76.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`
Required: No

 ** Status **   <a name="opensearchservice-Type-osis_PipelineEndpointConnection-Status"></a>
The current status of the pipeline endpoint connection.
Type: String
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | DELETING | REVOKING | REVOKED`
Required: No

 ** VpcEndpointOwner **   <a name="opensearchservice-Type-osis_PipelineEndpointConnection-VpcEndpointOwner"></a>
The AWS account ID that owns the VPC endpoint used in this connection.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\\d{12}$`
Required: No

## See Also
<a name="API_osis_PipelineEndpointConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/PipelineEndpointConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/PipelineEndpointConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/PipelineEndpointConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

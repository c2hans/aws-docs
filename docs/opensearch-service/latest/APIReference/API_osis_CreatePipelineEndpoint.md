---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_CreatePipelineEndpoint.html
---

# CreatePipelineEndpoint
<a name="API_osis_CreatePipelineEndpoint"></a>

Creates a VPC endpoint for an OpenSearch Ingestion pipeline. Pipeline endpoints allow you to ingest data from your VPC into pipelines that you have access to.

## Request Syntax
<a name="API_osis_CreatePipelineEndpoint_RequestSyntax"></a>

```
POST /2022-01-01/osis/createPipelineEndpoint HTTP/1.1
Content-type: application/json

{
   "PipelineArn": "{{string}}",
   "VpcOptions": {
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_osis_CreatePipelineEndpoint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_osis_CreatePipelineEndpoint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PipelineArn](#API_osis_CreatePipelineEndpoint_RequestSyntax) **   <a name="opensearchservice-osis_CreatePipelineEndpoint-request-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline to create the endpoint for.
Type: String
Length Constraints: Minimum length of 46. Maximum length of 76.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`
Required: Yes

 ** [VpcOptions](#API_osis_CreatePipelineEndpoint_RequestSyntax) **   <a name="opensearchservice-osis_CreatePipelineEndpoint-request-VpcOptions"></a>
Container for the VPC configuration for the pipeline endpoint, including subnet IDs and security group IDs.
Type: [PipelineEndpointVpcOptions](API_osis_PipelineEndpointVpcOptions.md) object
Required: Yes

## Response Syntax
<a name="API_osis_CreatePipelineEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EndpointId": "string",
   "PipelineArn": "string",
   "Status": "string",
   "VpcId": "string"
}
```

## Response Elements
<a name="API_osis_CreatePipelineEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointId](#API_osis_CreatePipelineEndpoint_ResponseSyntax) **   <a name="opensearchservice-osis_CreatePipelineEndpoint-response-EndpointId"></a>
The unique identifier of the pipeline endpoint.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 512.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]+$`

 ** [PipelineArn](#API_osis_CreatePipelineEndpoint_ResponseSyntax) **   <a name="opensearchservice-osis_CreatePipelineEndpoint-response-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline associated with the endpoint.
Type: String
Length Constraints: Minimum length of 46. Maximum length of 76.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`

 ** [Status](#API_osis_CreatePipelineEndpoint_ResponseSyntax) **   <a name="opensearchservice-osis_CreatePipelineEndpoint-response-Status"></a>
The current status of the pipeline endpoint.
Type: String
Valid Values: `CREATING | ACTIVE | CREATE_FAILED | DELETING | REVOKING | REVOKED`

 ** [VpcId](#API_osis_CreatePipelineEndpoint_ResponseSyntax) **   <a name="opensearchservice-osis_CreatePipelineEndpoint-response-VpcId"></a>
The ID of the VPC where the pipeline endpoint was created.
Type: String

## Errors
<a name="API_osis_CreatePipelineEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to access the resource.
HTTP Status Code: 403

 ** DisabledOperationException **
Exception is thrown when an operation has been disabled.
HTTP Status Code: 409

 ** InternalException **
The request failed because of an unknown error, exception, or failure (the failure is internal to the service).
HTTP Status Code: 500

 ** LimitExceededException **
You attempted to create more than the allowed number of tags.
HTTP Status Code: 409

 ** ResourceNotFoundException **
You attempted to access or delete a resource that does not exist.
HTTP Status Code: 404

 ** ValidationException **
An exception for missing or invalid input fields.
HTTP Status Code: 400

## See Also
<a name="API_osis_CreatePipelineEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/CreatePipelineEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/CreatePipelineEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/CreatePipelineEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/CreatePipelineEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/CreatePipelineEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/CreatePipelineEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/CreatePipelineEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/CreatePipelineEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/CreatePipelineEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/CreatePipelineEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

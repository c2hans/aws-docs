---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_GetPipeline.html
---

# GetPipeline
<a name="API_osis_GetPipeline"></a>

Retrieves information about an OpenSearch Ingestion pipeline.

## Request Syntax
<a name="API_osis_GetPipeline_RequestSyntax"></a>

```
GET /2022-01-01/osis/getPipeline/{{PipelineName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_osis_GetPipeline_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PipelineName](#API_osis_GetPipeline_RequestSyntax) **   <a name="opensearchservice-osis_GetPipeline-request-uri-PipelineName"></a>
The name of the pipeline.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_osis_GetPipeline_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_osis_GetPipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Pipeline": {
      "BufferOptions": {
         "PersistentBufferEnabled": boolean
      },
      "CreatedAt": number,
      "Destinations": [
         {
            "Endpoint": "string",
            "ServiceName": "string"
         }
      ],
      "EncryptionAtRestOptions": {
         "KmsKeyArn": "string"
      },
      "IngestEndpointUrls": [ "string" ],
      "LastUpdatedAt": number,
      "LogPublishingOptions": {
         "CloudWatchLogDestination": {
            "LogGroup": "string"
         },
         "IsLoggingEnabled": boolean
      },
      "MaxUnits": number,
      "MinUnits": number,
      "PipelineArn": "string",
      "PipelineConfigurationBody": "string",
      "PipelineName": "string",
      "PipelineRoleArn": "string",
      "ServiceVpcEndpoints": [
         {
            "ServiceName": "string",
            "VpcEndpointId": "string"
         }
      ],
      "Status": "string",
      "StatusReason": {
         "Description": "string"
      },
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "VpcEndpoints": [
         {
            "VpcEndpointId": "string",
            "VpcId": "string",
            "VpcOptions": {
               "SecurityGroupIds": [ "string" ],
               "SubnetIds": [ "string" ],
               "VpcAttachmentOptions": {
                  "AttachToVpc": boolean,
                  "CidrBlock": "string"
               },
               "VpcEndpointManagement": "string"
            }
         }
      ],
      "VpcEndpointService": "string"
   }
}
```

## Response Elements
<a name="API_osis_GetPipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Pipeline](#API_osis_GetPipeline_ResponseSyntax) **   <a name="opensearchservice-osis_GetPipeline-response-Pipeline"></a>
Detailed information about the requested pipeline.
Type: [Pipeline](API_osis_Pipeline.md) object

## Errors
<a name="API_osis_GetPipeline_Errors"></a>

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

 ** ResourceNotFoundException **
You attempted to access or delete a resource that does not exist.
HTTP Status Code: 404

 ** ValidationException **
An exception for missing or invalid input fields.
HTTP Status Code: 400

## See Also
<a name="API_osis_GetPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/GetPipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/GetPipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/GetPipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/GetPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/GetPipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/GetPipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/GetPipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/GetPipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/GetPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/GetPipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

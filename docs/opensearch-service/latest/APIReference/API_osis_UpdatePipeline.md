---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_UpdatePipeline.html
---

# UpdatePipeline
<a name="API_osis_UpdatePipeline"></a>

Updates an OpenSearch Ingestion pipeline. For more information, see [Updating Amazon OpenSearch Ingestion pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/update-pipeline.html).

## Request Syntax
<a name="API_osis_UpdatePipeline_RequestSyntax"></a>

```
PUT /2022-01-01/osis/updatePipeline/{{PipelineName}} HTTP/1.1
Content-type: application/json

{
   "BufferOptions": {
      "PersistentBufferEnabled": {{boolean}}
   },
   "EncryptionAtRestOptions": {
      "KmsKeyArn": "{{string}}"
   },
   "LogPublishingOptions": {
      "CloudWatchLogDestination": {
         "LogGroup": "{{string}}"
      },
      "IsLoggingEnabled": {{boolean}}
   },
   "MaxUnits": {{number}},
   "MinUnits": {{number}},
   "PipelineConfigurationBody": "{{string}}",
   "PipelineRoleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_osis_UpdatePipeline_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PipelineName](#API_osis_UpdatePipeline_RequestSyntax) **   <a name="opensearchservice-osis_UpdatePipeline-request-uri-PipelineName"></a>
The name of the pipeline to update.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_osis_UpdatePipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BufferOptions](#API_osis_UpdatePipeline_RequestSyntax) **   <a name="opensearchservice-osis_UpdatePipeline-request-BufferOptions"></a>
Key-value pairs to configure persistent buffering for the pipeline.
Type: [BufferOptions](API_osis_BufferOptions.md) object
Required: No

 ** [EncryptionAtRestOptions](#API_osis_UpdatePipeline_RequestSyntax) **   <a name="opensearchservice-osis_UpdatePipeline-request-EncryptionAtRestOptions"></a>
Key-value pairs to configure encryption for data that is written to a persistent buffer.
Type: [EncryptionAtRestOptions](API_osis_EncryptionAtRestOptions.md) object
Required: No

 ** [LogPublishingOptions](#API_osis_UpdatePipeline_RequestSyntax) **   <a name="opensearchservice-osis_UpdatePipeline-request-LogPublishingOptions"></a>
Key-value pairs to configure log publishing.
Type: [LogPublishingOptions](API_osis_LogPublishingOptions.md) object
Required: No

 ** [MaxUnits](#API_osis_UpdatePipeline_RequestSyntax) **   <a name="opensearchservice-osis_UpdatePipeline-request-MaxUnits"></a>
The maximum pipeline capacity, in Ingestion Compute Units (ICUs)
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [MinUnits](#API_osis_UpdatePipeline_RequestSyntax) **   <a name="opensearchservice-osis_UpdatePipeline-request-MinUnits"></a>
The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [PipelineConfigurationBody](#API_osis_UpdatePipeline_RequestSyntax) **   <a name="opensearchservice-osis_UpdatePipeline-request-PipelineConfigurationBody"></a>
The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with `\n`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: No

 ** [PipelineRoleArn](#API_osis_UpdatePipeline_RequestSyntax) **   <a name="opensearchservice-osis_UpdatePipeline-request-PipelineRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants the pipeline permission to access AWS resources.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b|aws\-iso\-e|aws\-iso\-f):iam::[0-9]+:role\/.*$`
Required: No

## Response Syntax
<a name="API_osis_UpdatePipeline_ResponseSyntax"></a>

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
<a name="API_osis_UpdatePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Pipeline](#API_osis_UpdatePipeline_ResponseSyntax) **   <a name="opensearchservice-osis_UpdatePipeline-response-Pipeline"></a>
Container for information about the updated pipeline.
Type: [Pipeline](API_osis_Pipeline.md) object

## Errors
<a name="API_osis_UpdatePipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to access the resource.
HTTP Status Code: 403

 ** ConflictException **
The client attempted to remove a resource that is currently in use.
HTTP Status Code: 409

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
<a name="API_osis_UpdatePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/UpdatePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/UpdatePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/UpdatePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/UpdatePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/UpdatePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/UpdatePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/UpdatePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/UpdatePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/UpdatePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/UpdatePipeline)

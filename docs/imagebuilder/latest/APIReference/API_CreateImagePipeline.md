---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImagePipeline.html
---

# CreateImagePipeline
<a name="API_CreateImagePipeline"></a>

Creates a new image pipeline. Image pipelines enable you to automate the creation and distribution of images.

## Request Syntax
<a name="API_CreateImagePipeline_RequestSyntax"></a>

```
PUT /CreateImagePipeline HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "containerRecipeArn": "{{string}}",
   "description": "{{string}}",
   "distributionConfigurationArn": "{{string}}",
   "enhancedImageMetadataEnabled": {{boolean}},
   "executionRole": "{{string}}",
   "imageRecipeArn": "{{string}}",
   "imageScanningConfiguration": {
      "ecrConfiguration": {
         "containerTags": [ "{{string}}" ],
         "repositoryName": "{{string}}"
      },
      "imageScanningEnabled": {{boolean}}
   },
   "imageTags": {
      "{{string}}" : "{{string}}"
   },
   "imageTestsConfiguration": {
      "imageTestsEnabled": {{boolean}},
      "timeoutMinutes": {{number}}
   },
   "infrastructureConfigurationArn": "{{string}}",
   "loggingConfiguration": {
      "imageLogGroupName": "{{string}}",
      "pipelineLogGroupName": "{{string}}"
   },
   "name": "{{string}}",
   "schedule": {
      "autoDisablePolicy": {
         "failureCount": {{number}}
      },
      "pipelineExecutionStartCondition": "{{string}}",
      "scheduleExpression": "{{string}}",
      "timezone": "{{string}}"
   },
   "status": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "workflows": [
      {
         "onFailure": "{{string}}",
         "parallelGroup": "{{string}}",
         "parameters": [
            {
               "name": "{{string}}",
               "value": [ "{{string}}" ]
            }
         ],
         "workflowArn": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateImagePipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateImagePipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-clientToken"></a>
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [containerRecipeArn](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-containerRecipeArn"></a>
The Amazon Resource Name (ARN) of the container recipe that is used to configure images created by this container pipeline.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

 ** [description](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-description"></a>
The description of the image pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [distributionConfigurationArn](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration that will be used to configure and distribute images created by this image pipeline.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`
Required: No

 ** [enhancedImageMetadataEnabled](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-enhancedImageMetadataEnabled"></a>
Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
Type: Boolean
Required: No

 ** [executionRole](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-executionRole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** [imageRecipeArn](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-imageRecipeArn"></a>
The Amazon Resource Name (ARN) of the image recipe that will be used to configure images created by this image pipeline.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

 ** [imageScanningConfiguration](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-imageScanningConfiguration"></a>
Contains settings for vulnerability scans.
Type: [ImageScanningConfiguration](API_ImageScanningConfiguration.md) object
Required: No

 ** [imageTags](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-imageTags"></a>
The tags to be applied to the images produced by this pipeline.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [imageTestsConfiguration](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-imageTestsConfiguration"></a>
The image test configuration of the image pipeline.
Type: [ImageTestsConfiguration](API_ImageTestsConfiguration.md) object
Required: No

 ** [infrastructureConfigurationArn](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that will be used to build images created by this image pipeline.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
Required: Yes

 ** [loggingConfiguration](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-loggingConfiguration"></a>
Specifies the logging configuration for the image pipeline. Use this to define custom CloudWatch Logs log groups for your pipeline execution logs and image build logs. The service manages log groups with names starting with `/aws/imagebuilder/` using the service-linked role. For custom log group names outside of this prefix, you must also provide an `executionRole`.
Type: [PipelineLoggingConfiguration](API_PipelineLoggingConfiguration.md) object
Required: No

 ** [name](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-name"></a>
The name of the image pipeline.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** [schedule](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-schedule"></a>
The schedule of the image pipeline.
Type: [Schedule](API_Schedule.md) object
Required: No

 ** [status](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-status"></a>
The status of the image pipeline.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** [tags](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-tags"></a>
The tags of the image pipeline.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [workflows](#API_CreateImagePipeline_RequestSyntax) **   <a name="imagebuilder-CreateImagePipeline-request-workflows"></a>
Contains an array of workflow configuration objects.
Type: Array of [WorkflowConfiguration](API_WorkflowConfiguration.md) objects
Required: No

## Response Syntax
<a name="API_CreateImagePipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "imagePipelineArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_CreateImagePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreateImagePipeline_ResponseSyntax) **   <a name="imagebuilder-CreateImagePipeline-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [imagePipelineArn](#API_CreateImagePipeline_ResponseSyntax) **   <a name="imagebuilder-CreateImagePipeline-response-imagePipelineArn"></a>
The Amazon Resource Name (ARN) of the image pipeline that was created by this request.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-pipeline/[a-z0-9-_]+$`

 ** [requestId](#API_CreateImagePipeline_ResponseSyntax) **   <a name="imagebuilder-CreateImagePipeline-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_CreateImagePipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the specific operation.
HTTP Status Code: 429

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The resource that you are trying to create already exists.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded the number of permitted resources or operations for this service. For service quotas, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder).
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_CreateImagePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/CreateImagePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/CreateImagePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CreateImagePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/CreateImagePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CreateImagePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/CreateImagePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/CreateImagePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/CreateImagePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateImagePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateImagePipeline)

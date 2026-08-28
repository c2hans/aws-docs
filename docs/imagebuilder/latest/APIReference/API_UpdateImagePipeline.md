---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateImagePipeline.html
---

# UpdateImagePipeline
<a name="API_UpdateImagePipeline"></a>

Updates an image pipeline. Image pipelines enable you to automate the creation and distribution of images. You must specify exactly one recipe for your image, using either a `containerRecipeArn` or an `imageRecipeArn`.

**Note**
UpdateImagePipeline does not support selective updates for the pipeline. You must specify all of the required properties in the update request, not just the properties that have changed.

## Request Syntax
<a name="API_UpdateImagePipeline_RequestSyntax"></a>

```
PUT /UpdateImagePipeline HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "containerRecipeArn": "{{string}}",
   "description": "{{string}}",
   "distributionConfigurationArn": "{{string}}",
   "enhancedImageMetadataEnabled": {{boolean}},
   "executionRole": "{{string}}",
   "imagePipelineArn": "{{string}}",
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
   "schedule": {
      "autoDisablePolicy": {
         "failureCount": {{number}}
      },
      "pipelineExecutionStartCondition": "{{string}}",
      "scheduleExpression": "{{string}}",
      "timezone": "{{string}}"
   },
   "status": "{{string}}",
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
<a name="API_UpdateImagePipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateImagePipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-clientToken"></a>
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [containerRecipeArn](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-containerRecipeArn"></a>
The Amazon Resource Name (ARN) of the container pipeline to update.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

 ** [description](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-description"></a>
The description of the image pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [distributionConfigurationArn](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration that Image Builder uses to configure and distribute images that this image pipeline has updated.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`
Required: No

 ** [enhancedImageMetadataEnabled](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-enhancedImageMetadataEnabled"></a>
Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
Type: Boolean
Required: No

 ** [executionRole](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-executionRole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** [imagePipelineArn](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-imagePipelineArn"></a>
The Amazon Resource Name (ARN) of the image pipeline that you want to update.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-pipeline/[a-z0-9-_]+$`
Required: Yes

 ** [imageRecipeArn](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-imageRecipeArn"></a>
The Amazon Resource Name (ARN) of the image recipe that will be used to configure images updated by this image pipeline.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

 ** [imageScanningConfiguration](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-imageScanningConfiguration"></a>
Contains settings for vulnerability scans.
Type: [ImageScanningConfiguration](API_ImageScanningConfiguration.md) object
Required: No

 ** [imageTags](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-imageTags"></a>
The tags to be applied to the images produced by this pipeline.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [imageTestsConfiguration](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-imageTestsConfiguration"></a>
The image test configuration of the image pipeline.
Type: [ImageTestsConfiguration](API_ImageTestsConfiguration.md) object
Required: No

 ** [infrastructureConfigurationArn](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that Image Builder uses to build images that this image pipeline has updated.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
Required: Yes

 ** [loggingConfiguration](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-loggingConfiguration"></a>
Update logging configuration for the output image that's created when the pipeline runs.
Type: [PipelineLoggingConfiguration](API_PipelineLoggingConfiguration.md) object
Required: No

 ** [schedule](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-schedule"></a>
The schedule of the image pipeline.
Type: [Schedule](API_Schedule.md) object
Required: No

 ** [status](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-status"></a>
The status of the image pipeline.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** [workflows](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-workflows"></a>
Contains the workflows to run for the pipeline.
Type: Array of [WorkflowConfiguration](API_WorkflowConfiguration.md) objects
Required: No

## Response Syntax
<a name="API_UpdateImagePipeline_ResponseSyntax"></a>

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
<a name="API_UpdateImagePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_UpdateImagePipeline_ResponseSyntax) **   <a name="imagebuilder-UpdateImagePipeline-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [imagePipelineArn](#API_UpdateImagePipeline_ResponseSyntax) **   <a name="imagebuilder-UpdateImagePipeline-response-imagePipelineArn"></a>
The Amazon Resource Name (ARN) of the image pipeline that was updated by this request.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-pipeline/[a-z0-9-_]+$`

 ** [requestId](#API_UpdateImagePipeline_ResponseSyntax) **   <a name="imagebuilder-UpdateImagePipeline-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_UpdateImagePipeline_Errors"></a>

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

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_UpdateImagePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/UpdateImagePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/UpdateImagePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/UpdateImagePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/UpdateImagePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/UpdateImagePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/UpdateImagePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/UpdateImagePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/UpdateImagePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/UpdateImagePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/UpdateImagePipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

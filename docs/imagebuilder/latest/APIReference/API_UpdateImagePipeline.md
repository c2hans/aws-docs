---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_UpdateImagePipeline.html
---

# UpdateImagePipeline
<a name="API_UpdateImagePipeline"></a>

Updates an image pipeline. Use image pipelines to automate the creation and distribution of images. You must specify exactly one recipe for your image, using either a `containerRecipeArn` or an `imageRecipeArn`. The recipe must be the same type, image or container, as the pipeline's current recipe.

**Note**
UpdateImagePipeline does not support selective updates. The request replaces the pipeline's entire configuration, so include every setting that you want to keep. Any optional property that you omit is removed or reset to its default.

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
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [containerRecipeArn](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-containerRecipeArn"></a>
The Amazon Resource Name (ARN) of the container recipe that is used to configure images created by this container pipeline. You must specify either this property or `imageRecipeArn`, but not both.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

 ** [description](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-description"></a>
The description of the image pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [distributionConfigurationArn](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration that Image Builder uses to configure and distribute images created by this image pipeline.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`
Required: No

 ** [enhancedImageMetadataEnabled](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-enhancedImageMetadataEnabled"></a>
Specifies whether to collect additional information about the image being created, including the operating system (OS) version and package list. Defaults to `true`.
Type: Boolean
Required: No

 ** [executionRole](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-executionRole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions. If you omit this property, the pipeline reverts to the Image Builder service-linked role.
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
The Amazon Resource Name (ARN) of the image recipe that configures images created by this image pipeline. You must specify either this property or `containerRecipeArn`, but not both.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

 ** [imageScanningConfiguration](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-imageScanningConfiguration"></a>
Contains settings for vulnerability scans that Amazon Inspector runs against the test instance during image creation.
Type: [ImageScanningConfiguration](API_ImageScanningConfiguration.md) object
Required: No

 ** [imageTags](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-imageTags"></a>
The tags that Image Builder applies to the Image Builder image resource that this pipeline's scheduled executions create. These tags don't apply to the output AMI. To tag output AMIs, use `amiTags` in the pipeline's distribution configuration.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [imageTestsConfiguration](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-imageTestsConfiguration"></a>
Specifies the test settings that Image Builder applies to images that this pipeline creates. If you don't provide test settings, Image Builder stores a default configuration with image tests enabled.
Type: [ImageTestsConfiguration](API_ImageTestsConfiguration.md) object
Required: No

 ** [infrastructureConfigurationArn](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that Image Builder uses to build images created by this image pipeline.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
Required: Yes

 ** [loggingConfiguration](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-loggingConfiguration"></a>
Specifies the logging configuration for the image pipeline. Use this to define custom CloudWatch Logs log groups for your pipeline execution logs and image build logs. The service manages log groups with names starting with `/aws/imagebuilder/` using the service-linked role. For custom log group names outside of this prefix, you must also provide an `executionRole`.
Type: [PipelineLoggingConfiguration](API_PipelineLoggingConfiguration.md) object
Required: No

 ** [schedule](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-schedule"></a>
The schedule of the image pipeline. Because the update replaces the entire configuration, omitting this property removes any existing schedule. The pipeline then runs only when you call [StartImagePipelineExecution](API_StartImagePipelineExecution.md).
Type: [Schedule](API_Schedule.md) object
Required: No

 ** [status](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-status"></a>
The status of the image pipeline. Defaults to `ENABLED` when omitted. To keep a pipeline disabled, include this property set to `DISABLED` in your update request.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** [workflows](#API_UpdateImagePipeline_RequestSyntax) **   <a name="imagebuilder-UpdateImagePipeline-request-workflows"></a>
The array of workflow configuration objects for builds that this pipeline starts. You must also specify `executionRole` when you provide workflows.
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
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_UpdateImagePipeline_Examples"></a>

### Update an image pipeline
<a name="API_UpdateImagePipeline_Example_1"></a>

The following example changes the pipeline's schedule to build every day at 6:00 AM UTC.

#### Sample Request
<a name="API_UpdateImagePipeline_Example_1_Request"></a>

```
PUT /UpdateImagePipeline HTTP/1.1
Content-type: application/json

{
    "imagePipelineArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline",
    "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0",
    "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure",
    "schedule": {
        "scheduleExpression": "cron(0 6 * * ? *)",
        "pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
    },
    "status": "ENABLED",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLEddddd"
}
```

#### Sample Response
<a name="API_UpdateImagePipeline_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "7a414b2d-e462-4850-ae7a-fe25a1223e0f",
    "imagePipelineArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-pipeline/my-example-pipeline"
}
```

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/UpdateImagePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/UpdateImagePipeline)

---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImage.html
---

# CreateImage
<a name="API_CreateImage"></a>

Creates a new image. This request will create a new image along with all of the configured output resources defined in the distribution configuration. You must specify exactly one recipe for your image, using either a ContainerRecipeArn or an ImageRecipeArn.

## Request Syntax
<a name="API_CreateImage_RequestSyntax"></a>

```
PUT /CreateImage HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "containerRecipeArn": "{{string}}",
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
   "imageTestsConfiguration": {
      "imageTestsEnabled": {{boolean}},
      "timeoutMinutes": {{number}}
   },
   "infrastructureConfigurationArn": "{{string}}",
   "loggingConfiguration": {
      "logGroupName": "{{string}}"
   },
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
<a name="API_CreateImage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateImage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-clientToken"></a>
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [containerRecipeArn](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-containerRecipeArn"></a>
The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

 ** [distributionConfigurationArn](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of your pipeline.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`
Required: No

 ** [enhancedImageMetadataEnabled](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-enhancedImageMetadataEnabled"></a>
Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
Type: Boolean
Required: No

 ** [executionRole](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-executionRole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** [imageRecipeArn](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-imageRecipeArn"></a>
The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

 ** [imageScanningConfiguration](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-imageScanningConfiguration"></a>
Contains settings for vulnerability scans.
Type: [ImageScanningConfiguration](API_ImageScanningConfiguration.md) object
Required: No

 ** [imageTestsConfiguration](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-imageTestsConfiguration"></a>
The image tests configuration of the image.
Type: [ImageTestsConfiguration](API_ImageTestsConfiguration.md) object
Required: No

 ** [infrastructureConfigurationArn](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
Required: Yes

 ** [loggingConfiguration](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-loggingConfiguration"></a>
Define logging configuration for the image build process.
Type: [ImageLoggingConfiguration](API_ImageLoggingConfiguration.md) object
Required: No

 ** [tags](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-tags"></a>
The tags of the image.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [workflows](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-workflows"></a>
Contains an array of workflow configuration objects.
Type: Array of [WorkflowConfiguration](API_WorkflowConfiguration.md) objects
Required: No

## Response Syntax
<a name="API_CreateImage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "imageBuildVersionArn": "string",
   "latestVersionReferences": {
      "latestMajorVersionArn": "string",
      "latestMinorVersionArn": "string",
      "latestPatchVersionArn": "string",
      "latestVersionArn": "string"
   },
   "requestId": "string"
}
```

## Response Elements
<a name="API_CreateImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreateImage_ResponseSyntax) **   <a name="imagebuilder-CreateImage-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [imageBuildVersionArn](#API_CreateImage_ResponseSyntax) **   <a name="imagebuilder-CreateImage-response-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image that the request created.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [latestVersionReferences](#API_CreateImage_ResponseSyntax) **   <a name="imagebuilder-CreateImage-response-latestVersionReferences"></a>
The resource ARNs with different wildcard variations of semantic versioning.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_CreateImage_ResponseSyntax) **   <a name="imagebuilder-CreateImage-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_CreateImage_Errors"></a>

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

 ** ServiceQuotaExceededException **
You have exceeded the number of permitted resources or operations for this service. For service quotas, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder).
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## See Also
<a name="API_CreateImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/CreateImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/CreateImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CreateImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/CreateImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CreateImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/CreateImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/CreateImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/CreateImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateImage)

---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImage.html
---

# CreateImage
<a name="API_CreateImage"></a>

Creates a new image along with all configured output resources defined in the distribution configuration. You must specify exactly one recipe for your image, using either a `containerRecipeArn` or an `imageRecipeArn`.

The response returns as soon as Image Builder creates the new image resource. The image build process runs asynchronously. To check its progress, call [GetImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImage.html) and check the image status.

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
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [containerRecipeArn](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-containerRecipeArn"></a>
The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested. You must specify either this property or `imageRecipeArn`, but not both.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):container-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

 ** [distributionConfigurationArn](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-distributionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of the image build. If you don't specify a distribution configuration, Image Builder creates the output image only in the account and AWS Region where the build runs.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):distribution-configuration/[a-z0-9-_]+$`
Required: No

 ** [enhancedImageMetadataEnabled](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-enhancedImageMetadataEnabled"></a>
Specifies whether to collect additional information about the image being created, including the operating system (OS) version and package list. Defaults to `true`.
Type: Boolean
Required: No

 ** [executionRole](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-executionRole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions. This property is required if you specify `workflows`. If you don't provide a role, Image Builder uses the Image Builder service-linked role in your account, and creates it if it doesn't exist.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: No

 ** [imageRecipeArn](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-imageRecipeArn"></a>
The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed. You must specify either this property or `containerRecipeArn`, but not both.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):image-recipe/[a-z0-9-_]+/(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
Required: No

 ** [imageScanningConfiguration](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-imageScanningConfiguration"></a>
Settings for vulnerability scans that Amazon Inspector runs during image creation. For AMI output, Amazon Inspector scans the test instance. For container output, Amazon Inspector scans the container image that Image Builder pushes to the Amazon ECR repository specified in `ecrConfiguration`.
Type: [ImageScanningConfiguration](API_ImageScanningConfiguration.md) object
Required: No

 ** [imageTestsConfiguration](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-imageTestsConfiguration"></a>
Settings that determine whether Image Builder runs tests on the image after building it. Image tests are enabled by default.
Type: [ImageTestsConfiguration](API_ImageTestsConfiguration.md) object
Required: No

 ** [infrastructureConfigurationArn](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-infrastructureConfigurationArn"></a>
The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws):infrastructure-configuration/[a-z0-9-_]+$`
Required: Yes

 ** [loggingConfiguration](#API_CreateImage_RequestSyntax) **   <a name="imagebuilder-CreateImage-request-loggingConfiguration"></a>
The CloudWatch Logs log group where Image Builder sends the image build logs. If you specify a log group name outside of the `/aws/imagebuilder/` namespace, you must also provide an `executionRole` that has permission to write to that log group.
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
The array of workflow configuration objects for the build. If you specify workflows, they replace the default workflows that Image Builder otherwise runs for the build, and you must also provide an `executionRole`.
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
A set of wildcard version ARNs that always reference the latest version of the resource. ARNs are included for the latest version overall, and for the latest versions within the same major, minor, and patch levels.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [requestId](#API_CreateImage_ResponseSyntax) **   <a name="imagebuilder-CreateImage-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_CreateImage_Errors"></a>

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

 ** ServiceQuotaExceededException **
You have exceeded the number of permitted resources or operations for this service. For service quotas, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder).
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_CreateImage_Examples"></a>

### Create an image
<a name="API_CreateImage_Example_1"></a>

The following example creates a new image from the specified image recipe and infrastructure configuration.

#### Sample Request
<a name="API_CreateImage_Example_1_Request"></a>

```
PUT /CreateImage HTTP/1.1
Content-type: application/json

{
    "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0",
    "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLEeeeee"
}
```

#### Sample Response
<a name="API_CreateImage_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "62e9b43f-a9fd-4272-89fb-ce6235d07ab4",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLEeeeee",
    "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1",
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0"
    }
}
```

### Create an image with custom build and parallel test workflows
<a name="API_CreateImage_Example_2"></a>

The following example creates an image that uses your custom build and test workflows. It uses the Image Builder service-linked role as the execution role. Both test workflows are in the same parallel group, so they can run at the same time after the build workflow completes.

#### Sample Request
<a name="API_CreateImage_Example_2_Request"></a>

```
PUT /CreateImage HTTP/1.1
Content-type: application/json

{
    "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:111122223333:image-recipe/my-example-recipe/1.0.0",
    "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:111122223333:infrastructure-configuration/my-example-infrastructure",
    "workflows": [
        {
            "workflowArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0/1"
        },
        {
            "workflowArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/test/my-example-integration-tests/1.0.0/1",
            "parallelGroup": "post-build-tests"
        },
        {
            "workflowArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/test/my-example-compliance-tests/1.0.0/1",
            "parallelGroup": "post-build-tests"
        }
    ],
    "executionRole": "arn:aws:iam::111122223333:role/aws-service-role/imagebuilder.amazonaws.com/AWSServiceRoleForImageBuilder",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE01234"
}
```

#### Sample Response
<a name="API_CreateImage_Example_2_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "359f18b1-814f-4857-987f-924214970897",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE01234",
    "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0/1",
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-recipe/1.0.0"
    }
}
```

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateImage)

---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImportVmImage.html
---

# ImportVmImage
<a name="API_ImportVmImage"></a>

Creates an Image Builder image resource from an Amazon EC2 VM import task. The response returns as soon as Image Builder creates the image resource in the `PENDING` state. Image Builder then monitors the import task asynchronously. When the task completes, Image Builder records the AMI that it produced as the new image's output resource and marks the image `AVAILABLE`. You can then use the imported image as the base image for your recipes.

To create the VM import task, use the Amazon EC2 API [ImportImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html) operation, or the [import-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/import-image.html) AWS CLI command.

## Request Syntax
<a name="API_ImportVmImage_RequestSyntax"></a>

```
PUT /ImportVmImage HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "loggingConfiguration": {
      "logGroupName": "{{string}}"
   },
   "name": "{{string}}",
   "osVersion": "{{string}}",
   "platform": "{{string}}",
   "semanticVersion": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "vmImportTaskId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ImportVmImage_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ImportVmImage_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [description](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-description"></a>
The description for the base image that is created by the import process.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [loggingConfiguration](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-loggingConfiguration"></a>
The CloudWatch Logs log group where Image Builder sends the import logs. For ImportVmImage, the log group name must be within the `/aws/imagebuilder/` namespace.
Type: [ImageLoggingConfiguration](API_ImageLoggingConfiguration.md) object
Required: No

 ** [name](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-name"></a>
The name of the base image that is created by the import process. Image Builder generates the image ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If an image with the same name and semantic version already exists in your account in the same AWS Region, the import creates a new build version for it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [osVersion](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-osVersion"></a>
The operating system version for the imported VM.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [platform](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-platform"></a>
The operating system platform for the imported VM.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: Yes

 ** [semanticVersion](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-semanticVersion"></a>
The semantic version to attach to the base image that was created during the import process. This version follows the semantic version syntax.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
 **Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: Yes

 ** [tags](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-tags"></a>
Tags that are attached to the import resources.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [vmImportTaskId](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-vmImportTaskId"></a>
The `importTaskId` (API) or `ImportTaskId` (AWS CLI) from the Amazon EC2 VM import process. The import task doesn't need to be complete when you call ImportVmImage - Image Builder monitors the task and finishes creating the image when the task completes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_ImportVmImage_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "imageArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ImportVmImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_ImportVmImage_ResponseSyntax) **   <a name="imagebuilder-ImportVmImage-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [imageArn](#API_ImportVmImage_ResponseSyntax) **   <a name="imagebuilder-ImportVmImage-response-imageArn"></a>
The Amazon Resource Name (ARN) of the Image Builder image resource that this request created. Image Builder records the AMI from the VM import task in the image's output resources after the task completes.
Type: String

 ** [requestId](#API_ImportVmImage_ResponseSyntax) **   <a name="imagebuilder-ImportVmImage-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ImportVmImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_ImportVmImage_Examples"></a>

### Import a virtual machine as an Image Builder image
<a name="API_ImportVmImage_Example_1"></a>

The following example registers the output of an EC2 VM Import/Export task (import-ami) as a new Image Builder image, so you can use the imported virtual machine as a base image.

#### Sample Request
<a name="API_ImportVmImage_Example_1_Request"></a>

```
PUT /ImportVmImage HTTP/1.1
Content-type: application/json

{
    "name": "my-example-imported-image",
    "semanticVersion": "1.0.0",
    "platform": "Linux",
    "osVersion": "Amazon Linux 2",
    "vmImportTaskId": "import-ami-1234567890abcdef0",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE00000"
}
```

#### Sample Response
<a name="API_ImportVmImage_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "requestId": "f8a1d0ce-42b7-4d6a-9b12-3c84a02e5f19",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE00000",
    "imageArn": "arn:aws:imagebuilder:us-west-2:111122223333:image/my-example-imported-image/1.0.0/1"
}
```

## See Also
<a name="API_ImportVmImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ImportVmImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ImportVmImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImportVmImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ImportVmImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImportVmImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ImportVmImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ImportVmImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ImportVmImage)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ImportVmImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImportVmImage)

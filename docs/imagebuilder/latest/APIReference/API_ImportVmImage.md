---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImportVmImage.html
---

# ImportVmImage
<a name="API_ImportVmImage"></a>

When you export your virtual machine (VM) from its virtualization environment, that process creates a set of one or more disk container files that act as snapshots of your VM’s environment, settings, and data. The Amazon EC2 API [ImportImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html) action uses those files to import your VM and create an AMI. To import using the AWS CLI command, see [import-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/import-image.html)

You can reference the task ID from the VM import to pull in the AMI that the import created as the base image for your Image Builder recipe.

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
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [description](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-description"></a>
The description for the base image that is created by the import process.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [loggingConfiguration](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-loggingConfiguration"></a>
Define logging configuration for the image build process.
Type: [ImageLoggingConfiguration](API_ImageLoggingConfiguration.md) object
Required: No

 ** [name](#API_ImportVmImage_RequestSyntax) **   <a name="imagebuilder-ImportVmImage-request-name"></a>
The name of the base image that is created by the import process.
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
 **Assignment:** For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.
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
The `importTaskId` (API) or `ImportTaskId` (AWS CLI) from the Amazon EC2 VM import process. Image Builder retrieves information from the import process to pull in the AMI that is created from the VM source as the base image for your recipe.
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
The Amazon Resource Name (ARN) of the AMI that was created during the VM import process. This AMI is used as the base image for the recipe that imported the VM.
Type: String

 ** [requestId](#API_ImportVmImage_ResponseSyntax) **   <a name="imagebuilder-ImportVmImage-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ImportVmImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **
These errors are usually caused by a client action, such as using an action or resource on behalf of a user that doesn't have permissions to use the action or resource, or specifying an invalid resource identifier.
HTTP Status Code: 400

 ** ServiceException **
This exception is thrown when the service encounters an unrecoverable exception.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

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
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ImportVmImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImportVmImage)

---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteExtension.html
---

# DeleteExtension
<a name="API_DeleteExtension"></a>

Deletes an AWS AppConfig extension. You must delete all associations to an extension before you delete the extension.

## Request Syntax
<a name="API_DeleteExtension_RequestSyntax"></a>

```
DELETE /extensions/{{ExtensionIdentifier}}?version={{VersionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteExtension_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ExtensionIdentifier](#API_DeleteExtension_RequestSyntax) **   <a name="appconfig-DeleteExtension-request-uri-ExtensionIdentifier"></a>
The name, ID, or Amazon Resource Name (ARN) of the extension you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [VersionNumber](#API_DeleteExtension_RequestSyntax) **   <a name="appconfig-DeleteExtension-request-uri-VersionNumber"></a>
A specific version of an extension to delete. If omitted, the highest version is deleted.

## Request Body
<a name="API_DeleteExtension_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteExtension_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteExtension_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteExtension_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_DeleteExtension_Examples"></a>

### Example
<a name="API_DeleteExtension_Example_1"></a>

This example illustrates one usage of DeleteExtension.

#### Sample Request
<a name="API_DeleteExtension_Example_1_Request"></a>

```
DELETE /extensions/my-test-extension HTTP/1.1
Host: appconfig.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.7.19 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/appconfig.delete-extension
X-Amz-Date: 20220803T223549Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220803/us-west-2/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_DeleteExtension_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/DeleteExtension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/DeleteExtension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/DeleteExtension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/DeleteExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/DeleteExtension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/DeleteExtension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/DeleteExtension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/DeleteExtension)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/DeleteExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/DeleteExtension)

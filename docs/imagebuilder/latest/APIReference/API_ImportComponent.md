---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImportComponent.html
---

# ImportComponent
<a name="API_ImportComponent"></a>

Imports a component and transforms its data into a component document.

## Request Syntax
<a name="API_ImportComponent_RequestSyntax"></a>

```
PUT /ImportComponent HTTP/1.1
Content-type: application/json

{
   "changeDescription": "{{string}}",
   "clientToken": "{{string}}",
   "data": "{{string}}",
   "description": "{{string}}",
   "format": "{{string}}",
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "platform": "{{string}}",
   "semanticVersion": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}",
   "uri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ImportComponent_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ImportComponent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [changeDescription](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-changeDescription"></a>
The change description of the component. This description indicates the change that has been made in this version, or what makes this version different from other versions of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [clientToken](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-clientToken"></a>
Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [data](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-data"></a>
The data of the component. Used to specify the data inline. Either `data` or `uri` can be used to specify the data within the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [description](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-description"></a>
The description of the component. Describes the contents of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [format](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-format"></a>
The format of the resource that you want to import as a component.
Type: String
Valid Values: `SHELL`
Required: Yes

 ** [kmsKeyId](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-kmsKeyId"></a>
The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this component. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [name](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-name"></a>
The name of the component.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** [platform](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-platform"></a>
The platform of the component.
Type: String
Valid Values: `Windows | Linux | macOS`
Required: Yes

 ** [semanticVersion](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-semanticVersion"></a>
The semantic version of the component. This version follows the semantic version syntax.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Filtering:** With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: Yes

 ** [tags](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-tags"></a>
The tags of the component.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [type](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-type"></a>
The type of the component denotes whether the component is used to build the image, or only to test it.
Type: String
Valid Values: `BUILD | TEST`
Required: Yes

 ** [uri](#API_ImportComponent_RequestSyntax) **   <a name="imagebuilder-ImportComponent-request-uri"></a>
The uri of the component. Must be an Amazon S3 URL and the requester must have permission to access the Amazon S3 bucket. If you use Amazon S3, you can specify component content up to your service quota. Either `data` or `uri` can be used to specify the data within the component.
Type: String
Required: No

## Response Syntax
<a name="API_ImportComponent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "componentBuildVersionArn": "string",
   "requestId": "string"
}
```

## Response Elements
<a name="API_ImportComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_ImportComponent_ResponseSyntax) **   <a name="imagebuilder-ImportComponent-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [componentBuildVersionArn](#API_ImportComponent_ResponseSyntax) **   <a name="imagebuilder-ImportComponent-response-componentBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the imported component.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

 ** [requestId](#API_ImportComponent_ResponseSyntax) **   <a name="imagebuilder-ImportComponent-response-requestId"></a>
The request ID that uniquely identifies this request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ImportComponent_Errors"></a>

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

 ** InvalidParameterCombinationException **
You have specified two or more mutually exclusive parameters. Review the error message for details.
HTTP Status Code: 400

 ** InvalidRequestException **
You have requested an action that that the service doesn't support.
HTTP Status Code: 400

 ** InvalidVersionNumberException **
Your version number is out of bounds or does not follow the required syntax.
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
<a name="API_ImportComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/ImportComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/ImportComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/ImportComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/ImportComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/ImportComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/ImportComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/ImportComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/ImportComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/ImportComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/ImportComponent)

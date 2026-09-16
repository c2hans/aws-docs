---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ImportWorkspaceMedia.html
---

# ImportWorkspaceMedia
<a name="API_ImportWorkspaceMedia"></a>

Imports a media asset (such as a logo) for use in a workspace.

## Request Syntax
<a name="API_ImportWorkspaceMedia_RequestSyntax"></a>

```
POST /workspaces/{{InstanceId}}/{{WorkspaceId}}/media HTTP/1.1
Content-type: application/json

{
   "MediaSource": "{{string}}",
   "MediaType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ImportWorkspaceMedia_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ImportWorkspaceMedia_RequestSyntax) **   <a name="connect-ImportWorkspaceMedia-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [WorkspaceId](#API_ImportWorkspaceMedia_RequestSyntax) **   <a name="connect-ImportWorkspaceMedia-request-uri-WorkspaceId"></a>
The identifier of the workspace.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Request Body
<a name="API_ImportWorkspaceMedia_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MediaSource](#API_ImportWorkspaceMedia_RequestSyntax) **   <a name="connect-ImportWorkspaceMedia-request-MediaSource"></a>
The media source. Can be an S3 presigned URL or a base64-encoded string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 533333.
Pattern: `.*\\S.*`
Required: Yes

 ** [MediaType](#API_ImportWorkspaceMedia_RequestSyntax) **   <a name="connect-ImportWorkspaceMedia-request-MediaType"></a>
The type of media. Valid values are: `IMAGE_LOGO_FAVICON` and `IMAGE_LOGO_HORIZONTAL`.
Type: String
Valid Values: `IMAGE_LOGO_LIGHT_FAVICON | IMAGE_LOGO_DARK_FAVICON | IMAGE_LOGO_LIGHT_HORIZONTAL | IMAGE_LOGO_DARK_HORIZONTAL`
Required: Yes

## Response Syntax
<a name="API_ImportWorkspaceMedia_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ImportWorkspaceMedia_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ImportWorkspaceMedia_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ImportWorkspaceMedia_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ImportWorkspaceMedia)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ImportWorkspaceMedia)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ImportWorkspaceMedia)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ImportWorkspaceMedia)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ImportWorkspaceMedia)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ImportWorkspaceMedia)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ImportWorkspaceMedia)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ImportWorkspaceMedia)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ImportWorkspaceMedia)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ImportWorkspaceMedia)

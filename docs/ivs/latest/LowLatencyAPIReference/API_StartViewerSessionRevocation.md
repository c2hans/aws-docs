---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_StartViewerSessionRevocation.html
---

# StartViewerSessionRevocation
<a name="API_StartViewerSessionRevocation"></a>

Starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID. Optionally, you can provide a version to revoke viewer sessions less than and including that version. For instructions on associating a viewer ID with a viewer session, see [Setting Up Private Channels](https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html).

## Request Syntax
<a name="API_StartViewerSessionRevocation_RequestSyntax"></a>

```
POST /StartViewerSessionRevocation HTTP/1.1
Content-type: application/json

{
   "channelArn": "{{string}}",
   "viewerId": "{{string}}",
   "viewerSessionVersionsLessThanOrEqualTo": {{number}}
}
```

## URI Request Parameters
<a name="API_StartViewerSessionRevocation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartViewerSessionRevocation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelArn](#API_StartViewerSessionRevocation_RequestSyntax) **   <a name="ivs-StartViewerSessionRevocation-request-channelArn"></a>
The ARN of the channel associated with the viewer session to revoke.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

 ** [viewerId](#API_StartViewerSessionRevocation_RequestSyntax) **   <a name="ivs-StartViewerSessionRevocation-request-viewerId"></a>
The ID of the viewer associated with the viewer session to revoke. Do not use this field for personally identifying, confidential, or sensitive information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Required: Yes

 ** [viewerSessionVersionsLessThanOrEqualTo](#API_StartViewerSessionRevocation_RequestSyntax) **   <a name="ivs-StartViewerSessionRevocation-request-viewerSessionVersionsLessThanOrEqualTo"></a>
An optional filter on which versions of the viewer session to revoke. All versions less than or equal to the specified version will be revoked. Default: 0.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_StartViewerSessionRevocation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StartViewerSessionRevocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartViewerSessionRevocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_StartViewerSessionRevocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/StartViewerSessionRevocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/StartViewerSessionRevocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/StartViewerSessionRevocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/StartViewerSessionRevocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/StartViewerSessionRevocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/StartViewerSessionRevocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/StartViewerSessionRevocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/StartViewerSessionRevocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/StartViewerSessionRevocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/StartViewerSessionRevocation)

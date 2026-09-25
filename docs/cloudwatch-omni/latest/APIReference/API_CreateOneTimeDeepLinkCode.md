---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_CreateOneTimeDeepLinkCode.html
---

# CreateOneTimeDeepLinkCode
<a name="API_CreateOneTimeDeepLinkCode"></a>

Generates a one-time code for deep-link authentication.

Direct the user's browser to the returned deepLinkUrl before it expires. The code is exchanged for an authenticated, domain-scoped session and can be used only once.

## Request Parameters
<a name="API_CreateOneTimeDeepLinkCode_RequestParameters"></a>

 ** domainId **
The ID of the domain to generate the code for.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** redirectUrl **
The URL to redirect to after the deep-link code is used. Must be an HTTPS URL in the domain with a path of /auth/callback, and cannot include a query string or fragment. If omitted, no redirect is applied.
Type: String
Required: No

 ** ttlSeconds **
How long the code remains valid, in seconds. Defaults to 300.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 600.
Required: No

## Response Elements
<a name="API_CreateOneTimeDeepLinkCode_ResponseElements"></a>

The following elements are returned by the service.

 ** code **
The one-time deep-link code.
Type: String

 ** deepLinkUrl **
The deep-link URL containing the one-time code.
Type: String

 ** expiresAt **
The timestamp when the code expires.
Type: Timestamp

## Errors
<a name="API_CreateOneTimeDeepLinkCode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** errorCode **
The error code associated with the failure.
 ** resourceId **
The identifier of the resource that could not be found. Not always present.
 ** resourceType **
The type of the resource that could not be found. Not always present.
HTTP Status Code: 404

 ** ThrottlingException **
The request was throttled due to exceeding the allowed request rate.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request. Not always present.
HTTP Status Code: 429

 ** ValidationException **
A parameter is specified incorrectly.
 ** errorCode **
The error code associated with the validation failure.
HTTP Status Code: 400

## Examples
<a name="API_CreateOneTimeDeepLinkCode_Examples"></a>

### Create a one-time deep-link code
<a name="API_CreateOneTimeDeepLinkCode_Example_1"></a>

The following example creates a one-time deep-link code for a domain that remains valid for 300 seconds and, once used, redirects the browser to the domain's /auth/callback path. Direct the user's browser to the returned deepLinkUrl before it expires; the code can be used only once. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_CreateOneTimeDeepLinkCode_Example_1_Request"></a>

```
{
  "domainId": "d-1a2b3c4d5e",
  "redirectUrl": "https://d-1a2b3c4d5e.cloudwatch-omni.global.app.aws/auth/callback",
  "ttlSeconds": 300
}
```

#### Sample Response
<a name="API_CreateOneTimeDeepLinkCode_Example_1_Response"></a>

```
{
  "code": "dlc-EXAMPLE1234567890",
  "deepLinkUrl": "https://d-1a2b3c4d5e.cloudwatch-omni.global.app.aws/deeplink?code=EXAMPLE1234567890",
  "expiresAt": "2026-09-16T14:27:31Z"
}
```

## See Also
<a name="API_CreateOneTimeDeepLinkCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/CreateOneTimeDeepLinkCode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/CreateOneTimeDeepLinkCode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/CreateOneTimeDeepLinkCode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/CreateOneTimeDeepLinkCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/CreateOneTimeDeepLinkCode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/CreateOneTimeDeepLinkCode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/CreateOneTimeDeepLinkCode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/CreateOneTimeDeepLinkCode)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/CreateOneTimeDeepLinkCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/CreateOneTimeDeepLinkCode)

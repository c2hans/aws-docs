---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_DeleteKey.html
---

# DeleteKey
<a name="API_geoapikeys_DeleteKey"></a>

Deletes the specified API key. The API key must have been deactivated more than 90 days previously.

For more information, see [Use API keys to authenticate](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geoapikeys_DeleteKey_RequestSyntax"></a>

```
DELETE /metadata/v0/keys/{{KeyName}}?forceDelete={{ForceDelete}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geoapikeys_DeleteKey_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ForceDelete](#API_geoapikeys_DeleteKey_RequestSyntax) **   <a name="location-geoapikeys_DeleteKey-request-uri-ForceDelete"></a>
ForceDelete bypasses an API key's expiry conditions and deletes the key. Set the parameter `true` to delete the key or to `false` to not preemptively delete the API key.
Valid values: `true`, or `false`.
Required: No
This action is irreversible. Only use ForceDelete if you are certain the key is no longer in use.

 ** [KeyName](#API_geoapikeys_DeleteKey_RequestSyntax) **   <a name="location-geoapikeys_DeleteKey-request-uri-KeyName"></a>
The name of the API key to delete.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_geoapikeys_DeleteKey_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geoapikeys_DeleteKey_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_geoapikeys_DeleteKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_geoapikeys_DeleteKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A resource associated with the request could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_geoapikeys_DeleteKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geoapikeys-2020-11-19/DeleteKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geoapikeys-2020-11-19/DeleteKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geoapikeys-2020-11-19/DeleteKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geoapikeys-2020-11-19/DeleteKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geoapikeys-2020-11-19/DeleteKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geoapikeys-2020-11-19/DeleteKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geoapikeys-2020-11-19/DeleteKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geoapikeys-2020-11-19/DeleteKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geoapikeys-2020-11-19/DeleteKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geoapikeys-2020-11-19/DeleteKey)

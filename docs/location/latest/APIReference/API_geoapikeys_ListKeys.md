---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_ListKeys.html
---

# ListKeys
<a name="API_geoapikeys_ListKeys"></a>

Lists API key resources in your AWS account.

For more information, see [Use API keys to authenticate](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geoapikeys_ListKeys_RequestSyntax"></a>

```
POST /metadata/v0/list-keys HTTP/1.1
Content-type: application/json

{
   "Filter": {
      "KeyStatus": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_geoapikeys_ListKeys_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_geoapikeys_ListKeys_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filter](#API_geoapikeys_ListKeys_RequestSyntax) **   <a name="location-geoapikeys_ListKeys-request-Filter"></a>
Optionally filter the list to only `Active` or `Expired` API keys.
Type: [ApiKeyFilter](API_geoapikeys_ApiKeyFilter.md) object
Required: No

 ** [MaxResults](#API_geoapikeys_ListKeys_RequestSyntax) **   <a name="location-geoapikeys_ListKeys-request-MaxResults"></a>
An optional limit for the number of resources returned in a single call.
Default value: `100`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_geoapikeys_ListKeys_RequestSyntax) **   <a name="location-geoapikeys_ListKeys-request-NextToken"></a>
The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.
Default value: `null`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_geoapikeys_ListKeys_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Entries": [
      {
         "CreateTime": "string",
         "Description": "string",
         "ExpireTime": "string",
         "KeyName": "string",
         "Restrictions": {
            "AllowActions": [ "string" ],
            "AllowAndroidApps": [
               {
                  "CertificateFingerprint": "string",
                  "Package": "string"
               }
            ],
            "AllowAppleApps": [
               {
                  "BundleId": "string"
               }
            ],
            "AllowReferers": [ "string" ],
            "AllowResources": [ "string" ]
         },
         "UpdateTime": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_geoapikeys_ListKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Entries](#API_geoapikeys_ListKeys_ResponseSyntax) **   <a name="location-geoapikeys_ListKeys-response-Entries"></a>
Contains API key resources in your AWS account. Details include API key name, allowed referers and timestamp for when the API key will expire.
Type: Array of [ListKeysResponseEntry](API_geoapikeys_ListKeysResponseEntry.md) objects

 ** [NextToken](#API_geoapikeys_ListKeys_ResponseSyntax) **   <a name="location-geoapikeys_ListKeys-response-NextToken"></a>
A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_geoapikeys_ListKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_geoapikeys_ListKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geoapikeys-2020-11-19/ListKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geoapikeys-2020-11-19/ListKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geoapikeys-2020-11-19/ListKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geoapikeys-2020-11-19/ListKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geoapikeys-2020-11-19/ListKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geoapikeys-2020-11-19/ListKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geoapikeys-2020-11-19/ListKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geoapikeys-2020-11-19/ListKeys)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geoapikeys-2020-11-19/ListKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geoapikeys-2020-11-19/ListKeys)

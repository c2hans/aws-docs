---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_ListStorageConfigurations.html
---

# ListStorageConfigurations
<a name="API_ListStorageConfigurations"></a>

Gets summary information about all storage configurations in your account, in the AWS region where the API request is processed.

## Request Syntax
<a name="API_ListStorageConfigurations_RequestSyntax"></a>

```
POST /ListStorageConfigurations HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListStorageConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListStorageConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListStorageConfigurations_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListStorageConfigurations-request-maxResults"></a>
Maximum number of storage configurations to return. Default: your service quota or 100, whichever is smaller.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListStorageConfigurations_RequestSyntax) **   <a name="ivsrealtimeeapireference-ListStorageConfigurations-request-nextToken"></a>
The first storage configuration to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`
Required: No

## Response Syntax
<a name="API_ListStorageConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "storageConfigurations": [
      {
         "arn": "string",
         "name": "string",
         "s3": {
            "bucketName": "string"
         },
         "tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListStorageConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListStorageConfigurations_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListStorageConfigurations-response-nextToken"></a>
If there are more storage configurations than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[a-zA-Z0-9+/=_-]*`

 ** [storageConfigurations](#API_ListStorageConfigurations_ResponseSyntax) **   <a name="ivsrealtimeeapireference-ListStorageConfigurations-response-storageConfigurations"></a>
List of the matching storage configurations.
Type: Array of [StorageConfigurationSummary](API_StorageConfigurationSummary.md) objects

## Errors
<a name="API_ListStorageConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **

 ** exceptionMessage **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **

 ** exceptionMessage **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **

 ** exceptionMessage **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListStorageConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/ListStorageConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/ListStorageConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/ListStorageConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/ListStorageConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/ListStorageConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/ListStorageConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/ListStorageConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/ListStorageConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/ListStorageConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/ListStorageConfigurations)

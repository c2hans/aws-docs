---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_ListLoggingConfigurations.html
---

# ListLoggingConfigurations
<a name="API_ListLoggingConfigurations"></a>

Gets summary information about all your logging configurations in the AWS region where the API request is processed.

## Request Syntax
<a name="API_ListLoggingConfigurations_RequestSyntax"></a>

```
POST /ListLoggingConfigurations HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListLoggingConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListLoggingConfigurations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListLoggingConfigurations_RequestSyntax) **   <a name="ivs-ListLoggingConfigurations-request-maxResults"></a>
Maximum number of logging configurations to return. Default: 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListLoggingConfigurations_RequestSyntax) **   <a name="ivs-ListLoggingConfigurations-request-nextToken"></a>
The first logging configurations to retrieve. This is used for pagination; see the `nextToken` response field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListLoggingConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "loggingConfigurations": [
      {
         "arn": "string",
         "createTime": "string",
         "destinationConfiguration": { ... },
         "id": "string",
         "name": "string",
         "state": "string",
         "tags": {
            "string" : "string"
         },
         "updateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListLoggingConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [loggingConfigurations](#API_ListLoggingConfigurations_ResponseSyntax) **   <a name="ivs-ListLoggingConfigurations-response-loggingConfigurations"></a>
List of the matching logging configurations (summary information only). There is only one type of destination (`cloudWatchLogs`, `firehose`, or `s3`) in a `destinationConfiguration`.
Type: Array of [LoggingConfigurationSummary](API_LoggingConfigurationSummary.md) objects

 ** [nextToken](#API_ListLoggingConfigurations_ResponseSyntax) **   <a name="ivs-ListLoggingConfigurations-response-nextToken"></a>
If there are more logging configurations than `maxResults`, use `nextToken` in the request to get the next set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_ListLoggingConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

HTTP Status Code: 403

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_ListLoggingConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivschat-2020-07-14/ListLoggingConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivschat-2020-07-14/ListLoggingConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivschat-2020-07-14/ListLoggingConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivschat-2020-07-14/ListLoggingConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivschat-2020-07-14/ListLoggingConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivschat-2020-07-14/ListLoggingConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivschat-2020-07-14/ListLoggingConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivschat-2020-07-14/ListLoggingConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivschat-2020-07-14/ListLoggingConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivschat-2020-07-14/ListLoggingConfigurations)

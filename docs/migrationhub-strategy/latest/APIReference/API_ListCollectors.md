---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListCollectors.html
---

# ListCollectors
<a name="API_ListCollectors"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Retrieves a list of all the installed collectors.

## Request Syntax
<a name="API_ListCollectors_RequestSyntax"></a>

```
GET /list-collectors?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCollectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListCollectors_RequestSyntax) **   <a name="migrationhubstrategy-ListCollectors-request-uri-maxResults"></a>
 The maximum number of items to include in the response. The maximum value is 100.

 ** [nextToken](#API_ListCollectors_RequestSyntax) **   <a name="migrationhubstrategy-ListCollectors-request-uri-nextToken"></a>
 The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set `maxResults` to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`

## Request Body
<a name="API_ListCollectors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCollectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Collectors": [
      {
         "collectorHealth": "string",
         "collectorId": "string",
         "collectorVersion": "string",
         "configurationSummary": {
            "ipAddressBasedRemoteInfoList": [
               {
                  "authType": "string",
                  "ipAddressConfigurationTimeStamp": "string",
                  "osType": "string"
               }
            ],
            "pipelineInfoList": [
               {
                  "pipelineConfigurationTimeStamp": "string",
                  "pipelineType": "string"
               }
            ],
            "remoteSourceCodeAnalysisServerInfo": {
               "remoteSourceCodeAnalysisServerConfigurationTimestamp": "string"
            },
            "vcenterBasedRemoteInfoList": [
               {
                  "osType": "string",
                  "vcenterConfigurationTimeStamp": "string"
               }
            ],
            "versionControlInfoList": [
               {
                  "versionControlConfigurationTimeStamp": "string",
                  "versionControlType": "string"
               }
            ]
         },
         "hostName": "string",
         "ipAddress": "string",
         "lastActivityTimeStamp": "string",
         "registeredTimeStamp": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCollectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Collectors](#API_ListCollectors_ResponseSyntax) **   <a name="migrationhubstrategy-ListCollectors-response-Collectors"></a>
 The list of all the installed collectors.
Type: Array of [Collector](API_Collector.md) objects

 ** [nextToken](#API_ListCollectors_ResponseSyntax) **   <a name="migrationhubstrategy-ListCollectors-response-nextToken"></a>
 The token you use to retrieve the next set of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*\S.*`

## Errors
<a name="API_ListCollectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_ListCollectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/ListCollectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/ListCollectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ListCollectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/ListCollectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ListCollectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/ListCollectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/ListCollectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/ListCollectors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/ListCollectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ListCollectors)

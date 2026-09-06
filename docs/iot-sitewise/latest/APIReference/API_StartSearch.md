---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_StartSearch.html
---

# StartSearch
<a name="API_StartSearch"></a>

Starts an asynchronous search over the data in a workspace. The search runs in the background; the response returns immediately with a `searchId` and an initial status of `QUEUED`. Use `DescribeSearch` to poll for completion and `GetSearchResults` to retrieve the results once the search reaches `SUCCEEDED`. The request is idempotent on `clientToken`: repeating a call with the same token returns the original search instead of starting a new one.

## Request Syntax
<a name="API_StartSearch_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/searches HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "groupId": "{{string}}",
   "queryStatement": "{{string}}",
   "searchFilters": {
      "datasetIds": [ "{{string}}" ],
      "timeIntervals": [
         {
            "endTime": {
               "offsetInNanos": {{number}},
               "timeInSeconds": {{number}}
            },
            "startTime": {
               "offsetInNanos": {{number}},
               "timeInSeconds": {{number}}
            }
         }
      ],
      "timeSeriesIds": [ "{{string}}" ]
   },
   "searchType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartSearch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceName](#API_StartSearch_RequestSyntax) **   <a name="iotsitewise-StartSearch-request-uri-workspaceName"></a>
The name of the workspace whose data is searched.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_StartSearch_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_StartSearch_RequestSyntax) **   <a name="iotsitewise-StartSearch-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure the request is idempotent. Repeating a StartSearch call with the same `clientToken` returns the original search rather than starting a new one. If omitted, the SDK autogenerates one.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [groupId](#API_StartSearch_RequestSyntax) **   <a name="iotsitewise-StartSearch-request-groupId"></a>
An optional caller-supplied identifier used to group related searches together.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`
Required: No

 ** [queryStatement](#API_StartSearch_RequestSyntax) **   <a name="iotsitewise-StartSearch-request-queryStatement"></a>
The natural-language query describing the data to search for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Required: Yes

 ** [searchFilters](#API_StartSearch_RequestSyntax) **   <a name="iotsitewise-StartSearch-request-searchFilters"></a>
Optional filters that restrict the search to a subset of the workspace's data.
Type: [SearchFilters](API_SearchFilters.md) object
Required: No

 ** [searchType](#API_StartSearch_RequestSyntax) **   <a name="iotsitewise-StartSearch-request-searchType"></a>
The search strategy to use. Defaults to `QUICK` when omitted.
Type: String
Valid Values: `DEEP | QUICK`
Required: No

## Response Syntax
<a name="API_StartSearch_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "groupId": "string",
   "searchId": "string",
   "status": "string",
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_StartSearch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [groupId](#API_StartSearch_ResponseSyntax) **   <a name="iotsitewise-StartSearch-response-groupId"></a>
The group identifier associated with the search, if one was supplied on the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`

 ** [searchId](#API_StartSearch_ResponseSyntax) **   <a name="iotsitewise-StartSearch-response-searchId"></a>
The unique identifier assigned to the newly started search.
Type: String
Length Constraints: Minimum length of 23. Maximum length of 36.
Pattern: `[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*`

 ** [status](#API_StartSearch_ResponseSyntax) **   <a name="iotsitewise-StartSearch-response-status"></a>
The initial status of the search. A newly started search is `QUEUED`.
Type: String
Valid Values: `QUEUED | RUNNING | SUCCEEDED | FAILED`

 ** [workspaceName](#API_StartSearch_ResponseSyntax) **   <a name="iotsitewise-StartSearch-response-workspaceName"></a>
The name of the workspace the search runs against.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_StartSearch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** LimitExceededException **
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 410

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_StartSearch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/StartSearch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/StartSearch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/StartSearch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/StartSearch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/StartSearch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/StartSearch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/StartSearch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/StartSearch)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/StartSearch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/StartSearch)

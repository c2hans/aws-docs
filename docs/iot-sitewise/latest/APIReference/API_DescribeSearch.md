---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeSearch.html
---

# DescribeSearch
<a name="API_DescribeSearch"></a>

Returns the current status and metadata of a single search, including the query that was submitted, the search type, and — when the search has failed — the reason. Use this to poll a search started with `StartSearch` until it reaches a terminal status (`SUCCEEDED` or `FAILED`).

## Request Syntax
<a name="API_DescribeSearch_RequestSyntax"></a>

```
GET /workspaces/{{workspaceName}}/searches/{{searchId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeSearch_RequestParameters"></a>

The request uses the following URI parameters.

 ** [searchId](#API_DescribeSearch_RequestSyntax) **   <a name="iotsitewise-DescribeSearch-request-uri-searchId"></a>
The identifier of the search to describe.
Length Constraints: Minimum length of 23. Maximum length of 36.
Pattern: `[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*`
Required: Yes

 ** [workspaceName](#API_DescribeSearch_RequestSyntax) **   <a name="iotsitewise-DescribeSearch-request-uri-workspaceName"></a>
The name of the workspace the search belongs to.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_DescribeSearch_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeSearch_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "groupId": "string",
   "queryStatement": "string",
   "searchId": "string",
   "searchType": "string",
   "startedAt": number,
   "status": "string",
   "statusReason": "string",
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_DescribeSearch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [groupId](#API_DescribeSearch_ResponseSyntax) **   <a name="iotsitewise-DescribeSearch-response-groupId"></a>
The group identifier associated with the search, if one was supplied on the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`

 ** [queryStatement](#API_DescribeSearch_ResponseSyntax) **   <a name="iotsitewise-DescribeSearch-response-queryStatement"></a>
The natural-language query that was submitted for the search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.

 ** [searchId](#API_DescribeSearch_ResponseSyntax) **   <a name="iotsitewise-DescribeSearch-response-searchId"></a>
The unique identifier of the search.
Type: String
Length Constraints: Minimum length of 23. Maximum length of 36.
Pattern: `[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*`

 ** [searchType](#API_DescribeSearch_ResponseSyntax) **   <a name="iotsitewise-DescribeSearch-response-searchType"></a>
The search strategy used for the search.
Type: String
Valid Values: `DEEP | QUICK`

 ** [startedAt](#API_DescribeSearch_ResponseSyntax) **   <a name="iotsitewise-DescribeSearch-response-startedAt"></a>
The time at which the search was started.
Type: Timestamp

 ** [status](#API_DescribeSearch_ResponseSyntax) **   <a name="iotsitewise-DescribeSearch-response-status"></a>
The current status of the search.
Type: String
Valid Values: `QUEUED | RUNNING | SUCCEEDED | FAILED`

 ** [statusReason](#API_DescribeSearch_ResponseSyntax) **   <a name="iotsitewise-DescribeSearch-response-statusReason"></a>
A human-readable explanation of the current status. Populated when the search has `FAILED`.
Type: String

 ** [workspaceName](#API_DescribeSearch_ResponseSyntax) **   <a name="iotsitewise-DescribeSearch-response-workspaceName"></a>
The name of the workspace the search runs against.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_DescribeSearch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_DescribeSearch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/DescribeSearch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/DescribeSearch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DescribeSearch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/DescribeSearch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DescribeSearch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/DescribeSearch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/DescribeSearch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/DescribeSearch)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/DescribeSearch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DescribeSearch)

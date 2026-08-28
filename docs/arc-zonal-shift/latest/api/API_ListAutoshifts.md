---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListAutoshifts.html
---

# ListAutoshifts
<a name="API_ListAutoshifts"></a>

Returns the autoshifts for an AWS Region. By default, the call returns only `ACTIVE` autoshifts. Optionally, you can specify the `status` parameter to return `COMPLETED` autoshifts.

## Request Syntax
<a name="API_ListAutoshifts_RequestSyntax"></a>

```
GET /autoshifts?maxResults={{maxResults}}&nextToken={{nextToken}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAutoshifts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAutoshifts_RequestSyntax) **   <a name="zonalshift-ListAutoshifts-request-uri-maxResults"></a>
The number of objects that you want to return with this call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAutoshifts_RequestSyntax) **   <a name="zonalshift-ListAutoshifts-request-uri-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.

 ** [status](#API_ListAutoshifts_RequestSyntax) **   <a name="zonalshift-ListAutoshifts-request-uri-status"></a>
The status of the autoshift.
Valid Values: `ACTIVE | COMPLETED`

## Request Body
<a name="API_ListAutoshifts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAutoshifts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "awayFrom": "string",
         "endTime": number,
         "startTime": number,
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAutoshifts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListAutoshifts_ResponseSyntax) **   <a name="zonalshift-ListAutoshifts-response-items"></a>
The items in the response list.
Type: Array of [AutoshiftSummary](API_AutoshiftSummary.md) objects

 ** [nextToken](#API_ListAutoshifts_ResponseSyntax) **   <a name="zonalshift-ListAutoshifts-response-nextToken"></a>
Specifies that you want to receive the next page of results. Valid only if you received a `nextToken` response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's `nextToken` response to request the next page of results.
Type: String

## Errors
<a name="API_ListAutoshifts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
There was an internal server error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_ListAutoshifts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/ListAutoshifts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/ListAutoshifts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/ListAutoshifts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/ListAutoshifts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/ListAutoshifts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/ListAutoshifts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/ListAutoshifts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/ListAutoshifts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/ListAutoshifts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/ListAutoshifts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-zonal-shift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

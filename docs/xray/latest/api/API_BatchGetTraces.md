---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html
---

# BatchGetTraces
<a name="API_BatchGetTraces"></a>

**Note**
You cannot find traces through this API if Transaction Search is enabled since trace is not indexed in X-Ray.

Retrieves a list of traces specified by ID. Each trace is a collection of segment documents that originates from a single request. Use `GetTraceSummaries` to get a list of trace IDs.

## Request Syntax
<a name="API_BatchGetTraces_RequestSyntax"></a>

```
POST /Traces HTTP/1.1
Content-type: application/json

{
   "NextToken": "{{string}}",
   "TraceIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetTraces_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetTraces_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [NextToken](#API_BatchGetTraces_RequestSyntax) **   <a name="xray-BatchGetTraces-request-NextToken"></a>
Pagination token.
Type: String
Required: No

 ** [TraceIds](#API_BatchGetTraces_RequestSyntax) **   <a name="xray-BatchGetTraces-request-TraceIds"></a>
Specify the trace IDs of requests for which to retrieve segments.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 35.
Required: Yes

## Response Syntax
<a name="API_BatchGetTraces_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Traces": [
      {
         "Duration": number,
         "Id": "string",
         "LimitExceeded": boolean,
         "Segments": [
            {
               "Document": "string",
               "Id": "string"
            }
         ]
      }
   ],
   "UnprocessedTraceIds": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetTraces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_BatchGetTraces_ResponseSyntax) **   <a name="xray-BatchGetTraces-response-NextToken"></a>
Pagination token.
Type: String

 ** [Traces](#API_BatchGetTraces_ResponseSyntax) **   <a name="xray-BatchGetTraces-response-Traces"></a>
Full traces for the specified requests.
Type: Array of [Trace](API_Trace.md) objects

 ** [UnprocessedTraceIds](#API_BatchGetTraces_ResponseSyntax) **   <a name="xray-BatchGetTraces-response-UnprocessedTraceIds"></a>
Trace IDs of requests that haven't been processed.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 35.

## Errors
<a name="API_BatchGetTraces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_BatchGetTraces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/BatchGetTraces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/BatchGetTraces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/BatchGetTraces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/BatchGetTraces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/BatchGetTraces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/BatchGetTraces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/BatchGetTraces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/BatchGetTraces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/BatchGetTraces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/BatchGetTraces)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

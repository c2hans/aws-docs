---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_CancelTraceRetrieval.html
---

# CancelTraceRetrieval
<a name="API_CancelTraceRetrieval"></a>

 Cancels an ongoing trace retrieval job initiated by `StartTraceRetrieval` using the provided `RetrievalToken`. A successful cancellation will return an HTTP 200 response.

## Request Syntax
<a name="API_CancelTraceRetrieval_RequestSyntax"></a>

```
POST /CancelTraceRetrieval HTTP/1.1
Content-type: application/json

{
   "RetrievalToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CancelTraceRetrieval_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CancelTraceRetrieval_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RetrievalToken](#API_CancelTraceRetrieval_RequestSyntax) **   <a name="xray-CancelTraceRetrieval-request-RetrievalToken"></a>
 Retrieval token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1020.
Required: Yes

## Response Syntax
<a name="API_CancelTraceRetrieval_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_CancelTraceRetrieval_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CancelTraceRetrieval_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.
HTTP Status Code: 404

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_CancelTraceRetrieval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/CancelTraceRetrieval)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/CancelTraceRetrieval)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/CancelTraceRetrieval)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/CancelTraceRetrieval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/CancelTraceRetrieval)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/CancelTraceRetrieval)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/CancelTraceRetrieval)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/CancelTraceRetrieval)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/CancelTraceRetrieval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/CancelTraceRetrieval)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

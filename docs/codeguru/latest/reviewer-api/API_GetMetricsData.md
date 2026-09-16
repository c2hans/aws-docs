---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_GetMetricsData.html
---

# GetMetricsData
<a name="API_GetMetricsData"></a>

**Note**
As of November 7, 2025, you cannot create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

Retrieves metrics data for CodeGuru Reviewer analysis, including findings and code analysis statistics.

## Request Syntax
<a name="API_GetMetricsData_RequestSyntax"></a>

```
GET /metrics HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMetricsData_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetMetricsData_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMetricsData_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "FindingsMetricsData": {
      "AnalyzedLinesOfCodeCount": number,
      "FindingJobsCount": number,
      "FindingsCount": number
   }
}
```

## Response Elements
<a name="API_GetMetricsData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FindingsMetricsData](#API_GetMetricsData_ResponseSyntax) **   <a name="reviewer-GetMetricsData-response-FindingsMetricsData"></a>
The metrics data containing findings and analysis statistics.
Type: [FindingsMetricsData](API_FindingsMetricsData.md) object

## Errors
<a name="API_GetMetricsData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_GetMetricsData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codeguru-reviewer-2019-09-19/GetMetricsData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codeguru-reviewer-2019-09-19/GetMetricsData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/GetMetricsData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codeguru-reviewer-2019-09-19/GetMetricsData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/GetMetricsData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codeguru-reviewer-2019-09-19/GetMetricsData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codeguru-reviewer-2019-09-19/GetMetricsData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codeguru-reviewer-2019-09-19/GetMetricsData)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codeguru-reviewer-2019-09-19/GetMetricsData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/GetMetricsData)

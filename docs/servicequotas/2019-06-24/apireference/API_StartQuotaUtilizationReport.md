---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_StartQuotaUtilizationReport.html
---

# StartQuotaUtilizationReport
<a name="API_StartQuotaUtilizationReport"></a>

Initiates the generation of a quota utilization report for your AWS account. This asynchronous operation analyzes your quota usage across all AWS services and returns a unique report identifier that you can use to retrieve the results.

The report generation process may take several seconds to complete, depending on the number of quotas in your account. Use the `GetQuotaUtilizationReport` operation to check the status and retrieve the results when the report is ready.

**Related Actions**
+  [GetQuotaUtilizationReport](API_GetQuotaUtilizationReport.md)

## Response Syntax
<a name="API_StartQuotaUtilizationReport_ResponseSyntax"></a>

```
{
   "Message": "string",
   "ReportId": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_StartQuotaUtilizationReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Message](#API_StartQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-StartQuotaUtilizationReport-response-Message"></a>
An optional message providing additional information about the report generation status. This field may contain details about the report initiation or indicate if an existing recent report is being reused.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350.
Pattern: `^.{0,350}$`

 ** [ReportId](#API_StartQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-StartQuotaUtilizationReport-response-ReportId"></a>
A unique identifier for the quota utilization report. Use this identifier with the `GetQuotaUtilizationReport` operation to retrieve the report results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-zA-Z][a-zA-Z0-9-]{1,128}`

 ** [Status](#API_StartQuotaUtilizationReport_ResponseSyntax) **   <a name="servicequotas-StartQuotaUtilizationReport-response-Status"></a>
The current status of the report generation. The status will be `PENDING` when the report is first initiated.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED`

## Errors
<a name="API_StartQuotaUtilizationReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** IllegalArgumentException **
Invalid input was provided.
HTTP Status Code: 400

 ** InvalidPaginationTokenException **
Invalid input was provided.
HTTP Status Code: 400

 ** NoSuchResourceException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceException **
Something went wrong.
HTTP Status Code: 500

 ** TooManyRequestsException **
Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.
HTTP Status Code: 400

## See Also
<a name="API_StartQuotaUtilizationReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/StartQuotaUtilizationReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/StartQuotaUtilizationReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/StartQuotaUtilizationReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/StartQuotaUtilizationReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/StartQuotaUtilizationReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/StartQuotaUtilizationReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/StartQuotaUtilizationReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/StartQuotaUtilizationReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/StartQuotaUtilizationReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/StartQuotaUtilizationReport)

---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetInsights.html
---

# GetInsights
<a name="API_GetInsights"></a>

**Important**
 AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html).

Gets the latest analytics data for all your current active assessments.

## Request Syntax
<a name="API_GetInsights_RequestSyntax"></a>

```
GET /insights HTTP/1.1
```

## URI Request Parameters
<a name="API_GetInsights_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetInsights_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetInsights_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "insights": {
      "activeAssessmentsCount": number,
      "assessmentControlsCountByNoncompliantEvidence": number,
      "compliantEvidenceCount": number,
      "inconclusiveEvidenceCount": number,
      "lastUpdated": number,
      "noncompliantEvidenceCount": number,
      "totalAssessmentControlsCount": number
   }
}
```

## Response Elements
<a name="API_GetInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [insights](#API_GetInsights_ResponseSyntax) **   <a name="auditmanager-GetInsights-response-insights"></a>
The analytics data that the `GetInsights` API returned.
Type: [Insights](API_Insights.md) object

## Errors
<a name="API_GetInsights_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 Your account isn't registered with AWS Audit Manager. Check the delegated administrator setup on the Audit Manager settings page, and try again.
HTTP Status Code: 403

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

## See Also
<a name="API_GetInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/auditmanager-2017-07-25/GetInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/auditmanager-2017-07-25/GetInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/GetInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/auditmanager-2017-07-25/GetInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/GetInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/auditmanager-2017-07-25/GetInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/auditmanager-2017-07-25/GetInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/auditmanager-2017-07-25/GetInsights)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/auditmanager-2017-07-25/GetInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/GetInsights)

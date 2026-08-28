---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetServiceQuota.html
---

# GetServiceQuota
<a name="API_GetServiceQuota"></a>

Retrieves the applied quota value for the specified account-level or resource-level quota. For some quotas, only the default values are available. If the applied quota value is not available for a quota, the quota is not retrieved.

**Related Actions**
+  [ListAWSDefaultServiceQuotas](API_ListAWSDefaultServiceQuotas.md)
+  [ListServices](API_ListServices.md)
+  [ListServiceQuotas](API_ListServiceQuotas.md)

## Request Syntax
<a name="API_GetServiceQuota_RequestSyntax"></a>

```
{
   "ContextId": "{{string}}",
   "QuotaCode": "{{string}}",
   "ServiceCode": "{{string}}"
}
```

## Request Parameters
<a name="API_GetServiceQuota_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContextId](#API_GetServiceQuota_RequestSyntax) **   <a name="servicequotas-GetServiceQuota-request-ContextId"></a>
Specifies the resource with an Amazon Resource Name (ARN).
Type: String
Required: No

 ** [QuotaCode](#API_GetServiceQuota_RequestSyntax) **   <a name="servicequotas-GetServiceQuota-request-QuotaCode"></a>
Specifies the quota identifier. To find the quota code for a specific quota, use the [ListServiceQuotas](API_ListServiceQuotas.md) operation, and look for the `QuotaCode` response in the output for the quota you want.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: Yes

 ** [ServiceCode](#API_GetServiceQuota_RequestSyntax) **   <a name="servicequotas-GetServiceQuota-request-ServiceCode"></a>
Specifies the service identifier. To find the service code value for an AWS service, use the [ListServices](API_ListServices.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,63}`
Required: Yes

## Response Syntax
<a name="API_GetServiceQuota_ResponseSyntax"></a>

```
{
   "Quota": {
      "Adjustable": boolean,
      "Description": "string",
      "ErrorReason": {
         "ErrorCode": "string",
         "ErrorMessage": "string"
      },
      "GlobalQuota": boolean,
      "Period": {
         "PeriodUnit": "string",
         "PeriodValue": number
      },
      "QuotaAppliedAtLevel": "string",
      "QuotaArn": "string",
      "QuotaCode": "string",
      "QuotaContext": {
         "ContextId": "string",
         "ContextScope": "string",
         "ContextScopeType": "string"
      },
      "QuotaName": "string",
      "ServiceCode": "string",
      "ServiceName": "string",
      "Unit": "string",
      "UsageMetric": {
         "MetricDimensions": {
            "string" : "string"
         },
         "MetricName": "string",
         "MetricNamespace": "string",
         "MetricStatisticRecommendation": "string"
      },
      "Value": number
   }
}
```

## Response Elements
<a name="API_GetServiceQuota_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Quota](#API_GetServiceQuota_ResponseSyntax) **   <a name="servicequotas-GetServiceQuota-response-Quota"></a>
Information about the quota.
Type: [ServiceQuota](API_ServiceQuota.md) object

## Errors
<a name="API_GetServiceQuota_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** IllegalArgumentException **
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
<a name="API_GetServiceQuota_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/GetServiceQuota)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/GetServiceQuota)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/GetServiceQuota)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/GetServiceQuota)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/GetServiceQuota)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/GetServiceQuota)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/GetServiceQuota)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/GetServiceQuota)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/GetServiceQuota)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/GetServiceQuota)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Service Quotas. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicequotas` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

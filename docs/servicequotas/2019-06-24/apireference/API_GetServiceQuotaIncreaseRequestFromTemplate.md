---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetServiceQuotaIncreaseRequestFromTemplate.html
---

# GetServiceQuotaIncreaseRequestFromTemplate
<a name="API_GetServiceQuotaIncreaseRequestFromTemplate"></a>

Retrieves information about the specified quota increase request in your quota request template.

**Related Actions**
+  [DeleteServiceQuotaIncreaseRequestFromTemplate](API_DeleteServiceQuotaIncreaseRequestFromTemplate.md)
+  [ListServiceQuotaIncreaseRequestsInTemplate](API_ListServiceQuotaIncreaseRequestsInTemplate.md)
+  [PutServiceQuotaIncreaseRequestIntoTemplate](API_PutServiceQuotaIncreaseRequestIntoTemplate.md)

## Request Syntax
<a name="API_GetServiceQuotaIncreaseRequestFromTemplate_RequestSyntax"></a>

```
{
   "AwsRegion": "{{string}}",
   "QuotaCode": "{{string}}",
   "ServiceCode": "{{string}}"
}
```

## Request Parameters
<a name="API_GetServiceQuotaIncreaseRequestFromTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AwsRegion](#API_GetServiceQuotaIncreaseRequestFromTemplate_RequestSyntax) **   <a name="servicequotas-GetServiceQuotaIncreaseRequestFromTemplate-request-AwsRegion"></a>
Specifies the AWS Region for which you made the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: Yes

 ** [QuotaCode](#API_GetServiceQuotaIncreaseRequestFromTemplate_RequestSyntax) **   <a name="servicequotas-GetServiceQuotaIncreaseRequestFromTemplate-request-QuotaCode"></a>
Specifies the quota identifier. To find the quota code for a specific quota, use the [ListServiceQuotas](API_ListServiceQuotas.md) operation, and look for the `QuotaCode` response in the output for the quota you want.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: Yes

 ** [ServiceCode](#API_GetServiceQuotaIncreaseRequestFromTemplate_RequestSyntax) **   <a name="servicequotas-GetServiceQuotaIncreaseRequestFromTemplate-request-ServiceCode"></a>
Specifies the service identifier. To find the service code value for an AWS service, use the [ListServices](API_ListServices.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,63}`
Required: Yes

## Response Syntax
<a name="API_GetServiceQuotaIncreaseRequestFromTemplate_ResponseSyntax"></a>

```
{
   "ServiceQuotaIncreaseRequestInTemplate": {
      "AwsRegion": "string",
      "DesiredValue": number,
      "GlobalQuota": boolean,
      "QuotaCode": "string",
      "QuotaName": "string",
      "ServiceCode": "string",
      "ServiceName": "string",
      "Unit": "string"
   }
}
```

## Response Elements
<a name="API_GetServiceQuotaIncreaseRequestFromTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ServiceQuotaIncreaseRequestInTemplate](#API_GetServiceQuotaIncreaseRequestFromTemplate_ResponseSyntax) **   <a name="servicequotas-GetServiceQuotaIncreaseRequestFromTemplate-response-ServiceQuotaIncreaseRequestInTemplate"></a>
Information about the quota increase request.
Type: [ServiceQuotaIncreaseRequestInTemplate](API_ServiceQuotaIncreaseRequestInTemplate.md) object

## Errors
<a name="API_GetServiceQuotaIncreaseRequestFromTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** AWSServiceAccessNotEnabledException **
The action you attempted is not allowed unless Service Access with Service Quotas is enabled in your organization.
HTTP Status Code: 400

 ** DependencyAccessDeniedException **
You can't perform this action because a dependency does not have access.
HTTP Status Code: 400

 ** IllegalArgumentException **
Invalid input was provided.
HTTP Status Code: 400

 ** NoAvailableOrganizationException **
The AWS account making this call is not a member of an organization.
HTTP Status Code: 400

 ** NoSuchResourceException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceException **
Something went wrong.
HTTP Status Code: 500

 ** TemplatesNotAvailableInRegionException **
The Service Quotas template is not available in this AWS Region.
HTTP Status Code: 400

 ** TooManyRequestsException **
Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.
HTTP Status Code: 400

## See Also
<a name="API_GetServiceQuotaIncreaseRequestFromTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/GetServiceQuotaIncreaseRequestFromTemplate)

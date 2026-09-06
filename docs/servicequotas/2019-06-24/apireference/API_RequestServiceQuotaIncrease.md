---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html
---

# RequestServiceQuotaIncrease
<a name="API_RequestServiceQuotaIncrease"></a>

Submits a quota increase request for the specified quota at the account or resource level.

**Related Actions**
+  [GetRequestedServiceQuotaChange](API_GetRequestedServiceQuotaChange.md)
+  [ListRequestedServiceQuotaChangeHistory](API_ListRequestedServiceQuotaChangeHistory.md)
+  [ListRequestedServiceQuotaChangeHistoryByQuota](API_ListRequestedServiceQuotaChangeHistoryByQuota.md)

## Request Syntax
<a name="API_RequestServiceQuotaIncrease_RequestSyntax"></a>

```
{
   "ContextId": "{{string}}",
   "DesiredValue": {{number}},
   "QuotaCode": "{{string}}",
   "ServiceCode": "{{string}}",
   "SupportCaseAllowed": {{boolean}}
}
```

## Request Parameters
<a name="API_RequestServiceQuotaIncrease_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContextId](#API_RequestServiceQuotaIncrease_RequestSyntax) **   <a name="servicequotas-RequestServiceQuotaIncrease-request-ContextId"></a>
Specifies the resource with an Amazon Resource Name (ARN).
Type: String
Required: No

 ** [DesiredValue](#API_RequestServiceQuotaIncrease_RequestSyntax) **   <a name="servicequotas-RequestServiceQuotaIncrease-request-DesiredValue"></a>
Specifies the new, increased value for the quota.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 10000000000.
Required: Yes

 ** [QuotaCode](#API_RequestServiceQuotaIncrease_RequestSyntax) **   <a name="servicequotas-RequestServiceQuotaIncrease-request-QuotaCode"></a>
Specifies the quota identifier. To find the quota code for a specific quota, use the [ListServiceQuotas](API_ListServiceQuotas.md) operation, and look for the `QuotaCode` response in the output for the quota you want.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: Yes

 ** [ServiceCode](#API_RequestServiceQuotaIncrease_RequestSyntax) **   <a name="servicequotas-RequestServiceQuotaIncrease-request-ServiceCode"></a>
Specifies the service identifier. To find the service code value for an AWS service, use the [ListServices](API_ListServices.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,63}`
Required: Yes

 ** [SupportCaseAllowed](#API_RequestServiceQuotaIncrease_RequestSyntax) **   <a name="servicequotas-RequestServiceQuotaIncrease-request-SupportCaseAllowed"></a>
Specifies if an AWS Support case can be opened for the quota increase request. This parameter is optional.
By default, this flag is set to `True` and AWS may create a support case for some quota increase requests. You can set this flag to `False` if you do not want a support case created when you request a quota increase. If you set the flag to `False`, AWS does not open a support case and updates the request status to `Not approved`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_RequestServiceQuotaIncrease_ResponseSyntax"></a>

```
{
   "RequestedQuota": {
      "CaseId": "string",
      "Created": number,
      "DesiredValue": number,
      "GlobalQuota": boolean,
      "Id": "string",
      "LastUpdated": number,
      "QuotaArn": "string",
      "QuotaCode": "string",
      "QuotaContext": {
         "ContextId": "string",
         "ContextScope": "string",
         "ContextScopeType": "string"
      },
      "QuotaName": "string",
      "QuotaRequestedAtLevel": "string",
      "Requester": "string",
      "RequestType": "string",
      "ServiceCode": "string",
      "ServiceName": "string",
      "Status": "string",
      "Unit": "string"
   }
}
```

## Response Elements
<a name="API_RequestServiceQuotaIncrease_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestedQuota](#API_RequestServiceQuotaIncrease_ResponseSyntax) **   <a name="servicequotas-RequestServiceQuotaIncrease-response-RequestedQuota"></a>
Information about the quota increase request.
Type: [RequestedServiceQuotaChange](API_RequestedServiceQuotaChange.md) object

## Errors
<a name="API_RequestServiceQuotaIncrease_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** DependencyAccessDeniedException **
You can't perform this action because a dependency does not have access.
HTTP Status Code: 400

 ** IllegalArgumentException **
Invalid input was provided.
HTTP Status Code: 400

 ** InvalidResourceStateException **
The resource is in an invalid state.
HTTP Status Code: 400

 ** NoSuchResourceException **
The specified resource does not exist.
HTTP Status Code: 400

 ** QuotaExceededException **
You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource already exists.
HTTP Status Code: 400

 ** ServiceException **
Something went wrong.
HTTP Status Code: 500

 ** TooManyRequestsException **
Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.
HTTP Status Code: 400

## See Also
<a name="API_RequestServiceQuotaIncrease_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/RequestServiceQuotaIncrease)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/RequestServiceQuotaIncrease)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/RequestServiceQuotaIncrease)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/RequestServiceQuotaIncrease)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/RequestServiceQuotaIncrease)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/RequestServiceQuotaIncrease)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/RequestServiceQuotaIncrease)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/RequestServiceQuotaIncrease)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/RequestServiceQuotaIncrease)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/RequestServiceQuotaIncrease)

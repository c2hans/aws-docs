---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_GetRequestedServiceQuotaChange.html
---

# GetRequestedServiceQuotaChange
<a name="API_GetRequestedServiceQuotaChange"></a>

Retrieves information about the specified quota increase request.

## Request Syntax
<a name="API_GetRequestedServiceQuotaChange_RequestSyntax"></a>

```
{
   "RequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetRequestedServiceQuotaChange_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RequestId](#API_GetRequestedServiceQuotaChange_RequestSyntax) **   <a name="servicequotas-GetRequestedServiceQuotaChange-request-RequestId"></a>
Specifies the ID of the quota increase request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-zA-Z][a-zA-Z0-9-]{1,128}`
Required: Yes

## Response Syntax
<a name="API_GetRequestedServiceQuotaChange_ResponseSyntax"></a>

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
<a name="API_GetRequestedServiceQuotaChange_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestedQuota](#API_GetRequestedServiceQuotaChange_ResponseSyntax) **   <a name="servicequotas-GetRequestedServiceQuotaChange-response-RequestedQuota"></a>
Information about the quota increase request.
Type: [RequestedServiceQuotaChange](API_RequestedServiceQuotaChange.md) object

## Errors
<a name="API_GetRequestedServiceQuotaChange_Errors"></a>

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
<a name="API_GetRequestedServiceQuotaChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/GetRequestedServiceQuotaChange)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/GetRequestedServiceQuotaChange)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/GetRequestedServiceQuotaChange)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/GetRequestedServiceQuotaChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/GetRequestedServiceQuotaChange)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/GetRequestedServiceQuotaChange)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/GetRequestedServiceQuotaChange)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/GetRequestedServiceQuotaChange)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/GetRequestedServiceQuotaChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/GetRequestedServiceQuotaChange)

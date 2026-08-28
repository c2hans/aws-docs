---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_ListRequestedServiceQuotaChangeHistory.html
---

# ListRequestedServiceQuotaChangeHistory
<a name="API_ListRequestedServiceQuotaChangeHistory"></a>

Retrieves the quota increase requests for the specified AWS service. Filter responses to return quota requests at either the account level, resource level, or all levels. Responses include any open or closed requests within 90 days.

## Request Syntax
<a name="API_ListRequestedServiceQuotaChangeHistory_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "QuotaRequestedAtLevel": "{{string}}",
   "ServiceCode": "{{string}}",
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRequestedServiceQuotaChangeHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListRequestedServiceQuotaChangeHistory_RequestSyntax) **   <a name="servicequotas-ListRequestedServiceQuotaChangeHistory-request-MaxResults"></a>
Specifies the maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the `NextToken` response element is present and has a value (is not null). Include that value as the `NextToken` request parameter in the next call to the operation to get the next part of the results.
An API operation can return fewer results than the maximum even when there are more results available. You should check `NextToken` after every operation to ensure that you receive all of the results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListRequestedServiceQuotaChangeHistory_RequestSyntax) **   <a name="servicequotas-ListRequestedServiceQuotaChangeHistory-request-NextToken"></a>
Specifies a value for receiving additional results after you receive a `NextToken` response in a previous request. A `NextToken` response indicates that more output is available. Set this parameter to the value of the previous call's `NextToken` response to indicate where the output should continue from.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9/+]*={0,2}$`
Required: No

 ** [QuotaRequestedAtLevel](#API_ListRequestedServiceQuotaChangeHistory_RequestSyntax) **   <a name="servicequotas-ListRequestedServiceQuotaChangeHistory-request-QuotaRequestedAtLevel"></a>
Filters the response to return quota requests for the `ACCOUNT`, `RESOURCE`, or `ALL` levels. `ACCOUNT` is the default.
Type: String
Valid Values: `ACCOUNT | RESOURCE | ALL`
Required: No

 ** [ServiceCode](#API_ListRequestedServiceQuotaChangeHistory_RequestSyntax) **   <a name="servicequotas-ListRequestedServiceQuotaChangeHistory-request-ServiceCode"></a>
Specifies the service identifier. To find the service code value for an AWS service, use the [ListServices](API_ListServices.md) operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z][a-zA-Z0-9-]{1,63}`
Required: No

 ** [Status](#API_ListRequestedServiceQuotaChangeHistory_RequestSyntax) **   <a name="servicequotas-ListRequestedServiceQuotaChangeHistory-request-Status"></a>
Specifies that you want to filter the results to only the requests with the matching status.
Type: String
Valid Values: `PENDING | CASE_OPENED | APPROVED | DENIED | CASE_CLOSED | NOT_APPROVED | INVALID_REQUEST`
Required: No

## Response Syntax
<a name="API_ListRequestedServiceQuotaChangeHistory_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RequestedQuotas": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListRequestedServiceQuotaChangeHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRequestedServiceQuotaChangeHistory_ResponseSyntax) **   <a name="servicequotas-ListRequestedServiceQuotaChangeHistory-response-NextToken"></a>
If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null`.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[a-zA-Z0-9/+]*={0,2}$`

 ** [RequestedQuotas](#API_ListRequestedServiceQuotaChangeHistory_ResponseSyntax) **   <a name="servicequotas-ListRequestedServiceQuotaChangeHistory-response-RequestedQuotas"></a>
Information about the quota increase requests.
Type: Array of [RequestedServiceQuotaChange](API_RequestedServiceQuotaChange.md) objects

## Errors
<a name="API_ListRequestedServiceQuotaChangeHistory_Errors"></a>

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
<a name="API_ListRequestedServiceQuotaChangeHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Service Quotas. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicequotas` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

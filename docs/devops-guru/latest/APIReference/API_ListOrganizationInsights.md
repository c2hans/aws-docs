---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListOrganizationInsights.html
---

# ListOrganizationInsights
<a name="API_ListOrganizationInsights"></a>

**Note**
End of support notice: On September 30, 2027, AWS will end support for Amazon DevOps Guru. After September 30, 2027, you will no longer be able to access the Amazon DevOps Guru console or Amazon DevOps Guru resources. For more information, see [Amazon DevOps Guru end of support](https://docs.aws.amazon.com/devops-guru/latest/userguide/devops-guru-end-of-support.html).

Returns a list of insights associated with the account or OU Id.

## Request Syntax
<a name="API_ListOrganizationInsights_RequestSyntax"></a>

```
POST /organization/insights HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "OrganizationalUnitIds": [ "{{string}}" ],
   "StatusFilter": {
      "Any": {
         "StartTimeRange": {
            "FromTime": {{number}},
            "ToTime": {{number}}
         },
         "Type": "{{string}}"
      },
      "Closed": {
         "EndTimeRange": {
            "FromTime": {{number}},
            "ToTime": {{number}}
         },
         "Type": "{{string}}"
      },
      "Ongoing": {
         "Type": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_ListOrganizationInsights_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListOrganizationInsights_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_ListOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-ListOrganizationInsights-request-AccountIds"></a>
The ID of the AWS account.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [MaxResults](#API_ListOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-ListOrganizationInsights-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-ListOrganizationInsights-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** [OrganizationalUnitIds](#API_ListOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-ListOrganizationInsights-request-OrganizationalUnitIds"></a>
The ID of the organizational unit.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Maximum length of 68.
Pattern: `^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$`
Required: No

 ** [StatusFilter](#API_ListOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-ListOrganizationInsights-request-StatusFilter"></a>
 A filter used by `ListInsights` to specify which insights to return.
Type: [ListInsightsStatusFilter](API_ListInsightsStatusFilter.md) object
Required: Yes

## Response Syntax
<a name="API_ListOrganizationInsights_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProactiveInsights": [
      {
         "AccountId": "string",
         "Id": "string",
         "InsightTimeRange": {
            "EndTime": number,
            "StartTime": number
         },
         "Name": "string",
         "OrganizationalUnitId": "string",
         "PredictionTimeRange": {
            "EndTime": number,
            "StartTime": number
         },
         "ResourceCollection": {
            "CloudFormation": {
               "StackNames": [ "string" ]
            },
            "Tags": [
               {
                  "AppBoundaryKey": "string",
                  "TagValues": [ "string" ]
               }
            ]
         },
         "ServiceCollection": {
            "ServiceNames": [ "string" ]
         },
         "Severity": "string",
         "Status": "string"
      }
   ],
   "ReactiveInsights": [
      {
         "AccountId": "string",
         "Id": "string",
         "InsightTimeRange": {
            "EndTime": number,
            "StartTime": number
         },
         "Name": "string",
         "OrganizationalUnitId": "string",
         "ResourceCollection": {
            "CloudFormation": {
               "StackNames": [ "string" ]
            },
            "Tags": [
               {
                  "AppBoundaryKey": "string",
                  "TagValues": [ "string" ]
               }
            ]
         },
         "ServiceCollection": {
            "ServiceNames": [ "string" ]
         },
         "Severity": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOrganizationInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOrganizationInsights_ResponseSyntax) **   <a name="DevOpsGuru-ListOrganizationInsights-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [ProactiveInsights](#API_ListOrganizationInsights_ResponseSyntax) **   <a name="DevOpsGuru-ListOrganizationInsights-response-ProactiveInsights"></a>
An integer that specifies the number of open proactive insights in your AWS account.
Type: Array of [ProactiveOrganizationInsightSummary](API_ProactiveOrganizationInsightSummary.md) objects

 ** [ReactiveInsights](#API_ListOrganizationInsights_ResponseSyntax) **   <a name="DevOpsGuru-ListOrganizationInsights-response-ReactiveInsights"></a>
An integer that specifies the number of open reactive insights in your AWS account.
Type: Array of [ReactiveOrganizationInsightSummary](API_ReactiveOrganizationInsightSummary.md) objects

## Errors
<a name="API_ListOrganizationInsights_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_ListOrganizationInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/ListOrganizationInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/ListOrganizationInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ListOrganizationInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/ListOrganizationInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ListOrganizationInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/ListOrganizationInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/ListOrganizationInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/ListOrganizationInsights)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/ListOrganizationInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ListOrganizationInsights)

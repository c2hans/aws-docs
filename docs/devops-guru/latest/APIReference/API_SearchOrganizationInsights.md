---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_SearchOrganizationInsights.html
---

# SearchOrganizationInsights
<a name="API_SearchOrganizationInsights"></a>

 Returns a list of insights in your organization. You can specify which insights are returned by their start time, one or more statuses (`ONGOING`, `CLOSED`, and `CLOSED`), one or more severities (`LOW`, `MEDIUM`, and `HIGH`), and type (`REACTIVE` or `PROACTIVE`).

 Use the `Filters` parameter to specify status and severity search parameters. Use the `Type` parameter to specify `REACTIVE` or `PROACTIVE` in your search.

## Request Syntax
<a name="API_SearchOrganizationInsights_RequestSyntax"></a>

```
POST /organization/insights/search HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "Filters": {
      "ResourceCollection": {
         "CloudFormation": {
            "StackNames": [ "{{string}}" ]
         },
         "Tags": [
            {
               "AppBoundaryKey": "{{string}}",
               "TagValues": [ "{{string}}" ]
            }
         ]
      },
      "ServiceCollection": {
         "ServiceNames": [ "{{string}}" ]
      },
      "Severities": [ "{{string}}" ],
      "Statuses": [ "{{string}}" ]
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StartTimeRange": {
      "FromTime": {{number}},
      "ToTime": {{number}}
   },
   "Type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchOrganizationInsights_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchOrganizationInsights_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_SearchOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-SearchOrganizationInsights-request-AccountIds"></a>
The ID of the AWS account.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: Yes

 ** [Filters](#API_SearchOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-SearchOrganizationInsights-request-Filters"></a>
 A `SearchOrganizationInsightsFilters` object that is used to set the severity and status filters on your insight search.
Type: [SearchOrganizationInsightsFilters](API_SearchOrganizationInsightsFilters.md) object
Required: No

 ** [MaxResults](#API_SearchOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-SearchOrganizationInsights-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-SearchOrganizationInsights-request-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** [StartTimeRange](#API_SearchOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-SearchOrganizationInsights-request-StartTimeRange"></a>
 A time range used to specify when the behavior of an insight or anomaly started.
Type: [StartTimeRange](API_StartTimeRange.md) object
Required: Yes

 ** [Type](#API_SearchOrganizationInsights_RequestSyntax) **   <a name="DevOpsGuru-SearchOrganizationInsights-request-Type"></a>
 The type of insights you are searching for (`REACTIVE` or `PROACTIVE`).
Type: String
Valid Values: `REACTIVE | PROACTIVE`
Required: Yes

## Response Syntax
<a name="API_SearchOrganizationInsights_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProactiveInsights": [
      {
         "AssociatedResourceArns": [ "string" ],
         "Id": "string",
         "InsightTimeRange": {
            "EndTime": number,
            "StartTime": number
         },
         "Name": "string",
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
         "AssociatedResourceArns": [ "string" ],
         "Id": "string",
         "InsightTimeRange": {
            "EndTime": number,
            "StartTime": number
         },
         "Name": "string",
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
<a name="API_SearchOrganizationInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_SearchOrganizationInsights_ResponseSyntax) **   <a name="DevOpsGuru-SearchOrganizationInsights-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [ProactiveInsights](#API_SearchOrganizationInsights_ResponseSyntax) **   <a name="DevOpsGuru-SearchOrganizationInsights-response-ProactiveInsights"></a>
An integer that specifies the number of open proactive insights in your AWS account.
Type: Array of [ProactiveInsightSummary](API_ProactiveInsightSummary.md) objects

 ** [ReactiveInsights](#API_SearchOrganizationInsights_ResponseSyntax) **   <a name="DevOpsGuru-SearchOrganizationInsights-response-ReactiveInsights"></a>
An integer that specifies the number of open reactive insights in your AWS account.
Type: Array of [ReactiveInsightSummary](API_ReactiveInsightSummary.md) objects

## Errors
<a name="API_SearchOrganizationInsights_Errors"></a>

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
<a name="API_SearchOrganizationInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/SearchOrganizationInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/SearchOrganizationInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/SearchOrganizationInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/SearchOrganizationInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/SearchOrganizationInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/SearchOrganizationInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/SearchOrganizationInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/SearchOrganizationInsights)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/SearchOrganizationInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/SearchOrganizationInsights)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

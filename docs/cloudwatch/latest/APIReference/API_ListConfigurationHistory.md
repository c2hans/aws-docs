---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListConfigurationHistory.html
---

# ListConfigurationHistory
<a name="API_ListConfigurationHistory"></a>

 Lists the INFO, WARN, and ERROR events for periodic configuration updates performed by Application Insights. Examples of events represented are:
+ INFO: creating a new alarm or updating an alarm threshold.
+ WARN: alarm not created due to insufficient data points used to predict thresholds.
+ ERROR: alarm not created due to permission errors or exceeding quotas.

## Request Syntax
<a name="API_ListConfigurationHistory_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "EndTime": {{number}},
   "EventStatus": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceGroupName": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_ListConfigurationHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_ListConfigurationHistory_RequestSyntax) **   <a name="appinsights-ListConfigurationHistory-request-AccountId"></a>
The AWS account ID for the resource group owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [EndTime](#API_ListConfigurationHistory_RequestSyntax) **   <a name="appinsights-ListConfigurationHistory-request-EndTime"></a>
The end time of the event.
Type: Timestamp
Required: No

 ** [EventStatus](#API_ListConfigurationHistory_RequestSyntax) **   <a name="appinsights-ListConfigurationHistory-request-EventStatus"></a>
The status of the configuration update event. Possible values include INFO, WARN, and ERROR.
Type: String
Valid Values: `INFO | WARN | ERROR`
Required: No

 ** [MaxResults](#API_ListConfigurationHistory_RequestSyntax) **   <a name="appinsights-ListConfigurationHistory-request-MaxResults"></a>
 The maximum number of results returned by `ListConfigurationHistory` in paginated output. When this parameter is used, `ListConfigurationHistory` returns only `MaxResults` in a single page along with a `NextToken` response element. The remaining results of the initial request can be seen by sending another `ListConfigurationHistory` request with the returned `NextToken` value. If this parameter is not used, then `ListConfigurationHistory` returns all results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 40.
Required: No

 ** [NextToken](#API_ListConfigurationHistory_RequestSyntax) **   <a name="appinsights-ListConfigurationHistory-request-NextToken"></a>
The `NextToken` value returned from a previous paginated `ListConfigurationHistory` request where `MaxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `NextToken` value. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [ResourceGroupName](#API_ListConfigurationHistory_RequestSyntax) **   <a name="appinsights-ListConfigurationHistory-request-ResourceGroupName"></a>
Resource group to which the application belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: No

 ** [StartTime](#API_ListConfigurationHistory_RequestSyntax) **   <a name="appinsights-ListConfigurationHistory-request-StartTime"></a>
The start time of the event.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_ListConfigurationHistory_ResponseSyntax"></a>

```
{
   "EventList": [
      {
         "AccountId": "string",
         "EventDetail": "string",
         "EventResourceName": "string",
         "EventResourceType": "string",
         "EventStatus": "string",
         "EventTime": number,
         "MonitoredResourceARN": "string",
         "ResourceGroupName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConfigurationHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventList](#API_ListConfigurationHistory_ResponseSyntax) **   <a name="appinsights-ListConfigurationHistory-response-EventList"></a>
 The list of configuration events and their corresponding details.
Type: Array of [ConfigurationEvent](API_ConfigurationEvent.md) objects

 ** [NextToken](#API_ListConfigurationHistory_ResponseSyntax) **   <a name="appinsights-ListConfigurationHistory-response-NextToken"></a>
The `NextToken` value to include in a future `ListConfigurationHistory` request. When the results of a `ListConfigurationHistory` request exceed `MaxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

## Errors
<a name="API_ListConfigurationHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource does not exist in the customer account.
HTTP Status Code: 400

 ** ValidationException **
The parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListConfigurationHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/ListConfigurationHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/ListConfigurationHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/ListConfigurationHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/ListConfigurationHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/ListConfigurationHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/ListConfigurationHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/ListConfigurationHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/ListConfigurationHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/ListConfigurationHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/ListConfigurationHistory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

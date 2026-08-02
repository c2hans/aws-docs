---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListProblems.html
---

# ListProblems
<a name="API_ListProblems"></a>

Lists the problems with your application.

## Request Syntax
<a name="API_ListProblems_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "ComponentName": "{{string}}",
   "EndTime": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceGroupName": "{{string}}",
   "StartTime": {{number}},
   "Visibility": "{{string}}"
}
```

## Request Parameters
<a name="API_ListProblems_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_ListProblems_RequestSyntax) **   <a name="appinsights-ListProblems-request-AccountId"></a>
The AWS account ID for the resource group owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [ComponentName](#API_ListProblems_RequestSyntax) **   <a name="appinsights-ListProblems-request-ComponentName"></a>
 The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `(?:^[\d\w\-_\.+]*$)|(?:^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$)`
Required: No

 ** [EndTime](#API_ListProblems_RequestSyntax) **   <a name="appinsights-ListProblems-request-EndTime"></a>
The time when the problem ended, in epoch seconds. If not specified, problems within the past seven days are returned.
Type: Timestamp
Required: No

 ** [MaxResults](#API_ListProblems_RequestSyntax) **   <a name="appinsights-ListProblems-request-MaxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 40.
Required: No

 ** [NextToken](#API_ListProblems_RequestSyntax) **   <a name="appinsights-ListProblems-request-NextToken"></a>
The token to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [ResourceGroupName](#API_ListProblems_RequestSyntax) **   <a name="appinsights-ListProblems-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: No

 ** [StartTime](#API_ListProblems_RequestSyntax) **   <a name="appinsights-ListProblems-request-StartTime"></a>
The time when the problem was detected, in epoch seconds. If you don't specify a time frame for the request, problems within the past seven days are returned.
Type: Timestamp
Required: No

 ** [Visibility](#API_ListProblems_RequestSyntax) **   <a name="appinsights-ListProblems-request-Visibility"></a>
Specifies whether or not you can view the problem. If not specified, visible and ignored problems are returned.
Type: String
Valid Values: `IGNORED | VISIBLE`
Required: No

## Response Syntax
<a name="API_ListProblems_ResponseSyntax"></a>

```
{
   "AccountId": "string",
   "NextToken": "string",
   "ProblemList": [
      {
         "AccountId": "string",
         "AffectedResource": "string",
         "EndTime": number,
         "Feedback": {
            "string" : "string"
         },
         "Id": "string",
         "Insights": "string",
         "LastRecurrenceTime": number,
         "RecurringCount": number,
         "ResolutionMethod": "string",
         "ResourceGroupName": "string",
         "SeverityLevel": "string",
         "ShortName": "string",
         "StartTime": number,
         "Status": "string",
         "Title": "string",
         "Visibility": "string"
      }
   ],
   "ResourceGroupName": "string"
}
```

## Response Elements
<a name="API_ListProblems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccountId](#API_ListProblems_ResponseSyntax) **   <a name="appinsights-ListProblems-response-AccountId"></a>
The AWS account ID for the resource group owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`

 ** [NextToken](#API_ListProblems_ResponseSyntax) **   <a name="appinsights-ListProblems-response-NextToken"></a>
The token used to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [ProblemList](#API_ListProblems_ResponseSyntax) **   <a name="appinsights-ListProblems-response-ProblemList"></a>
The list of problems.
Type: Array of [Problem](API_Problem.md) objects

 ** [ResourceGroupName](#API_ListProblems_ResponseSyntax) **   <a name="appinsights-ListProblems-response-ResourceGroupName"></a>
 The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`

## Errors
<a name="API_ListProblems_Errors"></a>

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
<a name="API_ListProblems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/ListProblems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/ListProblems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/ListProblems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/ListProblems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/ListProblems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/ListProblems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/ListProblems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/ListProblems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/ListProblems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/ListProblems)

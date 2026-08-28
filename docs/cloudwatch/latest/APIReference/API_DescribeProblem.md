---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeProblem.html
---

# DescribeProblem
<a name="API_DescribeProblem"></a>

Describes an application problem.

## Request Syntax
<a name="API_DescribeProblem_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "ProblemId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeProblem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_DescribeProblem_RequestSyntax) **   <a name="appinsights-DescribeProblem-request-AccountId"></a>
The AWS account ID for the owner of the resource group affected by the problem.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [ProblemId](#API_DescribeProblem_RequestSyntax) **   <a name="appinsights-DescribeProblem-request-ProblemId"></a>
The ID of the problem.
Type: String
Length Constraints: Fixed length of 38.
Pattern: `p-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
Required: Yes

## Response Syntax
<a name="API_DescribeProblem_ResponseSyntax"></a>

```
{
   "Problem": {
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
   },
   "SNSNotificationArn": "string"
}
```

## Response Elements
<a name="API_DescribeProblem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Problem](#API_DescribeProblem_ResponseSyntax) **   <a name="appinsights-DescribeProblem-response-Problem"></a>
Information about the problem.
Type: [Problem](API_Problem.md) object

 ** [SNSNotificationArn](#API_DescribeProblem_ResponseSyntax) **   <a name="appinsights-DescribeProblem-response-SNSNotificationArn"></a>
 The SNS notification topic ARN of the problem.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 300.
Pattern: `^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$`

## Errors
<a name="API_DescribeProblem_Errors"></a>

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
<a name="API_DescribeProblem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/DescribeProblem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/DescribeProblem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/DescribeProblem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/DescribeProblem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/DescribeProblem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/DescribeProblem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/DescribeProblem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/DescribeProblem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/DescribeProblem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/DescribeProblem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

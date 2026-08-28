---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateProblem.html
---

# UpdateProblem
<a name="API_UpdateProblem"></a>

Updates the visibility of the problem or specifies the problem as `RESOLVED`.

## Request Syntax
<a name="API_UpdateProblem_RequestSyntax"></a>

```
{
   "ProblemId": "{{string}}",
   "UpdateStatus": "{{string}}",
   "Visibility": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateProblem_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProblemId](#API_UpdateProblem_RequestSyntax) **   <a name="appinsights-UpdateProblem-request-ProblemId"></a>
The ID of the problem.
Type: String
Length Constraints: Fixed length of 38.
Pattern: `p-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
Required: Yes

 ** [UpdateStatus](#API_UpdateProblem_RequestSyntax) **   <a name="appinsights-UpdateProblem-request-UpdateStatus"></a>
The status of the problem. Arguments can be passed for only problems that show a status of `RECOVERING`.
Type: String
Valid Values: `RESOLVED`
Required: No

 ** [Visibility](#API_UpdateProblem_RequestSyntax) **   <a name="appinsights-UpdateProblem-request-Visibility"></a>
The visibility of a problem. When you pass a value of `IGNORED`, the problem is removed from the default view, and all notifications for the problem are suspended. When `VISIBLE` is passed, the `IGNORED` action is reversed.
Type: String
Valid Values: `IGNORED | VISIBLE`
Required: No

## Response Elements
<a name="API_UpdateProblem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateProblem_Errors"></a>

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
<a name="API_UpdateProblem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/UpdateProblem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/UpdateProblem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/UpdateProblem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/UpdateProblem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/UpdateProblem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/UpdateProblem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/UpdateProblem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/UpdateProblem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/UpdateProblem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/UpdateProblem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

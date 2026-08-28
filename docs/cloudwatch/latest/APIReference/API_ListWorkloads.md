---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListWorkloads.html
---

# ListWorkloads
<a name="API_ListWorkloads"></a>

Lists the workloads that are configured on a given component.

## Request Syntax
<a name="API_ListWorkloads_RequestSyntax"></a>

```
{
   "AccountId": "{{string}}",
   "ComponentName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListWorkloads_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountId](#API_ListWorkloads_RequestSyntax) **   <a name="appinsights-ListWorkloads-request-AccountId"></a>
The AWS account ID of the owner of the workload.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** [ComponentName](#API_ListWorkloads_RequestSyntax) **   <a name="appinsights-ListWorkloads-request-ComponentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `(?:^[\d\w\-_\.+]*$)|(?:^arn:aws(-\w+)*:[\w\d-]+:([\w\d-]*)?:[\w\d_-]*([:/].+)*$)`
Required: Yes

 ** [MaxResults](#API_ListWorkloads_RequestSyntax) **   <a name="appinsights-ListWorkloads-request-MaxResults"></a>
The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned `NextToken` value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 40.
Required: No

 ** [NextToken](#API_ListWorkloads_RequestSyntax) **   <a name="appinsights-ListWorkloads-request-NextToken"></a>
The token to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [ResourceGroupName](#API_ListWorkloads_RequestSyntax) **   <a name="appinsights-ListWorkloads-request-ResourceGroupName"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: Yes

## Response Syntax
<a name="API_ListWorkloads_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "WorkloadList": [
      {
         "ComponentName": "string",
         "MissingWorkloadConfig": boolean,
         "Tier": "string",
         "WorkloadId": "string",
         "WorkloadName": "string",
         "WorkloadRemarks": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkloads_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListWorkloads_ResponseSyntax) **   <a name="appinsights-ListWorkloads-response-NextToken"></a>
The token to request the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [WorkloadList](#API_ListWorkloads_ResponseSyntax) **   <a name="appinsights-ListWorkloads-response-WorkloadList"></a>
The list of workloads.
Type: Array of [Workload](API_Workload.md) objects

## Errors
<a name="API_ListWorkloads_Errors"></a>

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
<a name="API_ListWorkloads_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-insights-2018-11-25/ListWorkloads)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-insights-2018-11-25/ListWorkloads)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/ListWorkloads)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-insights-2018-11-25/ListWorkloads)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/ListWorkloads)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-insights-2018-11-25/ListWorkloads)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-insights-2018-11-25/ListWorkloads)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-insights-2018-11-25/ListWorkloads)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-insights-2018-11-25/ListWorkloads)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/ListWorkloads)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

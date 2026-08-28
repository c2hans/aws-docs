---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_StopQueryWorkloadInsightsTopContributors.html
---

# StopQueryWorkloadInsightsTopContributors
<a name="API_StopQueryWorkloadInsightsTopContributors"></a>

Stop a top contributors query for workload insights. Specify the query that you want to stop by providing a query ID and a scope ID.

Top contributors in Network Flow Monitor are network flows with the highest values for a specific metric type. Top contributors can be across all workload insights, for a given scope, or for a specific monitor. Use the applicable call for the top contributors that you want to be returned.

## Request Syntax
<a name="API_StopQueryWorkloadInsightsTopContributors_RequestSyntax"></a>

```
DELETE /workloadInsights/{{scopeId}}/topContributorsQueries/{{queryId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_StopQueryWorkloadInsightsTopContributors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [queryId](#API_StopQueryWorkloadInsightsTopContributors_RequestSyntax) **   <a name="networkflowmonitor-StopQueryWorkloadInsightsTopContributors-request-uri-queryId"></a>
The identifier for the query. A query ID is an internally-generated identifier for a specific query returned from an API call to create a query.
Required: Yes

 ** [scopeId](#API_StopQueryWorkloadInsightsTopContributors_RequestSyntax) **   <a name="networkflowmonitor-StopQueryWorkloadInsightsTopContributors-request-uri-scopeId"></a>
The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.
Required: Yes

## Request Body
<a name="API_StopQueryWorkloadInsightsTopContributors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopQueryWorkloadInsightsTopContributors_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StopQueryWorkloadInsightsTopContributors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopQueryWorkloadInsightsTopContributors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request exceeded a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
Invalid request.
HTTP Status Code: 400

## See Also
<a name="API_StopQueryWorkloadInsightsTopContributors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkflowmonitor-2023-04-19/StopQueryWorkloadInsightsTopContributors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkflowmonitor-2023-04-19/StopQueryWorkloadInsightsTopContributors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/StopQueryWorkloadInsightsTopContributors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkflowmonitor-2023-04-19/StopQueryWorkloadInsightsTopContributors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/StopQueryWorkloadInsightsTopContributors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkflowmonitor-2023-04-19/StopQueryWorkloadInsightsTopContributors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkflowmonitor-2023-04-19/StopQueryWorkloadInsightsTopContributors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkflowmonitor-2023-04-19/StopQueryWorkloadInsightsTopContributors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkflowmonitor-2023-04-19/StopQueryWorkloadInsightsTopContributors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/StopQueryWorkloadInsightsTopContributors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Flow Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkflowmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

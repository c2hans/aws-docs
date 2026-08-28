---
source_url: https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html
---

# ListWorkloads
<a name="API_ListWorkloads"></a>

Lists the available workload names. You can use the [ListWorkloadDeploymentPatterns](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html) operation to discover the available deployment patterns for a given workload.

## Request Syntax
<a name="API_ListWorkloads_RequestSyntax"></a>

```
POST /listWorkloads HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListWorkloads_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListWorkloads_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListWorkloads_RequestSyntax) **   <a name="launchwizard-ListWorkloads-request-maxResults"></a>
The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListWorkloads_RequestSyntax) **   <a name="launchwizard-ListWorkloads-request-nextToken"></a>
The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListWorkloads_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "workloads": [
      {
         "displayName": "string",
         "status": "string",
         "workloadName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListWorkloads_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListWorkloads_ResponseSyntax) **   <a name="launchwizard-ListWorkloads-response-nextToken"></a>
The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [workloads](#API_ListWorkloads_ResponseSyntax) **   <a name="launchwizard-ListWorkloads-response-workloads"></a>
Information about the workloads.
Type: Array of [WorkloadDataSummary](API_WorkloadDataSummary.md) objects

## Errors
<a name="API_ListWorkloads_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred. Retry your request, but if the problem persists, contact us with details by posting a question on [re:Post](https://repost.aws/).
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListWorkloads_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/launch-wizard-2018-05-10/ListWorkloads)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/launch-wizard-2018-05-10/ListWorkloads)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/launch-wizard-2018-05-10/ListWorkloads)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/launch-wizard-2018-05-10/ListWorkloads)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/launch-wizard-2018-05-10/ListWorkloads)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/launch-wizard-2018-05-10/ListWorkloads)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/launch-wizard-2018-05-10/ListWorkloads)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/launch-wizard-2018-05-10/ListWorkloads)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/launch-wizard-2018-05-10/ListWorkloads)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/launch-wizard-2018-05-10/ListWorkloads)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Launch Wizard. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query launchwizard` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

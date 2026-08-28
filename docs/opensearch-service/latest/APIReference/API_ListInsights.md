---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListInsights.html
---

# ListInsights
<a name="API_ListInsights"></a>

Lists insights for an Amazon OpenSearch Service domain or Amazon Web Services account. Returns a paginated list of insights based on the specified entity, filters, time range, and sort order.

## Request Syntax
<a name="API_ListInsights_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/insights HTTP/1.1
Content-type: application/json

{
   "Entity": {
      "Type": "{{string}}",
      "Value": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortOrder": "{{string}}",
   "TimeRange": {
      "From": {{number}},
      "To": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_ListInsights_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListInsights_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Entity](#API_ListInsights_RequestSyntax) **   <a name="opensearchservice-ListInsights-request-Entity"></a>
The entity for which to list insights. Specifies the type and value of the entity, such as a domain name or Amazon Web Services account ID.
Type: [InsightEntity](API_InsightEntity.md) object
Required: Yes

 ** [MaxResults](#API_ListInsights_RequestSyntax) **   <a name="opensearchservice-ListInsights-request-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `NextToken` to get the next page of results. Valid values are 1 to 500.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListInsights_RequestSyntax) **   <a name="opensearchservice-ListInsights-request-NextToken"></a>
If your initial `ListInsights` operation returns a `NextToken`, include the returned `NextToken` in subsequent `ListInsights` operations to retrieve the next page of results.
Type: String
Required: No

 ** [SortOrder](#API_ListInsights_RequestSyntax) **   <a name="opensearchservice-ListInsights-request-SortOrder"></a>
The sort order for the results. Possible values are `ASC` (ascending) and `DESC` (descending).
Type: String
Valid Values: `ASC | DESC`
Required: No

 ** [TimeRange](#API_ListInsights_RequestSyntax) **   <a name="opensearchservice-ListInsights-request-TimeRange"></a>
The time range for filtering insights, specified as epoch millisecond timestamps.
Type: [InsightTimeRange](API_InsightTimeRange.md) object
Required: No

## Response Syntax
<a name="API_ListInsights_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Insights": [
      {
         "CreationTime": number,
         "DisplayName": "string",
         "InsightId": "string",
         "IsExperimental": boolean,
         "Priority": "string",
         "Status": "string",
         "Type": "string",
         "UpdateTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInsights_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Insights](#API_ListInsights_ResponseSyntax) **   <a name="opensearchservice-ListInsights-response-Insights"></a>
The list of insights returned for the specified entity.
Type: Array of [Insight](API_Insight.md) objects

 ** [NextToken](#API_ListInsights_ResponseSyntax) **   <a name="opensearchservice-ListInsights-response-NextToken"></a>
When `NextToken` is returned, there are more results available. The value of `NextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListInsights_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_ListInsights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListInsights)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListInsights)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListInsights)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListInsights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListInsights)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListInsights)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListInsights)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListInsights)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListInsights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListInsights)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

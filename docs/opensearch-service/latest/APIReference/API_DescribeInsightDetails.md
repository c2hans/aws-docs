---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInsightDetails.html
---

# DescribeInsightDetails
<a name="API_DescribeInsightDetails"></a>

Describes the details of an existing insight for an Amazon OpenSearch Service domain. Returns detailed fields associated with the specified insight, such as text descriptions and metric data.

## Request Syntax
<a name="API_DescribeInsightDetails_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/insight-details HTTP/1.1
Content-type: application/json

{
   "Entity": {
      "Type": "{{string}}",
      "Value": "{{string}}"
   },
   "InsightId": "{{string}}",
   "ShowHtmlContent": {{boolean}}
}
```

## URI Request Parameters
<a name="API_DescribeInsightDetails_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeInsightDetails_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Entity](#API_DescribeInsightDetails_RequestSyntax) **   <a name="opensearchservice-DescribeInsightDetails-request-Entity"></a>
The entity for which to retrieve insight details. Specifies the type and value of the entity, such as a domain name or Amazon Web Services account ID.
Type: [InsightEntity](API_InsightEntity.md) object
Required: Yes

 ** [InsightId](#API_DescribeInsightDetails_RequestSyntax) **   <a name="opensearchservice-DescribeInsightDetails-request-InsightId"></a>
The unique identifier of the insight to describe.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`
Required: Yes

 ** [ShowHtmlContent](#API_DescribeInsightDetails_RequestSyntax) **   <a name="opensearchservice-DescribeInsightDetails-request-ShowHtmlContent"></a>
Specifies whether to show response with HTML content in response or not.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribeInsightDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Fields": [
      {
         "Name": "string",
         "Type": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeInsightDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Fields](#API_DescribeInsightDetails_ResponseSyntax) **   <a name="opensearchservice-DescribeInsightDetails-response-Fields"></a>
The list of fields that contain detailed information about the insight.
Type: Array of [InsightField](API_InsightField.md) objects

## Errors
<a name="API_DescribeInsightDetails_Errors"></a>

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
<a name="API_DescribeInsightDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeInsightDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeInsightDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeInsightDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeInsightDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeInsightDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeInsightDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeInsightDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeInsightDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeInsightDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeInsightDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

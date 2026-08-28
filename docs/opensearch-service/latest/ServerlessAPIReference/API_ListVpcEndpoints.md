---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListVpcEndpoints.html
---

# ListVpcEndpoints
<a name="API_ListVpcEndpoints"></a>

Returns the OpenSearch Serverless-managed interface VPC endpoints associated with the current account. For more information, see [Access Amazon OpenSearch Serverless using an interface endpoint](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vpc.html).

## Request Syntax
<a name="API_ListVpcEndpoints_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "vpcEndpointFilters": {
      "status": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ListVpcEndpoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListVpcEndpoints_RequestSyntax) **   <a name="opensearchserverless-ListVpcEndpoints-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results. The default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListVpcEndpoints_RequestSyntax) **   <a name="opensearchserverless-ListVpcEndpoints-request-nextToken"></a>
If your initial `ListVpcEndpoints` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListVpcEndpoints` operations, which returns results in the next page.
Type: String
Required: No

 ** [vpcEndpointFilters](#API_ListVpcEndpoints_RequestSyntax) **   <a name="opensearchserverless-ListVpcEndpoints-request-vpcEndpointFilters"></a>
Filter the results according to the current status of the VPC endpoint. Possible statuses are `CREATING`, `DELETING`, `UPDATING`, `ACTIVE`, and `FAILED`.
Type: [VpcEndpointFilters](API_VpcEndpointFilters.md) object
Required: No

## Response Syntax
<a name="API_ListVpcEndpoints_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "vpcEndpointSummaries": [
      {
         "id": "string",
         "name": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListVpcEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListVpcEndpoints_ResponseSyntax) **   <a name="opensearchserverless-ListVpcEndpoints-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String

 ** [vpcEndpointSummaries](#API_ListVpcEndpoints_ResponseSyntax) **   <a name="opensearchserverless-ListVpcEndpoints-response-vpcEndpointSummaries"></a>
Details about each VPC endpoint, including the name and current status.
Type: Array of [VpcEndpointSummary](API_VpcEndpointSummary.md) objects

## Errors
<a name="API_ListVpcEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_ListVpcEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/ListVpcEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/ListVpcEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/ListVpcEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/ListVpcEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/ListVpcEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/ListVpcEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/ListVpcEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/ListVpcEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/ListVpcEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/ListVpcEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

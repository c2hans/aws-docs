---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListEnabledProductsForImport.html
---

# ListEnabledProductsForImport
<a name="API_ListEnabledProductsForImport"></a>

Lists all findings-generating solutions (products) that you are subscribed to receive findings from in Security Hub CSPM.

## Request Syntax
<a name="API_ListEnabledProductsForImport_RequestSyntax"></a>

```
GET /productSubscriptions?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEnabledProductsForImport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListEnabledProductsForImport_RequestSyntax) **   <a name="securityhub-ListEnabledProductsForImport-request-uri-MaxResults"></a>
The maximum number of items to return in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListEnabledProductsForImport_RequestSyntax) **   <a name="securityhub-ListEnabledProductsForImport-request-uri-NextToken"></a>
The token that is required for pagination. On your first call to the `ListEnabledProductsForImport` operation, set the value of this parameter to `NULL`.
For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.

## Request Body
<a name="API_ListEnabledProductsForImport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEnabledProductsForImport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProductSubscriptions": [ "string" ]
}
```

## Response Elements
<a name="API_ListEnabledProductsForImport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListEnabledProductsForImport_ResponseSyntax) **   <a name="securityhub-ListEnabledProductsForImport-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String

 ** [ProductSubscriptions](#API_ListEnabledProductsForImport_ResponseSyntax) **   <a name="securityhub-ListEnabledProductsForImport-response-ProductSubscriptions"></a>
The list of ARNs for the resources that represent your subscriptions to products.
Type: Array of strings
Pattern: `.*\S.*`

## Errors
<a name="API_ListEnabledProductsForImport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListEnabledProductsForImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListEnabledProductsForImport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListEnabledProductsForImport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListEnabledProductsForImport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListEnabledProductsForImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListEnabledProductsForImport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListEnabledProductsForImport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListEnabledProductsForImport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListEnabledProductsForImport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListEnabledProductsForImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListEnabledProductsForImport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListOrders.html
---

# ListOrders
<a name="API_ListOrders"></a>

Lists the Outpost orders for your AWS account.

## Request Syntax
<a name="API_ListOrders_RequestSyntax"></a>

```
GET /list-orders?MaxResults={{MaxResults}}&NextToken={{NextToken}}&OutpostIdentifierFilter={{OutpostIdentifierFilter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListOrders_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListOrders_RequestSyntax) **   <a name="outposts-ListOrders-request-uri-MaxResults"></a>
The maximum page size.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListOrders_RequestSyntax) **   <a name="outposts-ListOrders-request-uri-NextToken"></a>
The pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [OutpostIdentifierFilter](#API_ListOrders_RequestSyntax) **   <a name="outposts-ListOrders-request-uri-OutpostIdentifierFilter"></a>
 The ID or the Amazon Resource Name (ARN) of the Outpost.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`

## Request Body
<a name="API_ListOrders_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListOrders_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Orders": [
      {
         "LineItemCountsByStatus": {
            "string" : number
         },
         "OrderFulfilledDate": number,
         "OrderId": "string",
         "OrderSubmissionDate": number,
         "OrderType": "string",
         "OutpostId": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOrders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOrders_ResponseSyntax) **   <a name="outposts-ListOrders-response-NextToken"></a>
The pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^(\d+)##(\S+)$`

 ** [Orders](#API_ListOrders_ResponseSyntax) **   <a name="outposts-ListOrders-response-Orders"></a>
 Information about the orders.
Type: Array of [OrderSummary](API_OrderSummary.md) objects

## Errors
<a name="API_ListOrders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListOrders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/ListOrders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/ListOrders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/ListOrders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/ListOrders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/ListOrders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/ListOrders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/ListOrders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/ListOrders)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/ListOrders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/ListOrders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

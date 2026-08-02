---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeProducts.html
---

# DescribeProducts
<a name="API_DescribeProducts"></a>

Returns information about product integrations in Security Hub CSPM.

You can optionally provide an integration ARN. If you provide an integration ARN, then the results only include that integration.

If you don't provide an integration ARN, then the results include all of the available product integrations.

## Request Syntax
<a name="API_DescribeProducts_RequestSyntax"></a>

```
GET /products?MaxResults={{MaxResults}}&NextToken={{NextToken}}&ProductArn={{ProductArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeProducts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_DescribeProducts_RequestSyntax) **   <a name="securityhub-DescribeProducts-request-uri-MaxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_DescribeProducts_RequestSyntax) **   <a name="securityhub-DescribeProducts-request-uri-NextToken"></a>
The token that is required for pagination. On your first call to the `DescribeProducts` operation, set the value of this parameter to `NULL`.
For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.

 ** [ProductArn](#API_DescribeProducts_RequestSyntax) **   <a name="securityhub-DescribeProducts-request-uri-ProductArn"></a>
The ARN of the integration to return.
Pattern: `.*\S.*`

## Request Body
<a name="API_DescribeProducts_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeProducts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Products": [
      {
         "ActivationUrl": "string",
         "Categories": [ "string" ],
         "CompanyName": "string",
         "Description": "string",
         "IntegrationTypes": [ "string" ],
         "MarketplaceUrl": "string",
         "ProductArn": "string",
         "ProductName": "string",
         "ProductSubscriptionResourcePolicy": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeProducts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeProducts_ResponseSyntax) **   <a name="securityhub-DescribeProducts-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String

 ** [Products](#API_DescribeProducts_ResponseSyntax) **   <a name="securityhub-DescribeProducts-response-Products"></a>
A list of products, including details for each product.
Type: Array of [Product](API_Product.md) objects

## Errors
<a name="API_DescribeProducts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeProducts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DescribeProducts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DescribeProducts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DescribeProducts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DescribeProducts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DescribeProducts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DescribeProducts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DescribeProducts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DescribeProducts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DescribeProducts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DescribeProducts)

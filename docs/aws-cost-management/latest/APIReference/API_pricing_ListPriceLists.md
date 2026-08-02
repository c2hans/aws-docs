---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html
---

# ListPriceLists
<a name="API_pricing_ListPriceLists"></a>

This returns a list of Price List references that the requester if authorized to view, given a `ServiceCode`, `CurrencyCode`, and an `EffectiveDate`. Use without a `RegionCode` filter to list Price List references from all available AWS Regions. Use with a `RegionCode` filter to get the Price List reference that's specific to a specific AWS Region. You can use the `PriceListArn` from the response to get your preferred Price List files through the [GetPriceListFileUrl](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetPriceListFileUrl.html) API.

## Request Syntax
<a name="API_pricing_ListPriceLists_RequestSyntax"></a>

```
{
   "CurrencyCode": "{{string}}",
   "EffectiveDate": {{number}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RegionCode": "{{string}}",
   "ServiceCode": "{{string}}"
}
```

## Request Parameters
<a name="API_pricing_ListPriceLists_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CurrencyCode](#API_pricing_ListPriceLists_RequestSyntax) **   <a name="awscostmanagement-pricing_ListPriceLists-request-CurrencyCode"></a>
The three alphabetical character ISO-4217 currency code that the Price List files are denominated in.
Type: String
Pattern: `[A-Z]{3}`
Required: Yes

 ** [EffectiveDate](#API_pricing_ListPriceLists_RequestSyntax) **   <a name="awscostmanagement-pricing_ListPriceLists-request-EffectiveDate"></a>
The date that the Price List file prices are effective from.
Type: Timestamp
Required: Yes

 ** [MaxResults](#API_pricing_ListPriceLists_RequestSyntax) **   <a name="awscostmanagement-pricing_ListPriceLists-request-MaxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_pricing_ListPriceLists_RequestSyntax) **   <a name="awscostmanagement-pricing_ListPriceLists-request-NextToken"></a>
The pagination token that indicates the next set of results that you want to retrieve.
Type: String
Required: No

 ** [RegionCode](#API_pricing_ListPriceLists_RequestSyntax) **   <a name="awscostmanagement-pricing_ListPriceLists-request-RegionCode"></a>
This is used to filter the Price List by AWS Region. For example, to get the price list only for the `US East (N. Virginia)` Region, use `us-east-1`. If nothing is specified, you retrieve price lists for all applicable Regions. The available `RegionCode` list can be retrieved from [GetAttributeValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.html) API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [ServiceCode](#API_pricing_ListPriceLists_RequestSyntax) **   <a name="awscostmanagement-pricing_ListPriceLists-request-ServiceCode"></a>
The service code or the Savings Plans service code for the attributes that you want to retrieve. For example, to get the list of applicable Amazon EC2 price lists, use `AmazonEC2`. For a full list of service codes containing On-Demand and Reserved Instance (RI) pricing, use the [DescribeServices](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_DescribeServices.html#awscostmanagement-pricing_DescribeServices-request-FormatVersion) API.
To retrieve the Reserved Instance and Compute Savings Plans price lists, use `ComputeSavingsPlans`.
To retrieve Machine Learning Savings Plans price lists, use `MachineLearningSavingsPlans`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

## Response Syntax
<a name="API_pricing_ListPriceLists_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PriceLists": [
      {
         "CurrencyCode": "string",
         "FileFormats": [ "string" ],
         "PriceListArn": "string",
         "RegionCode": "string"
      }
   ]
}
```

## Response Elements
<a name="API_pricing_ListPriceLists_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_pricing_ListPriceLists_ResponseSyntax) **   <a name="awscostmanagement-pricing_ListPriceLists-response-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String

 ** [PriceLists](#API_pricing_ListPriceLists_ResponseSyntax) **   <a name="awscostmanagement-pricing_ListPriceLists-response-PriceLists"></a>
The type of price list references that match your request.
Type: Array of [PriceList](API_pricing_PriceList.md) objects

## Errors
<a name="API_pricing_ListPriceLists_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
General authentication failure. The request wasn't signed correctly.
HTTP Status Code: 400

 ** ExpiredNextTokenException **
The pagination token expired. Try again without a pagination token.
HTTP Status Code: 400

 ** InternalErrorException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters had an invalid value.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource can't be found.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 400

 ** ThrottlingException **
You've made too many requests exceeding service quotas.
HTTP Status Code: 400

## Examples
<a name="API_pricing_ListPriceLists_Examples"></a>

### The following is a sample request and response of the ListPriceLists operation.
<a name="API_pricing_ListPriceLists_Example_1"></a>

This example illustrates one usage of ListPriceLists.

#### Sample Request
<a name="API_pricing_ListPriceLists_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.pricing.<region>.<domain>
x-amz-Date: <Date>Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>Connection: Keep-Alive
X-Amz-Target: AWSPriceListService.ListPriceLists{
    "ServiceCode": "AmazonEC2",
    "EffectiveDate": 1651363200,
    "CurrencyCode": "USD",
    "RegionCode": "us-east-1",
    "NextToken": null,
    "MaxResults": 10
}
```

#### Sample Response
<a name="API_pricing_ListPriceLists_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "PriceLists": [
        {
            "PriceListArn": "arn:aws:pricing:::price-list/aws/AmazonEC2/USD/20220603151047/us-east-1",
            "RegionCode": "us-east-1",
            "CurrencyCode": "USD",
            "FileFormats": [
                "json",
                "csv"
            ]
        }
    ],
    "NextToken": "abcdefg123"
}
```

## See Also
<a name="API_pricing_ListPriceLists_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pricing-2017-10-15/ListPriceLists)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pricing-2017-10-15/ListPriceLists)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-2017-10-15/ListPriceLists)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pricing-2017-10-15/ListPriceLists)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-2017-10-15/ListPriceLists)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pricing-2017-10-15/ListPriceLists)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pricing-2017-10-15/ListPriceLists)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pricing-2017-10-15/ListPriceLists)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pricing-2017-10-15/ListPriceLists)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-2017-10-15/ListPriceLists)

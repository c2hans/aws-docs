---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetProducts.html
---

# GetProducts
<a name="API_pricing_GetProducts"></a>

Returns a list of all products that match the filter criteria.

## Request Syntax
<a name="API_pricing_GetProducts_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Field": "{{string}}",
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "FormatVersion": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ServiceCode": "{{string}}"
}
```

## Request Parameters
<a name="API_pricing_GetProducts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_pricing_GetProducts_RequestSyntax) **   <a name="awscostmanagement-pricing_GetProducts-request-Filters"></a>
The list of filters that limit the returned products. only products that match all filters are returned.
Type: Array of [Filter](API_pricing_Filter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [FormatVersion](#API_pricing_GetProducts_RequestSyntax) **   <a name="awscostmanagement-pricing_GetProducts-request-FormatVersion"></a>
The format version that you want the response to be in.
Valid values are: `aws_v1`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** [MaxResults](#API_pricing_GetProducts_RequestSyntax) **   <a name="awscostmanagement-pricing_GetProducts-request-MaxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_pricing_GetProducts_RequestSyntax) **   <a name="awscostmanagement-pricing_GetProducts-request-NextToken"></a>
The pagination token that indicates the next set of results that you want to retrieve.
Type: String
Required: No

 ** [ServiceCode](#API_pricing_GetProducts_RequestSyntax) **   <a name="awscostmanagement-pricing_GetProducts-request-ServiceCode"></a>
The code for the service whose products you want to retrieve.
Type: String
Required: Yes

## Response Syntax
<a name="API_pricing_GetProducts_ResponseSyntax"></a>

```
{
   "FormatVersion": "string",
   "NextToken": "string",
   "PriceList": [ "string" ]
}
```

## Response Elements
<a name="API_pricing_GetProducts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FormatVersion](#API_pricing_GetProducts_ResponseSyntax) **   <a name="awscostmanagement-pricing_GetProducts-response-FormatVersion"></a>
The format version of the response. For example, aws\_v1.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.

 ** [NextToken](#API_pricing_GetProducts_ResponseSyntax) **   <a name="awscostmanagement-pricing_GetProducts-response-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String

 ** [PriceList](#API_pricing_GetProducts_ResponseSyntax) **   <a name="awscostmanagement-pricing_GetProducts-response-PriceList"></a>
The list of products that match your filters. The list contains both the product metadata and the price information.
Type: Array of strings

## Errors
<a name="API_pricing_GetProducts_Errors"></a>

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

 ** ThrottlingException **
You've made too many requests exceeding service quotas.
HTTP Status Code: 400

## Examples
<a name="API_pricing_GetProducts_Examples"></a>

### The following is a sample request and response of the GetProducts operation.
<a name="API_pricing_GetProducts_Example_1"></a>

This example illustrates one usage of GetProducts.

#### Sample Request
<a name="API_pricing_GetProducts_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.pricing.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSPriceListService.GetProducts
{
    "Filters": [
        {
            "Type": "TERM_MATCH",
            "Field": "ServiceCode",
            "Value": "AmazonEC2"
        },
        {
            "Type": "TERM_MATCH",
            "Field": "volumeType",
            "Value": "Provisioned IOPS"
        }
    ],
    "FormatVersion": "aws_v1",
    "NextToken": null,
    "MaxResults": 1,
    "ServiceCode":"AmazonEC2"
}
```

#### Sample Response
<a name="API_pricing_GetProducts_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "FormatVersion": "aws_v1",
    "NextToken": "57r3UcqRjDujbzWfHF7Ciw==:ywSmZsD3mtpQmQLQ5XfOsIMkYybSj+vAT+kGmwMFq+K9DGmIoJkz7lunVeamiOPgthdWSO2a7YKojCO+zY4dJmuNl2QvbNhXs+AJ2Ufn7xGmJncNI2TsEuAsVCUfTAvAQNcwwamtk6XuZ4YdNnooV62FjkV3ZAn40d9+wAxV7+FImvhUHi/+f8afgZdGh2zPUlH8jlV9uUtj0oHp8+DhPUuHXh+WBII1E/aoKpPSm3c=",
    "PriceList": [
        "{\"product\":{\"productFamily\":\"Storage\",\"attributes\":{\"storageMedia\":\"SSD-backed\",\"maxThroughputvolume\":\"320 MB/sec\",\"volumeType\":\"Provisioned IOPS\",\"maxIopsvolume\":\"20000\",\"servicecode\":\"AmazonEC2\",\"usagetype\":\"CAN1-EBS:VolumeUsage.piops\",\"locationType\":\"AWS Region\",\"location\":\"Canada (Central)\",\"servicename\":\"Amazon Elastic Compute Cloud\",\"maxVolumeSize\":\"16 TiB\",\"operation\":\"\"},\"sku\":\"WQGC34PB2AWS8R4U\"},\"serviceCode\":\"AmazonEC2\",\"terms\":{\"OnDemand\":{\"WQGC34PB2AWS8R4U.JRTCKXETXF\":{\"priceDimensions\":{\"WQGC34PB2AWS8R4U.JRTCKXETXF.6YS6EN2CT7\":{\"unit\":\"GB-Mo\",\"endRange\":\"Inf\",\"description\":\"$0.138 per GB-month of Provisioned IOPS SSD (io1)  provisioned storage - Canada (Central)\",\"appliesTo\":[],\"rateCode\":\"WQGC34PB2AWS8R4U.JRTCKXETXF.6YS6EN2CT7\",\"beginRange\":\"0\",\"pricePerUnit\":{\"USD\":\"0.1380000000\"}}},\"sku\":\"WQGC34PB2AWS8R4U\",\"effectiveDate\":\"2017-08-01T00:00:00Z\",\"offerTermCode\":\"JRTCKXETXF\",\"termAttributes\":{}}}},\"version\":\"20170901182201\",\"publicationDate\":\"2017-09-01T18:22:01Z\"}"
    ]
}
```

## See Also
<a name="API_pricing_GetProducts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pricing-2017-10-15/GetProducts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pricing-2017-10-15/GetProducts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-2017-10-15/GetProducts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pricing-2017-10-15/GetProducts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-2017-10-15/GetProducts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pricing-2017-10-15/GetProducts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pricing-2017-10-15/GetProducts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pricing-2017-10-15/GetProducts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pricing-2017-10-15/GetProducts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-2017-10-15/GetProducts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetPriceListFileUrl.html
---

# GetPriceListFileUrl
<a name="API_pricing_GetPriceListFileUrl"></a>

This returns the URL that you can retrieve your Price List file from. This URL is based on the `PriceListArn` and `FileFormat` that you retrieve from the [ListPriceLists](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html) response.

## Request Syntax
<a name="API_pricing_GetPriceListFileUrl_RequestSyntax"></a>

```
{
   "FileFormat": "{{string}}",
   "PriceListArn": "{{string}}"
}
```

## Request Parameters
<a name="API_pricing_GetPriceListFileUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FileFormat](#API_pricing_GetPriceListFileUrl_RequestSyntax) **   <a name="awscostmanagement-pricing_GetPriceListFileUrl-request-FileFormat"></a>
The format that you want to retrieve your Price List files in. The `FileFormat` can be obtained from the [ListPriceLists](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html) response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [PriceListArn](#API_pricing_GetPriceListFileUrl_RequestSyntax) **   <a name="awscostmanagement-pricing_GetPriceListFileUrl-request-PriceListArn"></a>
The unique identifier that maps to where your Price List files are located. `PriceListArn` can be obtained from the [ListPriceLists](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html) response.
Type: String
Length Constraints: Minimum length of 18. Maximum length of 2048.
Pattern: `arn:[A-Za-z0-9][-.A-Za-z0-9]{0,62}:pricing:::price-list/[A-Za-z0-9+_/.-]{1,1023}`
Required: Yes

## Response Syntax
<a name="API_pricing_GetPriceListFileUrl_ResponseSyntax"></a>

```
{
   "Url": "string"
}
```

## Response Elements
<a name="API_pricing_GetPriceListFileUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Url](#API_pricing_GetPriceListFileUrl_ResponseSyntax) **   <a name="awscostmanagement-pricing_GetPriceListFileUrl-response-Url"></a>
The URL to download your Price List file from.
Type: String

## Errors
<a name="API_pricing_GetPriceListFileUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
General authentication failure. The request wasn't signed correctly.
HTTP Status Code: 400

 ** InternalErrorException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

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
<a name="API_pricing_GetPriceListFileUrl_Examples"></a>

### The following is a sample request and response of the GetPriceListFileUrl operation.
<a name="API_pricing_GetPriceListFileUrl_Example_1"></a>

This example illustrates one usage of GetPriceListFileUrl.

#### Sample Request
<a name="API_pricing_GetPriceListFileUrl_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.pricing.<region>.<domain>
x-amz-Date: <Date>Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>Connection: Keep-Alive
X-Amz-Target: AWSPriceListService.GetPriceListFileUrl{
    "PriceListArn": "arn:aws:pricing:::price-list/aws/AmazonEC2/USD/20220603151047/us-east-1",
    "FileFormat": "json"
}
```

#### Sample Response
<a name="API_pricing_GetPriceListFileUrl_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "Url": "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/20220603151047/us-east-1/index.json"
}
```

## See Also
<a name="API_pricing_GetPriceListFileUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pricing-2017-10-15/GetPriceListFileUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pricing-2017-10-15/GetPriceListFileUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-2017-10-15/GetPriceListFileUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pricing-2017-10-15/GetPriceListFileUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-2017-10-15/GetPriceListFileUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pricing-2017-10-15/GetPriceListFileUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pricing-2017-10-15/GetPriceListFileUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pricing-2017-10-15/GetPriceListFileUrl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pricing-2017-10-15/GetPriceListFileUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-2017-10-15/GetPriceListFileUrl)

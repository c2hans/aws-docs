---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.html
---

# GetAttributeValues
<a name="API_pricing_GetAttributeValues"></a>

Returns a list of attribute values. Attributes are similar to the details in a Price List API offer file. For a list of available attributes, see [Offer File Definitions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/reading-an-offer.html#pps-defs) in the [AWS Billing and Cost Management User Guide](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html).

## Request Syntax
<a name="API_pricing_GetAttributeValues_RequestSyntax"></a>

```
{
   "AttributeName": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ServiceCode": "{{string}}"
}
```

## Request Parameters
<a name="API_pricing_GetAttributeValues_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AttributeName](#API_pricing_GetAttributeValues_RequestSyntax) **   <a name="awscostmanagement-pricing_GetAttributeValues-request-AttributeName"></a>
The name of the attribute that you want to retrieve the values for, such as `volumeType`.
Type: String
Required: Yes

 ** [MaxResults](#API_pricing_GetAttributeValues_RequestSyntax) **   <a name="awscostmanagement-pricing_GetAttributeValues-request-MaxResults"></a>
The maximum number of results to return in response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

 ** [NextToken](#API_pricing_GetAttributeValues_RequestSyntax) **   <a name="awscostmanagement-pricing_GetAttributeValues-request-NextToken"></a>
The pagination token that indicates the next set of results that you want to retrieve.
Type: String
Required: No

 ** [ServiceCode](#API_pricing_GetAttributeValues_RequestSyntax) **   <a name="awscostmanagement-pricing_GetAttributeValues-request-ServiceCode"></a>
The service code for the service whose attributes you want to retrieve. For example, if you want the retrieve an EC2 attribute, use `AmazonEC2`.
Type: String
Required: Yes

## Response Syntax
<a name="API_pricing_GetAttributeValues_ResponseSyntax"></a>

```
{
   "AttributeValues": [
      {
         "Value": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_pricing_GetAttributeValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttributeValues](#API_pricing_GetAttributeValues_ResponseSyntax) **   <a name="awscostmanagement-pricing_GetAttributeValues-response-AttributeValues"></a>
The list of values for an attribute. For example, `Throughput Optimized HDD` and `Provisioned IOPS` are two available values for the `AmazonEC2` `volumeType`.
Type: Array of [AttributeValue](API_pricing_AttributeValue.md) objects

 ** [NextToken](#API_pricing_GetAttributeValues_ResponseSyntax) **   <a name="awscostmanagement-pricing_GetAttributeValues-response-NextToken"></a>
The pagination token that indicates the next set of results to retrieve.
Type: String

## Errors
<a name="API_pricing_GetAttributeValues_Errors"></a>

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
<a name="API_pricing_GetAttributeValues_Examples"></a>

### The following is a sample request and response of the GetAttributeValues operation.
<a name="API_pricing_GetAttributeValues_Example_1"></a>

This example illustrates one usage of GetAttributeValues.

#### Sample Request
<a name="API_pricing_GetAttributeValues_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: api.pricing.<region>.<domain>
x-amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=contenttype;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid,Signature=<Signature>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: AWSPriceListService.GetAttributeValues
{
    "ServiceCode": "AmazonEC2",
    "AttributeName": "volumeType",
    "NextToken": null,
    "MaxResults": 2
}
```

#### Sample Response
<a name="API_pricing_GetAttributeValues_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
    "AttributeValues": [
        {
            "Value": "Throughput Optimized HDD"
        },
        {
            "Value": "Provisioned IOPS"
        }
    ],
    "NextToken": "GpgauTGIY7LGezucl5LV0w==:7GzYJ0nw0DBTJ2J66EoTIIynE6O1uXwQtTRqioJzQadBnDVgHPzI1en4BUQnPCLpzeBk9RQQAWaFieA4+DapFAGLgk+Z/9/cTw9GldnPOHN98+FdmJP7wKU3QQpQ8MQr5KOeBkIsAqvAQYdL0DkL7tHwPtE5iCEByAmg9gcC/yBU1vAOsf7R3VaNN4M5jMDv3woSWqASSIlBVB6tgW78YL22KhssoItM/jWW+aP6Jqtq4mldxp/ct6DWAl+xLFwHU/CbketimPPXyqHF3/UXDw=="
}
```

## See Also
<a name="API_pricing_GetAttributeValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pricing-2017-10-15/GetAttributeValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pricing-2017-10-15/GetAttributeValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pricing-2017-10-15/GetAttributeValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pricing-2017-10-15/GetAttributeValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pricing-2017-10-15/GetAttributeValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pricing-2017-10-15/GetAttributeValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pricing-2017-10-15/GetAttributeValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pricing-2017-10-15/GetAttributeValues)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pricing-2017-10-15/GetAttributeValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pricing-2017-10-15/GetAttributeValues)

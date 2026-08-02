---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ViewBilling.html
---

# ViewBilling
<a name="API_domains_ViewBilling"></a>

Returns all the domain-related billing records for the current AWS account for a specified period

## Request Syntax
<a name="API_domains_ViewBilling_RequestSyntax"></a>

```
{
   "End": {{number}},
   "Marker": "{{string}}",
   "MaxItems": {{number}},
   "Start": {{number}}
}
```

## Request Parameters
<a name="API_domains_ViewBilling_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [End](#API_domains_ViewBilling_RequestSyntax) **   <a name="Route53Domains-domains_ViewBilling-request-End"></a>
The end date and time for the time period for which you want a list of billing records. Specify the date and time in Unix time format and Coordinated Universal time (UTC).
Type: Timestamp
Required: No

 ** [Marker](#API_domains_ViewBilling_RequestSyntax) **   <a name="Route53Domains-domains_ViewBilling-request-Marker"></a>
For an initial request for a list of billing records, omit this element. If the number of billing records that are associated with the current AWS account during the specified period is greater than the value that you specified for `MaxItems`, you can use `Marker` to return additional billing records. Get the value of `NextPageMarker` from the previous response, and submit another request that includes the value of `NextPageMarker` in the `Marker` element.
Constraints: The marker must match the value of `NextPageMarker` that was returned in the previous response.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [MaxItems](#API_domains_ViewBilling_RequestSyntax) **   <a name="Route53Domains-domains_ViewBilling-request-MaxItems"></a>
The number of billing records to be returned.
Default: 20
Type: Integer
Valid Range: Maximum value of 100.
Required: No

 ** [Start](#API_domains_ViewBilling_RequestSyntax) **   <a name="Route53Domains-domains_ViewBilling-request-Start"></a>
The beginning date and time for the time period for which you want a list of billing records. Specify the date and time in Unix time format and Coordinated Universal time (UTC).
Type: Timestamp
Required: No

## Response Syntax
<a name="API_domains_ViewBilling_ResponseSyntax"></a>

```
{
   "BillingRecords": [
      {
         "BillDate": number,
         "DomainName": "string",
         "InvoiceId": "string",
         "Operation": "string",
         "Price": number
      }
   ],
   "NextPageMarker": "string"
}
```

## Response Elements
<a name="API_domains_ViewBilling_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BillingRecords](#API_domains_ViewBilling_ResponseSyntax) **   <a name="Route53Domains-domains_ViewBilling-response-BillingRecords"></a>
A summary of billing records.
Type: Array of [BillingRecord](API_domains_BillingRecord.md) objects

 ** [NextPageMarker](#API_domains_ViewBilling_ResponseSyntax) **   <a name="Route53Domains-domains_ViewBilling-response-NextPageMarker"></a>
If there are more billing records than you specified for `MaxItems` in the request, submit another request and include the value of `NextPageMarker` in the value of `Marker`.
Type: String
Length Constraints: Maximum length of 4096.

## Errors
<a name="API_domains_ViewBilling_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

## Examples
<a name="API_domains_ViewBilling_Examples"></a>

### ViewBilling Example
<a name="API_domains_ViewBilling_Example_1"></a>

This example illustrates one usage of ViewBilling.

#### Sample Request
<a name="API_domains_ViewBilling_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205230Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domains_v20140515.ViewBilling
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
    "Start": 1461006299,
    "End": 1463598304,
    "MaxItems": 20
}
```

#### Sample Response
<a name="API_domains_ViewBilling_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{
    "BillingRecords": [
        {
            "BillDate": 1431211111,
            "DomainName": "example.net",
            "InvoiceId": "1111111111",
            "Operation": "REGISTER_DOMAIN",
            "Price": 12
        }, {
            "BillDate": 1431222222,
            "DomainName": "example.com",
            "InvoiceId": "2222222222",
            "Operation": "TRANSFER_IN_DOMAIN",
            "Price": 12
        }, {
            "BillDate": 1431233333,
            "DomainName": "example.org",
            "InvoiceId": "3333333333",
            "Operation": "RENEW_DOMAIN",
            "Price": 12
        }
    ]
}
```

## See Also
<a name="API_domains_ViewBilling_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/ViewBilling)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/ViewBilling)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/ViewBilling)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/ViewBilling)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/ViewBilling)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/ViewBilling)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/ViewBilling)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/ViewBilling)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/ViewBilling)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/ViewBilling)

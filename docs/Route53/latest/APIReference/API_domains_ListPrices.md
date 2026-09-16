---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListPrices.html
---

# ListPrices
<a name="API_domains_ListPrices"></a>

Lists the following prices for either all the TLDs supported by Route 53, or the specified TLD:
+ Registration
+ Transfer
+ Owner change
+ Domain renewal
+ Domain restoration

## Request Syntax
<a name="API_domains_ListPrices_RequestSyntax"></a>

```
{
   "Marker": "{{string}}",
   "MaxItems": {{number}},
   "Tld": "{{string}}"
}
```

## Request Parameters
<a name="API_domains_ListPrices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_domains_ListPrices_RequestSyntax) **   <a name="Route53Domains-domains_ListPrices-request-Marker"></a>
For an initial request for a list of prices, omit this element. If the number of prices that are not yet complete is greater than the value that you specified for `MaxItems`, you can use `Marker` to return additional prices. Get the value of `NextPageMarker` from the previous response, and submit another request that includes the value of `NextPageMarker` in the `Marker` element.
Used only for all TLDs. If you specify a TLD, don't specify a `Marker`.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** [MaxItems](#API_domains_ListPrices_RequestSyntax) **   <a name="Route53Domains-domains_ListPrices-request-MaxItems"></a>
Number of `Prices` to be returned.
Used only for all TLDs. If you specify a TLD, don't specify a `MaxItems`.
Type: Integer
Valid Range: Maximum value of 1000.
Required: No

 ** [Tld](#API_domains_ListPrices_RequestSyntax) **   <a name="Route53Domains-domains_ListPrices-request-Tld"></a>
The TLD for which you want to receive the pricing information. For example. `.net`.
If a `Tld` value is not provided, a list of prices for all TLDs supported by Route 53 is returned.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_domains_ListPrices_ResponseSyntax"></a>

```
{
   "NextPageMarker": "string",
   "Prices": [
      {
         "ChangeOwnershipPrice": {
            "Currency": "string",
            "Price": number
         },
         "Name": "string",
         "RegistrationPrice": {
            "Currency": "string",
            "Price": number
         },
         "RenewalPrice": {
            "Currency": "string",
            "Price": number
         },
         "RestorationPrice": {
            "Currency": "string",
            "Price": number
         },
         "TransferPrice": {
            "Currency": "string",
            "Price": number
         }
      }
   ]
}
```

## Response Elements
<a name="API_domains_ListPrices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageMarker](#API_domains_ListPrices_ResponseSyntax) **   <a name="Route53Domains-domains_ListPrices-response-NextPageMarker"></a>
If there are more prices than you specified for `MaxItems` in the request, submit another request and include the value of `NextPageMarker` in the value of `Marker`.
Used only for all TLDs. If you specify a TLD, don't specify a `NextPageMarker`.
Type: String
Length Constraints: Maximum length of 4096.

 ** [Prices](#API_domains_ListPrices_ResponseSyntax) **   <a name="Route53Domains-domains_ListPrices-response-Prices"></a>
A complex type that includes all the pricing information. If you specify a TLD, this array contains only the pricing for that TLD.
Type: Array of [DomainPrice](API_domains_DomainPrice.md) objects

## Errors
<a name="API_domains_ListPrices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

 ** UnsupportedTLD **
Amazon Route 53 does not support this top-level domain (TLD).
 ** message **
Amazon Route 53 does not support this top-level domain (TLD).
HTTP Status Code: 400

## See Also
<a name="API_domains_ListPrices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/ListPrices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/ListPrices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/ListPrices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/ListPrices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/ListPrices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/ListPrices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/ListPrices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/ListPrices)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/ListPrices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/ListPrices)

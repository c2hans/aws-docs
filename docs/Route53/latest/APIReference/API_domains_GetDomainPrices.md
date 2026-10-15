---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainPrices.html
---

# GetDomainPrices
<a name="API_domains_GetDomainPrices"></a>

Returns the following prices for the specified domain:
+ Registration
+ Transfer
+ Owner change
+ Renewal
+ Restoration

For most domains, the prices match the standard prices for the TLD that the [ListPrices](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ListPrices.html) operation returns. For a premium domain, the registry sets the price individually. Premium prices might differ from the standard prices and can change over time.

## Request Syntax
<a name="API_domains_GetDomainPrices_RequestSyntax"></a>

```
{
   "DomainName": "{{string}}"
}
```

## Request Parameters
<a name="API_domains_GetDomainPrices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_domains_GetDomainPrices_RequestSyntax) **   <a name="Route53Domains-domains_GetDomainPrices-request-DomainName"></a>
The name of the domain that you want to get the prices for.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_domains_GetDomainPrices_ResponseSyntax"></a>

```
{
   "DomainPrice": {
      "ChangeOwnershipPrice": {
         "Currency": "string",
         "Price": number,
         "PriceType": "string"
      },
      "Name": "string",
      "RegistrationPrice": {
         "Currency": "string",
         "Price": number,
         "PriceType": "string"
      },
      "RenewalPrice": {
         "Currency": "string",
         "Price": number,
         "PriceType": "string"
      },
      "RestorationPrice": {
         "Currency": "string",
         "Price": number,
         "PriceType": "string"
      },
      "TransferPrice": {
         "Currency": "string",
         "Price": number,
         "PriceType": "string"
      }
   }
}
```

## Response Elements
<a name="API_domains_GetDomainPrices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainPrice](#API_domains_GetDomainPrices_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainPrices-response-DomainPrice"></a>
The registration, transfer, owner change, renewal, and restoration prices for the specified domain.
Type: [DomainPrice](API_domains_DomainPrice.md) object

## Errors
<a name="API_domains_GetDomainPrices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

 ** TLDInMaintenance **
The top-level domain is currently undergoing maintenance and the request cannot be processed. Try again later.
 ** message **
The top-level domain is currently undergoing maintenance and the request cannot be processed. Try again later.
 ** tld **
The top-level domain that is currently undergoing maintenance.
HTTP Status Code: 400

 ** UnsupportedTLD **
Amazon Route 53 does not support this top-level domain (TLD).
 ** message **
Amazon Route 53 does not support this top-level domain (TLD).
HTTP Status Code: 400

## See Also
<a name="API_domains_GetDomainPrices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/GetDomainPrices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/GetDomainPrices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/GetDomainPrices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/GetDomainPrices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/GetDomainPrices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/GetDomainPrices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/GetDomainPrices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/GetDomainPrices)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/GetDomainPrices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/GetDomainPrices)

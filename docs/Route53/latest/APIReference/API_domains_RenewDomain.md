---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RenewDomain.html
---

# RenewDomain
<a name="API_domains_RenewDomain"></a>

This operation renews a domain for the specified number of years. The cost of renewing your domain is billed to your AWS account.

We recommend that you renew your domain several weeks before the expiration date. Some TLD registries delete domains before the expiration date if you haven't renewed far enough in advance. For more information about renewing domain registration, see [Renewing Registration for a Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-renew.html) in the *Amazon Route 53 Developer Guide*.

## Request Syntax
<a name="API_domains_RenewDomain_RequestSyntax"></a>

```
{
   "CurrentExpiryYear": {{number}},
   "DomainName": "{{string}}",
   "DurationInYears": {{number}}
}
```

## Request Parameters
<a name="API_domains_RenewDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CurrentExpiryYear](#API_domains_RenewDomain_RequestSyntax) **   <a name="Route53Domains-domains_RenewDomain-request-CurrentExpiryYear"></a>
The year when the registration for the domain is set to expire. This value must match the current expiration date for the domain.
Type: Integer
Required: Yes

 ** [DomainName](#API_domains_RenewDomain_RequestSyntax) **   <a name="Route53Domains-domains_RenewDomain-request-DomainName"></a>
The name of the domain that you want to renew.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [DurationInYears](#API_domains_RenewDomain_RequestSyntax) **   <a name="Route53Domains-domains_RenewDomain-request-DurationInYears"></a>
The number of years that you want to renew the domain for. The maximum number of years depends on the top-level domain. For the range of valid values for your domain, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide*.
Default: 1
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

## Response Syntax
<a name="API_domains_RenewDomain_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_domains_RenewDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_domains_RenewDomain_ResponseSyntax) **   <a name="Route53Domains-domains_RenewDomain-response-OperationId"></a>
Identifier for tracking the progress of the request. To query the operation status, use [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_domains_RenewDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateRequest **
The request is already in progress for the domain.
 ** message **
The request is already in progress for the domain.
 ** requestId **
ID of the request operation.
HTTP Status Code: 400

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

 ** OperationLimitExceeded **
The number of operations or jobs running exceeded the allowed threshold for the account.
 ** message **
The number of operations or jobs running exceeded the allowed threshold for the account.
HTTP Status Code: 400

 ** TLDRulesViolation **
The top-level domain does not support this operation.
 ** message **
The top-level domain does not support this operation.
HTTP Status Code: 400

 ** UnsupportedTLD **
Amazon Route 53 does not support this top-level domain (TLD).
 ** message **
Amazon Route 53 does not support this top-level domain (TLD).
HTTP Status Code: 400

## Examples
<a name="API_domains_RenewDomain_Examples"></a>

### RenewDomain Example
<a name="API_domains_RenewDomain_Example_1"></a>

This example illustrates one usage of RenewDomain.

#### Sample Request
<a name="API_domains_RenewDomain_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205230Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
              x-amz-target:Route53Domains_v20140515.RenewDomain
              user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
   "DomainName":"example.com",
   "DurationInYears":"6",
   "CurrentExpiryYear":"2017"
}
```

#### Sample Response
<a name="API_domains_RenewDomain_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]{}
```

## See Also
<a name="API_domains_RenewDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/RenewDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/RenewDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/RenewDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/RenewDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/RenewDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/RenewDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/RenewDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/RenewDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/RenewDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/RenewDomain)

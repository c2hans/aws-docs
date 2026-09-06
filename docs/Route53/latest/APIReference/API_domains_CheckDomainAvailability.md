---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_CheckDomainAvailability.html
---

# CheckDomainAvailability
<a name="API_domains_CheckDomainAvailability"></a>

This operation checks the availability of one domain name. Note that if the availability status of a domain is pending, you must submit another request to determine the availability of the domain name.

## Request Syntax
<a name="API_domains_CheckDomainAvailability_RequestSyntax"></a>

```
{
   "DomainName": "{{string}}",
   "IdnLangCode": "{{string}}"
}
```

## Request Parameters
<a name="API_domains_CheckDomainAvailability_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_domains_CheckDomainAvailability_RequestSyntax) **   <a name="Route53Domains-domains_CheckDomainAvailability-request-DomainName"></a>
The name of the domain that you want to get availability for. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide*.
The domain name can contain only the following characters:
+ Letters a through z. Domain names are not case sensitive.
+ Numbers 0 through 9.
+ Hyphen (-). You can't specify a hyphen at the beginning or end of a label.
+ Period (.) to separate the labels in the name, such as the `.` in `example.com`.
Internationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html). For more information, see [Formatting Internationalized Domain Names](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html#domain-name-format-idns).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [IdnLangCode](#API_domains_CheckDomainAvailability_RequestSyntax) **   <a name="Route53Domains-domains_CheckDomainAvailability-request-IdnLangCode"></a>
Reserved for future use.
Type: String
Pattern: `|[A-Za-z]{2,3}`
Required: No

## Response Syntax
<a name="API_domains_CheckDomainAvailability_ResponseSyntax"></a>

```
{
   "Availability": "string"
}
```

## Response Elements
<a name="API_domains_CheckDomainAvailability_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Availability](#API_domains_CheckDomainAvailability_ResponseSyntax) **   <a name="Route53Domains-domains_CheckDomainAvailability-response-Availability"></a>
Whether the domain name is available for registering.
You can register only domains designated as `AVAILABLE`.
Valid values:
AVAILABLE
The domain name is available.
AVAILABLE\_RESERVED
The domain name is reserved under specific conditions.
AVAILABLE\_PREORDER
The domain name is available and can be preordered.
DONT\_KNOW
The TLD registry didn't reply with a definitive answer about whether the domain name is available. Route 53 can return this response for a variety of reasons, for example, the registry is performing maintenance. Try again later.
INVALID\_NAME\_FOR\_TLD
The TLD isn't valid. For example, it can contain characters that aren't allowed.
PENDING
The TLD registry didn't return a response in the expected amount of time. When the response is delayed, it usually takes just a few extra seconds. You can resubmit the request immediately.
RESERVED
The domain name has been reserved for another person or organization.
UNAVAILABLE
The domain name is not available.
UNAVAILABLE\_PREMIUM
The domain name is not available.
UNAVAILABLE\_RESTRICTED
The domain name is forbidden.
Type: String
Valid Values: `AVAILABLE | AVAILABLE_RESERVED | AVAILABLE_PREORDER | UNAVAILABLE | UNAVAILABLE_PREMIUM | UNAVAILABLE_RESTRICTED | RESERVED | DONT_KNOW | INVALID_NAME_FOR_TLD | PENDING`

## Errors
<a name="API_domains_CheckDomainAvailability_Errors"></a>

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

## Examples
<a name="API_domains_CheckDomainAvailability_Examples"></a>

### CheckDomainAvailability Example
<a name="API_domains_CheckDomainAvailability_Example_1"></a>

This example illustrates one usage of CheckDomainAvailability.

#### Sample Request
<a name="API_domains_CheckDomainAvailability_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205225Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domains_v20140515.CheckDomainAvailability
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
connections:Keep-Alive
{
   "DomainName":"example.com"
}
```

#### Sample Response
<a name="API_domains_CheckDomainAvailability_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{
   "Availability":"AVAILABLE"
}
```

## See Also
<a name="API_domains_CheckDomainAvailability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/CheckDomainAvailability)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/CheckDomainAvailability)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/CheckDomainAvailability)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/CheckDomainAvailability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/CheckDomainAvailability)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/CheckDomainAvailability)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/CheckDomainAvailability)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/CheckDomainAvailability)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/CheckDomainAvailability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/CheckDomainAvailability)

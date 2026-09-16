---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RegisterDomain.html
---

# RegisterDomain
<a name="API_domains_RegisterDomain"></a>

This operation registers a domain. For some top-level domains (TLDs), this operation requires extra parameters.

When you register a domain, Amazon Route 53 does the following:
+ Creates a Route 53 hosted zone that has the same name as the domain. Route 53 assigns four name servers to your hosted zone and automatically updates your domain registration with the names of these name servers.
+ Enables auto renew, so your domain registration will renew automatically each year. We'll notify you in advance of the renewal date so you can choose whether to renew the registration.
+ Optionally enables privacy protection, so WHOIS queries return contact for the registrar or the phrase "REDACTED FOR PRIVACY", or "On behalf of <domain name> owner." If you don't enable privacy protection, WHOIS queries return the information that you entered for the administrative, registrant, and technical contacts.
**Note**
While some domains may allow different privacy settings per contact, we recommend specifying the same privacy setting for all contacts.
+ If registration is successful, returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant is notified by email.
+ Charges your AWS account an amount based on the top-level domain. For more information, see [Amazon Route 53 Pricing](http://aws.amazon.com/route53/pricing/).

## Request Syntax
<a name="API_domains_RegisterDomain_RequestSyntax"></a>

```
{
   "AdminContact": {
      "AddressLine1": "{{string}}",
      "AddressLine2": "{{string}}",
      "City": "{{string}}",
      "ContactType": "{{string}}",
      "CountryCode": "{{string}}",
      "Email": "{{string}}",
      "ExtraParams": [
         {
            "Name": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Fax": "{{string}}",
      "FirstName": "{{string}}",
      "LastName": "{{string}}",
      "OrganizationName": "{{string}}",
      "PhoneNumber": "{{string}}",
      "State": "{{string}}",
      "ZipCode": "{{string}}"
   },
   "AutoRenew": {{boolean}},
   "BillingContact": {
      "AddressLine1": "{{string}}",
      "AddressLine2": "{{string}}",
      "City": "{{string}}",
      "ContactType": "{{string}}",
      "CountryCode": "{{string}}",
      "Email": "{{string}}",
      "ExtraParams": [
         {
            "Name": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Fax": "{{string}}",
      "FirstName": "{{string}}",
      "LastName": "{{string}}",
      "OrganizationName": "{{string}}",
      "PhoneNumber": "{{string}}",
      "State": "{{string}}",
      "ZipCode": "{{string}}"
   },
   "DomainName": "{{string}}",
   "DurationInYears": {{number}},
   "IdnLangCode": "{{string}}",
   "PrivacyProtectAdminContact": {{boolean}},
   "PrivacyProtectBillingContact": {{boolean}},
   "PrivacyProtectRegistrantContact": {{boolean}},
   "PrivacyProtectTechContact": {{boolean}},
   "RegistrantContact": {
      "AddressLine1": "{{string}}",
      "AddressLine2": "{{string}}",
      "City": "{{string}}",
      "ContactType": "{{string}}",
      "CountryCode": "{{string}}",
      "Email": "{{string}}",
      "ExtraParams": [
         {
            "Name": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Fax": "{{string}}",
      "FirstName": "{{string}}",
      "LastName": "{{string}}",
      "OrganizationName": "{{string}}",
      "PhoneNumber": "{{string}}",
      "State": "{{string}}",
      "ZipCode": "{{string}}"
   },
   "TechContact": {
      "AddressLine1": "{{string}}",
      "AddressLine2": "{{string}}",
      "City": "{{string}}",
      "ContactType": "{{string}}",
      "CountryCode": "{{string}}",
      "Email": "{{string}}",
      "ExtraParams": [
         {
            "Name": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "Fax": "{{string}}",
      "FirstName": "{{string}}",
      "LastName": "{{string}}",
      "OrganizationName": "{{string}}",
      "PhoneNumber": "{{string}}",
      "State": "{{string}}",
      "ZipCode": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_domains_RegisterDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdminContact](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-AdminContact"></a>
Provides detailed contact information. For information about the values that you specify for each element, see [ContactDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html).
Type: [ContactDetail](API_domains_ContactDetail.md) object
Required: Yes

 ** [AutoRenew](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-AutoRenew"></a>
Indicates whether the domain will be automatically renewed (`true`) or not (`false`). Auto renewal only takes effect after the account is charged.
Default: `true`
Type: Boolean
Required: No

 ** [BillingContact](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-BillingContact"></a>
Provides detailed contact information. For information about the values that you specify for each element, see [ContactDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html).
Type: [ContactDetail](API_domains_ContactDetail.md) object
Required: No

 ** [DomainName](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-DomainName"></a>
The domain name that you want to register. The top-level domain (TLD), such as .com, must be a TLD that Route 53 supports. For a list of supported TLDs, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide*.
The domain name can contain only the following characters:
+ Letters a through z. Domain names are not case sensitive.
+ Numbers 0 through 9.
+ Hyphen (-). You can't specify a hyphen at the beginning or end of a label.
+ Period (.) to separate the labels in the name, such as the `.` in `example.com`.
Internationalized domain names are not supported for some top-level domains. To determine whether the TLD that you want to use supports internationalized domain names, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html). For more information, see [Formatting Internationalized Domain Names](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html#domain-name-format-idns).
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [DurationInYears](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-DurationInYears"></a>
The number of years that you want to register the domain for. Domains are registered for a minimum of one year. The maximum period depends on the top-level domain. For the range of valid values for your domain, see [Domains that You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html) in the *Amazon Route 53 Developer Guide*.
Default: 1
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: Yes

 ** [IdnLangCode](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-IdnLangCode"></a>
Reserved for future use.
Type: String
Pattern: `|[A-Za-z]{2,3}`
Required: No

 ** [PrivacyProtectAdminContact](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-PrivacyProtectAdminContact"></a>
Whether you want to conceal contact information from WHOIS queries. If you specify `true`, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false`, WHOIS queries return the information that you entered for the admin contact.
You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.
Default: `true`
Type: Boolean
Required: No

 ** [PrivacyProtectBillingContact](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-PrivacyProtectBillingContact"></a>
Whether you want to conceal contact information from WHOIS queries. If you specify `true`, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false`, WHOIS queries return the information that you entered for the billing contact.
You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.
Type: Boolean
Required: No

 ** [PrivacyProtectRegistrantContact](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-PrivacyProtectRegistrantContact"></a>
Whether you want to conceal contact information from WHOIS queries. If you specify `true`, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false`, WHOIS queries return the information that you entered for the registrant contact (the domain owner).
You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.
Default: `true`
Type: Boolean
Required: No

 ** [PrivacyProtectTechContact](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-PrivacyProtectTechContact"></a>
Whether you want to conceal contact information from WHOIS queries. If you specify `true`, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If you specify `false`, WHOIS queries return the information that you entered for the technical contact.
You must specify the same privacy setting for the administrative, billing, registrant, and technical contacts.
Default: `true`
Type: Boolean
Required: No

 ** [RegistrantContact](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-RegistrantContact"></a>
Provides detailed contact information. For information about the values that you specify for each element, see [ContactDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html).
Type: [ContactDetail](API_domains_ContactDetail.md) object
Required: Yes

 ** [TechContact](#API_domains_RegisterDomain_RequestSyntax) **   <a name="Route53Domains-domains_RegisterDomain-request-TechContact"></a>
Provides detailed contact information. For information about the values that you specify for each element, see [ContactDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html).
Type: [ContactDetail](API_domains_ContactDetail.md) object
Required: Yes

## Response Syntax
<a name="API_domains_RegisterDomain_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_domains_RegisterDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_domains_RegisterDomain_ResponseSyntax) **   <a name="Route53Domains-domains_RegisterDomain-response-OperationId"></a>
Identifier for tracking the progress of the request. To query the operation status, use [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_domains_RegisterDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DomainLimitExceeded **
The number of domains has exceeded the allowed threshold for the account.
 ** message **
The number of domains has exceeded the allowed threshold for the account.
HTTP Status Code: 400

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
<a name="API_domains_RegisterDomain_Examples"></a>

### RegisterDomain Example
<a name="API_domains_RegisterDomain_Example_1"></a>

This example illustrates one usage of RegisterDomain.

#### Sample Request
<a name="API_domains_RegisterDomain_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205230Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domains_v20140515.RegisterDomain
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
   "DomainName":"example.com",
   "DurationInYears":1,
   "AutoRenew":true,
   "AdminContact":{
      "FirstName":"John",
      "MiddleName":"Richard",
      "LastName":"Doe",
      "ContactType":"PERSON",
      "OrganizationName":"",
      "AddressLine1":"123 Any Street",
      "AddressLine2":"",
      "City":"Any Town",
      "State":"WA",
      "CountryCode":"US",
      "ZipCode":"98101",
      "PhoneNumber":"+1.1234567890",
      "Email":"john@example.com",
      "Fax":"+1.1234567891"
   },
   "RegistrantContact":{
      "FirstName":"John",
      "MiddleName":"Richard",
      "LastName":"Doe",
      "ContactType":"PERSON",
      "OrganizationName":"",
      "AddressLine1":"123 Any Street",
      "AddressLine2":"",
      "City":"Any Town",
      "State":"WA",
      "CountryCode":"US",
      "ZipCode":"98101",
      "PhoneNumber":"+1.1234567890",
      "Email":"john@example.com",
      "Fax":"+1.1234567891"
   },
   "TechContact":{
      "FirstName":"John",
      "MiddleName":"Richard",
      "LastName":"Doe",
      "ContactType":"PERSON",
      "OrganizationName":"",
      "AddressLine1":"123 Any Street",
      "AddressLine2":"",
      "City":"Any Town",
      "State":"WA",
      "CountryCode":"US",
      "ZipCode":"98101",
      "PhoneNumber":"+1.1234567890",
      "Email":"john@example.com",
      "Fax":"+1.1234567891"
},
"PrivacyProtectAdminContact":true,
"PrivacyProtectRegistrantContact":true,
"PrivacyProtectTechContact":true
}
```

#### Sample Response
<a name="API_domains_RegisterDomain_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{
   "OperationId":"308c56712-faa4-40fe-94c8-b423069de3f6"
}
```

## See Also
<a name="API_domains_RegisterDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/RegisterDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/RegisterDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/RegisterDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/RegisterDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/RegisterDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/RegisterDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/RegisterDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/RegisterDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/RegisterDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/RegisterDomain)

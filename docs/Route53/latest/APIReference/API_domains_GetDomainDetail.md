---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainDetail.html
---

# GetDomainDetail
<a name="API_domains_GetDomainDetail"></a>

This operation returns detailed information about a specified domain that is associated with the current AWS account. Contact information for the domain is also returned as part of the output.

## Request Syntax
<a name="API_domains_GetDomainDetail_RequestSyntax"></a>

```
{
   "DomainName": "{{string}}"
}
```

## Request Parameters
<a name="API_domains_GetDomainDetail_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_domains_GetDomainDetail_RequestSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-request-DomainName"></a>
The name of the domain that you want to get detailed information about.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_domains_GetDomainDetail_ResponseSyntax"></a>

```
{
   "AbuseContactEmail": "string",
   "AbuseContactPhone": "string",
   "AdminContact": {
      "AddressLine1": "string",
      "AddressLine2": "string",
      "City": "string",
      "ContactType": "string",
      "CountryCode": "string",
      "Email": "string",
      "ExtraParams": [
         {
            "Name": "string",
            "Value": "string"
         }
      ],
      "Fax": "string",
      "FirstName": "string",
      "LastName": "string",
      "OrganizationName": "string",
      "PhoneNumber": "string",
      "State": "string",
      "ZipCode": "string"
   },
   "AdminPrivacy": boolean,
   "AutoRenew": boolean,
   "BillingContact": {
      "AddressLine1": "string",
      "AddressLine2": "string",
      "City": "string",
      "ContactType": "string",
      "CountryCode": "string",
      "Email": "string",
      "ExtraParams": [
         {
            "Name": "string",
            "Value": "string"
         }
      ],
      "Fax": "string",
      "FirstName": "string",
      "LastName": "string",
      "OrganizationName": "string",
      "PhoneNumber": "string",
      "State": "string",
      "ZipCode": "string"
   },
   "BillingPrivacy": boolean,
   "CreationDate": number,
   "DnsSec": "string",
   "DnssecKeys": [
      {
         "Algorithm": number,
         "Digest": "string",
         "DigestType": number,
         "Flags": number,
         "Id": "string",
         "KeyTag": number,
         "PublicKey": "string"
      }
   ],
   "DomainName": "string",
   "ExpirationDate": number,
   "Nameservers": [
      {
         "GlueIps": [ "string" ],
         "Name": "string"
      }
   ],
   "RegistrantContact": {
      "AddressLine1": "string",
      "AddressLine2": "string",
      "City": "string",
      "ContactType": "string",
      "CountryCode": "string",
      "Email": "string",
      "ExtraParams": [
         {
            "Name": "string",
            "Value": "string"
         }
      ],
      "Fax": "string",
      "FirstName": "string",
      "LastName": "string",
      "OrganizationName": "string",
      "PhoneNumber": "string",
      "State": "string",
      "ZipCode": "string"
   },
   "RegistrantPrivacy": boolean,
   "RegistrarName": "string",
   "RegistrarUrl": "string",
   "RegistryDomainId": "string",
   "Reseller": "string",
   "StatusList": [ "string" ],
   "TechContact": {
      "AddressLine1": "string",
      "AddressLine2": "string",
      "City": "string",
      "ContactType": "string",
      "CountryCode": "string",
      "Email": "string",
      "ExtraParams": [
         {
            "Name": "string",
            "Value": "string"
         }
      ],
      "Fax": "string",
      "FirstName": "string",
      "LastName": "string",
      "OrganizationName": "string",
      "PhoneNumber": "string",
      "State": "string",
      "ZipCode": "string"
   },
   "TechPrivacy": boolean,
   "UpdatedDate": number,
   "WhoIsServer": "string"
}
```

## Response Elements
<a name="API_domains_GetDomainDetail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AbuseContactEmail](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-AbuseContactEmail"></a>
Email address to contact to report incorrect contact information for a domain, to report that the domain is being used to send spam, to report that someone is cybersquatting on a domain name, or report some other type of abuse.
Type: String
Length Constraints: Maximum length of 254.

 ** [AbuseContactPhone](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-AbuseContactPhone"></a>
Phone number for reporting abuse.
Type: String
Length Constraints: Maximum length of 30.

 ** [AdminContact](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-AdminContact"></a>
Provides details about the domain administrative contact.
Type: [ContactDetail](API_domains_ContactDetail.md) object

 ** [AdminPrivacy](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-AdminPrivacy"></a>
Specifies whether contact information is concealed from WHOIS queries. If the value is `true`, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is `false`, WHOIS queries return the information that you entered for the admin contact.
Type: Boolean

 ** [AutoRenew](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-AutoRenew"></a>
Specifies whether the domain registration is set to renew automatically.
Type: Boolean

 ** [BillingContact](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-BillingContact"></a>
Provides details about the domain billing contact.
Type: [ContactDetail](API_domains_ContactDetail.md) object

 ** [BillingPrivacy](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-BillingPrivacy"></a>
Specifies whether contact information is concealed from WHOIS queries. If the value is `true`, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is `false`, WHOIS queries return the information that you entered for the billing contact.
Type: Boolean

 ** [CreationDate](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-CreationDate"></a>
The date when the domain was created as found in the response to a WHOIS query. The date and time is in Unix time format and Coordinated Universal time (UTC).
Type: Timestamp

 ** [DnsSec](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-DnsSec"></a>
Deprecated.
Type: String

 ** [DnssecKeys](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-DnssecKeys"></a>
A complex type that contains information about the DNSSEC configuration.
Type: Array of [DnssecKey](API_domains_DnssecKey.md) objects

 ** [DomainName](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-DomainName"></a>
The name of a domain.
Type: String
Length Constraints: Maximum length of 255.

 ** [ExpirationDate](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-ExpirationDate"></a>
The date when the registration for the domain is set to expire. The date and time is in Unix time format and Coordinated Universal time (UTC).
Type: Timestamp

 ** [Nameservers](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-Nameservers"></a>
The name servers of the domain.
Type: Array of [Nameserver](API_domains_Nameserver.md) objects

 ** [RegistrantContact](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-RegistrantContact"></a>
Provides details about the domain registrant.
Type: [ContactDetail](API_domains_ContactDetail.md) object

 ** [RegistrantPrivacy](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-RegistrantPrivacy"></a>
Specifies whether contact information is concealed from WHOIS queries. If the value is `true`, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is `false`, WHOIS queries return the information that you entered for the registrant contact (domain owner).
Type: Boolean

 ** [RegistrarName](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-RegistrarName"></a>
Name of the registrar of the domain as identified in the registry.
Type: String

 ** [RegistrarUrl](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-RegistrarUrl"></a>
Web address of the registrar.
Type: String

 ** [RegistryDomainId](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-RegistryDomainId"></a>
Reserved for future use.
Type: String

 ** [Reseller](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-Reseller"></a>
Reserved for future use.
Type: String

 ** [StatusList](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-StatusList"></a>
An array of domain name status codes, also known as Extensible Provisioning Protocol (EPP) status codes.
ICANN, the organization that maintains a central database of domain names, has developed a set of domain name status codes that tell you the status of a variety of operations on a domain name, for example, registering a domain name, transferring a domain name to another registrar, renewing the registration for a domain name, and so on. All registrars use this same set of status codes.
For a current list of domain name status codes and an explanation of what each code means, go to the [ICANN website](https://www.icann.org/) and search for `epp status codes`. (Search on the ICANN website; web searches sometimes return an old version of the document.)
Type: Array of strings

 ** [TechContact](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-TechContact"></a>
Provides details about the domain technical contact.
Type: [ContactDetail](API_domains_ContactDetail.md) object

 ** [TechPrivacy](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-TechPrivacy"></a>
Specifies whether contact information is concealed from WHOIS queries. If the value is `true`, WHOIS ("who is") queries return contact information either for Amazon Registrar or for our registrar associate, Gandi. If the value is `false`, WHOIS queries return the information that you entered for the technical contact.
Type: Boolean

 ** [UpdatedDate](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-UpdatedDate"></a>
The last updated date of the domain as found in the response to a WHOIS query. The date and time is in Unix time format and Coordinated Universal time (UTC).
Type: Timestamp

 ** [WhoIsServer](#API_domains_GetDomainDetail_ResponseSyntax) **   <a name="Route53Domains-domains_GetDomainDetail-response-WhoIsServer"></a>
The fully qualified name of the WHOIS server that can answer the WHOIS query for the domain.
Type: String

## Errors
<a name="API_domains_GetDomainDetail_Errors"></a>

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
<a name="API_domains_GetDomainDetail_Examples"></a>

### GetDomainDetail Example
<a name="API_domains_GetDomainDetail_Example_1"></a>

This example illustrates one usage of GetDomainDetail.

#### Sample Request
<a name="API_domains_GetDomainDetail_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205230Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domains_v20140515.GetDomainDetail
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
   "DomainName":"example.com"
}
```

#### Sample Response
<a name="API_domains_GetDomainDetail_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{
   "AbuseContactEmail":"abuse@support.gandi.net",
   "AbuseContactPhone":"+33.170377661",
   "AdminContact":{
      "AddressLine1":"1 Any Street",
      "AddressLine2":"",
      "City":"Anytown",
      "CountryCode":"US",
      "Email":"john@example.com",
      "ExtraParams":[
      ],
      "FirstName":"John",
      "LastName":"Doe",
      "PhoneNumber":"+1.1234567890",
      "State":"WA",
      "ZipCode":"98101"
   },
   "AdminPrivacy":true,
   "AutoRenew":true,
   "CreationDate":1400010459,
   "DomainName":"example.com",
   "ExpirationDate":1431539259,
   "Nameservers":[
      {
         "GlueIps":[
         ],
         "Name":"ns-2048.awsdns-64.com"
      },
      {
         "GlueIps":[
         ],
         "Name":"ns-2051.awsdns-67.co.uk"
      },
      {
         "GlueIps":[
         ],
         "Name":"ns-2050.awsdns-66.org"
      },
      {
         "GlueIps":[
         ],
         "Name":"ns-2049.awsdns-65.net"
      }
   ],
   "RegistrantContact":{
      "AddressLine1":"1 Any Street",
      "AddressLine2":"",
      "City":"Anytown",
      "CountryCode":"US",
      "Email":"john@example.com",
      "ExtraParams":[
      ],
      "FirstName":"John",
      "LastName":"Doe",
      "PhoneNumber":"+1.1234567890",
      "State":"WA",
      "ZipCode":"98101"
   },
   "RegistrantPrivacy":true,
   "RegistrarName":"GANDI SAS",
   "RegistrarUrl":"http://www.gandi.net",
   "StatusList":[
   "clientTransferProhibited"
   ],
   "TechContact":{
      "AddressLine1":"1 Any Street",
      "AddressLine2":"",
      "City":"Anytown",
      "CountryCode":"US",
      "Email":"john@example.com",
      "ExtraParams":[
      ],
      "FirstName":"John",
      "LastName":"Doe",
      "PhoneNumber":"+1.1234567890",
      "State":"WA",
      "ZipCode":"98101"
      },
   "TechPrivacy":true,
   "UpdatedDate":1400010459,
   "WhoIsServer":"whois.gandi.net"
}
```

## See Also
<a name="API_domains_GetDomainDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/GetDomainDetail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/GetDomainDetail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/GetDomainDetail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/GetDomainDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/GetDomainDetail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/GetDomainDetail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/GetDomainDetail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/GetDomainDetail)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/GetDomainDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/GetDomainDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

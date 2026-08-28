---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainContact.html
---

# UpdateDomainContact
<a name="API_domains_UpdateDomainContact"></a>

This operation updates the contact information for a particular domain. You must specify information for at least one contact: registrant, administrator, or technical.

If the update is successful, this method returns an operation ID that you can use to track the progress and completion of the operation. If the request is not completed successfully, the domain registrant will be notified by email.

## Request Syntax
<a name="API_domains_UpdateDomainContact_RequestSyntax"></a>

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
   "Consent": {
      "Currency": "{{string}}",
      "MaxPrice": {{number}}
   },
   "DomainName": "{{string}}",
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
<a name="API_domains_UpdateDomainContact_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AdminContact](#API_domains_UpdateDomainContact_RequestSyntax) **   <a name="Route53Domains-domains_UpdateDomainContact-request-AdminContact"></a>
Provides detailed contact information.
Type: [ContactDetail](API_domains_ContactDetail.md) object
Required: No

 ** [BillingContact](#API_domains_UpdateDomainContact_RequestSyntax) **   <a name="Route53Domains-domains_UpdateDomainContact-request-BillingContact"></a>
Provides detailed contact information.
Type: [ContactDetail](API_domains_ContactDetail.md) object
Required: No

 ** [Consent](#API_domains_UpdateDomainContact_RequestSyntax) **   <a name="Route53Domains-domains_UpdateDomainContact-request-Consent"></a>
 Customer's consent for the owner change request. Required if the domain is not free (consent price is more than $0.00).
Type: [Consent](API_domains_Consent.md) object
Required: No

 ** [DomainName](#API_domains_UpdateDomainContact_RequestSyntax) **   <a name="Route53Domains-domains_UpdateDomainContact-request-DomainName"></a>
The name of the domain that you want to update contact information for.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

 ** [RegistrantContact](#API_domains_UpdateDomainContact_RequestSyntax) **   <a name="Route53Domains-domains_UpdateDomainContact-request-RegistrantContact"></a>
Provides detailed contact information.
Type: [ContactDetail](API_domains_ContactDetail.md) object
Required: No

 ** [TechContact](#API_domains_UpdateDomainContact_RequestSyntax) **   <a name="Route53Domains-domains_UpdateDomainContact-request-TechContact"></a>
Provides detailed contact information.
Type: [ContactDetail](API_domains_ContactDetail.md) object
Required: No

## Response Syntax
<a name="API_domains_UpdateDomainContact_ResponseSyntax"></a>

```
{
   "OperationId": "string"
}
```

## Response Elements
<a name="API_domains_UpdateDomainContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OperationId](#API_domains_UpdateDomainContact_ResponseSyntax) **   <a name="Route53Domains-domains_UpdateDomainContact-response-OperationId"></a>
Identifier for tracking the progress of the request. To query the operation status, use [GetOperationDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html).
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_domains_UpdateDomainContact_Errors"></a>

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
<a name="API_domains_UpdateDomainContact_Examples"></a>

### UpdateDomainContact Example
<a name="API_domains_UpdateDomainContact_Example_1"></a>

This example illustrates one usage of UpdateDomainContact.

#### Sample Request
<a name="API_domains_UpdateDomainContact_Example_1_Request"></a>

```
POST / HTTP/1.1
host:route53domains.us-east-1.amazonaws.com
x-amz-date:20140711T205230Z
authorization:AWS4-HMAC-SHA256
              Credential=AKIAIOSFODNN7EXAMPLE/20140711/us-east-1/route53domains/aws4_request,
              SignedHeaders=content-length;content-type;host;user-agent;x-amz-date;x-amz-target,
              Signature=[calculated-signature]
x-amz-target:Route53Domains_v20140515.UpdateDomainContact
user-agent:aws-sdk-java/1.8.3 Linux/2.6.18-164.el5PAE Java_HotSpot (TM )_Server_VM/24.60-b09/1.7.0_60
content-type:application/x-amz-json-1.1
content-length:[number of characters in the JSON string]
{
   "DomainName":"example.com",
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
}
```

#### Sample Response
<a name="API_domains_UpdateDomainContact_Example_1_Response"></a>

```
HTTP/1.1 200
Content-Length:[number of characters in the JSON string]
{
"OperationId":"308c56712-faa4-40fe-94c8-b423069de3f6"
}
```

## See Also
<a name="API_domains_UpdateDomainContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/UpdateDomainContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/UpdateDomainContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/UpdateDomainContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/UpdateDomainContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/UpdateDomainContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/UpdateDomainContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/UpdateDomainContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/UpdateDomainContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/UpdateDomainContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/UpdateDomainContact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

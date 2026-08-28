---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateProfile.html
---

# CreateProfile
<a name="API_connect-customer-profiles_CreateProfile"></a>

Creates a standard profile.

A standard profile represents the following attributes for a customer profile in a domain.

## Request Syntax
<a name="API_connect-customer-profiles_CreateProfile_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/profiles HTTP/1.1
Content-type: application/json

{
   "AccountNumber": "{{string}}",
   "AdditionalInformation": "{{string}}",
   "Address": {
      "Address1": "{{string}}",
      "Address2": "{{string}}",
      "Address3": "{{string}}",
      "Address4": "{{string}}",
      "City": "{{string}}",
      "Country": "{{string}}",
      "County": "{{string}}",
      "PostalCode": "{{string}}",
      "Province": "{{string}}",
      "State": "{{string}}"
   },
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "BillingAddress": {
      "Address1": "{{string}}",
      "Address2": "{{string}}",
      "Address3": "{{string}}",
      "Address4": "{{string}}",
      "City": "{{string}}",
      "Country": "{{string}}",
      "County": "{{string}}",
      "PostalCode": "{{string}}",
      "Province": "{{string}}",
      "State": "{{string}}"
   },
   "BirthDate": "{{string}}",
   "BusinessEmailAddress": "{{string}}",
   "BusinessName": "{{string}}",
   "BusinessPhoneNumber": "{{string}}",
   "EmailAddress": "{{string}}",
   "EngagementPreferences": {
      "Email": [
         {
            "ContactType": "{{string}}",
            "KeyName": "{{string}}",
            "KeyValue": "{{string}}",
            "ProfileId": "{{string}}"
         }
      ],
      "Phone": [
         {
            "ContactType": "{{string}}",
            "KeyName": "{{string}}",
            "KeyValue": "{{string}}",
            "ProfileId": "{{string}}"
         }
      ]
   },
   "FirstName": "{{string}}",
   "Gender": "{{string}}",
   "GenderString": "{{string}}",
   "HomePhoneNumber": "{{string}}",
   "LastName": "{{string}}",
   "MailingAddress": {
      "Address1": "{{string}}",
      "Address2": "{{string}}",
      "Address3": "{{string}}",
      "Address4": "{{string}}",
      "City": "{{string}}",
      "Country": "{{string}}",
      "County": "{{string}}",
      "PostalCode": "{{string}}",
      "Province": "{{string}}",
      "State": "{{string}}"
   },
   "MiddleName": "{{string}}",
   "MobilePhoneNumber": "{{string}}",
   "PartyType": "{{string}}",
   "PartyTypeString": "{{string}}",
   "PersonalEmailAddress": "{{string}}",
   "PhoneNumber": "{{string}}",
   "ProfileType": "{{string}}",
   "ShippingAddress": {
      "Address1": "{{string}}",
      "Address2": "{{string}}",
      "Address3": "{{string}}",
      "Address4": "{{string}}",
      "City": "{{string}}",
      "Country": "{{string}}",
      "County": "{{string}}",
      "PostalCode": "{{string}}",
      "Province": "{{string}}",
      "State": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_CreateProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_CreateProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountNumber](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-AccountNumber"></a>
An account number that you have assigned to the customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [AdditionalInformation](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-AdditionalInformation"></a>
Any additional information relevant to the customer’s profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** [Address](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-Address"></a>
A generic address associated with the customer that is not mailing, shipping, or billing.
Type: [Address](API_connect-customer-profiles_Address.md) object
Required: No

 ** [Attributes](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-Attributes"></a>
A key value pair of attributes of a customer profile.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [BillingAddress](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-BillingAddress"></a>
The customer’s billing address.
Type: [Address](API_connect-customer-profiles_Address.md) object
Required: No

 ** [BirthDate](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-BirthDate"></a>
The customer’s birth date.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [BusinessEmailAddress](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-BusinessEmailAddress"></a>
The customer’s business email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [BusinessName](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-BusinessName"></a>
The name of the customer’s business.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [BusinessPhoneNumber](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-BusinessPhoneNumber"></a>
The customer’s business phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [EmailAddress](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-EmailAddress"></a>
The customer’s email address, which has not been specified as a personal or business address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [EngagementPreferences](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-EngagementPreferences"></a>
Object that defines the preferred methods of engagement, per channel.
Type: [EngagementPreferences](API_connect-customer-profiles_EngagementPreferences.md) object
Required: No

 ** [FirstName](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-FirstName"></a>
The customer’s first name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [Gender](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-Gender"></a>
 *This parameter has been deprecated.*
The gender with which the customer identifies.
Type: String
Valid Values: `MALE | FEMALE | UNSPECIFIED`
Required: No

 ** [GenderString](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-GenderString"></a>
An alternative to `Gender` which accepts any string as input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [HomePhoneNumber](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-HomePhoneNumber"></a>
The customer’s home phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [LastName](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-LastName"></a>
The customer’s last name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [MailingAddress](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-MailingAddress"></a>
The customer’s mailing address.
Type: [Address](API_connect-customer-profiles_Address.md) object
Required: No

 ** [MiddleName](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-MiddleName"></a>
The customer’s middle name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [MobilePhoneNumber](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-MobilePhoneNumber"></a>
The customer’s mobile phone number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [PartyType](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-PartyType"></a>
 *This parameter has been deprecated.*
The type of profile used to describe the customer.
Type: String
Valid Values: `INDIVIDUAL | BUSINESS | OTHER`
Required: No

 ** [PartyTypeString](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-PartyTypeString"></a>
An alternative to `PartyType` which accepts any string as input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [PersonalEmailAddress](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-PersonalEmailAddress"></a>
The customer’s personal email address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [PhoneNumber](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-PhoneNumber"></a>
The customer’s phone number, which has not been specified as a mobile, home, or business number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [ProfileType](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-ProfileType"></a>
The type of the profile.
Type: String
Valid Values: `ACCOUNT_PROFILE | PROFILE`
Required: No

 ** [ShippingAddress](#API_connect-customer-profiles_CreateProfile_RequestSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-request-ShippingAddress"></a>
The customer’s shipping address.
Type: [Address](API_connect-customer-profiles_Address.md) object
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_CreateProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProfileId": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_CreateProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProfileId](#API_connect-customer-profiles_CreateProfile_ResponseSyntax) **   <a name="connect-connect-customer-profiles_CreateProfile-response-ProfileId"></a>
The unique identifier of a customer profile.
Type: String
Pattern: `[a-f0-9]{32}`

## Errors
<a name="API_connect-customer-profiles_CreateProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## Examples
<a name="API_connect-customer-profiles_CreateProfile_Examples"></a>

### Example
<a name="API_connect-customer-profiles_CreateProfile_Example_1"></a>

This example illustrates one usage of CreateProfile.

#### Sample Request
<a name="API_connect-customer-profiles_CreateProfile_Example_1_Request"></a>

```
POST /domains/ExampleDomainName/profiles HTTP/1.1

Content-type: application/json
{
   "AccountNumber": "ACCT12344",
   "Address": {
      "Address1": "123 Sample St",
      "Address2": "Apt 4",
      "Address3": "null",
      "Address4": "null",
      "City": "Seattle",
      "Country": "USA",
      "County": "King",
      "PostalCode": "98011",
      "Province": "",
      "State": "WA"
   },
   "Attributes": {
      "SSN" : "123-44-3433",
      "LoyaltyPoints" : "3000"
   },
   "BillingAddress": {
      "Address1": "789 Sample St",
      "Address2": "Apt 1",
      "City": "Seattle",
      "Country": "USA",
      "County": "King",
      "PostalCode": "98011",
      "Province": "",
      "State": "WA"
   },
   "BirthDate": "07/12/1980",
   "BusinessEmailAddress": "example@amazon.com",
   "BusinessName": "My Awesome Company",
   "BusinessPhoneNumber": "555-334-3389",
   "EmailAddress": "example@gmail.com",
   "FirstName": "John",
   "Gender": "MALE",
   "HomePhoneNumber": "555-334-3344",
   "LastName": "Doe",
   "MailingAddress": {
      "Address1": "234 Home St",
      "Address2": "Apt 5",
      "City": "Seattle",
      "Country": "USA",
      "County": "King",
      "PostalCode": "98011",
      "Province": "",
      "State": "WA"
   },
   "AdditionalInformation": "High Profile Customer",
   "MiddleName": "",
   "MobilePhoneNumber": "555-334-7777",
   "PartyType": "INDIVIDUAL",
   "PersonalEmailAddress": "email1@gmail.com",
   "PhoneNumber": "",
   "ShippingAddress": {
      "Address1": "555 A St",
      "Address2": "Suite 100",
      "City": "Seattle",
      "Country": "USA",
      "County": "King",
      "PostalCode": "98011",
      "Province": "",
      "State": "WA"
   }
}
```

#### Sample Response
<a name="API_connect-customer-profiles_CreateProfile_Example_1_Response"></a>

```
Content-type: application/json
{
   "ProfileId" : "3991a7d959d248bb982546b2dEXAMPLE"
}
```

## See Also
<a name="API_connect-customer-profiles_CreateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/CreateProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/CreateProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/CreateProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/CreateProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/CreateProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/CreateProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/CreateProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/CreateProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/CreateProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/CreateProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

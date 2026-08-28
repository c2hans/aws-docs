---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html
---

# SearchProfiles
<a name="API_connect-customer-profiles_SearchProfiles"></a>

Searches for profiles within a specific domain using one or more predefined search keys (e.g., \_fullName, \_phone, \_email, \_account, etc.) and/or custom-defined search keys. A search key is a data type pair that consists of a `KeyName` and `Values` list.

This operation supports searching for profiles with a minimum of 1 key-value(s) pair and up to 5 key-value(s) pairs using either `AND` or `OR` logic.

## Request Syntax
<a name="API_connect-customer-profiles_SearchProfiles_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/profiles/search?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "AdditionalSearchKeys": [
      {
         "KeyName": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "KeyName": "{{string}}",
   "LogicalOperator": "{{string}}",
   "Values": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_SearchProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_SearchProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchProfiles-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_SearchProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchProfiles-request-uri-MaxResults"></a>
The maximum number of objects returned per page.
The default is 20 if this parameter is not included in the request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_SearchProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchProfiles-request-uri-NextToken"></a>
The pagination token from the previous SearchProfiles API call.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_SearchProfiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdditionalSearchKeys](#API_connect-customer-profiles_SearchProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchProfiles-request-AdditionalSearchKeys"></a>
A list of `AdditionalSearchKey` objects that are each searchable identifiers of a profile. Each `AdditionalSearchKey` object contains a `KeyName` and a list of `Values` associated with that specific key (i.e., a key-value(s) pair). These additional search keys will be used in conjunction with the `LogicalOperator` and the required `KeyName` and `Values` parameters to search for profiles that satisfy the search criteria.
Type: Array of [AdditionalSearchKey](API_connect-customer-profiles_AdditionalSearchKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

 ** [KeyName](#API_connect-customer-profiles_SearchProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchProfiles-request-KeyName"></a>
A searchable identifier of a customer profile. The predefined keys you can use to search include: \_account, \_profileId, \_assetId, \_caseId, \_orderId, \_fullName, \_phone, \_email, \_ctrContactId, \_marketoLeadId, \_salesforceAccountId, \_salesforceContactId, \_salesforceAssetId, \_zendeskUserId, \_zendeskExternalId, \_zendeskTicketId, \_serviceNowSystemId, \_serviceNowIncidentId, \_segmentUserId, \_shopifyCustomerId, \_shopifyOrderId.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [LogicalOperator](#API_connect-customer-profiles_SearchProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchProfiles-request-LogicalOperator"></a>
Relationship between all specified search keys that will be used to search for profiles. This includes the required `KeyName` and `Values` parameters as well as any key-value(s) pairs specified in the `AdditionalSearchKeys` list.
This parameter influences which profiles will be returned in the response in the following manner:
+  `AND` - The response only includes profiles that match all of the search keys.
+  `OR` - The response includes profiles that match at least one of the search keys.
The `OR` relationship is the default behavior if this parameter is not included in the request.
Type: String
Valid Values: `AND | OR`
Required: No

 ** [Values](#API_connect-customer-profiles_SearchProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_SearchProfiles-request-Values"></a>
A list of key values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_SearchProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "AccountNumber": "string",
         "AdditionalInformation": "string",
         "Address": {
            "Address1": "string",
            "Address2": "string",
            "Address3": "string",
            "Address4": "string",
            "City": "string",
            "Country": "string",
            "County": "string",
            "PostalCode": "string",
            "Province": "string",
            "State": "string"
         },
         "Attributes": {
            "string" : "string"
         },
         "BillingAddress": {
            "Address1": "string",
            "Address2": "string",
            "Address3": "string",
            "Address4": "string",
            "City": "string",
            "Country": "string",
            "County": "string",
            "PostalCode": "string",
            "Province": "string",
            "State": "string"
         },
         "BirthDate": "string",
         "BusinessEmailAddress": "string",
         "BusinessName": "string",
         "BusinessPhoneNumber": "string",
         "EmailAddress": "string",
         "EngagementPreferences": {
            "Email": [
               {
                  "ContactType": "string",
                  "KeyName": "string",
                  "KeyValue": "string",
                  "ProfileId": "string"
               }
            ],
            "Phone": [
               {
                  "ContactType": "string",
                  "KeyName": "string",
                  "KeyValue": "string",
                  "ProfileId": "string"
               }
            ]
         },
         "FirstName": "string",
         "FoundByItems": [
            {
               "KeyName": "string",
               "Values": [ "string" ]
            }
         ],
         "Gender": "string",
         "GenderString": "string",
         "HomePhoneNumber": "string",
         "LastName": "string",
         "MailingAddress": {
            "Address1": "string",
            "Address2": "string",
            "Address3": "string",
            "Address4": "string",
            "City": "string",
            "Country": "string",
            "County": "string",
            "PostalCode": "string",
            "Province": "string",
            "State": "string"
         },
         "MiddleName": "string",
         "MobilePhoneNumber": "string",
         "PartyType": "string",
         "PartyTypeString": "string",
         "PersonalEmailAddress": "string",
         "PhoneNumber": "string",
         "ProfileId": "string",
         "ProfileType": "string",
         "ShippingAddress": {
            "Address1": "string",
            "Address2": "string",
            "Address3": "string",
            "Address4": "string",
            "City": "string",
            "Country": "string",
            "County": "string",
            "PostalCode": "string",
            "Province": "string",
            "State": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_SearchProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_connect-customer-profiles_SearchProfiles_ResponseSyntax) **   <a name="connect-connect-customer-profiles_SearchProfiles-response-Items"></a>
The list of Profiles matching the search criteria.
Type: Array of [Profile](API_connect-customer-profiles_Profile.md) objects

 ** [NextToken](#API_connect-customer-profiles_SearchProfiles_ResponseSyntax) **   <a name="connect-connect-customer-profiles_SearchProfiles-response-NextToken"></a>
The pagination token from the previous SearchProfiles API call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_connect-customer-profiles_SearchProfiles_Errors"></a>

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
<a name="API_connect-customer-profiles_SearchProfiles_Examples"></a>

### Example 1
<a name="API_connect-customer-profiles_SearchProfiles_Example_1"></a>

This example illustrates one usage of SearchProfiles.

#### Sample Request
<a name="API_connect-customer-profiles_SearchProfiles_Example_1_Request"></a>

```
POST /domains/ExampleDomainName/profiles/search?max-results=10&next-token=nextTokenString HTTP/1.1
Content-type: application/json

{
   "KeyName": "_phone",
   "Values": ["555-333-7777"]
}
```

#### Sample Response
<a name="API_connect-customer-profiles_SearchProfiles_Example_1_Response"></a>

```
Content-type: application/json
{
  "NextToken": "5231b533-ba17-4787-98a3-f2df3EXAMPLE",
  "Items":[
    {
        "ProfileId" : "3991a7d95sd248bba82546b2dEXAMPLE",
        "AccountNumber": "ACCT12344",
        "Address": {
            "Address1": "123 Sample St",
            "Address2": "Apt 4",
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        },
        "Attributes": {
            "SSN" : "123-44-3433",
            "LoyaltyPoints" : "4000"
        },
        "BillingAddress": {
            "Address1": "789 Sample St",
            "Address2": "Apt 1",
            "Address3": "",
            "Address4": "",
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
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        },
        "AdditionalInformation": "High Profile Customer",
        "MiddleName": "",
        "MobilePhoneNumber": "555-333-7777",
        "PartyType": "INDIVIDUAL",
        "PersonalEmailAddress": "email1@gmail.com",
        "PhoneNumber": "",
        "ShippingAddress": {
            "Address1": "555 A St",
            "Address2": "Suite 100",
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        }
  },
  {
        "ProfileId" : "ef30fad550894e0a95f9d64cbEXAMPLE",
        "AccountNumber": "ACCT12344",
        "Address": {
            "Address1": "123 Sample St",
            "Address2": "Apt 4",
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        },
        "Attributes": {
            "SSN" : "123-44-3433",
            "LoyaltyPoints" : "4000"
        },
        "BillingAddress": {
            "Address1": "789 Sample St",
            "Address2": "Apt 1",
            "Address3": "",
            "Address4": "",
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
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        },
        "AdditionalInformation": "High Profile Customer",
        "MiddleName": "",
        "MobilePhoneNumber": "555-333-7777",
        "PartyType": "INDIVIDUAL",
        "PersonalEmailAddress": "email1@gmail.com",
        "PhoneNumber": "",
        "ShippingAddress": {
            "Address1": "555 A St",
            "Address2": "Suite 100",
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        }
  }
 ]
}
```

### Example 2
<a name="API_connect-customer-profiles_SearchProfiles_Example_2"></a>

This example illustrates one usage of SearchProfiles.

#### Sample Request
<a name="API_connect-customer-profiles_SearchProfiles_Example_2_Request"></a>

```
POST /domains/ExampleDomainName/profiles/search?max-results=10&next-token=nextTokenString HTTP/1.1
Content-type: application/json

{
   "KeyName": "_email",
   "Values": ["email1@gmail.com"]
}
```

#### Sample Response
<a name="API_connect-customer-profiles_SearchProfiles_Example_2_Response"></a>

```
Content-type: application/json
{
  "NextToken": "5231b533-ba17-4787-98a3-f2df3EXAMPLE",
  "Items":[
    {
        "ProfileId" : "ef30fad55099ee0a95f9d64cbEXAMPLE",
        "AccountNumber": "ACCT12344",
        "Address": {
            "Address1": "123 Sample St",
            "Address2": "Apt 4",
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        },
        "Attributes": {
            "SSN" : "123-44-3433",
            "LoyaltyPoints" : "4000"
        },
        "BillingAddress": {
            "Address1": "789 Sample St",
            "Address2": "Apt 1",
            "Address3": "",
            "Address4": "",
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
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        },
        "AdditionalInformation": "High Profile Customer",
        "MiddleName": "",
        "MobilePhoneNumber": "555-333-7777",
        "PartyType": "INDIVIDUAL",
        "PersonalEmailAddress": "email5@gmail.com",
        "PhoneNumber": "",
        "ShippingAddress": {
            "Address1": "555 A St",
            "Address2": "Suite 100",
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        }
  },
  {
        "ProfileId" : "3991a7d959d238bba82546b2dEXAMPLE",
        "AccountNumber": "ACCT12344",
        "Address": {
            "Address1": "123 Sample St",
            "Address2": "Apt 4",
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        },
        "Attributes": {
            "SSN" : "123-44-3433",
            "LoyaltyPoints" : "4000"
        },
        "BillingAddress": {
            "Address1": "789 Sample St",
            "Address2": "Apt 1",
            "Address3": "",
            "Address4": "",
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
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        },
        "AdditionalInformation": "High Profile Customer",
        "MiddleName": "",
        "MobilePhoneNumber": "555-333-7777",
        "PartyType": "INDIVIDUAL",
        "PersonalEmailAddress": "email1@gmail.com",
        "PhoneNumber": "",
        "ShippingAddress": {
            "Address1": "555 A St",
            "Address2": "Suite 100",
            "Address3": "",
            "Address4": "",
            "City": "Seattle",
            "Country": "USA",
            "County": "King",
            "PostalCode": "98011",
            "Province": "",
            "State": "WA"
        }
  }
 ]
}
```

## See Also
<a name="API_connect-customer-profiles_SearchProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/SearchProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/SearchProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/SearchProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/SearchProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/SearchProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/SearchProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/SearchProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/SearchProfiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/SearchProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/SearchProfiles)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

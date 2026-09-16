---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetSegmentMembership.html
---

# GetSegmentMembership
<a name="API_connect-customer-profiles_GetSegmentMembership"></a>

Determines if the given profiles are within a segment.

## Request Syntax
<a name="API_connect-customer-profiles_GetSegmentMembership_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/segments/{{SegmentDefinitionName}}/membership HTTP/1.1
Content-type: application/json

{
   "ProfileIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetSegmentMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetSegmentMembership_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentMembership-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [SegmentDefinitionName](#API_connect-customer-profiles_GetSegmentMembership_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentMembership-request-uri-SegmentDefinitionName"></a>
The Id of the wanted segment. Needs to be a valid, and existing segment Id.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetSegmentMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ProfileIds](#API_connect-customer-profiles_GetSegmentMembership_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentMembership-request-ProfileIds"></a>
The list of profile IDs to query for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_GetSegmentMembership_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Failures": [
      {
         "Message": "string",
         "ProfileId": "string",
         "Status": number
      }
   ],
   "LastComputedAt": number,
   "Profiles": [
      {
         "Profile": {
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
         },
         "ProfileId": "string",
         "QueryResult": "string"
      }
   ],
   "SegmentDefinitionName": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetSegmentMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failures](#API_connect-customer-profiles_GetSegmentMembership_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentMembership-response-Failures"></a>
An array of maps where each contains a response per profile failed for the request.
Type: Array of [ProfileQueryFailures](API_connect-customer-profiles_ProfileQueryFailures.md) objects

 ** [LastComputedAt](#API_connect-customer-profiles_GetSegmentMembership_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentMembership-response-LastComputedAt"></a>
The timestamp indicating when the segment membership was last computed or updated.
Type: Timestamp

 ** [Profiles](#API_connect-customer-profiles_GetSegmentMembership_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentMembership-response-Profiles"></a>
An array of maps where each contains a response per profile requested.
Type: Array of [ProfileQueryResult](API_connect-customer-profiles_ProfileQueryResult.md) objects

 ** [SegmentDefinitionName](#API_connect-customer-profiles_GetSegmentMembership_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSegmentMembership-response-SegmentDefinitionName"></a>
The unique name of the segment definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_connect-customer-profiles_GetSegmentMembership_Errors"></a>

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

## See Also
<a name="API_connect-customer-profiles_GetSegmentMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetSegmentMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetSegmentMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetSegmentMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetSegmentMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetSegmentMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetSegmentMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetSegmentMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetSegmentMembership)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetSegmentMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetSegmentMembership)

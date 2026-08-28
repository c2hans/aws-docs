---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_PutDomainObjectType.html
---

# PutDomainObjectType
<a name="API_connect-customer-profiles_PutDomainObjectType"></a>

Create/Update a DomainObjectType in a Customer Profiles domain. To create a new DomainObjectType, Data Store needs to be enabled on the Domain.

## Request Syntax
<a name="API_connect-customer-profiles_PutDomainObjectType_RequestSyntax"></a>

```
PUT /domains/{{DomainName}}/domain-object-types/{{ObjectTypeName}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "EncryptionKey": "{{string}}",
   "Fields": {
      "{{string}}" : {
         "ContentType": "{{string}}",
         "FeatureType": "{{string}}",
         "Source": "{{string}}",
         "Target": "{{string}}"
      }
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_PutDomainObjectType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_PutDomainObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [ObjectTypeName](#API_connect-customer-profiles_PutDomainObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-request-uri-ObjectTypeName"></a>
The unique name of the domain object type.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_PutDomainObjectType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_connect-customer-profiles_PutDomainObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-request-Description"></a>
The description of the domain object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

 ** [EncryptionKey](#API_connect-customer-profiles_PutDomainObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-request-EncryptionKey"></a>
The customer provided KMS key used to encrypt this type of domain object.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [Fields](#API_connect-customer-profiles_PutDomainObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-request-Fields"></a>
A map of field names to their corresponding domain object type field definitions.
Type: String to [DomainObjectTypeField](API_connect-customer-profiles_DomainObjectTypeField.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`
Required: Yes

 ** [Tags](#API_connect-customer-profiles_PutDomainObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_PutDomainObjectType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreatedAt": number,
   "Description": "string",
   "EncryptionKey": "string",
   "Fields": {
      "string" : {
         "ContentType": "string",
         "FeatureType": "string",
         "Source": "string",
         "Target": "string"
      }
   },
   "LastUpdatedAt": number,
   "ObjectTypeName": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-customer-profiles_PutDomainObjectType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_PutDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-response-CreatedAt"></a>
The timestamp of when the domain object type was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_PutDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-response-Description"></a>
The description of the domain object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.

 ** [EncryptionKey](#API_connect-customer-profiles_PutDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-response-EncryptionKey"></a>
The customer provided KMS key used to encrypt this type of domain object.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [Fields](#API_connect-customer-profiles_PutDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-response-Fields"></a>
A map of field names to their corresponding domain object type field definitions.
Type: String to [DomainObjectTypeField](API_connect-customer-profiles_DomainObjectTypeField.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`

 ** [LastUpdatedAt](#API_connect-customer-profiles_PutDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-response-LastUpdatedAt"></a>
The timestamp of when the domain object type was most recently edited.
Type: Timestamp

 ** [ObjectTypeName](#API_connect-customer-profiles_PutDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-response-ObjectTypeName"></a>
The unique name of the domain object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`

 ** [Tags](#API_connect-customer-profiles_PutDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutDomainObjectType-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_PutDomainObjectType_Errors"></a>

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
<a name="API_connect-customer-profiles_PutDomainObjectType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/PutDomainObjectType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/PutDomainObjectType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/PutDomainObjectType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/PutDomainObjectType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/PutDomainObjectType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/PutDomainObjectType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/PutDomainObjectType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/PutDomainObjectType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/PutDomainObjectType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/PutDomainObjectType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

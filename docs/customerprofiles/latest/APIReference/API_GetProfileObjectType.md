---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileObjectType.html
---

# GetProfileObjectType
<a name="API_connect-customer-profiles_GetProfileObjectType"></a>

Returns the object types for a specific domain.

## Request Syntax
<a name="API_connect-customer-profiles_GetProfileObjectType_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/object-types/{{ObjectTypeName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetProfileObjectType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [ObjectTypeName](#API_connect-customer-profiles_GetProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-request-uri-ObjectTypeName"></a>
The name of the profile object type.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetProfileObjectType_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AllowProfileCreation": boolean,
   "CreatedAt": number,
   "Description": "string",
   "EncryptionKey": "string",
   "ExpirationDays": number,
   "Fields": {
      "string" : {
         "ContentType": "string",
         "Source": "string",
         "Target": "string"
      }
   },
   "Keys": {
      "string" : [
         {
            "FieldNames": [ "string" ],
            "StandardIdentifiers": [ "string" ]
         }
      ]
   },
   "LastUpdatedAt": number,
   "MaxAvailableProfileObjectCount": number,
   "MaxProfileObjectCount": number,
   "ObjectTypeName": "string",
   "SourceLastUpdatedTimestampFormat": "string",
   "SourcePriority": number,
   "Tags": {
      "string" : "string"
   },
   "TemplateId": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetProfileObjectType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AllowProfileCreation](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-AllowProfileCreation"></a>
Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is `FALSE`. If the AllowProfileCreation flag is set to `FALSE`, then the service tries to fetch a standard profile and associate this object with the profile. If it is set to `TRUE`, and if no match is found, then the service creates a new standard profile.
Type: Boolean

 ** [CreatedAt](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-CreatedAt"></a>
The timestamp of when the domain was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-Description"></a>
The description of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [EncryptionKey](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-EncryptionKey"></a>
The customer-provided key to encrypt the profile object that will be created in this profile object type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [ExpirationDays](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-ExpirationDays"></a>
The number of days until the data in the object expires.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1098.

 ** [Fields](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-Fields"></a>
A map of the name and ObjectType field.
Type: String to [ObjectTypeField](API_connect-customer-profiles_ObjectTypeField.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`

 ** [Keys](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-Keys"></a>
A list of unique keys that can be used to map data to the profile.
Type: String to array of [ObjectTypeKey](API_connect-customer-profiles_ObjectTypeKey.md) objects map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_-]+$`

 ** [LastUpdatedAt](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-LastUpdatedAt"></a>
The timestamp of when the domain was most recently edited.
Type: Timestamp

 ** [MaxAvailableProfileObjectCount](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-MaxAvailableProfileObjectCount"></a>
The amount of provisioned profile object max count available.
Type: Integer
Valid Range: Minimum value of 0.

 ** [MaxProfileObjectCount](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-MaxProfileObjectCount"></a>
The amount of profile object max count assigned to the object type.
Type: Integer
Valid Range: Minimum value of 1.

 ** [ObjectTypeName](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-ObjectTypeName"></a>
The name of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`

 ** [SourceLastUpdatedTimestampFormat](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-SourceLastUpdatedTimestampFormat"></a>
The format of your `sourceLastUpdatedTimestamp` that was previously set up.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [SourcePriority](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-SourcePriority"></a>
An integer that determines the priority of this object type when data from multiple sources is ingested. Lower values take priority. Object types without a specified source priority default to the lowest priority.
Type: Integer
Valid Range: Minimum value of 1.

 ** [Tags](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

 ** [TemplateId](#API_connect-customer-profiles_GetProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectType-response-TemplateId"></a>
A unique identifier for the object template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_connect-customer-profiles_GetProfileObjectType_Errors"></a>

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
<a name="API_connect-customer-profiles_GetProfileObjectType_Examples"></a>

### Example
<a name="API_connect-customer-profiles_GetProfileObjectType_Example_1"></a>

This example illustrates one usage of GetProfileObjectType.

#### Sample Request
<a name="API_connect-customer-profiles_GetProfileObjectType_Example_1_Request"></a>

```
GET /domains/ExampleDomainName/object-types/MyCustomObject HTTP/1.1
```

#### Sample Response
<a name="API_connect-customer-profiles_GetProfileObjectType_Example_1_Response"></a>

```
Content-type: application/jsonContent-type: application/json
{
   "CreatedAt": 1479249799770,
   "Description": "Internal ERP System",
   "EncryptionKey": "arn:aws:kms:us-east-1:123456789012:key/1988472d-6b77-4bb6-ae39-efce5EXAMPLE",
   "AllowProfileCreation": "FALSE",
   "ExpirationDays": 100,
   "Fields": {
      "email" : {
         "ContentType": "EMAIL_ADDRESS",
         "Source": "_source.email",
         "Target": "_profile.BusinessEmailAddress"
      },
      "phone" : {
         "ContentType": "PHONE_NUMBER",
         "Source": "_source.phone",
         "Target": "_profile.BusinessPhoneNumber"
      },
      "loyaltyPoints" : {
         "ContentType": "NUMBER",
         "Source": "_source.loyaltypoints",
         "Target": "_profile.Attributes.loyaltypoints"
      }
   },
   "Keys": {
      "email" : [
         {
            "FieldNames": [ "email" ],
            "StandardIdentifiers": [ "PROFILE", "UNIQUE" ]
         }
      ],
      "loyaltypoints" : [
         {
            "FieldNames": [ "loyaltyPoints" ],
            "StandardIdentifiers": [ "PROFILE"]
         }
      ]
   },
   "LastUpdatedAt": 1479249799770,
   "ObjectTypeName": "CustomProfileObjectTypeName",
   "SourcePriority": 2,
   "TemplateId": "MyTemplateId"
}
```

## See Also
<a name="API_connect-customer-profiles_GetProfileObjectType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetProfileObjectType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetProfileObjectType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetProfileObjectType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetProfileObjectType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetProfileObjectType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetProfileObjectType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetProfileObjectType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetProfileObjectType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetProfileObjectType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetProfileObjectType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_PutProfileObjectType.html
---

# PutProfileObjectType
<a name="API_connect-customer-profiles_PutProfileObjectType"></a>

Defines a ProfileObjectType.

To add or remove tags on an existing ObjectType, see [ TagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html)/[UntagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html).

## Request Syntax
<a name="API_connect-customer-profiles_PutProfileObjectType_RequestSyntax"></a>

```
PUT /domains/{{DomainName}}/object-types/{{ObjectTypeName}} HTTP/1.1
Content-type: application/json

{
   "AllowProfileCreation": {{boolean}},
   "Description": "{{string}}",
   "EncryptionKey": "{{string}}",
   "ExpirationDays": {{number}},
   "Fields": {
      "{{string}}" : {
         "ContentType": "{{string}}",
         "Source": "{{string}}",
         "Target": "{{string}}"
      }
   },
   "Keys": {
      "{{string}}" : [
         {
            "FieldNames": [ "{{string}}" ],
            "StandardIdentifiers": [ "{{string}}" ]
         }
      ]
   },
   "MaxProfileObjectCount": {{number}},
   "SourceLastUpdatedTimestampFormat": "{{string}}",
   "SourcePriority": {{number}},
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TemplateId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_PutProfileObjectType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [ObjectTypeName](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-uri-ObjectTypeName"></a>
The name of the profile object type.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_PutProfileObjectType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllowProfileCreation](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-AllowProfileCreation"></a>
Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is `FALSE`. If the AllowProfileCreation flag is set to `FALSE`, then the service tries to fetch a standard profile and associate this object with the profile. If it is set to `TRUE`, and if no match is found, then the service creates a new standard profile.
Type: Boolean
Required: No

 ** [Description](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-Description"></a>
Description of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** [EncryptionKey](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-EncryptionKey"></a>
The customer-provided key to encrypt the profile object that will be created in this profile object type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [ExpirationDays](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-ExpirationDays"></a>
The number of days until the data in the object expires.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1098.
Required: No

 ** [Fields](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-Fields"></a>
A map of the name and ObjectType field.
Type: String to [ObjectTypeField](API_connect-customer-profiles_ObjectTypeField.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`
Required: No

 ** [Keys](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-Keys"></a>
A list of unique keys that can be used to map data to the profile.
Type: String to array of [ObjectTypeKey](API_connect-customer-profiles_ObjectTypeKey.md) objects map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** [MaxProfileObjectCount](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-MaxProfileObjectCount"></a>
The amount of profile object max count assigned to the object type
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [SourceLastUpdatedTimestampFormat](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-SourceLastUpdatedTimestampFormat"></a>
The format of your `sourceLastUpdatedTimestamp` that was previously set up.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [SourcePriority](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-SourcePriority"></a>
An integer that determines the priority of this object type when data from multiple sources is ingested. Lower values take priority. Object types without a specified source priority default to the lowest priority.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Tags](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [TemplateId](#API_connect-customer-profiles_PutProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-request-TemplateId"></a>
A unique identifier for the object template. For some attributes in the request, the service will use the default value from the object template when TemplateId is present. If these attributes are present in the request, the service may return a `BadRequestException`. These attributes include: AllowProfileCreation, SourceLastUpdatedTimestampFormat, Fields, and Keys. For example, if AllowProfileCreation is set to true when TemplateId is set, the service may return a `BadRequestException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax"></a>

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
<a name="API_connect-customer-profiles_PutProfileObjectType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AllowProfileCreation](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-AllowProfileCreation"></a>
Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is `FALSE`. If the AllowProfileCreation flag is set to `FALSE`, then the service tries to fetch a standard profile and associate this object with the profile. If it is set to `TRUE`, and if no match is found, then the service creates a new standard profile.
Type: Boolean

 ** [CreatedAt](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-CreatedAt"></a>
The timestamp of when the domain was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-Description"></a>
Description of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

 ** [EncryptionKey](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-EncryptionKey"></a>
The customer-provided key to encrypt the profile object that will be created in this profile object type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [ExpirationDays](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-ExpirationDays"></a>
The number of days until the data in the object expires.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1098.

 ** [Fields](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-Fields"></a>
A map of the name and ObjectType field.
Type: String to [ObjectTypeField](API_connect-customer-profiles_ObjectTypeField.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`

 ** [Keys](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-Keys"></a>
A list of unique keys that can be used to map data to the profile.
Type: String to array of [ObjectTypeKey](API_connect-customer-profiles_ObjectTypeKey.md) objects map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_-]+$`

 ** [LastUpdatedAt](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-LastUpdatedAt"></a>
The timestamp of when the domain was most recently edited.
Type: Timestamp

 ** [MaxAvailableProfileObjectCount](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-MaxAvailableProfileObjectCount"></a>
The amount of provisioned profile object max count available.
Type: Integer
Valid Range: Minimum value of 0.

 ** [MaxProfileObjectCount](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-MaxProfileObjectCount"></a>
The amount of profile object max count assigned to the object type.
Type: Integer
Valid Range: Minimum value of 1.

 ** [ObjectTypeName](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-ObjectTypeName"></a>
The name of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`

 ** [SourceLastUpdatedTimestampFormat](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-SourceLastUpdatedTimestampFormat"></a>
The format of your `sourceLastUpdatedTimestamp` that was previously set up in fields that were parsed using [SimpleDateFormat](https://docs.oracle.com/javase/10/docs/api/java/text/SimpleDateFormat.html). If you have `sourceLastUpdatedTimestamp` in your field, you must set up `sourceLastUpdatedTimestampFormat`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [SourcePriority](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-SourcePriority"></a>
An integer that determines the priority of this object type when data from multiple sources is ingested. Lower values take priority. Object types without a specified source priority default to the lowest priority.
Type: Integer
Valid Range: Minimum value of 1.

 ** [Tags](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

 ** [TemplateId](#API_connect-customer-profiles_PutProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_PutProfileObjectType-response-TemplateId"></a>
A unique identifier for the object template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_connect-customer-profiles_PutProfileObjectType_Errors"></a>

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
<a name="API_connect-customer-profiles_PutProfileObjectType_Examples"></a>

### Example 1
<a name="API_connect-customer-profiles_PutProfileObjectType_Example_1"></a>

In the request, replace the `Fields` and `Keys` request parameters with your own. If specifying a `TemplateId`, replace it with your own `TemplateId` value. You must either specify both `Fields` and `Keys`, or you can specify `TemplateId`. You can't include all three.

#### Sample Request
<a name="API_connect-customer-profiles_PutProfileObjectType_Example_1_Request"></a>

```
PUT /domains/ExampleDomainName/object-types/CustomProfileObjectTypeName HTTP/1.1

{
   "Description": "Internal ERP System",
   "EncryptionKey": "arn:aws:kms:us-east-1:123456789012:key/1988472d-6b77-4bb6-ae39-efce5EXAMPLE",
   "AllowProfileCreation": false,
   "ExpirationDays": 1000,
   "Fields": {
      "email" : {
         "ContentType": "EMAIL_ADDRESS",
         "Source": "_source.email",
         "Target": "_profile.BusinessEmail"
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
      "_email" : [
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
   "SourcePriority": 2,
   "TemplateId": "MyTemplateId"
}
```

#### Sample Response
<a name="API_connect-customer-profiles_PutProfileObjectType_Example_1_Response"></a>

```
Content-type: application/json
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

### Example 2
<a name="API_connect-customer-profiles_PutProfileObjectType_Example_2"></a>

This example illustrates one usage of PutProfileObjectType.

#### Sample Request
<a name="API_connect-customer-profiles_PutProfileObjectType_Example_2_Request"></a>

```
PUT /domains/ExampleDomainName/object-types/CTR HTTP/1.1
Content-type: application/json
{
   "Description": "CTR",
   "TemplateId": "CTR-NoInferred"
}
```

### Example 2.5
<a name="API_connect-customer-profiles_PutProfileObjectType_Example_3"></a>

This command associates Contact Records with already existing profiles with the same phone number. In the example below, replace `ExampleDomainName` with your domain name, and replace the description with your desired description.

#### Sample Request
<a name="API_connect-customer-profiles_PutProfileObjectType_Example_3_Request"></a>

```
aws profile put-object-type --domain-name ExampleDomainName --object-type-name CTR --description "CTR" --template-id "CTR-NoInferred"
```

## See Also
<a name="API_connect-customer-profiles_PutProfileObjectType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/PutProfileObjectType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/PutProfileObjectType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/PutProfileObjectType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/PutProfileObjectType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/PutProfileObjectType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/PutProfileObjectType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/PutProfileObjectType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/PutProfileObjectType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/PutProfileObjectType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/PutProfileObjectType)

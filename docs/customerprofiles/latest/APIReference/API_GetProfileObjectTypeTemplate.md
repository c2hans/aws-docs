---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileObjectTypeTemplate.html
---

# GetProfileObjectTypeTemplate
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate"></a>

Returns the template information for a specific object type.

A template is a predefined ProfileObjectType, such as “Salesforce-Account” or “Salesforce-Contact.” When a user sends a ProfileObject, using the PutProfileObject API, with an ObjectTypeName that matches one of the TemplateIds, it uses the mappings from the template.

## Request Syntax
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_RequestSyntax"></a>

```
GET /templates/{{TemplateId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TemplateId](#API_connect-customer-profiles_GetProfileObjectTypeTemplate_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectTypeTemplate-request-uri-TemplateId"></a>
A unique identifier for the object template.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AllowProfileCreation": boolean,
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
   "SourceLastUpdatedTimestampFormat": "string",
   "SourceName": "string",
   "SourceObject": "string",
   "TemplateId": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AllowProfileCreation](#API_connect-customer-profiles_GetProfileObjectTypeTemplate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectTypeTemplate-response-AllowProfileCreation"></a>
Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is `FALSE`. If the AllowProfileCreation flag is set to `FALSE`, then the service tries to fetch a standard profile and associate this object with the profile. If it is set to `TRUE`, and if no match is found, then the service creates a new standard profile.
Type: Boolean

 ** [Fields](#API_connect-customer-profiles_GetProfileObjectTypeTemplate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectTypeTemplate-response-Fields"></a>
A map of the name and ObjectType field.
Type: String to [ObjectTypeField](API_connect-customer-profiles_ObjectTypeField.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`

 ** [Keys](#API_connect-customer-profiles_GetProfileObjectTypeTemplate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectTypeTemplate-response-Keys"></a>
A list of unique keys that can be used to map data to the profile.
Type: String to array of [ObjectTypeKey](API_connect-customer-profiles_ObjectTypeKey.md) objects map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_-]+$`

 ** [SourceLastUpdatedTimestampFormat](#API_connect-customer-profiles_GetProfileObjectTypeTemplate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectTypeTemplate-response-SourceLastUpdatedTimestampFormat"></a>
The format of your `sourceLastUpdatedTimestamp` that was previously set up.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [SourceName](#API_connect-customer-profiles_GetProfileObjectTypeTemplate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectTypeTemplate-response-SourceName"></a>
The name of the source of the object template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [SourceObject](#API_connect-customer-profiles_GetProfileObjectTypeTemplate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectTypeTemplate-response-SourceObject"></a>
The source of the object template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [TemplateId](#API_connect-customer-profiles_GetProfileObjectTypeTemplate_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetProfileObjectTypeTemplate-response-TemplateId"></a>
A unique identifier for the object template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_Errors"></a>

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
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_Examples"></a>

### Example
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_Example_1"></a>

This example illustrates one usage of GetProfileObjectTypeTemplate.

#### Sample Request
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_Example_1_Request"></a>

```
GET /templates/{TemplateId} HTTP/1.1
```

#### Sample Response
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_Example_1_Response"></a>

```
Content-type: application/json
{
   "AllowProfileCreätion": "FALSE",
   "Fields": {
      "email" : {
         "ContentType": "EMAIL_ADDRESS",
         "Source": "_source.email",
         "Target": "_profile.BusinessEmailAddress"
      },
      "phone" : {
         "ContentType": "PHONE_NUMBER",
         "Source": "_source.phone",
         "Target": "_profile.Businessphonenumber"
      }
   },
   "Keys": {
      "_email" : [
         {
            "FieldNames": [ "email" ],
            "StandardIdentifiers": [ "PROFILE", "UNIQUE" ]
         }
      ]
   },
   "SourceName": "Saleforce-Account",
   "SourceObject": "Account",
   "TemplateId": "Saleforce-Account"
}
```

## See Also
<a name="API_connect-customer-profiles_GetProfileObjectTypeTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetProfileObjectTypeTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetProfileObjectTypeTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetProfileObjectTypeTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetProfileObjectTypeTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetProfileObjectTypeTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetProfileObjectTypeTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetProfileObjectTypeTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetProfileObjectTypeTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetProfileObjectTypeTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetProfileObjectTypeTemplate)

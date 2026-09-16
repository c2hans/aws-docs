---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetDomainObjectType.html
---

# GetDomainObjectType
<a name="API_connect-customer-profiles_GetDomainObjectType"></a>

Return a DomainObjectType for the input Domain and ObjectType names.

## Request Syntax
<a name="API_connect-customer-profiles_GetDomainObjectType_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/domain-object-types/{{ObjectTypeName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetDomainObjectType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetDomainObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetDomainObjectType-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [ObjectTypeName](#API_connect-customer-profiles_GetDomainObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetDomainObjectType-request-uri-ObjectTypeName"></a>
The unique name of the domain object type.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetDomainObjectType_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetDomainObjectType_ResponseSyntax"></a>

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
<a name="API_connect-customer-profiles_GetDomainObjectType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_connect-customer-profiles_GetDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetDomainObjectType-response-CreatedAt"></a>
The timestamp of when the domain object type was created.
Type: Timestamp

 ** [Description](#API_connect-customer-profiles_GetDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetDomainObjectType-response-Description"></a>
The description of the domain object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.

 ** [EncryptionKey](#API_connect-customer-profiles_GetDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetDomainObjectType-response-EncryptionKey"></a>
The customer provided KMS key used to encrypt this type of domain object.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [Fields](#API_connect-customer-profiles_GetDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetDomainObjectType-response-Fields"></a>
A map of field names to their corresponding domain object type field definitions.
Type: String to [DomainObjectTypeField](API_connect-customer-profiles_DomainObjectTypeField.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z0-9_.-]+$`

 ** [LastUpdatedAt](#API_connect-customer-profiles_GetDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetDomainObjectType-response-LastUpdatedAt"></a>
The timestamp of when the domain object type was most recently edited.
Type: Timestamp

 ** [ObjectTypeName](#API_connect-customer-profiles_GetDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetDomainObjectType-response-ObjectTypeName"></a>
The unique name of the domain object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`

 ** [Tags](#API_connect-customer-profiles_GetDomainObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetDomainObjectType-response-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_connect-customer-profiles_GetDomainObjectType_Errors"></a>

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
<a name="API_connect-customer-profiles_GetDomainObjectType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetDomainObjectType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetDomainObjectType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetDomainObjectType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetDomainObjectType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetDomainObjectType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetDomainObjectType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetDomainObjectType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetDomainObjectType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetDomainObjectType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetDomainObjectType)

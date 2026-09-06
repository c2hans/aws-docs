---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_UpdateMessageTemplate.html
---

# UpdateMessageTemplate
<a name="API_amazon-q-connect_UpdateMessageTemplate"></a>

Updates the Amazon Q in Connect message template. Partial update is supported. If any field is not supplied, it will remain unchanged for the message template that is referenced by the `$LATEST` qualifier. Any modification will only apply to the message template that is referenced by the `$LATEST` qualifier. The fields for all available versions will remain unchanged.

## Request Syntax
<a name="API_amazon-q-connect_UpdateMessageTemplate_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/messageTemplates/{{messageTemplateId}} HTTP/1.1
Content-type: application/json

{
   "content": { ... },
   "defaultAttributes": {
      "agentAttributes": {
         "firstName": "{{string}}",
         "lastName": "{{string}}"
      },
      "customAttributes": {
         "{{string}}" : "{{string}}"
      },
      "customerProfileAttributes": {
         "accountNumber": "{{string}}",
         "additionalInformation": "{{string}}",
         "address1": "{{string}}",
         "address2": "{{string}}",
         "address3": "{{string}}",
         "address4": "{{string}}",
         "billingAddress1": "{{string}}",
         "billingAddress2": "{{string}}",
         "billingAddress3": "{{string}}",
         "billingAddress4": "{{string}}",
         "billingCity": "{{string}}",
         "billingCountry": "{{string}}",
         "billingCounty": "{{string}}",
         "billingPostalCode": "{{string}}",
         "billingProvince": "{{string}}",
         "billingState": "{{string}}",
         "birthDate": "{{string}}",
         "businessEmailAddress": "{{string}}",
         "businessName": "{{string}}",
         "businessPhoneNumber": "{{string}}",
         "city": "{{string}}",
         "country": "{{string}}",
         "county": "{{string}}",
         "custom": {
            "{{string}}" : "{{string}}"
         },
         "emailAddress": "{{string}}",
         "firstName": "{{string}}",
         "gender": "{{string}}",
         "homePhoneNumber": "{{string}}",
         "lastName": "{{string}}",
         "mailingAddress1": "{{string}}",
         "mailingAddress2": "{{string}}",
         "mailingAddress3": "{{string}}",
         "mailingAddress4": "{{string}}",
         "mailingCity": "{{string}}",
         "mailingCountry": "{{string}}",
         "mailingCounty": "{{string}}",
         "mailingPostalCode": "{{string}}",
         "mailingProvince": "{{string}}",
         "mailingState": "{{string}}",
         "middleName": "{{string}}",
         "mobilePhoneNumber": "{{string}}",
         "partyType": "{{string}}",
         "phoneNumber": "{{string}}",
         "postalCode": "{{string}}",
         "profileARN": "{{string}}",
         "profileId": "{{string}}",
         "province": "{{string}}",
         "shippingAddress1": "{{string}}",
         "shippingAddress2": "{{string}}",
         "shippingAddress3": "{{string}}",
         "shippingAddress4": "{{string}}",
         "shippingCity": "{{string}}",
         "shippingCountry": "{{string}}",
         "shippingCounty": "{{string}}",
         "shippingPostalCode": "{{string}}",
         "shippingProvince": "{{string}}",
         "shippingState": "{{string}}",
         "state": "{{string}}"
      },
      "systemAttributes": {
         "customerEndpoint": {
            "address": "{{string}}"
         },
         "name": "{{string}}",
         "systemEndpoint": {
            "address": "{{string}}"
         }
      }
   },
   "language": "{{string}}",
   "sourceConfiguration": { ... }
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_UpdateMessageTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_UpdateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateMessageTemplate-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [messageTemplateId](#API_amazon-q-connect_UpdateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateMessageTemplate-request-uri-messageTemplateId"></a>
The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_UpdateMessageTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [content](#API_amazon-q-connect_UpdateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateMessageTemplate-request-content"></a>
The content of the message template.
Type: [MessageTemplateContentProvider](API_amazon-q-connect_MessageTemplateContentProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [defaultAttributes](#API_amazon-q-connect_UpdateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateMessageTemplate-request-defaultAttributes"></a>
An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.
Type: [MessageTemplateAttributes](API_amazon-q-connect_MessageTemplateAttributes.md) object
Required: No

 ** [language](#API_amazon-q-connect_UpdateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateMessageTemplate-request-language"></a>
The language code value for the language in which the quick response is written. The supported language codes include `de_DE`, `en_US`, `es_ES`, `fr_FR`, `id_ID`, `it_IT`, `ja_JP`, `ko_KR`, `pt_BR`, `zh_CN`, `zh_TW`
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: No

 ** [sourceConfiguration](#API_amazon-q-connect_UpdateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateMessageTemplate-request-sourceConfiguration"></a>
The source configuration of the message template. Only set this argument for WHATSAPP channel subtype.
Type: [MessageTemplateSourceConfiguration](API_amazon-q-connect_MessageTemplateSourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_amazon-q-connect_UpdateMessageTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "messageTemplate": {
      "attributeTypes": [ "string" ],
      "channel": "string",
      "channelSubtype": "string",
      "content": { ... },
      "createdTime": "string",
      "defaultAttributes": {
         "agentAttributes": {
            "firstName": "string",
            "lastName": "string"
         },
         "customAttributes": {
            "string" : "string"
         },
         "customerProfileAttributes": {
            "accountNumber": "string",
            "additionalInformation": "string",
            "address1": "string",
            "address2": "string",
            "address3": "string",
            "address4": "string",
            "billingAddress1": "string",
            "billingAddress2": "string",
            "billingAddress3": "string",
            "billingAddress4": "string",
            "billingCity": "string",
            "billingCountry": "string",
            "billingCounty": "string",
            "billingPostalCode": "string",
            "billingProvince": "string",
            "billingState": "string",
            "birthDate": "string",
            "businessEmailAddress": "string",
            "businessName": "string",
            "businessPhoneNumber": "string",
            "city": "string",
            "country": "string",
            "county": "string",
            "custom": {
               "string" : "string"
            },
            "emailAddress": "string",
            "firstName": "string",
            "gender": "string",
            "homePhoneNumber": "string",
            "lastName": "string",
            "mailingAddress1": "string",
            "mailingAddress2": "string",
            "mailingAddress3": "string",
            "mailingAddress4": "string",
            "mailingCity": "string",
            "mailingCountry": "string",
            "mailingCounty": "string",
            "mailingPostalCode": "string",
            "mailingProvince": "string",
            "mailingState": "string",
            "middleName": "string",
            "mobilePhoneNumber": "string",
            "partyType": "string",
            "phoneNumber": "string",
            "postalCode": "string",
            "profileARN": "string",
            "profileId": "string",
            "province": "string",
            "shippingAddress1": "string",
            "shippingAddress2": "string",
            "shippingAddress3": "string",
            "shippingAddress4": "string",
            "shippingCity": "string",
            "shippingCountry": "string",
            "shippingCounty": "string",
            "shippingPostalCode": "string",
            "shippingProvince": "string",
            "shippingState": "string",
            "state": "string"
         },
         "systemAttributes": {
            "customerEndpoint": {
               "address": "string"
            },
            "name": "string",
            "systemEndpoint": {
               "address": "string"
            }
         }
      },
      "description": "string",
      "groupingConfiguration": {
         "criteria": "string",
         "values": [ "string" ]
      },
      "knowledgeBaseArn": "string",
      "knowledgeBaseId": "string",
      "language": "string",
      "lastModifiedBy": "string",
      "lastModifiedTime": "string",
      "messageTemplateArn": "string",
      "messageTemplateContentSha256": "string",
      "messageTemplateId": "string",
      "name": "string",
      "sourceConfigurationSummary": { ... },
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_UpdateMessageTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messageTemplate](#API_amazon-q-connect_UpdateMessageTemplate_ResponseSyntax) **   <a name="connect-amazon-q-connect_UpdateMessageTemplate-response-messageTemplate"></a>
The message template.
Type: [MessageTemplateData](API_amazon-q-connect_MessageTemplateData.md) object

## Errors
<a name="API_amazon-q-connect_UpdateMessageTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_UpdateMessageTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/UpdateMessageTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/UpdateMessageTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/UpdateMessageTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/UpdateMessageTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/UpdateMessageTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/UpdateMessageTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/UpdateMessageTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/UpdateMessageTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/UpdateMessageTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/UpdateMessageTemplate)

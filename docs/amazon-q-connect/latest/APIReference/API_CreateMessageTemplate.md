---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_CreateMessageTemplate.html
---

# CreateMessageTemplate
<a name="API_amazon-q-connect_CreateMessageTemplate"></a>

Creates an Amazon Q in Connect message template. The name of the message template has to be unique for each knowledge base. The channel subtype of the message template is immutable and cannot be modified after creation. After the message template is created, you can use the `$LATEST` qualifier to reference the created message template.

## Request Syntax
<a name="API_amazon-q-connect_CreateMessageTemplate_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/messageTemplates HTTP/1.1
Content-type: application/json

{
   "channelSubtype": "{{string}}",
   "clientToken": "{{string}}",
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
   "description": "{{string}}",
   "groupingConfiguration": {
      "criteria": "{{string}}",
      "values": [ "{{string}}" ]
   },
   "language": "{{string}}",
   "name": "{{string}}",
   "sourceConfiguration": { ... },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateMessageTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_CreateMessageTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channelSubtype](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-channelSubtype"></a>
The channel subtype this message template applies to.
Type: String
Valid Values: `EMAIL | SMS | WHATSAPP | PUSH`
Required: Yes

 ** [clientToken](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [content](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-content"></a>
The content of the message template.
Type: [MessageTemplateContentProvider](API_amazon-q-connect_MessageTemplateContentProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [defaultAttributes](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-defaultAttributes"></a>
An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.
Type: [MessageTemplateAttributes](API_amazon-q-connect_MessageTemplateAttributes.md) object
Required: No

 ** [description](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-description"></a>
The description of the message template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** [groupingConfiguration](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-groupingConfiguration"></a>
The configuration information of the grouping of Amazon Q in Connect users.
Type: [GroupingConfiguration](API_amazon-q-connect_GroupingConfiguration.md) object
Required: No

 ** [language](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-language"></a>
The language code value for the language in which the quick response is written. The supported language codes include `de_DE`, `en_US`, `es_ES`, `fr_FR`, `id_ID`, `it_IT`, `ja_JP`, `ko_KR`, `pt_BR`, `zh_CN`, `zh_TW`
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: No

 ** [name](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-name"></a>
The name of the message template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** [sourceConfiguration](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-sourceConfiguration"></a>
The source configuration of the message template. Only set this argument for WHATSAPP channel subtype.
Type: [MessageTemplateSourceConfiguration](API_amazon-q-connect_MessageTemplateSourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [tags](#API_amazon-q-connect_CreateMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_amazon-q-connect_CreateMessageTemplate_ResponseSyntax"></a>

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
<a name="API_amazon-q-connect_CreateMessageTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messageTemplate](#API_amazon-q-connect_CreateMessageTemplate_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplate-response-messageTemplate"></a>
The message template.
Type: [MessageTemplateData](API_amazon-q-connect_MessageTemplateData.md) object

## Errors
<a name="API_amazon-q-connect_CreateMessageTemplate_Errors"></a>

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

 ** ServiceQuotaExceededException **
You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_CreateMessageTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateMessageTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateMessageTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateMessageTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateMessageTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateMessageTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateMessageTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateMessageTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateMessageTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateMessageTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateMessageTemplate)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_RenderMessageTemplate.html
---

# RenderMessageTemplate
<a name="API_amazon-q-connect_RenderMessageTemplate"></a>

Renders the Amazon Q in Connect message template based on the attribute values provided and generates the message content. For any variable present in the message template, if the attribute value is neither provided in the attribute request parameter nor the default attribute of the message template, the rendered message content will keep the variable placeholder as it is and return the attribute keys that are missing.

## Request Syntax
<a name="API_amazon-q-connect_RenderMessageTemplate_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/messageTemplates/{{messageTemplateId}}/render HTTP/1.1
Content-type: application/json

{
   "attributes": {
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
   }
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_RenderMessageTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_RenderMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_RenderMessageTemplate-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [messageTemplateId](#API_amazon-q-connect_RenderMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_RenderMessageTemplate-request-uri-messageTemplateId"></a>
The identifier of the message template. Can be either the ID or the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_RenderMessageTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_amazon-q-connect_RenderMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_RenderMessageTemplate-request-attributes"></a>
An object that specifies the values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the value for that variable.
Type: [MessageTemplateAttributes](API_amazon-q-connect_MessageTemplateAttributes.md) object
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_RenderMessageTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attachments": [
      {
         "attachmentId": "string",
         "contentDisposition": "string",
         "name": "string",
         "uploadedTime": "string",
         "url": "string",
         "urlExpiry": "string"
      }
   ],
   "attributesNotInterpolated": [ "string" ],
   "content": { ... },
   "sourceConfigurationSummary": { ... }
}
```

## Response Elements
<a name="API_amazon-q-connect_RenderMessageTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attachments](#API_amazon-q-connect_RenderMessageTemplate_ResponseSyntax) **   <a name="connect-amazon-q-connect_RenderMessageTemplate-response-attachments"></a>
The message template attachments.
Type: Array of [MessageTemplateAttachment](API_amazon-q-connect_MessageTemplateAttachment.md) objects

 ** [attributesNotInterpolated](#API_amazon-q-connect_RenderMessageTemplate_ResponseSyntax) **   <a name="connect-amazon-q-connect_RenderMessageTemplate-response-attributesNotInterpolated"></a>
The attribute keys that are not resolved.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 32767.

 ** [content](#API_amazon-q-connect_RenderMessageTemplate_ResponseSyntax) **   <a name="connect-amazon-q-connect_RenderMessageTemplate-response-content"></a>
The content of the message template.
Type: [MessageTemplateContentProvider](API_amazon-q-connect_MessageTemplateContentProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [sourceConfigurationSummary](#API_amazon-q-connect_RenderMessageTemplate_ResponseSyntax) **   <a name="connect-amazon-q-connect_RenderMessageTemplate-response-sourceConfigurationSummary"></a>
The source configuration of the message template.
Type: [MessageTemplateSourceConfigurationSummary](API_amazon-q-connect_MessageTemplateSourceConfigurationSummary.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_amazon-q-connect_RenderMessageTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_amazon-q-connect_RenderMessageTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/RenderMessageTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/RenderMessageTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/RenderMessageTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/RenderMessageTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/RenderMessageTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/RenderMessageTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/RenderMessageTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/RenderMessageTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/RenderMessageTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/RenderMessageTemplate)

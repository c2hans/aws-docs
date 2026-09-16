---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateMessageTemplateVersion.html
---

# CreateMessageTemplateVersion
<a name="API_amazon-q-connect_CreateMessageTemplateVersion"></a>

Creates a new Amazon Q in Connect message template version from the current content and configuration of a message template. Versions are immutable and monotonically increasing. Once a version is created, you can reference a specific version of the message template by passing in `<message-template-id>:<versionNumber>` as the message template identifier. An error is displayed if the supplied `messageTemplateContentSha256` is different from the `messageTemplateContentSha256` of the message template with `$LATEST` qualifier. If multiple `CreateMessageTemplateVersion` requests are made while the message template remains the same, only the first invocation creates a new version and the succeeding requests will return the same response as the first invocation.

## Request Syntax
<a name="API_amazon-q-connect_CreateMessageTemplateVersion_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/messageTemplates/{{messageTemplateId}}/versions HTTP/1.1
Content-type: application/json

{
   "messageTemplateContentSha256": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateMessageTemplateVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_CreateMessageTemplateVersion_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateVersion-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [messageTemplateId](#API_amazon-q-connect_CreateMessageTemplateVersion_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateVersion-request-uri-messageTemplateId"></a>
The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_CreateMessageTemplateVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [messageTemplateContentSha256](#API_amazon-q-connect_CreateMessageTemplateVersion_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateVersion-request-messageTemplateContentSha256"></a>
The checksum value of the message template content that is referenced by the `$LATEST` qualifier. It can be returned in `MessageTemplateData` or `ExtendedMessageTemplateData`. It’s calculated by content, language, `defaultAttributes` and `Attachments` of the message template. If not supplied, the message template version will be created based on the message template content that is referenced by the `$LATEST` qualifier by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: No

## Response Syntax
<a name="API_amazon-q-connect_CreateMessageTemplateVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "messageTemplate": {
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
      "isActive": boolean,
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
      },
      "versionNumber": number
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_CreateMessageTemplateVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messageTemplate](#API_amazon-q-connect_CreateMessageTemplateVersion_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateVersion-response-messageTemplate"></a>
The message template.
Type: [ExtendedMessageTemplateData](API_amazon-q-connect_ExtendedMessageTemplateData.md) object

## Errors
<a name="API_amazon-q-connect_CreateMessageTemplateVersion_Errors"></a>

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
<a name="API_amazon-q-connect_CreateMessageTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateMessageTemplateVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateMessageTemplateVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateMessageTemplateVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateMessageTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateMessageTemplateVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateMessageTemplateVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateMessageTemplateVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateMessageTemplateVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateMessageTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateMessageTemplateVersion)

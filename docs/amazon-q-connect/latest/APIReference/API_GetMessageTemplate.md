---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetMessageTemplate.html
---

# GetMessageTemplate
<a name="API_amazon-q-connect_GetMessageTemplate"></a>

Retrieves the Amazon Q in Connect message template. The message template identifier can contain an optional qualifier, for example, `<message-template-id>:<qualifier>`, which is either an actual version number or an Amazon Q Connect managed qualifier `$ACTIVE_VERSION` \| `$LATEST`. If it is not supplied, then `$LATEST` is assumed implicitly.

## Request Syntax
<a name="API_amazon-q-connect_GetMessageTemplate_RequestSyntax"></a>

```
GET /knowledgeBases/{{knowledgeBaseId}}/messageTemplates/{{messageTemplateId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_GetMessageTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_GetMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_GetMessageTemplate-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [messageTemplateId](#API_amazon-q-connect_GetMessageTemplate_RequestSyntax) **   <a name="connect-amazon-q-connect_GetMessageTemplate-request-uri-messageTemplateId"></a>
The identifier of the message template. Can be either the ID or the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_GetMessageTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_GetMessageTemplate_ResponseSyntax"></a>

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
<a name="API_amazon-q-connect_GetMessageTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messageTemplate](#API_amazon-q-connect_GetMessageTemplate_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetMessageTemplate-response-messageTemplate"></a>
The message template.
Type: [ExtendedMessageTemplateData](API_amazon-q-connect_ExtendedMessageTemplateData.md) object

## Errors
<a name="API_amazon-q-connect_GetMessageTemplate_Errors"></a>

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

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_GetMessageTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/GetMessageTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/GetMessageTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GetMessageTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/GetMessageTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GetMessageTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/GetMessageTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/GetMessageTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/GetMessageTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/GetMessageTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GetMessageTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

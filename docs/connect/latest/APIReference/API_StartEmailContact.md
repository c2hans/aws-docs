---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEmailContact.html
---

# StartEmailContact
<a name="API_StartEmailContact"></a>

Creates an inbound email contact and initiates a flow to start the email contact for the customer. Response of this API provides the ContactId of the email contact created.

## Request Syntax
<a name="API_StartEmailContact_RequestSyntax"></a>

```
PUT /contact/email HTTP/1.1
Content-type: application/json

{
   "AdditionalRecipients": {
      "CcAddresses": [
         {
            "DisplayName": "{{string}}",
            "EmailAddress": "{{string}}"
         }
      ],
      "ToAddresses": [
         {
            "DisplayName": "{{string}}",
            "EmailAddress": "{{string}}"
         }
      ]
   },
   "Attachments": [
      {
         "FileName": "{{string}}",
         "S3Url": "{{string}}"
      }
   ],
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "ClientToken": "{{string}}",
   "ContactFlowId": "{{string}}",
   "Description": "{{string}}",
   "DestinationEmailAddress": "{{string}}",
   "EmailMessage": {
      "MessageSourceType": "{{string}}",
      "RawMessage": {
         "Body": "{{string}}",
         "ContentType": "{{string}}",
         "Headers": {
            "{{string}}" : "{{string}}"
         },
         "Subject": "{{string}}"
      }
   },
   "FromEmailAddress": {
      "DisplayName": "{{string}}",
      "EmailAddress": "{{string}}"
   },
   "InstanceId": "{{string}}",
   "Name": "{{string}}",
   "References": {
      "{{string}}" : {
         "Arn": "{{string}}",
         "Status": "{{string}}",
         "StatusReason": "{{string}}",
         "Type": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "RelatedContactId": "{{string}}",
   "SegmentAttributes": {
      "{{string}}" : {
         "ValueArn": "{{string}}",
         "ValueInteger": {{number}},
         "ValueList": [
            "SegmentAttributeValue"
         ],
         "ValueMap": {
            "{{string}}" : "SegmentAttributeValue"
         },
         "ValueString": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_StartEmailContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartEmailContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdditionalRecipients](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-AdditionalRecipients"></a>
The additional recipients address of the email.
Type: [InboundAdditionalRecipients](API_InboundAdditionalRecipients.md) object
Required: No

 ** [Attachments](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-Attachments"></a>
List of S3 presigned URLs of email attachments and their file name.
Type: Array of [EmailAttachment](API_EmailAttachment.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [Attributes](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-Attributes"></a>
A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.
There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** [ClientToken](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactFlowId](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-ContactFlowId"></a>
The identifier of the flow for initiating the emails. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to **Routing**, **Flows**. Choose the flow. On the flow page, under the name of the flow, choose **Show additional flow information**. The ContactFlowId is the last part of the ARN, shown here in bold:
arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/**846ec553-a005-41c0-8341-xxxxxxxxxxxx**
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Description](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-Description"></a>
A description of the email contact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [DestinationEmailAddress](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-DestinationEmailAddress"></a>
The email address associated with the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[^\s@]+@[^\s@]+\.[^\s@]+`
Required: Yes

 ** [EmailMessage](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-EmailMessage"></a>
The email message body to be sent to the newly created email.
Type: [InboundEmailContent](API_InboundEmailContent.md) object
Required: Yes

 ** [FromEmailAddress](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-FromEmailAddress"></a>
The email address of the customer.
Type: [EmailAddressInfo](API_EmailAddressInfo.md) object
Required: Yes

 ** [InstanceId](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Name](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-Name"></a>
The name of a email that is shown to an agent in the Contact Control Panel (CCP).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [References](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-References"></a>
A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Emails can have the following reference types at the time of creation: `URL` \| `NUMBER` \| `STRING` \| `DATE`. `EMAIL` \| `EMAIL_MESSAGE` \|`ATTACHMENT` are not a supported reference type during email creation.
Type: String to [Reference](API_Reference.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [RelatedContactId](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-RelatedContactId"></a>
The contactId that is related to this contact. Linking emails together by using `RelatedContactID` copies over contact attributes from the related email contact to the new email contact. All updates to user-defined attributes in the new email contact are limited to the individual contact ID. There are no limits to the number of contacts that can be linked by using `RelatedContactId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [SegmentAttributes](#API_StartEmailContact_RequestSyntax) **   <a name="connect-StartEmailContact-request-SegmentAttributes"></a>
A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.
Attribute keys can include only alphanumeric, -, and \_.
This field can be used to show channel subtype, such as `connect:Guide`.
To set contact expiry, a `ValueMap` must be specified containing the integer number of minutes the contact will be active for before expiring, with `SegmentAttributes` like { ` "connect:ContactExpiry": {"ValueMap" : { "ExpiryDuration": { "ValueInteger":135}}}}`.
Type: String to [SegmentAttributeValue](API_SegmentAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_StartEmailContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactId": "string"
}
```

## Response Elements
<a name="API_StartEmailContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactId](#API_StartEmailContact_ResponseSyntax) **   <a name="connect-StartEmailContact-response-ContactId"></a>
The identifier of this contact within the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_StartEmailContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_StartEmailContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartEmailContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartEmailContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartEmailContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartEmailContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartEmailContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartEmailContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartEmailContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartEmailContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartEmailContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartEmailContact)

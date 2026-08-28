---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SendOutboundEmail.html
---

# SendOutboundEmail
<a name="API_SendOutboundEmail"></a>

Send outbound email for outbound campaigns. For more information about outbound campaigns, see [Set up Connect Customer outbound campaigns](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html).

**Note**
Only the Connect Customer outbound campaigns service principal is allowed to assume a role in your account and call this API.

## Request Syntax
<a name="API_SendOutboundEmail_RequestSyntax"></a>

```
PUT /instance/{{InstanceId}}/outbound-email HTTP/1.1
Content-type: application/json

{
   "AdditionalRecipients": {
      "CcEmailAddresses": [
         {
            "DisplayName": "{{string}}",
            "EmailAddress": "{{string}}"
         }
      ]
   },
   "ClientToken": "{{string}}",
   "DestinationEmailAddress": {
      "DisplayName": "{{string}}",
      "EmailAddress": "{{string}}"
   },
   "EmailMessage": {
      "MessageSourceType": "{{string}}",
      "RawMessage": {
         "Body": "{{string}}",
         "ContentType": "{{string}}",
         "Subject": "{{string}}"
      },
      "TemplatedMessageConfig": {
         "KnowledgeBaseId": "{{string}}",
         "MessageTemplateId": "{{string}}",
         "TemplateAttributes": {
            "CustomAttributes": {
               "{{string}}" : "{{string}}"
            },
            "CustomerProfileAttributes": "{{string}}"
         }
      }
   },
   "FromEmailAddress": {
      "DisplayName": "{{string}}",
      "EmailAddress": "{{string}}"
   },
   "SourceCampaign": {
      "CampaignId": "{{string}}",
      "OutboundRequestId": "{{string}}"
   },
   "TrafficType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SendOutboundEmail_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_SendOutboundEmail_RequestSyntax) **   <a name="connect-SendOutboundEmail-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_SendOutboundEmail_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdditionalRecipients](#API_SendOutboundEmail_RequestSyntax) **   <a name="connect-SendOutboundEmail-request-AdditionalRecipients"></a>
The additional recipients address of the email in CC.
Type: [OutboundAdditionalRecipients](API_OutboundAdditionalRecipients.md) object
Required: No

 ** [ClientToken](#API_SendOutboundEmail_RequestSyntax) **   <a name="connect-SendOutboundEmail-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [DestinationEmailAddress](#API_SendOutboundEmail_RequestSyntax) **   <a name="connect-SendOutboundEmail-request-DestinationEmailAddress"></a>
The email address to send the email to.
Type: [EmailAddressInfo](API_EmailAddressInfo.md) object
Required: Yes

 ** [EmailMessage](#API_SendOutboundEmail_RequestSyntax) **   <a name="connect-SendOutboundEmail-request-EmailMessage"></a>
The email message body to be sent to the newly created email.
Type: [OutboundEmailContent](API_OutboundEmailContent.md) object
Required: Yes

 ** [FromEmailAddress](#API_SendOutboundEmail_RequestSyntax) **   <a name="connect-SendOutboundEmail-request-FromEmailAddress"></a>
The email address to be used for sending email.
Type: [EmailAddressInfo](API_EmailAddressInfo.md) object
Required: Yes

 ** [SourceCampaign](#API_SendOutboundEmail_RequestSyntax) **   <a name="connect-SendOutboundEmail-request-SourceCampaign"></a>
A Campaign object need for Campaign traffic type.
Type: [SourceCampaign](API_SourceCampaign.md) object
Required: No

 ** [TrafficType](#API_SendOutboundEmail_RequestSyntax) **   <a name="connect-SendOutboundEmail-request-TrafficType"></a>
Denotes the class of traffic.
Only the CAMPAIGN traffic type is supported.
Type: String
Valid Values: `GENERAL | CAMPAIGN`
Required: Yes

## Response Syntax
<a name="API_SendOutboundEmail_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_SendOutboundEmail_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SendOutboundEmail_Errors"></a>

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
<a name="API_SendOutboundEmail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SendOutboundEmail)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SendOutboundEmail)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SendOutboundEmail)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SendOutboundEmail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SendOutboundEmail)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SendOutboundEmail)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SendOutboundEmail)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SendOutboundEmail)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SendOutboundEmail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SendOutboundEmail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundVoiceContact.html
---

# StartOutboundVoiceContact
<a name="API_StartOutboundVoiceContact"></a>

Places an outbound call to a contact, and then initiates the flow. It performs the actions in the flow that's specified (in `ContactFlowId`).

Agents do not initiate the outbound API, which means that they do not dial the contact. If the flow places an outbound call to a contact, and then puts the contact in queue, the call is then routed to the agent, like any other inbound case.

Dialing timeout for this operation can be configured with the “RingTimeoutInSeconds” parameter. If not specified, the default dialing timeout will be 60 seconds which means if the call is not connected within 60 seconds, it fails.

**Note**
UK numbers with a 447 prefix are not allowed by default. Before you can dial these UK mobile numbers, you must submit a service quota increase request. For more information, see [Connect Customer Service Quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) in the *Connect Customer Administrator Guide*.

**Note**
Campaign calls are not allowed by default. Before you can make a call with `TrafficType` = `CAMPAIGN`, you must submit a service quota increase request to the quota [Connect Customer campaigns](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#outbound-communications-quotas).

**Note**
For Preview dialing mode, only the Amazon Connect outbound campaigns service principal is allowed to assume a role in your account and call this API with OutboundStrategy.

## Request Syntax
<a name="API_StartOutboundVoiceContact_RequestSyntax"></a>

```
PUT /contact/outbound-voice HTTP/1.1
Content-type: application/json

{
   "AnswerMachineDetectionConfig": {
      "AwaitAnswerMachinePrompt": {{boolean}},
      "EnableAnswerMachineDetection": {{boolean}}
   },
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "CampaignId": "{{string}}",
   "ClientToken": "{{string}}",
   "ContactFlowId": "{{string}}",
   "Description": "{{string}}",
   "DestinationPhoneNumber": "{{string}}",
   "InstanceId": "{{string}}",
   "Name": "{{string}}",
   "OutboundStrategy": {
      "Config": {
         "AgentFirst": {
            "Preview": {
               "AllowedUserActions": [ "{{string}}" ],
               "PostAcceptTimeoutConfig": {
                  "DurationInSeconds": {{number}}
               }
            }
         }
      },
      "Type": "{{string}}"
   },
   "QueueId": "{{string}}",
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
   "RingTimeoutInSeconds": {{number}},
   "SourcePhoneNumber": "{{string}}",
   "TrafficType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartOutboundVoiceContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartOutboundVoiceContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AnswerMachineDetectionConfig](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-AnswerMachineDetectionConfig"></a>
Configuration of the answering machine detection for this outbound call.
Type: [AnswerMachineDetectionConfig](API_AnswerMachineDetectionConfig.md) object
Required: No

 ** [Attributes](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-Attributes"></a>
A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.
There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** [CampaignId](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-CampaignId"></a>
The campaign identifier of the outbound communication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [ClientToken](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/). The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactFlowId](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-ContactFlowId"></a>
The identifier of the flow for the outbound call. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to **Routing**, **Contact Flows**. Choose the flow. On the flow page, under the name of the flow, choose **Show additional flow information**. The ContactFlowId is the last part of the ARN, shown here in bold:
arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/**846ec553-a005-41c0-8341-xxxxxxxxxxxx**
Type: String
Length Constraints: Maximum length of 500.
Required: Yes

 ** [Description](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-Description"></a>
A description of the voice contact that appears in the agent's snapshot in the CCP logs. For more information about CCP logs, see [Download and review CCP logs](https://docs.aws.amazon.com/connect/latest/adminguide/download-ccp-logs.html) in the *Connect Customer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [DestinationPhoneNumber](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-DestinationPhoneNumber"></a>
The phone number of the customer, in E.164 format.
Type: String
Pattern: `\\+[1-9]\\d{1,14}$`
Required: Yes

 ** [InstanceId](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Name](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-Name"></a>
The name of a voice contact that is shown to an agent in the Contact Control Panel (CCP).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [OutboundStrategy](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-OutboundStrategy"></a>
Information about the outbound strategy.
Type: [OutboundStrategy](API_OutboundStrategy.md) object
Required: No

 ** [QueueId](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-QueueId"></a>
The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the flow is used. If you do not specify a queue, you must specify a source phone number.
Type: String
Required: No

 ** [References](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-References"></a>
A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Contacts can have the following reference types at the time of creation: `URL` \| `NUMBER` \| `STRING` \| `DATE` \| `EMAIL`. `ATTACHMENT` is not a supported reference type during voice contact creation.
Type: String to [Reference](API_Reference.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [RelatedContactId](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-RelatedContactId"></a>
The `contactId` that is related to this contact. Linking voice, task, or chat by using `RelatedContactID` copies over contact attributes from the related contact to the new contact. All updates to user-defined attributes in the new contact are limited to the individual contact ID. There are no limits to the number of contacts that can be linked by using `RelatedContactId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [RingTimeoutInSeconds](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-RingTimeoutInSeconds"></a>
The maximum time the outbound call will wait for the destination to answer the call, in seconds
Type: Integer
Valid Range: Minimum value of 15. Maximum value of 60.
Required: No

 ** [SourcePhoneNumber](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-SourcePhoneNumber"></a>
The phone number associated with the Connect Customer instance, in E.164 format. If you do not specify a source phone number, you must specify a queue.
Type: String
Pattern: `\\+[1-9]\\d{1,14}$`
Required: No

 ** [TrafficType](#API_StartOutboundVoiceContact_RequestSyntax) **   <a name="connect-StartOutboundVoiceContact-request-TrafficType"></a>
Denotes the class of traffic. Calls with different traffic types are handled differently by Connect Customer. The default value is `GENERAL`. Use `CAMPAIGN` if `EnableAnswerMachineDetection` is set to `true`. For all other cases, use `GENERAL`.
Type: String
Valid Values: `GENERAL | CAMPAIGN`
Required: No

## Response Syntax
<a name="API_StartOutboundVoiceContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactId": "string"
}
```

## Response Elements
<a name="API_StartOutboundVoiceContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactId](#API_StartOutboundVoiceContact_ResponseSyntax) **   <a name="connect-StartOutboundVoiceContact-response-ContactId"></a>
The identifier of this contact within the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_StartOutboundVoiceContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DestinationNotAllowedException **
Outbound calls to the destination number are not allowed.
 ** Message **
The message about the outbound calls.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** OutboundContactNotPermittedException **
The contact is not permitted.
 ** Message **
The message about the contact.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_StartOutboundVoiceContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartOutboundVoiceContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartOutboundVoiceContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartOutboundVoiceContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartOutboundVoiceContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartOutboundVoiceContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartOutboundVoiceContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartOutboundVoiceContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartOutboundVoiceContact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartOutboundVoiceContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartOutboundVoiceContact)

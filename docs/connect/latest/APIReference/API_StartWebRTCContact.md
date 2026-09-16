---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartWebRTCContact.html
---

# StartWebRTCContact
<a name="API_StartWebRTCContact"></a>

Places an inbound in-app, web, or video call to a contact, and then initiates the flow. It performs the actions in the flow that are specified (in ContactFlowId) and present in the Connect Customer instance (specified as InstanceId).

## Request Syntax
<a name="API_StartWebRTCContact_RequestSyntax"></a>

```
PUT /contact/webrtc HTTP/1.1
Content-type: application/json

{
   "AllowedCapabilities": {
      "Agent": {
         "ScreenShare": "{{string}}",
         "Video": "{{string}}"
      },
      "Customer": {
         "ScreenShare": "{{string}}",
         "Video": "{{string}}"
      }
   },
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "ClientToken": "{{string}}",
   "ContactFlowId": "{{string}}",
   "Description": "{{string}}",
   "InstanceId": "{{string}}",
   "ParticipantDetails": {
      "DisplayName": "{{string}}"
   },
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
<a name="API_StartWebRTCContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartWebRTCContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllowedCapabilities](#API_StartWebRTCContact_RequestSyntax) **   <a name="connect-StartWebRTCContact-request-AllowedCapabilities"></a>
Information about the video sharing capabilities of the participants (customer, agent).
Type: [AllowedCapabilities](API_AllowedCapabilities.md) object
Required: No

 ** [Attributes](#API_StartWebRTCContact_RequestSyntax) **   <a name="connect-StartWebRTCContact-request-Attributes"></a>
A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.
There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, -, and \_ characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** [ClientToken](#API_StartWebRTCContact_RequestSyntax) **   <a name="connect-StartWebRTCContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactFlowId](#API_StartWebRTCContact_RequestSyntax) **   <a name="connect-StartWebRTCContact-request-ContactFlowId"></a>
The identifier of the flow for the call. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to **Routing**, **Flows**. Choose the flow. On the flow page, under the name of the flow, choose **Show additional flow information**. The ContactFlowId is the last part of the ARN, shown here in bold:
arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/**846ec553-a005-41c0-8341-xxxxxxxxxxxx**
Type: String
Length Constraints: Maximum length of 500.
Required: Yes

 ** [Description](#API_StartWebRTCContact_RequestSyntax) **   <a name="connect-StartWebRTCContact-request-Description"></a>
A description of the task that is shown to an agent in the Contact Control Panel (CCP).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [InstanceId](#API_StartWebRTCContact_RequestSyntax) **   <a name="connect-StartWebRTCContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [ParticipantDetails](#API_StartWebRTCContact_RequestSyntax) **   <a name="connect-StartWebRTCContact-request-ParticipantDetails"></a>
The details of the participant, including their display name.
Type: [ParticipantDetails](API_ParticipantDetails.md) object
Required: Yes

 ** [References](#API_StartWebRTCContact_RequestSyntax) **   <a name="connect-StartWebRTCContact-request-References"></a>
A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Tasks can have the following reference types at the time of creation: `URL` \| `NUMBER` \| `STRING` \| `DATE` \| `EMAIL`. `ATTACHMENT` is not a supported reference type during task creation.
Type: String to [Reference](API_Reference.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [RelatedContactId](#API_StartWebRTCContact_RequestSyntax) **   <a name="connect-StartWebRTCContact-request-RelatedContactId"></a>
The unique identifier for an Connect Customer contact. This identifier is related to the contact starting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [SegmentAttributes](#API_StartWebRTCContact_RequestSyntax) **   <a name="connect-StartWebRTCContact-request-SegmentAttributes"></a>
A map of system-defined attributes for the WebRTC contact segment. Use the `connect:Subtype` attribute to specify the channel subtype, such as `connect:WebRTC`.
Type: String to [SegmentAttributeValue](API_SegmentAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## Response Syntax
<a name="API_StartWebRTCContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConnectionData": {
      "Attendee": {
         "AttendeeId": "string",
         "JoinToken": "string"
      },
      "Meeting": {
         "MediaPlacement": {
            "AudioFallbackUrl": "string",
            "AudioHostUrl": "string",
            "EventIngestionUrl": "string",
            "SignalingUrl": "string",
            "TurnControlUrl": "string"
         },
         "MediaRegion": "string",
         "MeetingFeatures": {
            "Audio": {
               "EchoReduction": "string"
            }
         },
         "MeetingId": "string"
      }
   },
   "ContactId": "string",
   "ParticipantId": "string",
   "ParticipantToken": "string"
}
```

## Response Elements
<a name="API_StartWebRTCContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectionData](#API_StartWebRTCContact_ResponseSyntax) **   <a name="connect-StartWebRTCContact-response-ConnectionData"></a>
Information required for the client application (mobile application or website) to connect to the call.
Type: [ConnectionData](API_ConnectionData.md) object

 ** [ContactId](#API_StartWebRTCContact_ResponseSyntax) **   <a name="connect-StartWebRTCContact-response-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ParticipantId](#API_StartWebRTCContact_ResponseSyntax) **   <a name="connect-StartWebRTCContact-response-ParticipantId"></a>
The identifier for a contact participant. The `ParticipantId` for a contact participant is the same throughout the contact lifecycle.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ParticipantToken](#API_StartWebRTCContact_ResponseSyntax) **   <a name="connect-StartWebRTCContact-response-ParticipantToken"></a>
The token used by the contact participant to call the [CreateParticipantConnection](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html) API. The participant token is valid for the lifetime of a contact participant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.

## Errors
<a name="API_StartWebRTCContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

## See Also
<a name="API_StartWebRTCContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartWebRTCContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartWebRTCContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartWebRTCContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartWebRTCContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartWebRTCContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartWebRTCContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartWebRTCContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartWebRTCContact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartWebRTCContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartWebRTCContact)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContact.html
---

# CreateContact
<a name="API_CreateContact"></a>

**Important**
Only the VOICE, EMAIL, and TASK channels are supported.
For VOICE: The supported initiation method is `TRANSFER`. The contacts created with this initiation method have a subtype `connect:ExternalAudio`.
For EMAIL: The supported initiation methods are `OUTBOUND`, `AGENT_REPLY`, and `FLOW`.
For TASK: The supported initiation method is `API`. Contacts created with this API have a sub-type of `connect:ExternalTask`.

Creates a new VOICE, EMAIL, or TASK contact.

After a contact is created, you can move it to the desired state by using the `InitiateAs` parameter. While you can use API to create task contacts that are in the `COMPLETED` state, you must contact AWS Support before using it for bulk import use cases. Bulk import causes your requests to be throttled or fail if your CreateContact limits aren't high enough.

## Request Syntax
<a name="API_CreateContact_RequestSyntax"></a>

```
PUT /contact/create-contact HTTP/1.1
Content-type: application/json

{
   "Attributes": {
      "{{string}}" : "{{string}}"
   },
   "Channel": "{{string}}",
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "ExpiryDurationInMinutes": {{number}},
   "InitiateAs": "{{string}}",
   "InitiationMethod": "{{string}}",
   "InstanceId": "{{string}}",
   "Name": "{{string}}",
   "PreviousContactId": "{{string}}",
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
   },
   "UserInfo": {
      "UserId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Attributes](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-Attributes"></a>
A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.
There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** [Channel](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-Channel"></a>
The channel for the contact.
The CHAT channel is not supported. The following information is incorrect. We're working to correct it.
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: Yes

 ** [ClientToken](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Description](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-Description"></a>
A description of the contact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [ExpiryDurationInMinutes](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-ExpiryDurationInMinutes"></a>
Number of minutes the contact will be active for before expiring
Type: Integer
Required: No

 ** [InitiateAs](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-InitiateAs"></a>
Initial state of the contact when it's created. Only TASK channel contacts can be initiated with `COMPLETED` state.
Type: String
Valid Values: `CONNECTED_TO_USER | COMPLETED`
Required: No

 ** [InitiationMethod](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-InitiationMethod"></a>
Indicates how the contact was initiated.
CreateContact only supports the following initiation methods. Valid values by channel are:
+ For VOICE: `TRANSFER` and the subtype `connect:ExternalAudio`
+ For EMAIL: `OUTBOUND` \| `AGENT_REPLY` \| `FLOW`
+ For TASK: `API`
The other channels listed below are incorrect. We're working to correct this information.
Type: String
Valid Values: `INBOUND | OUTBOUND | TRANSFER | QUEUE_TRANSFER | CALLBACK | API | DISCONNECT | MONITOR | EXTERNAL_OUTBOUND | WEBRTC_API | AGENT_REPLY | FLOW`
Required: Yes

 ** [InstanceId](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Name](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-Name"></a>
The name of a the contact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [PreviousContactId](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-PreviousContactId"></a>
The ID of the previous contact when creating a transfer contact. This value can be provided only for external audio contacts. For more information, see [Integrate Connect Customer Contact Lens with external voice systems](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html) in the *Connect Customer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [References](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-References"></a>
A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Tasks can have the following reference types at the time of creation: `URL` \| `NUMBER` \| `STRING` \| `DATE` \| `EMAIL` \| `ATTACHMENT`.
Type: String to [Reference](API_Reference.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [RelatedContactId](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-RelatedContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [SegmentAttributes](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-SegmentAttributes"></a>
A set of system defined key-value pairs stored on individual contact segments (unique contact ID) using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.
Attribute keys can include only alphanumeric, -, and \_.
This field can be used to set Segment Contact Expiry as a duration in minutes.
To set contact expiry, a ValueMap must be specified containing the integer number of minutes the contact will be active for before expiring, with `SegmentAttributes` like { ` "connect:ContactExpiry": {"ValueMap" : { "ExpiryDuration": { "ValueInteger": 135}}}}`.
Type: String to [SegmentAttributeValue](API_SegmentAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [UserInfo](#API_CreateContact_RequestSyntax) **   <a name="connect-CreateContact-request-UserInfo"></a>
User details for the contact
UserInfo is required when creating an EMAIL contact with `OUTBOUND` and `AGENT_REPLY` contact initiation methods.
Type: [UserInfo](API_UserInfo.md) object
Required: No

## Response Syntax
<a name="API_CreateContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactArn": "string",
   "ContactId": "string"
}
```

## Response Elements
<a name="API_CreateContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactArn](#API_CreateContact_ResponseSyntax) **   <a name="connect-CreateContact-response-ContactArn"></a>
The Amazon Resource Name (ARN) of the created contact.
Type: String

 ** [ContactId](#API_CreateContact_ResponseSyntax) **   <a name="connect-CreateContact-response-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Operation cannot be performed at this time as there is a conflict with another operation or contact state.
HTTP Status Code: 409

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

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
<a name="API_CreateContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateContact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_StartTaskContact.html
---

# StartTaskContact
<a name="API_StartTaskContact"></a>

Initiates a flow to start a new task contact. For more information about task contacts, see [Concepts: Tasks in Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/tasks.html) in the *Connect Customer Administrator Guide*.

When using `PreviousContactId` and `RelatedContactId` input parameters, note the following:
+  `PreviousContactId`
  + Any updates to user-defined task contact attributes on any contact linked through the same `PreviousContactId` will affect every contact in the chain.
  + There can be a maximum of 12 linked task contacts in a chain. That is, 12 task contacts can be created that share the same `PreviousContactId`.
+  `RelatedContactId`
  + Copies contact attributes from the related task contact to the new contact.
  + Any update on attributes in a new task contact does not update attributes on previous contact.
  + There’s no limit on the number of task contacts that can be created that use the same `RelatedContactId`.

In addition, when calling StartTaskContact include only one of these parameters: `ContactFlowID`, `QuickConnectID`, or `TaskTemplateID`. Only one parameter is required as long as the task template has a flow configured to run it. If more than one parameter is specified, or only the `TaskTemplateID` is specified but it does not have a flow configured, the request returns an error because Connect Customer cannot identify the unique flow to run when the task is created.

A `ServiceQuotaExceededException` occurs when the number of open tasks exceeds the active tasks quota or there are already 12 tasks referencing the same `PreviousContactId`. For more information about service quotas for task contacts, see [Connect Customer service quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_StartTaskContact_RequestSyntax"></a>

```
PUT /contact/task HTTP/1.1
Content-type: application/json

{
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
   "InstanceId": "{{string}}",
   "Name": "{{string}}",
   "PreviousContactId": "{{string}}",
   "QuickConnectId": "{{string}}",
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
   "ScheduledTime": {{number}},
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
   "TaskTemplateId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartTaskContact_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartTaskContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Attachments](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-Attachments"></a>
List of S3 presigned URLs of task attachments and their file name. You can have a maximum of 5 attachments per task.
Type: Array of [TaskAttachment](API_TaskAttachment.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [Attributes](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-Attributes"></a>
A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.
There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** [ClientToken](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [ContactFlowId](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-ContactFlowId"></a>
The identifier of the flow for initiating the tasks. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to **Routing**, **Flows**. Choose the flow. On the flow page, under the name of the flow, choose **Show additional flow information**. The ContactFlowId is the last part of the ARN, shown here in bold:
arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/**846ec553-a005-41c0-8341-xxxxxxxxxxxx**
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Description](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-Description"></a>
A description of the task that is shown to an agent in the Contact Control Panel (CCP).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [InstanceId](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [Name](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-Name"></a>
The name of a task that is shown to an agent in the Contact Control Panel (CCP).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** [PreviousContactId](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-PreviousContactId"></a>
The identifier of the previous chat, voice, or task contact. Any updates to user-defined attributes to task contacts linked using the same `PreviousContactID` will affect every contact in the chain. There can be a maximum of 12 linked task contacts in a chain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [QuickConnectId](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-QuickConnectId"></a>
The identifier for the quick connect. Tasks that are created by using `QuickConnectId` will use the flow that is defined on agent or queue quick connect. For more information about quick connects, see [Create quick connects](https://docs.aws.amazon.com/connect/latest/adminguide/quick-connects.html).
Type: String
Required: No

 ** [References](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-References"></a>
A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Tasks can have the following reference types at the time of creation: `URL` \| `NUMBER` \| `STRING` \| `DATE` \| `EMAIL`. `ATTACHMENT` is not a supported reference type during task creation.
Type: String to [Reference](API_Reference.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [RelatedContactId](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-RelatedContactId"></a>
The contactId that is [related](https://docs.aws.amazon.com/connect/latest/adminguide/tasks.html#linked-tasks) to this contact. Linking tasks together by using `RelatedContactID` copies over contact attributes from the related task contact to the new task contact. All updates to user-defined attributes in the new task contact are limited to the individual contact ID, unlike what happens when tasks are linked by using `PreviousContactID`. There are no limits to the number of contacts that can be linked by using `RelatedContactId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [ScheduledTime](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-ScheduledTime"></a>
The timestamp, in Unix Epoch seconds format, at which to start running the inbound flow. The scheduled time cannot be in the past. It must be within up to 6 days in future.
Type: Timestamp
Required: No

 ** [SegmentAttributes](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-SegmentAttributes"></a>
A set of system defined key-value pairs stored on individual contact segments (unique contact ID) using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.
Attribute keys can include only alphanumeric, -, and \_.
This field can be used to set Contact Expiry as a duration in minutes and set a UserId for the User who created a task.
To set contact expiry, a ValueMap must be specified containing the integer number of minutes the contact will be active for before expiring, with `SegmentAttributes` like { ` "connect:ContactExpiry": {"ValueMap" : { "ExpiryDuration": { "ValueInteger": 135}}}}`.
To set the created by user, a valid AgentResourceId must be supplied, with `SegmentAttributes` like { `"connect:CreatedByUser" { "ValueString": "arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/agent/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}}}`.
Type: String to [SegmentAttributeValue](API_SegmentAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [TaskTemplateId](#API_StartTaskContact_RequestSyntax) **   <a name="connect-StartTaskContact-request-TaskTemplateId"></a>
A unique identifier for the task template. For more information about task templates, see [Create task templates](https://docs.aws.amazon.com/connect/latest/adminguide/task-templates.html) in the *Connect Customer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## Response Syntax
<a name="API_StartTaskContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactId": "string"
}
```

## Response Elements
<a name="API_StartTaskContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactId](#API_StartTaskContact_ResponseSyntax) **   <a name="connect-StartTaskContact-response-ContactId"></a>
The identifier of this contact within the Connect Customer instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_StartTaskContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_StartTaskContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/StartTaskContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/StartTaskContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/StartTaskContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/StartTaskContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/StartTaskContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/StartTaskContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/StartTaskContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/StartTaskContact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/StartTaskContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/StartTaskContact)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContact.html
---

# UpdateContact
<a name="API_UpdateContact"></a>

This API is in preview release for Connect Customer and is subject to change.

Adds or updates user-defined contact information associated with the specified contact. At least one field to be updated must be present in the request.

**Important**
You can add or update user-defined contact information for both ongoing and completed contacts.

## Request Syntax
<a name="API_UpdateContact_RequestSyntax"></a>

```
POST /contacts/{{InstanceId}}/{{ContactId}} HTTP/1.1
Content-type: application/json

{
   "CustomerEndpoint": {
      "Address": "{{string}}",
      "Type": "{{string}}"
   },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "QueueInfo": {
      "Id": "{{string}}"
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
   "SystemEndpoint": {
      "Address": "{{string}}",
      "Type": "{{string}}"
   },
   "UserInfo": {
      "UserId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateContact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactId](#API_UpdateContact_RequestSyntax) **   <a name="connect-UpdateContact-request-uri-ContactId"></a>
The identifier of the contact. This is the identifier of the contact associated with the first interaction with your contact center.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateContact_RequestSyntax) **   <a name="connect-UpdateContact-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateContact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CustomerEndpoint](#API_UpdateContact_RequestSyntax) **   <a name="connect-UpdateContact-request-CustomerEndpoint"></a>
The endpoint of the customer for which the contact was initiated. For external audio contacts, this is usually the end customer's phone number. This value can only be updated for external audio contacts. For more information, see [Connect Customer Contact Lens integration](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html) in the *Connect Customer Administrator Guide*.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** [Description](#API_UpdateContact_RequestSyntax) **   <a name="connect-UpdateContact-request-Description"></a>
The description of the contact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [Name](#API_UpdateContact_RequestSyntax) **   <a name="connect-UpdateContact-request-Name"></a>
The name of the contact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [QueueInfo](#API_UpdateContact_RequestSyntax) **   <a name="connect-UpdateContact-request-QueueInfo"></a>
 Information about the queue associated with a contact. This parameter can only be updated for external audio contacts. It is used when you integrate third-party systems with Contact Lens for analytics. For more information, see [Connect Customer Contact Lens integration](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html) in the * Connect Customer Administrator Guide*.
Type: [QueueInfoInput](API_QueueInfoInput.md) object
Required: No

 ** [References](#API_UpdateContact_RequestSyntax) **   <a name="connect-UpdateContact-request-References"></a>
Well-formed data on contact, shown to agents on Contact Control Panel (CCP).
Type: String to [Reference](API_Reference.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [SegmentAttributes](#API_UpdateContact_RequestSyntax) **   <a name="connect-UpdateContact-request-SegmentAttributes"></a>
A set of system defined key-value pairs stored on individual contact segments (unique contact ID) using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.
Attribute keys can include only alphanumeric, -, and \_.
This field can be used to show channel subtype, such as `connect:Guide`.
Contact Expiry, and user-defined attributes (String - String) that are defined in predefined attributes, can be updated by using the UpdateContact API.
Type: String to [SegmentAttributeValue](API_SegmentAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [SystemEndpoint](#API_UpdateContact_RequestSyntax) **   <a name="connect-UpdateContact-request-SystemEndpoint"></a>
External system endpoint for the contact was initiated. For external audio contacts, this is the phone number of the external system such as the contact center. This value can only be updated for external audio contacts. For more information, see [Connect Customer Contact Lens integration](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html) in the *Connect Customer Administrator Guide*.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** [UserInfo](#API_UpdateContact_RequestSyntax) **   <a name="connect-UpdateContact-request-UserInfo"></a>
Information about the agent associated with a contact. This parameter can only be updated for external audio contacts. It is used when you integrate third-party systems with Contact Lens for analytics. For more information, see [Connect Customer Contact Lens integration](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html) in the * Connect Customer Administrator Guide*.
Type: [UserInfo](API_UserInfo.md) object
Required: No

## Response Syntax
<a name="API_UpdateContact_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Operation cannot be performed at this time as there is a conflict with another operation or contact state.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidActiveRegionException **
This exception occurs when an API request is made to a non-active region in an Amazon Connect instance configured with Amazon Connect Global Resiliency. For example, if the active region is US West (Oregon) and a request is made to US East (N. Virginia), the exception will be returned.
HTTP Status Code: 400

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateContact)

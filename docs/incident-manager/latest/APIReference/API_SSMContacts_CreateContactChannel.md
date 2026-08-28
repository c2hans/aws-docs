---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_CreateContactChannel.html
---

# CreateContactChannel
<a name="API_SSMContacts_CreateContactChannel"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

A contact channel is the method that Incident Manager uses to engage your contact.

## Request Syntax
<a name="API_SSMContacts_CreateContactChannel_RequestSyntax"></a>

```
{
   "ContactId": "{{string}}",
   "DeferActivation": {{boolean}},
   "DeliveryAddress": {
      "SimpleAddress": "{{string}}"
   },
   "IdempotencyToken": "{{string}}",
   "Name": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_CreateContactChannel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactId](#API_SSMContacts_CreateContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContactChannel-request-ContactId"></a>
The Amazon Resource Name (ARN) of the contact you are adding the contact channel to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [DeferActivation](#API_SSMContacts_CreateContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContactChannel-request-DeferActivation"></a>
If you want to activate the channel at a later time, you can choose to defer activation. Incident Manager can't engage your contact channel until it has been activated.
Type: Boolean
Required: No

 ** [DeliveryAddress](#API_SSMContacts_CreateContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContactChannel-request-DeliveryAddress"></a>
The details that Incident Manager uses when trying to engage the contact channel. The format is dependent on the type of the contact channel. The following are the expected formats:
+ SMS - '\+' followed by the country code and phone number
+ VOICE - '\+' followed by the country code and phone number
+ EMAIL - any standard email format
Type: [ContactChannelAddress](API_SSMContacts_ContactChannelAddress.md) object
Required: Yes

 ** [IdempotencyToken](#API_SSMContacts_CreateContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContactChannel-request-IdempotencyToken"></a>
A token ensuring that the operation is called only once with the specified details.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [Name](#API_SSMContacts_CreateContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContactChannel-request-Name"></a>
The name of the contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\p{L}\p{Z}\p{N}_.\-]*$`
Required: Yes

 ** [Type](#API_SSMContacts_CreateContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContactChannel-request-Type"></a>
Incident Manager supports three types of contact channels:
+  `SMS`
+  `VOICE`
+  `EMAIL`
Type: String
Valid Values: `SMS | VOICE | EMAIL`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_CreateContactChannel_ResponseSyntax"></a>

```
{
   "ContactChannelArn": "string"
}
```

## Response Elements
<a name="API_SSMContacts_CreateContactChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactChannelArn](#API_SSMContacts_CreateContactChannel_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_CreateContactChannel-response-ContactChannelArn"></a>
The Amazon Resource Name (ARN) of the contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

## Errors
<a name="API_SSMContacts_CreateContactChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 400

 ** ConflictException **
Updating or deleting a resource causes an inconsistent state.
HTTP Status Code: 400

 ** DataEncryptionException **
The operation failed to due an encryption key error.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_SSMContacts_CreateContactChannel_Examples"></a>

### Example
<a name="API_SSMContacts_CreateContactChannel_Example_1"></a>

This example illustrates one usage of CreateContactChannel.

#### Sample Request
<a name="API_SSMContacts_CreateContactChannel_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.CreateContactChannel
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.create-contact-channel
X-Amz-Date: 20220812T174315Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220812/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 229

{
	"ContactId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam",
	"Name": "akuas sms-test",
	"Type": "SMS",
	"DeliveryAddress": {"SimpleAddress": "+15005550199"},
	"IdempotencyToken": "922b8f50-9bb9-4dd7-83cf-a4c25EXAMPLE"
}
```

#### Sample Response
<a name="API_SSMContacts_CreateContactChannel_Example_1_Response"></a>

```
{
    "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE"
}
```

## See Also
<a name="API_SSMContacts_CreateContactChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/CreateContactChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/CreateContactChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/CreateContactChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/CreateContactChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/CreateContactChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/CreateContactChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/CreateContactChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/CreateContactChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/CreateContactChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/CreateContactChannel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_UpdateContactChannel.html
---

# UpdateContactChannel
<a name="API_SSMContacts_UpdateContactChannel"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Updates a contact's contact channel.

## Request Syntax
<a name="API_SSMContacts_UpdateContactChannel_RequestSyntax"></a>

```
{
   "ContactChannelId": "{{string}}",
   "DeliveryAddress": {
      "SimpleAddress": "{{string}}"
   },
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_UpdateContactChannel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactChannelId](#API_SSMContacts_UpdateContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateContactChannel-request-ContactChannelId"></a>
The Amazon Resource Name (ARN) of the contact channel you want to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [DeliveryAddress](#API_SSMContacts_UpdateContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateContactChannel-request-DeliveryAddress"></a>
The details that Incident Manager uses when trying to engage the contact channel.
Type: [ContactChannelAddress](API_SSMContacts_ContactChannelAddress.md) object
Required: No

 ** [Name](#API_SSMContacts_UpdateContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateContactChannel-request-Name"></a>
The name of the contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\p{L}\p{Z}\p{N}_.\-]*$`
Required: No

## Response Elements
<a name="API_SSMContacts_UpdateContactChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SSMContacts_UpdateContactChannel_Errors"></a>

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

 ** ResourceNotFoundException **
Request references a resource that doesn't exist.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_SSMContacts_UpdateContactChannel_Examples"></a>

### Example
<a name="API_SSMContacts_UpdateContactChannel_Example_1"></a>

This example illustrates one usage of UpdateContactChannel.

#### Sample Request
<a name="API_SSMContacts_UpdateContactChannel_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.UpdateContactChannel
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.update-contact-channel
X-Amz-Date: 20220812T182356Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220812/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 211

{
	"ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE",
	"Name": "akuas voice channel",
	"DeliveryAddress": {
		"SimpleAddress": "+15005550198"
	}
}
```

#### Sample Response
<a name="API_SSMContacts_UpdateContactChannel_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_SSMContacts_UpdateContactChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/UpdateContactChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/UpdateContactChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/UpdateContactChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/UpdateContactChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/UpdateContactChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/UpdateContactChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/UpdateContactChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/UpdateContactChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/UpdateContactChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/UpdateContactChannel)

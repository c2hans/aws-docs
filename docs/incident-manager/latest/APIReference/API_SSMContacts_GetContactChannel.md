---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_GetContactChannel.html
---

# GetContactChannel
<a name="API_SSMContacts_GetContactChannel"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

List details about a specific contact channel.

## Request Syntax
<a name="API_SSMContacts_GetContactChannel_RequestSyntax"></a>

```
{
   "ContactChannelId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_GetContactChannel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactChannelId](#API_SSMContacts_GetContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_GetContactChannel-request-ContactChannelId"></a>
The Amazon Resource Name (ARN) of the contact channel you want information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_GetContactChannel_ResponseSyntax"></a>

```
{
   "ActivationStatus": "string",
   "ContactArn": "string",
   "ContactChannelArn": "string",
   "DeliveryAddress": {
      "SimpleAddress": "string"
   },
   "Name": "string",
   "Type": "string"
}
```

## Response Elements
<a name="API_SSMContacts_GetContactChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActivationStatus](#API_SSMContacts_GetContactChannel_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetContactChannel-response-ActivationStatus"></a>
A Boolean value indicating if the contact channel has been activated or not.
Type: String
Valid Values: `ACTIVATED | NOT_ACTIVATED`

 ** [ContactArn](#API_SSMContacts_GetContactChannel_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetContactChannel-response-ContactArn"></a>
The ARN of the contact that the channel belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [ContactChannelArn](#API_SSMContacts_GetContactChannel_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetContactChannel-response-ContactChannelArn"></a>
The ARN of the contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [DeliveryAddress](#API_SSMContacts_GetContactChannel_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetContactChannel-response-DeliveryAddress"></a>
The details that Incident Manager uses when trying to engage the contact channel.
Type: [ContactChannelAddress](API_SSMContacts_ContactChannelAddress.md) object

 ** [Name](#API_SSMContacts_GetContactChannel_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetContactChannel-response-Name"></a>
The name of the contact channel
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\p{L}\p{Z}\p{N}_.\-]*$`

 ** [Type](#API_SSMContacts_GetContactChannel_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetContactChannel-response-Type"></a>
The type of contact channel. The type is `SMS`, `VOICE`, or `EMAIL`.
Type: String
Valid Values: `SMS | VOICE | EMAIL`

## Errors
<a name="API_SSMContacts_GetContactChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
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
<a name="API_SSMContacts_GetContactChannel_Examples"></a>

### Example
<a name="API_SSMContacts_GetContactChannel_Example_1"></a>

This example illustrates one usage of GetContactChannel.

#### Sample Request
<a name="API_SSMContacts_GetContactChannel_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.GetContactChannel
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.get-contact-channel
X-Amz-Date: 20220816T211314Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220816/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 126

{
	"ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE"
}
```

#### Sample Response
<a name="API_SSMContacts_GetContactChannel_Example_1_Response"></a>

```
{
    "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam",
    "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE",
    "Name": "akuas voice channel",
    "Type": "SMS",
    "DeliveryAddress": {
        "SimpleAddress": "+15005550199"
    },
    "ActivationStatus": "ACTIVATED"
}
```

## See Also
<a name="API_SSMContacts_GetContactChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/GetContactChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/GetContactChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/GetContactChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/GetContactChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/GetContactChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/GetContactChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/GetContactChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/GetContactChannel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/GetContactChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/GetContactChannel)

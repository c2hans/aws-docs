---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DeactivateContactChannel.html
---

# DeactivateContactChannel
<a name="API_SSMContacts_DeactivateContactChannel"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

To no longer receive Incident Manager engagements to a contact channel, you can deactivate the channel.

## Request Syntax
<a name="API_SSMContacts_DeactivateContactChannel_RequestSyntax"></a>

```
{
   "ContactChannelId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_DeactivateContactChannel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactChannelId](#API_SSMContacts_DeactivateContactChannel_RequestSyntax) **   <a name="IncidentManager-SSMContacts_DeactivateContactChannel-request-ContactChannelId"></a>
The Amazon Resource Name (ARN) of the contact channel you're deactivating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

## Response Elements
<a name="API_SSMContacts_DeactivateContactChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SSMContacts_DeactivateContactChannel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
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
<a name="API_SSMContacts_DeactivateContactChannel_Examples"></a>

### Example
<a name="API_SSMContacts_DeactivateContactChannel_Example_1"></a>

This example illustrates one usage of DeactivateContactChannel.

#### Sample Request
<a name="API_SSMContacts_DeactivateContactChannel_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.DeactivateContactChannel
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.deactivate-contact-channel
X-Amz-Date: 20220817T184424Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220817/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 126

{
	"ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE"
}
```

#### Sample Response
<a name="API_SSMContacts_DeactivateContactChannel_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_SSMContacts_DeactivateContactChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/DeactivateContactChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/DeactivateContactChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/DeactivateContactChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/DeactivateContactChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/DeactivateContactChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/DeactivateContactChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/DeactivateContactChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/DeactivateContactChannel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/DeactivateContactChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/DeactivateContactChannel)

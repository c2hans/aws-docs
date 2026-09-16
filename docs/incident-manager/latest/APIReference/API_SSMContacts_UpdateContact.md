---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_UpdateContact.html
---

# UpdateContact
<a name="API_SSMContacts_UpdateContact"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Updates the contact or escalation plan specified.

## Request Syntax
<a name="API_SSMContacts_UpdateContact_RequestSyntax"></a>

```
{
   "ContactId": "{{string}}",
   "DisplayName": "{{string}}",
   "Plan": {
      "RotationIds": [ "{{string}}" ],
      "Stages": [
         {
            "DurationInMinutes": {{number}},
            "Targets": [
               {
                  "ChannelTargetInfo": {
                     "ContactChannelId": "{{string}}",
                     "RetryIntervalInMinutes": {{number}}
                  },
                  "ContactTargetInfo": {
                     "ContactId": "{{string}}",
                     "IsEssential": {{boolean}}
                  }
               }
            ]
         }
      ]
   }
}
```

## Request Parameters
<a name="API_SSMContacts_UpdateContact_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactId](#API_SSMContacts_UpdateContact_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateContact-request-ContactId"></a>
The Amazon Resource Name (ARN) of the contact or escalation plan you're updating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [DisplayName](#API_SSMContacts_UpdateContact_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateContact-request-DisplayName"></a>
The full name of the contact or escalation plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^[\p{L}\p{Z}\p{N}_.\-]*$`
Required: No

 ** [Plan](#API_SSMContacts_UpdateContact_RequestSyntax) **   <a name="IncidentManager-SSMContacts_UpdateContact-request-Plan"></a>
A list of stages. A contact has an engagement plan with stages for specified contact channels. An escalation plan uses these stages to contact specified contacts.
Type: [Plan](API_SSMContacts_Plan.md) object
Required: No

## Response Elements
<a name="API_SSMContacts_UpdateContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SSMContacts_UpdateContact_Errors"></a>

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

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_SSMContacts_UpdateContact_Examples"></a>

### Example
<a name="API_SSMContacts_UpdateContact_Example_1"></a>

This example illustrates one usage of UpdateContact.

#### Sample Request
<a name="API_SSMContacts_UpdateContact_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.UpdateContact
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.update-contact
X-Amz-Date: 20220812T181127Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220812/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 534

{
	"ContactId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam",
	"Plan": {
		"Stages": [
			{
				"DurationInMinutes": 5,
				"Targets": [
					{
						"ChannelTargetInfo": {
							"ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/31111aa5-9b84-4591-a5a6-5a8f9EXAMPLE",
							"RetryIntervalInMinutes": 1
						}
					}
				]
			},
			{
				"DurationInMinutes": 5,
				"Targets": [
					{
						"ChannelTargetInfo": {
							"ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/e5bd2c57-406a-487f-8d26-7c032EXAMPLE",
							"RetryIntervalInMinutes": 1
						}
					}
				]
			}
		]
	}
}
```

#### Sample Response
<a name="API_SSMContacts_UpdateContact_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_SSMContacts_UpdateContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/UpdateContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/UpdateContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/UpdateContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/UpdateContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/UpdateContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/UpdateContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/UpdateContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/UpdateContact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/UpdateContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/UpdateContact)

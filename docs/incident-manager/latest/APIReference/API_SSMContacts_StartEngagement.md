---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_StartEngagement.html
---

# StartEngagement
<a name="API_SSMContacts_StartEngagement"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Starts an engagement to a contact or escalation plan. The engagement engages each contact specified in the incident.

## Request Syntax
<a name="API_SSMContacts_StartEngagement_RequestSyntax"></a>

```
{
   "ContactId": "{{string}}",
   "Content": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "IncidentId": "{{string}}",
   "PublicContent": "{{string}}",
   "PublicSubject": "{{string}}",
   "Sender": "{{string}}",
   "Subject": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_StartEngagement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactId](#API_SSMContacts_StartEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_StartEngagement-request-ContactId"></a>
The Amazon Resource Name (ARN) of the contact being engaged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [Content](#API_SSMContacts_StartEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_StartEngagement-request-Content"></a>
The secure content of the message that was sent to the contact. Use this field for engagements to `VOICE` or `EMAIL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[.\s\S]*$`
Required: Yes

 ** [IdempotencyToken](#API_SSMContacts_StartEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_StartEngagement-request-IdempotencyToken"></a>
A token ensuring that the operation is called only once with the specified details.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [IncidentId](#API_SSMContacts_StartEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_StartEngagement-request-IncidentId"></a>
The ARN of the incident that the engagement is part of.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`
Required: No

 ** [PublicContent](#API_SSMContacts_StartEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_StartEngagement-request-PublicContent"></a>
The insecure content of the message that was sent to the contact. Use this field for engagements to `SMS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[.\s\S]*$`
Required: No

 ** [PublicSubject](#API_SSMContacts_StartEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_StartEngagement-request-PublicSubject"></a>
The insecure subject of the message that was sent to the contact. Use this field for engagements to `SMS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[.\s\S]*$`
Required: No

 ** [Sender](#API_SSMContacts_StartEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_StartEngagement-request-Sender"></a>
The user that started the engagement.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`
Required: Yes

 ** [Subject](#API_SSMContacts_StartEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_StartEngagement-request-Subject"></a>
The secure subject of the message that was sent to the contact. Use this field for engagements to `VOICE` or `EMAIL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[.\s\S]*$`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_StartEngagement_ResponseSyntax"></a>

```
{
   "EngagementArn": "string"
}
```

## Response Elements
<a name="API_SSMContacts_StartEngagement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EngagementArn](#API_SSMContacts_StartEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_StartEngagement-response-EngagementArn"></a>
The ARN of the engagement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

## Errors
<a name="API_SSMContacts_StartEngagement_Errors"></a>

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
<a name="API_SSMContacts_StartEngagement_Examples"></a>

### Example
<a name="API_SSMContacts_StartEngagement_Example_1"></a>

This example illustrates one usage of StartEngagement.

#### Sample Request
<a name="API_SSMContacts_StartEngagement_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.StartEngagement
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.start-engagement
X-Amz-Date: 20220816T184849Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220816/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 307

{
	"ContactId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/test_escalation_plan",
	"Sender": "cli",
	"Subject": "cli-test",
	"Content": "Testing engagements via CLI",
	"PublicSubject": "cli-test",
	"PublicContent": "Testing engagements via CLI",
	"IdempotencyToken": "23a2a9b9-f63b-49b1-80c6-b21dfEXAMPLE"
}
```

#### Sample Response
<a name="API_SSMContacts_StartEngagement_Example_1_Response"></a>

```
{
    "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/test_escalation_plan/27bd86cf-6d50-49d2-a9ab-da39bEXAMPLE"
}
```

## See Also
<a name="API_SSMContacts_StartEngagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/StartEngagement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/StartEngagement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/StartEngagement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/StartEngagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/StartEngagement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/StartEngagement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/StartEngagement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/StartEngagement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/StartEngagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/StartEngagement)

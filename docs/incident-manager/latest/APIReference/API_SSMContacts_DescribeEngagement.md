---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DescribeEngagement.html
---

# DescribeEngagement
<a name="API_SSMContacts_DescribeEngagement"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Incident Manager uses engagements to engage contacts and escalation plans during an incident. Use this command to describe the engagement that occurred during an incident.

## Request Syntax
<a name="API_SSMContacts_DescribeEngagement_RequestSyntax"></a>

```
{
   "EngagementId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_DescribeEngagement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EngagementId](#API_SSMContacts_DescribeEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-request-EngagementId"></a>
The Amazon Resource Name (ARN) of the engagement you want the details of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_DescribeEngagement_ResponseSyntax"></a>

```
{
   "ContactArn": "string",
   "Content": "string",
   "EngagementArn": "string",
   "IncidentId": "string",
   "PublicContent": "string",
   "PublicSubject": "string",
   "Sender": "string",
   "StartTime": number,
   "StopTime": number,
   "Subject": "string"
}
```

## Response Elements
<a name="API_SSMContacts_DescribeEngagement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactArn](#API_SSMContacts_DescribeEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-response-ContactArn"></a>
The ARN of the escalation plan or contacts involved in the engagement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [Content](#API_SSMContacts_DescribeEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-response-Content"></a>
The secure content of the message that was sent to the contact. Use this field for engagements to `VOICE` and `EMAIL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[.\s\S]*$`

 ** [EngagementArn](#API_SSMContacts_DescribeEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-response-EngagementArn"></a>
The ARN of the engagement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [IncidentId](#API_SSMContacts_DescribeEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-response-IncidentId"></a>
The ARN of the incident in which the engagement occurred.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`

 ** [PublicContent](#API_SSMContacts_DescribeEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-response-PublicContent"></a>
The insecure content of the message that was sent to the contact. Use this field for engagements to `SMS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[.\s\S]*$`

 ** [PublicSubject](#API_SSMContacts_DescribeEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-response-PublicSubject"></a>
The insecure subject of the message that was sent to the contact. Use this field for engagements to `SMS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[.\s\S]*$`

 ** [Sender](#API_SSMContacts_DescribeEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-response-Sender"></a>
The user that started the engagement.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`

 ** [StartTime](#API_SSMContacts_DescribeEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-response-StartTime"></a>
The time that the engagement started.
Type: Timestamp

 ** [StopTime](#API_SSMContacts_DescribeEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-response-StopTime"></a>
The time that the engagement ended.
Type: Timestamp

 ** [Subject](#API_SSMContacts_DescribeEngagement_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribeEngagement-response-Subject"></a>
The secure subject of the message that was sent to the contact. Use this field for engagements to `VOICE` and `EMAIL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[.\s\S]*$`

## Errors
<a name="API_SSMContacts_DescribeEngagement_Errors"></a>

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
<a name="API_SSMContacts_DescribeEngagement_Examples"></a>

### Example
<a name="API_SSMContacts_DescribeEngagement_Example_1"></a>

This example illustrates one usage of DescribeEngagement.

#### Sample Request
<a name="API_SSMContacts_DescribeEngagement_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.DescribeEngagement
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.describe-engagement
X-Amz-Date: 20220816T192348Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220816/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 132

{
	"EngagementId": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/test_escalation_plan/27bd86cf-6d50-49d2-a9ab-da39bEXAMPLE"
}
```

#### Sample Response
<a name="API_SSMContacts_DescribeEngagement_Example_1_Response"></a>

```
{
    "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/test_escalation_plan",
    "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/test_escalation_plan/27bd86cf-6d50-49d2-a9ab-da39bEXAMPLE",
    "Sender": "cli",
    "Subject": "cli-test",
    "Content": "Testing engagements via CLI",
    "PublicSubject": "cli-test",
    "PublicContent": "Testing engagements via CLI",
    "StartTime": "2022-08-16T18:48:50.153000+00:00"
}
```

## See Also
<a name="API_SSMContacts_DescribeEngagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/DescribeEngagement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/DescribeEngagement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/DescribeEngagement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/DescribeEngagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/DescribeEngagement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/DescribeEngagement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/DescribeEngagement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/DescribeEngagement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/DescribeEngagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/DescribeEngagement)

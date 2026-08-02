---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DescribePage.html
---

# DescribePage
<a name="API_SSMContacts_DescribePage"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Lists details of the engagement to a contact channel.

## Request Syntax
<a name="API_SSMContacts_DescribePage_RequestSyntax"></a>

```
{
   "PageId": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_DescribePage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PageId](#API_SSMContacts_DescribePage_RequestSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-request-PageId"></a>
The ID of the engagement to a contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_DescribePage_ResponseSyntax"></a>

```
{
   "ContactArn": "string",
   "Content": "string",
   "DeliveryTime": number,
   "EngagementArn": "string",
   "IncidentId": "string",
   "PageArn": "string",
   "PublicContent": "string",
   "PublicSubject": "string",
   "ReadTime": number,
   "Sender": "string",
   "SentTime": number,
   "Subject": "string"
}
```

## Response Elements
<a name="API_SSMContacts_DescribePage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactArn](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-ContactArn"></a>
The ARN of the contact that was engaged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [Content](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-Content"></a>
The secure content of the message that was sent to the contact. Use this field for engagements to `VOICE` and `EMAIL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[.\s\S]*$`

 ** [DeliveryTime](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-DeliveryTime"></a>
The time that the contact channel received the engagement.
Type: Timestamp

 ** [EngagementArn](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-EngagementArn"></a>
The ARN of the engagement that engaged the contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [IncidentId](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-IncidentId"></a>
The ARN of the incident that engaged the contact channel.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`

 ** [PageArn](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-PageArn"></a>
The Amazon Resource Name (ARN) of the engagement to a contact channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [PublicContent](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-PublicContent"></a>
The insecure content of the message that was sent to the contact. Use this field for engagements to `SMS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `^[.\s\S]*$`

 ** [PublicSubject](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-PublicSubject"></a>
The insecure subject of the message that was sent to the contact. Use this field for engagements to `SMS`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[.\s\S]*$`

 ** [ReadTime](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-ReadTime"></a>
The time that the contact channel acknowledged the engagement.
Type: Timestamp

 ** [Sender](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-Sender"></a>
The user that started the engagement.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[\\a-zA-Z0-9_@#%*+=:?.\/!\s-]*$`

 ** [SentTime](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-SentTime"></a>
The time the engagement was sent to the contact channel.
Type: Timestamp

 ** [Subject](#API_SSMContacts_DescribePage_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_DescribePage-response-Subject"></a>
The secure subject of the message that was sent to the contact. Use this field for engagements to `VOICE` and `EMAIL`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[.\s\S]*$`

## Errors
<a name="API_SSMContacts_DescribePage_Errors"></a>

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
<a name="API_SSMContacts_DescribePage_Examples"></a>

### Example
<a name="API_SSMContacts_DescribePage_Example_1"></a>

This example illustrates one usage of DescribePage.

#### Sample Request
<a name="API_SSMContacts_DescribePage_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.DescribePage
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.describe-page
X-Amz-Date: 20220816T193722Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220816/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 105

{
	"PageId": "arn:aws:ssm-contacts:us-east-2:111122223333:page/akuam/2f92b456-2350-442b-95e7-ed8b0EXAMPLE"
}
```

#### Sample Response
<a name="API_SSMContacts_DescribePage_Example_1_Response"></a>

```
{
    "PageArn": "arn:aws:ssm-contacts:us-east-2:111122223333:page/akuam/2f92b456-2350-442b-95e7-ed8b0EXAMPLE",
    "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/akuam/27bd86cf-6d50-49d2-a9ab-da39bEXAMPLE",
    "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam",
    "Sender": "cli",
    "Subject": "cli-test",
    "Content": "Testing engagements via CLI",
    "PublicSubject": "cli-test",
    "PublicContent": "Testing engagements via CLI",
    "SentTime": "2022-08-16T18:57:52.058000+00:00",
    "ReadTime": "2022-08-16T19:11:58.746000+00:00"
}
```

## See Also
<a name="API_SSMContacts_DescribePage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/DescribePage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/DescribePage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/DescribePage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/DescribePage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/DescribePage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/DescribePage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/DescribePage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/DescribePage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/DescribePage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/DescribePage)

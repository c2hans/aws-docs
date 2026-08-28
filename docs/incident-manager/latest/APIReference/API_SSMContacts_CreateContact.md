---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_CreateContact.html
---

# CreateContact
<a name="API_SSMContacts_CreateContact"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Contacts are either the contacts that Incident Manager engages during an incident or the escalation plans that Incident Manager uses to engage contacts in phases during an incident.

## Request Syntax
<a name="API_SSMContacts_CreateContact_RequestSyntax"></a>

```
{
   "Alias": "{{string}}",
   "DisplayName": "{{string}}",
   "IdempotencyToken": "{{string}}",
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
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_CreateContact_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Alias](#API_SSMContacts_CreateContact_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContact-request-Alias"></a>
The short name to quickly identify a contact or escalation plan. The contact alias must be unique and identifiable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-z0-9_\-]*$`
Required: Yes

 ** [DisplayName](#API_SSMContacts_CreateContact_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContact-request-DisplayName"></a>
The full name of the contact or escalation plan.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^[\p{L}\p{Z}\p{N}_.\-]*$`
Required: No

 ** [IdempotencyToken](#API_SSMContacts_CreateContact_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContact-request-IdempotencyToken"></a>
A token ensuring that the operation is called only once with the specified details.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^[\\\/a-zA-Z0-9_+=\-]*$`
Required: No

 ** [Plan](#API_SSMContacts_CreateContact_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContact-request-Plan"></a>
A list of stages. A contact has an engagement plan with stages that contact specified contact channels. An escalation plan uses stages that contact specified contacts.
Type: [Plan](API_SSMContacts_Plan.md) object
Required: Yes

 ** [Tags](#API_SSMContacts_CreateContact_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContact-request-Tags"></a>
Adds a tag to the target. You can only tag resources created in the first Region of your replication set.
Type: Array of [Tag](API_SSMContacts_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [Type](#API_SSMContacts_CreateContact_RequestSyntax) **   <a name="IncidentManager-SSMContacts_CreateContact-request-Type"></a>
The type of contact to create.
+  `PERSONAL`: A single, individual contact.
+  `ESCALATION`: An escalation plan.
+  `ONCALL_SCHEDULE`: An on-call schedule.
Type: String
Valid Values: `PERSONAL | ESCALATION | ONCALL_SCHEDULE`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_CreateContact_ResponseSyntax"></a>

```
{
   "ContactArn": "string"
}
```

## Response Elements
<a name="API_SSMContacts_CreateContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactArn](#API_SSMContacts_CreateContact_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_CreateContact-response-ContactArn"></a>
The Amazon Resource Name (ARN) of the created contact or escalation plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

## Errors
<a name="API_SSMContacts_CreateContact_Errors"></a>

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
<a name="API_SSMContacts_CreateContact_Examples"></a>

### Example
<a name="API_SSMContacts_CreateContact_Example_1"></a>

This example illustrates one usage of CreateContact.

#### Sample Request
<a name="API_SSMContacts_CreateContact_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.CreateContact
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.create-contact
X-Amz-Date: 20220812T172928Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220812/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=AKIAIOSFODNN7EXAMPLE
Content-Length: 151

{
	"Alias": "akuam",
	"DisplayName": "Akua Mansa",
	"Type": "PERSONAL",
	"Plan": {
		"Stages": []
	},
	"IdempotencyToken": "5b03013e-6255-404c-a673-1aa10EXAMPLE"
}
```

#### Sample Response
<a name="API_SSMContacts_CreateContact_Example_1_Response"></a>

```
{
    "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam"
}
```

## See Also
<a name="API_SSMContacts_CreateContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/CreateContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/CreateContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/CreateContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/CreateContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/CreateContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/CreateContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/CreateContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/CreateContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/CreateContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/CreateContact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

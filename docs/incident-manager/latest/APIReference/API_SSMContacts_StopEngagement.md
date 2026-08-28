---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_StopEngagement.html
---

# StopEngagement
<a name="API_SSMContacts_StopEngagement"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Stops an engagement before it finishes the final stage of the escalation plan or engagement plan. Further contacts aren't engaged.

## Request Syntax
<a name="API_SSMContacts_StopEngagement_RequestSyntax"></a>

```
{
   "EngagementId": "{{string}}",
   "Reason": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_StopEngagement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EngagementId](#API_SSMContacts_StopEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_StopEngagement-request-EngagementId"></a>
The Amazon Resource Name (ARN) of the engagement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [Reason](#API_SSMContacts_StopEngagement_RequestSyntax) **   <a name="IncidentManager-SSMContacts_StopEngagement-request-Reason"></a>
The reason that you're stopping the engagement.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^[.\s\S]*$`
Required: No

## Response Elements
<a name="API_SSMContacts_StopEngagement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SSMContacts_StopEngagement_Errors"></a>

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
<a name="API_SSMContacts_StopEngagement_Examples"></a>

### Example
<a name="API_SSMContacts_StopEngagement_Example_1"></a>

This example illustrates one usage of StopEngagement.

#### Sample Request
<a name="API_SSMContacts_StopEngagement_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.StopEngagement
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.stop-engagement
X-Amz-Date: 20220817T183804Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220817/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 132

{
	"EngagementId": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/test_escalation_plan/27bd86cf-6d50-49d2-a9ab-da39bEXAMPLE"
}
```

#### Sample Response
<a name="API_SSMContacts_StopEngagement_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_SSMContacts_StopEngagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/StopEngagement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/StopEngagement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/StopEngagement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/StopEngagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/StopEngagement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/StopEngagement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/StopEngagement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/StopEngagement)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/StopEngagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/StopEngagement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

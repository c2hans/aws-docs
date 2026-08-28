---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_PutContactPolicy.html
---

# PutContactPolicy
<a name="API_SSMContacts_PutContactPolicy"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Adds a resource policy to the specified contact or escalation plan. The resource policy is used to share the contact or escalation plan using AWS Resource Access Manager (AWS RAM). For more information about cross-account sharing, see [Setting up cross-account functionality](https://docs.aws.amazon.com/incident-manager/latest/userguide/xa.html).

## Request Syntax
<a name="API_SSMContacts_PutContactPolicy_RequestSyntax"></a>

```
{
   "ContactArn": "{{string}}",
   "Policy": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_PutContactPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactArn](#API_SSMContacts_PutContactPolicy_RequestSyntax) **   <a name="IncidentManager-SSMContacts_PutContactPolicy-request-ContactArn"></a>
The Amazon Resource Name (ARN) of the contact or escalation plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

 ** [Policy](#API_SSMContacts_PutContactPolicy_RequestSyntax) **   <a name="IncidentManager-SSMContacts_PutContactPolicy-request-Policy"></a>
Details of the resource policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 395000.
Pattern: `.*\S.*`
Required: Yes

## Response Elements
<a name="API_SSMContacts_PutContactPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_SSMContacts_PutContactPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 400

 ** ConflictException **
Updating or deleting a resource causes an inconsistent state.
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
<a name="API_SSMContacts_PutContactPolicy_Examples"></a>

### Example
<a name="API_SSMContacts_PutContactPolicy_Example_1"></a>

This example illustrates one usage of PutContactPolicy.

#### Sample Request
<a name="API_SSMContacts_PutContactPolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.PutContactPolicy
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.put-contact-policy
X-Amz-Date: 20220816T212604Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220816/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 546

{
	"ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam",
	"Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"ExampleResourcePolicy\",\"Action\":[\"ssm-contacts:GetContact\",\"ssm-contacts:StartEngagement\",\"ssm-contacts:DescribeEngagement\",\"ssm-contacts:ListPagesByEngagement\",\"ssm-contacts:StopEngagement\"],\"Principal\":{\"AWS\":\"444455556666\"},\"Effect\":\"Allow\",\"Resource\":[\"arn:aws:ssm-contacts:*:111122223333:contact\\/akuam\",\"arn:aws:ssm-contacts:*:111122223333:engagement\\/akuam\\/*\"]}]}"
}
```

#### Sample Response
<a name="API_SSMContacts_PutContactPolicy_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_SSMContacts_PutContactPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/PutContactPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/PutContactPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/PutContactPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/PutContactPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/PutContactPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/PutContactPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/PutContactPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/PutContactPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/PutContactPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/PutContactPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

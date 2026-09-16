---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_GetContactPolicy.html
---

# GetContactPolicy
<a name="API_SSMContacts_GetContactPolicy"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Retrieves the resource policies attached to the specified contact or escalation plan.

## Request Syntax
<a name="API_SSMContacts_GetContactPolicy_RequestSyntax"></a>

```
{
   "ContactArn": "{{string}}"
}
```

## Request Parameters
<a name="API_SSMContacts_GetContactPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ContactArn](#API_SSMContacts_GetContactPolicy_RequestSyntax) **   <a name="IncidentManager-SSMContacts_GetContactPolicy-request-ContactArn"></a>
The Amazon Resource Name (ARN) of the contact or escalation plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`
Required: Yes

## Response Syntax
<a name="API_SSMContacts_GetContactPolicy_ResponseSyntax"></a>

```
{
   "ContactArn": "string",
   "Policy": "string"
}
```

## Response Elements
<a name="API_SSMContacts_GetContactPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContactArn](#API_SSMContacts_GetContactPolicy_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetContactPolicy-response-ContactArn"></a>
The ARN of the contact or escalation plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):ssm-contacts:[-\w+=\/,.@]*:[0-9]+:([\w+=\/,.@:-])*`

 ** [Policy](#API_SSMContacts_GetContactPolicy_ResponseSyntax) **   <a name="IncidentManager-SSMContacts_GetContactPolicy-response-Policy"></a>
Details about the resource policy attached to the contact or escalation plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 395000.
Pattern: `.*\S.*`

## Errors
<a name="API_SSMContacts_GetContactPolicy_Errors"></a>

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
<a name="API_SSMContacts_GetContactPolicy_Examples"></a>

### Example
<a name="API_SSMContacts_GetContactPolicy_Example_1"></a>

This example illustrates one usage of GetContactPolicy.

#### Sample Request
<a name="API_SSMContacts_GetContactPolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm-contacts.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: SSMContacts.GetContactPolicy
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-contacts.get-contact-policy
X-Amz-Date: 20220816T213040Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220816/us-east-2/ssm-contacts/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 75

{
	"ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam"
}
```

#### Sample Response
<a name="API_SSMContacts_GetContactPolicy_Example_1_Response"></a>

```
{
    "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam",
    "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"ExampleResourcePolicy\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"444455556666\"},\"Action\":[\"ssm-contacts:GetContact\",\"ssm-contacts:StartEngagement\",\"ssm-contacts:DescribeEngagement\",\"ssm-contacts:ListPagesByEngagement\",\"ssm-contacts:StopEngagement\"],\"Resource\":[\"arn:aws:ssm-contacts:*:111122223333:contact/akuam\",\"arn:aws:ssm-contacts:*:111122223333:engagement/akuam/*\"]}]}"
}
```

## See Also
<a name="API_SSMContacts_GetContactPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-contacts-2021-05-03/GetContactPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-contacts-2021-05-03/GetContactPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/GetContactPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-contacts-2021-05-03/GetContactPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/GetContactPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-contacts-2021-05-03/GetContactPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-contacts-2021-05-03/GetContactPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-contacts-2021-05-03/GetContactPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-contacts-2021-05-03/GetContactPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/GetContactPolicy)

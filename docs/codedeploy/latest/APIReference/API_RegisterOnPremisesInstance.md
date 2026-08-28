---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RegisterOnPremisesInstance.html
---

# RegisterOnPremisesInstance
<a name="API_RegisterOnPremisesInstance"></a>

Registers an on-premises instance.

**Note**
Only one IAM ARN (an IAM session ARN or IAM user ARN) is supported in the request. You cannot use both.

## Request Syntax
<a name="API_RegisterOnPremisesInstance_RequestSyntax"></a>

```
{
   "iamSessionArn": "{{string}}",
   "iamUserArn": "{{string}}",
   "instanceName": "{{string}}"
}
```

## Request Parameters
<a name="API_RegisterOnPremisesInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [iamSessionArn](#API_RegisterOnPremisesInstance_RequestSyntax) **   <a name="CodeDeploy-RegisterOnPremisesInstance-request-iamSessionArn"></a>
The ARN of the IAM session to associate with the on-premises instance.
Type: String
Required: No

 ** [iamUserArn](#API_RegisterOnPremisesInstance_RequestSyntax) **   <a name="CodeDeploy-RegisterOnPremisesInstance-request-iamUserArn"></a>
The ARN of the user to associate with the on-premises instance.
Type: String
Required: No

 ** [instanceName](#API_RegisterOnPremisesInstance_RequestSyntax) **   <a name="CodeDeploy-RegisterOnPremisesInstance-request-instanceName"></a>
The name of the on-premises instance to register.
Type: String
Required: Yes

## Response Elements
<a name="API_RegisterOnPremisesInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RegisterOnPremisesInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IamArnRequiredException **
No IAM ARN was included in the request. You must use an IAM session ARN or user ARN in the request.
HTTP Status Code: 400

 ** IamSessionArnAlreadyRegisteredException **
The request included an IAM session ARN that has already been used to register a different instance.
HTTP Status Code: 400

 ** IamUserArnAlreadyRegisteredException **
The specified user ARN is already registered with an on-premises instance.
HTTP Status Code: 400

 ** IamUserArnRequiredException **
An user ARN was not specified.
HTTP Status Code: 400

 ** InstanceNameAlreadyRegisteredException **
The specified on-premises instance name is already registered.
HTTP Status Code: 400

 ** InstanceNameRequiredException **
An on-premises instance name was not specified.
HTTP Status Code: 400

 ** InvalidIamSessionArnException **
The IAM session ARN was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidIamUserArnException **
The user ARN was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidInstanceNameException **
The on-premises instance name was specified in an invalid format.
HTTP Status Code: 400

 ** MultipleIamArnsProvidedException **
Both an user ARN and an IAM session ARN were included in the request. Use only one ARN type.
HTTP Status Code: 400

## Examples
<a name="API_RegisterOnPremisesInstance_Examples"></a>

### Example
<a name="API_RegisterOnPremisesInstance_Example_1"></a>

This example illustrates one usage of RegisterOnPremisesInstance.

#### Sample Request
<a name="API_RegisterOnPremisesInstance_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 257
X-Amz-Target: CodeDeploy_20141006.RegisterOnPremisesInstance
X-Amz-Date: 20160707T024712Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "IamUserArn": "arn:aws:iam::444455556666:user/janedoe",
    "instanceName": "grp-o-inst-5"
}
```

#### Sample Response
<a name="API_RegisterOnPremisesInstance_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 4ccc9cf0-88c9-11e5-8ce3-2704437d0309
Content-Type: application/x-amz-json-1.1
Content-Length: 0
```

## See Also
<a name="API_RegisterOnPremisesInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/RegisterOnPremisesInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/RegisterOnPremisesInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/RegisterOnPremisesInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/RegisterOnPremisesInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/RegisterOnPremisesInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/RegisterOnPremisesInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/RegisterOnPremisesInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/RegisterOnPremisesInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/RegisterOnPremisesInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/RegisterOnPremisesInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteDeploymentGroup.html
---

# DeleteDeploymentGroup
<a name="API_DeleteDeploymentGroup"></a>

Deletes a deployment group.

## Request Syntax
<a name="API_DeleteDeploymentGroup_RequestSyntax"></a>

```
{
   "applicationName": "{{string}}",
   "deploymentGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDeploymentGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationName](#API_DeleteDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-DeleteDeploymentGroup-request-applicationName"></a>
The name of an AWS CodeDeploy application associated with the user or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: Yes

 ** [deploymentGroupName](#API_DeleteDeploymentGroup_RequestSyntax) **   <a name="CodeDeploy-DeleteDeploymentGroup-request-deploymentGroupName"></a>
The name of a deployment group for the specified application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: Yes

## Response Syntax
<a name="API_DeleteDeploymentGroup_ResponseSyntax"></a>

```
{
   "hooksNotCleanedUp": [
      {
         "hook": "string",
         "name": "string",
         "terminationHook": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DeleteDeploymentGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [hooksNotCleanedUp](#API_DeleteDeploymentGroup_ResponseSyntax) **   <a name="CodeDeploy-DeleteDeploymentGroup-response-hooksNotCleanedUp"></a>
If the output contains no data, and the corresponding deployment group contained at least one Auto Scaling group, AWS CodeDeploy successfully removed all corresponding Auto Scaling lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group. If the output contains data, AWS CodeDeploy could not remove some Auto Scaling lifecycle event hooks from the Amazon EC2 instances in the Auto Scaling group.
Type: Array of [AutoScalingGroup](API_AutoScalingGroup.md) objects

## Errors
<a name="API_DeleteDeploymentGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ApplicationNameRequiredException **
The minimum number of required application names was not specified.
HTTP Status Code: 400

 ** DeploymentGroupNameRequiredException **
The deployment group name was not specified.
HTTP Status Code: 400

 ** InvalidApplicationNameException **
The application name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidDeploymentGroupNameException **
The deployment group name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidRoleException **
The service role ARN was specified in an invalid format. Or, if an Auto Scaling group was specified, the specified service role does not grant the appropriate permissions to Amazon EC2 Auto Scaling.
HTTP Status Code: 400

## Examples
<a name="API_DeleteDeploymentGroup_Examples"></a>

### Example
<a name="API_DeleteDeploymentGroup_Example_1"></a>

This example illustrates one usage of DeleteDeploymentGroup.

#### Sample Request
<a name="API_DeleteDeploymentGroup_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 71
X-Amz-Target: CodeDeploy_20141006.DeleteDeploymentGroup
X-Amz-Date: 20160707T013700Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "applicationName": "TestApp-eu-west-1",
    "deploymentGroupName": "dep-group-abc-123"
}
```

#### Sample Response
<a name="API_DeleteDeploymentGroup_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: dec21774-88dd-11e5-96e5-8bf4ee0ce84e
Content-Type: application/x-amz-json-1.1
Content-Length: 24

{
    "hooksNotCleanedUp": []
}
```

## See Also
<a name="API_DeleteDeploymentGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/DeleteDeploymentGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/DeleteDeploymentGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeleteDeploymentGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/DeleteDeploymentGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeleteDeploymentGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/DeleteDeploymentGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/DeleteDeploymentGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/DeleteDeploymentGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/DeleteDeploymentGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeleteDeploymentGroup)

---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateManagedInstanceRole.html
---

# UpdateManagedInstanceRole
<a name="API_UpdateManagedInstanceRole"></a>

Changes the AWS Identity and Access Management (IAM) role that is assigned to the on-premises server, edge device, or virtual machines (VM). IAM roles are first assigned to these hybrid nodes during the activation process. For more information, see [CreateActivation](API_CreateActivation.md).

## Request Syntax
<a name="API_UpdateManagedInstanceRole_RequestSyntax"></a>

```
{
   "IamRole": "{{string}}",
   "InstanceId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateManagedInstanceRole_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IamRole](#API_UpdateManagedInstanceRole_RequestSyntax) **   <a name="systemsmanager-UpdateManagedInstanceRole-request-IamRole"></a>
The name of the AWS Identity and Access Management (IAM) role that you want to assign to the managed node. This IAM role must provide AssumeRole permissions for the AWS Systems Manager service principal `ssm.amazonaws.com`. For more information, see [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-service-role.html) in the * AWS Systems Manager User Guide*.
You can't specify an IAM service-linked role for this parameter. You must create a unique role.
Type: String
Length Constraints: Maximum length of 64.
Required: Yes

 ** [InstanceId](#API_UpdateManagedInstanceRole_RequestSyntax) **   <a name="systemsmanager-UpdateManagedInstanceRole-request-InstanceId"></a>
The ID of the managed node where you want to update the role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 124.
Pattern: `(^mi-[0-9a-f]{17}$)|(^eks_c:[0-9A-Za-z][A-Za-z0-9\-_]{0,99}_\w{17}$)`
Required: Yes

## Response Elements
<a name="API_UpdateManagedInstanceRole_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateManagedInstanceRole_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

## Examples
<a name="API_UpdateManagedInstanceRole_Examples"></a>

### Example
<a name="API_UpdateManagedInstanceRole_Example_1"></a>

This example illustrates one usage of UpdateManagedInstanceRole.

#### Sample Request
<a name="API_UpdateManagedInstanceRole_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UpdateManagedInstanceRole
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T191724Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 56

{
    "InstanceId": "mi-0ce084dd39EXAMPLE",
    "IamRole": "SSM"
}
```

#### Sample Response
<a name="API_UpdateManagedInstanceRole_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_UpdateManagedInstanceRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateManagedInstanceRole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateManagedInstanceRole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateManagedInstanceRole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateManagedInstanceRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateManagedInstanceRole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateManagedInstanceRole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateManagedInstanceRole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateManagedInstanceRole)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateManagedInstanceRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateManagedInstanceRole)

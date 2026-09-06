---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DeregisterManagedInstance.html
---

# DeregisterManagedInstance
<a name="API_DeregisterManagedInstance"></a>

Removes the server or virtual machine from the list of registered servers.

If you want to reregister an on-premises server, edge device, or VM, you must use a different Activation Code and Activation ID than used to register the machine previously. The Activation Code and Activation ID must not have already been used on the maximum number of activations specified when they were created. For more information, see [Deregistering managed nodes in a hybrid and multicloud environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-deregister-hybrid-nodes.html) in the * AWS Systems Manager User Guide*.

## Request Syntax
<a name="API_DeregisterManagedInstance_RequestSyntax"></a>

```
{
   "InstanceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterManagedInstance_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceId](#API_DeregisterManagedInstance_RequestSyntax) **   <a name="systemsmanager-DeregisterManagedInstance-request-InstanceId"></a>
The ID assigned to the managed node when you registered it using the activation process.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 124.
Pattern: `(^mi-[0-9a-f]{17}$)|(^eks_c:[0-9A-Za-z][A-Za-z0-9\-_]{0,99}_\w{17}$)`
Required: Yes

## Response Elements
<a name="API_DeregisterManagedInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeregisterManagedInstance_Errors"></a>

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
<a name="API_DeregisterManagedInstance_Examples"></a>

### Example
<a name="API_DeregisterManagedInstance_Example_1"></a>

This example illustrates one usage of DeregisterManagedInstance.

#### Sample Request
<a name="API_DeregisterManagedInstance_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DeregisterManagedInstance
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240220T234004Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240220/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 37

{
    "InstanceId": "mi-017431b35cEXAMPLE"
}
```

#### Sample Response
<a name="API_DeregisterManagedInstance_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeregisterManagedInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DeregisterManagedInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DeregisterManagedInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DeregisterManagedInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DeregisterManagedInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DeregisterManagedInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DeregisterManagedInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DeregisterManagedInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DeregisterManagedInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DeregisterManagedInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DeregisterManagedInstance)

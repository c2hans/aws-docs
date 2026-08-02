---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteDeploymentConfig.html
---

# DeleteDeploymentConfig
<a name="API_DeleteDeploymentConfig"></a>

Deletes a deployment configuration.

**Note**
A deployment configuration cannot be deleted if it is currently in use. Predefined configurations cannot be deleted.

## Request Syntax
<a name="API_DeleteDeploymentConfig_RequestSyntax"></a>

```
{
   "deploymentConfigName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDeploymentConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentConfigName](#API_DeleteDeploymentConfig_RequestSyntax) **   <a name="CodeDeploy-DeleteDeploymentConfig-request-deploymentConfigName"></a>
The name of a deployment configuration associated with the user or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Elements
<a name="API_DeleteDeploymentConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDeploymentConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeploymentConfigInUseException **
The deployment configuration is still in use.
HTTP Status Code: 400

 ** DeploymentConfigNameRequiredException **
The deployment configuration name was not specified.
HTTP Status Code: 400

 ** InvalidDeploymentConfigNameException **
The deployment configuration name was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidOperationException **
An invalid operation was detected.
HTTP Status Code: 400

## Examples
<a name="API_DeleteDeploymentConfig_Examples"></a>

### Example
<a name="API_DeleteDeploymentConfig_Example_1"></a>

This example illustrates one usage of DeleteDeploymentConfig.

#### Sample Request
<a name="API_DeleteDeploymentConfig_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 41
X-Amz-Target: CodeDeploy_20141006.DeleteDeploymentConfig
X-Amz-Date: 20160707T013153Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "deploymentConfigName": "dep-group-ghi-789"
}
```

#### Sample Response
<a name="API_DeleteDeploymentConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 4ccc9cf0-88c9-11e5-8ce3-2704437d0309
Content-Type: application/x-amz-json-1.1
Content-Length: 0
```

## See Also
<a name="API_DeleteDeploymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/DeleteDeploymentConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/DeleteDeploymentConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/DeleteDeploymentConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/DeleteDeploymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/DeleteDeploymentConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/DeleteDeploymentConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/DeleteDeploymentConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/DeleteDeploymentConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/DeleteDeploymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/DeleteDeploymentConfig)

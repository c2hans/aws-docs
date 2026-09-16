---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteDeploymentStrategy.html
---

# DeleteDeploymentStrategy
<a name="API_DeleteDeploymentStrategy"></a>

Deletes a deployment strategy.

## Request Syntax
<a name="API_DeleteDeploymentStrategy_RequestSyntax"></a>

```
DELETE /deployementstrategies/{{DeploymentStrategyId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDeploymentStrategy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeploymentStrategyId](#API_DeleteDeploymentStrategy_RequestSyntax) **   <a name="appconfig-DeleteDeploymentStrategy-request-uri-DeploymentStrategyId"></a>
The ID of the deployment strategy you want to delete.
Pattern: `(^[a-z0-9]{4,7}$|^AppConfig\.[A-Za-z0-9]{9,40}$)`
Required: Yes

## Request Body
<a name="API_DeleteDeploymentStrategy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDeploymentStrategy_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteDeploymentStrategy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteDeploymentStrategy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_DeleteDeploymentStrategy_Examples"></a>

### Example
<a name="API_DeleteDeploymentStrategy_Example_1"></a>

This example illustrates one usage of DeleteDeploymentStrategy.

#### Sample Request
<a name="API_DeleteDeploymentStrategy_Example_1_Request"></a>

```
DELETE /deployementstrategies/1225qzk HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.delete-deployment-strategy
X-Amz-Date: 20210920T221109Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_DeleteDeploymentStrategy_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteDeploymentStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/DeleteDeploymentStrategy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/DeleteDeploymentStrategy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/DeleteDeploymentStrategy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/DeleteDeploymentStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/DeleteDeploymentStrategy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/DeleteDeploymentStrategy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/DeleteDeploymentStrategy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/DeleteDeploymentStrategy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/DeleteDeploymentStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/DeleteDeploymentStrategy)

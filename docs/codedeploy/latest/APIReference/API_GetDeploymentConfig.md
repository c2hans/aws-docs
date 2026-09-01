---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentConfig.html
---

# GetDeploymentConfig
<a name="API_GetDeploymentConfig"></a>

Gets information about a deployment configuration.

## Request Syntax
<a name="API_GetDeploymentConfig_RequestSyntax"></a>

```
{
   "deploymentConfigName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetDeploymentConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [deploymentConfigName](#API_GetDeploymentConfig_RequestSyntax) **   <a name="CodeDeploy-GetDeploymentConfig-request-deploymentConfigName"></a>
The name of a deployment configuration associated with the user or AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: Yes

## Response Syntax
<a name="API_GetDeploymentConfig_ResponseSyntax"></a>

```
{
   "deploymentConfigInfo": {
      "computePlatform": "string",
      "createTime": number,
      "deploymentConfigId": "string",
      "deploymentConfigName": "string",
      "minimumHealthyHosts": {
         "type": "string",
         "value": number
      },
      "trafficRoutingConfig": {
         "timeBasedCanary": {
            "canaryInterval": number,
            "canaryPercentage": number
         },
         "timeBasedLinear": {
            "linearInterval": number,
            "linearPercentage": number
         },
         "type": "string"
      },
      "zonalConfig": {
         "firstZoneMonitorDurationInSeconds": number,
         "minimumHealthyHostsPerZone": {
            "type": "string",
            "value": number
         },
         "monitorDurationInSeconds": number
      }
   }
}
```

## Response Elements
<a name="API_GetDeploymentConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentConfigInfo](#API_GetDeploymentConfig_ResponseSyntax) **   <a name="CodeDeploy-GetDeploymentConfig-response-deploymentConfigInfo"></a>
Information about the deployment configuration.
Type: [DeploymentConfigInfo](API_DeploymentConfigInfo.md) object

## Errors
<a name="API_GetDeploymentConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeploymentConfigDoesNotExistException **
The deployment configuration does not exist with the user or AWS account.
HTTP Status Code: 400

 ** DeploymentConfigNameRequiredException **
The deployment configuration name was not specified.
HTTP Status Code: 400

 ** InvalidComputePlatformException **
The computePlatform is invalid. The computePlatform should be `Lambda`, `Server`, or `ECS`.
HTTP Status Code: 400

 ** InvalidDeploymentConfigNameException **
The deployment configuration name was specified in an invalid format.
HTTP Status Code: 400

## Examples
<a name="API_GetDeploymentConfig_Examples"></a>

### Example
<a name="API_GetDeploymentConfig_Example_1"></a>

This example illustrates one usage of GetDeploymentConfig.

#### Sample Request
<a name="API_GetDeploymentConfig_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 56
X-Amz-Target: CodeDeploy_20141006.GetDeploymentConfig
X-Amz-Date: 20160707T015738Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "deploymentConfigName": "CodeDeployDefault.OneAtATime"
}
```

#### Sample Response
<a name="API_GetDeploymentConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: c177704f-88e0-11e5-b497-75c493756c4d
Content-Type: application/x-amz-json-1.1
Content-Length: 200

{
    "deploymentConfigInfo": {
        "createTime": 1446744188.711,
        "deploymentConfigId": "00000000-0000-0000-0000-000000000001",
        "deploymentConfigName": "CodeDeployDefault.OneAtATime",
        "minimumHealthyHosts": {
            "type": "MOST_CONCURRENCY",
            "value": 1
        }
    }
}
```

## See Also
<a name="API_GetDeploymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/GetDeploymentConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/GetDeploymentConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/GetDeploymentConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/GetDeploymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/GetDeploymentConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/GetDeploymentConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/GetDeploymentConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/GetDeploymentConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/GetDeploymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/GetDeploymentConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

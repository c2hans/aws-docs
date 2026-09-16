---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeploymentConfig.html
---

# CreateDeploymentConfig
<a name="API_CreateDeploymentConfig"></a>

 Creates a deployment configuration.

## Request Syntax
<a name="API_CreateDeploymentConfig_RequestSyntax"></a>

```
{
   "computePlatform": "{{string}}",
   "deploymentConfigName": "{{string}}",
   "minimumHealthyHosts": {
      "type": "{{string}}",
      "value": {{number}}
   },
   "trafficRoutingConfig": {
      "timeBasedCanary": {
         "canaryInterval": {{number}},
         "canaryPercentage": {{number}}
      },
      "timeBasedLinear": {
         "linearInterval": {{number}},
         "linearPercentage": {{number}}
      },
      "type": "{{string}}"
   },
   "zonalConfig": {
      "firstZoneMonitorDurationInSeconds": {{number}},
      "minimumHealthyHostsPerZone": {
         "type": "{{string}}",
         "value": {{number}}
      },
      "monitorDurationInSeconds": {{number}}
   }
}
```

## Request Parameters
<a name="API_CreateDeploymentConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [computePlatform](#API_CreateDeploymentConfig_RequestSyntax) **   <a name="CodeDeploy-CreateDeploymentConfig-request-computePlatform"></a>
The destination platform type for the deployment (`Lambda`, `Server`, or `ECS`).
Type: String
Valid Values: `Server | Lambda | ECS | Kubernetes`
Required: No

 ** [deploymentConfigName](#API_CreateDeploymentConfig_RequestSyntax) **   <a name="CodeDeploy-CreateDeploymentConfig-request-deploymentConfigName"></a>
The name of the deployment configuration to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[A-Za-z0-9+=,.@_-]*`
Required: Yes

 ** [minimumHealthyHosts](#API_CreateDeploymentConfig_RequestSyntax) **   <a name="CodeDeploy-CreateDeploymentConfig-request-minimumHealthyHosts"></a>
The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.
The type parameter takes either of the following values:
+ HOST\_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value.
+ FLEET\_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET\_PERCENT, at the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of instances and rounds up fractional instances.
The value parameter takes an integer.
For example, to set a minimum of 95% healthy instance, specify a type of FLEET\_PERCENT and a value of 95.
Type: [MinimumHealthyHosts](API_MinimumHealthyHosts.md) object
Required: No

 ** [trafficRoutingConfig](#API_CreateDeploymentConfig_RequestSyntax) **   <a name="CodeDeploy-CreateDeploymentConfig-request-trafficRoutingConfig"></a>
The configuration that specifies how the deployment traffic is routed.
Type: [TrafficRoutingConfig](API_TrafficRoutingConfig.md) object
Required: No

 ** [zonalConfig](#API_CreateDeploymentConfig_RequestSyntax) **   <a name="CodeDeploy-CreateDeploymentConfig-request-zonalConfig"></a>
Configure the `ZonalConfig` object if you want AWS CodeDeploy to deploy your application to one [Availability Zone](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) at a time, within an AWS Region.
For more information about the zonal configuration feature, see [zonal configuration](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations-create.html#zonal-config) in the *CodeDeploy User Guide*.
Type: [ZonalConfig](API_ZonalConfig.md) object
Required: No

## Response Syntax
<a name="API_CreateDeploymentConfig_ResponseSyntax"></a>

```
{
   "deploymentConfigId": "string"
}
```

## Response Elements
<a name="API_CreateDeploymentConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deploymentConfigId](#API_CreateDeploymentConfig_ResponseSyntax) **   <a name="CodeDeploy-CreateDeploymentConfig-response-deploymentConfigId"></a>
A unique deployment configuration ID.
Type: String

## Errors
<a name="API_CreateDeploymentConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeploymentConfigAlreadyExistsException **
A deployment configuration with the specified name with the user or AWS account already exists.
HTTP Status Code: 400

 ** DeploymentConfigLimitExceededException **
The deployment configurations limit was exceeded.
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

 ** InvalidMinimumHealthyHostValueException **
The minimum healthy instance value was specified in an invalid format.
HTTP Status Code: 400

 ** InvalidTrafficRoutingConfigurationException **
 The configuration that specifies how traffic is routed during a deployment is invalid.
HTTP Status Code: 400

 ** InvalidZonalDeploymentConfigurationException **
The `ZonalConfig` object is not valid.
HTTP Status Code: 400

## Examples
<a name="API_CreateDeploymentConfig_Examples"></a>

### Example
<a name="API_CreateDeploymentConfig_Example_1"></a>

This example illustrates one usage of CreateDeploymentConfig.

#### Sample Request
<a name="API_CreateDeploymentConfig_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codedeploy.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 103
X-Amz-Target: CodeDeploy_20141006.CreateDeploymentConfig
X-Amz-Date: 20160707T235925Z
User-Agent: aws-cli/1.10.6 Python/2.7.9 Windows/7 botocore/1.3.28
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20160707/us-east-1/codedeploy/aws4_request,
	SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "minimumHealthyHosts": {
        "type": "HOST_COUNT",
        "value": 1
    },
    "deploymentConfigName": "CustomConfig.One"
}
```

#### Sample Response
<a name="API_CreateDeploymentConfig_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 3ea3b855-88d0-11e5-9958-cd5094947bf1
Content-Type: application/x-amz-json-1.1
Content-Length: 61

{
    "deploymentConfigId": "e0839cbd-af8a-4a6c-921g-9ad0245d3459"
}
```

## See Also
<a name="API_CreateDeploymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codedeploy-2014-10-06/CreateDeploymentConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codedeploy-2014-10-06/CreateDeploymentConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/CreateDeploymentConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codedeploy-2014-10-06/CreateDeploymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/CreateDeploymentConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codedeploy-2014-10-06/CreateDeploymentConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codedeploy-2014-10-06/CreateDeploymentConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codedeploy-2014-10-06/CreateDeploymentConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codedeploy-2014-10-06/CreateDeploymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/CreateDeploymentConfig)

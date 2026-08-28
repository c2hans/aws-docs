---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateEndpoint.html
---

# UpdateEndpoint
<a name="API_UpdateEndpoint"></a>

Deploys the `EndpointConfig` specified in the request to a new fleet of instances. SageMaker shifts endpoint traffic to the new instances with the updated endpoint configuration and then deletes the old instances using the previous `EndpointConfig` (there is no availability loss). For more information about how to control the update and traffic shifting process, see [ Update models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html).

When SageMaker receives the request, it sets the endpoint status to `Updating`. After updating the endpoint, it sets the status to `InService`. To check the status of an endpoint, use the [DescribeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeEndpoint.html) API.

**Note**
You must not delete an `EndpointConfig` in use by an endpoint that is live or while the `UpdateEndpoint` or `CreateEndpoint` operations are being performed on the endpoint. To update an endpoint, you must create a new `EndpointConfig`.
If you delete the `EndpointConfig` of an endpoint that is active or being created or updated you may lose visibility into the instance type the endpoint is using. The endpoint must be deleted in order to stop incurring charges.

## Request Syntax
<a name="API_UpdateEndpoint_RequestSyntax"></a>

```
{
   "DeploymentConfig": {
      "AutoRollbackConfiguration": {
         "Alarms": [
            {
               "AlarmName": "{{string}}"
            }
         ]
      },
      "BlueGreenUpdatePolicy": {
         "MaximumExecutionTimeoutInSeconds": {{number}},
         "TerminationWaitInSeconds": {{number}},
         "TrafficRoutingConfiguration": {
            "CanarySize": {
               "Type": "{{string}}",
               "Value": {{number}}
            },
            "LinearStepSize": {
               "Type": "{{string}}",
               "Value": {{number}}
            },
            "Type": "{{string}}",
            "WaitIntervalInSeconds": {{number}}
         }
      },
      "RollingUpdatePolicy": {
         "MaximumBatchSize": {
            "Type": "{{string}}",
            "Value": {{number}}
         },
         "MaximumExecutionTimeoutInSeconds": {{number}},
         "RollbackMaximumBatchSize": {
            "Type": "{{string}}",
            "Value": {{number}}
         },
         "WaitIntervalInSeconds": {{number}}
      }
   },
   "EndpointConfigName": "{{string}}",
   "EndpointName": "{{string}}",
   "ExcludeRetainedVariantProperties": [
      {
         "VariantPropertyType": "{{string}}"
      }
   ],
   "RetainAllVariantProperties": {{boolean}},
   "RetainDeploymentConfig": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdateEndpoint_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeploymentConfig](#API_UpdateEndpoint_RequestSyntax) **   <a name="sagemaker-UpdateEndpoint-request-DeploymentConfig"></a>
The deployment configuration for an endpoint, which contains the desired deployment strategy and rollback configurations.
Type: [DeploymentConfig](API_DeploymentConfig.md) object
Required: No

 ** [EndpointConfigName](#API_UpdateEndpoint_RequestSyntax) **   <a name="sagemaker-UpdateEndpoint-request-EndpointConfigName"></a>
The name of the new endpoint configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [EndpointName](#API_UpdateEndpoint_RequestSyntax) **   <a name="sagemaker-UpdateEndpoint-request-EndpointName"></a>
The name of the endpoint whose configuration you want to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ExcludeRetainedVariantProperties](#API_UpdateEndpoint_RequestSyntax) **   <a name="sagemaker-UpdateEndpoint-request-ExcludeRetainedVariantProperties"></a>
When you are updating endpoint resources with `RetainAllVariantProperties`, whose value is set to `true`, `ExcludeRetainedVariantProperties` specifies the list of type [VariantProperty](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VariantProperty.html) to override with the values provided by `EndpointConfig`. If you don't specify a value for `ExcludeRetainedVariantProperties`, no variant properties are overridden.
Type: Array of [VariantProperty](API_VariantProperty.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

 ** [RetainAllVariantProperties](#API_UpdateEndpoint_RequestSyntax) **   <a name="sagemaker-UpdateEndpoint-request-RetainAllVariantProperties"></a>
When updating endpoint resources, enables or disables the retention of [variant properties](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VariantProperty.html), such as the instance count or the variant weight. To retain the variant properties of an endpoint when updating it, set `RetainAllVariantProperties` to `true`. To use the variant properties specified in a new `EndpointConfig` call when updating an endpoint, set `RetainAllVariantProperties` to `false`. The default is `false`.
Type: Boolean
Required: No

 ** [RetainDeploymentConfig](#API_UpdateEndpoint_RequestSyntax) **   <a name="sagemaker-UpdateEndpoint-request-RetainDeploymentConfig"></a>
Specifies whether to reuse the last deployment configuration. The default value is false (the configuration is not reused).
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateEndpoint_ResponseSyntax"></a>

```
{
   "EndpointArn": "string"
}
```

## Response Elements
<a name="API_UpdateEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointArn](#API_UpdateEndpoint_ResponseSyntax) **   <a name="sagemaker-UpdateEndpoint-response-EndpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:endpoint/.*`

## Errors
<a name="API_UpdateEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_UpdateEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

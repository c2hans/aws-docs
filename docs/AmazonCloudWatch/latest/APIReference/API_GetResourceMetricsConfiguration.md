---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetResourceMetricsConfiguration.html
---

# GetResourceMetricsConfiguration
<a name="API_GetResourceMetricsConfiguration"></a>

Retrieves the current resource metrics configuration for an AWS resource. The response includes the resource ARN, any metric selections, and the times at which the configuration was created and last updated.

This operation returns a `ResourceNotFoundException` if no resource metrics configuration exists for the specified resource ARN. To create a configuration, use [CreateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html).

To retrieve a resource metrics configuration, you must have the `cloudwatch:GetResourceMetricsConfiguration` permission. For information about scoping this permission to specific resources, see [Condition keys for resource metrics configuration access](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-resource-arn.html) in the *Amazon CloudWatch User Guide*.

## Request Syntax
<a name="API_GetResourceMetricsConfiguration_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourceMetricsConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_GetResourceMetricsConfiguration_RequestSyntax) **   <a name="ACW-GetResourceMetricsConfiguration-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the AWS resource to retrieve the resource metrics configuration for.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-zA-Z0-9-]+:[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:.+`
Required: Yes

## Response Syntax
<a name="API_GetResourceMetricsConfiguration_ResponseSyntax"></a>

```
{
   "ResourceMetricsConfiguration": {
      "CreatedAt": number,
      "MetricSelections": [
         {
            "IncludeMetrics": [ "string" ]
         }
      ],
      "ResourceArn": "string",
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_GetResourceMetricsConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceMetricsConfiguration](#API_GetResourceMetricsConfiguration_ResponseSyntax) **   <a name="ACW-GetResourceMetricsConfiguration-response-ResourceMetricsConfiguration"></a>
The resource metrics configuration for the specified resource.
Type: [ResourceMetricsConfiguration](API_ResourceMetricsConfiguration.md) object

## Errors
<a name="API_GetResourceMetricsConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## See Also
<a name="API_GetResourceMetricsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetResourceMetricsConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetResourceMetricsConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetResourceMetricsConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetResourceMetricsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetResourceMetricsConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetResourceMetricsConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetResourceMetricsConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetResourceMetricsConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetResourceMetricsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetResourceMetricsConfiguration)

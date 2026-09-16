---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_StartDiscovery.html
---

# StartDiscovery
<a name="API_StartDiscovery"></a>

Enables this AWS account to be able to use CloudWatch Application Signals by creating the *AWSServiceRoleForCloudWatchApplicationSignals* service-linked role. This service- linked role has the following permissions:
+  `xray:GetServiceGraph`
+  `logs:StartQuery`
+  `logs:GetQueryResults`
+  `cloudwatch:GetMetricData`
+  `cloudwatch:ListMetrics`
+  `tag:GetResources`
+  `autoscaling:DescribeAutoScalingGroups`

A service-linked CloudTrail event channel is created to process CloudTrail events and return change event information. This includes last deployment time, userName, eventName, and other event metadata.

After completing this step, you still need to instrument your Java and Python applications to send data to Application Signals. For more information, see [ Enabling Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html).

## Request Syntax
<a name="API_StartDiscovery_RequestSyntax"></a>

```
POST /start-discovery HTTP/1.1
```

## URI Request Parameters
<a name="API_StartDiscovery_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartDiscovery_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StartDiscovery_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StartDiscovery_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StartDiscovery_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ThrottlingException **
The request was throttled because of quota limits.
HTTP Status Code: 429

 ** ValidationException **
The resource is not valid.
HTTP Status Code: 400

## See Also
<a name="API_StartDiscovery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-signals-2024-04-15/StartDiscovery)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-signals-2024-04-15/StartDiscovery)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/StartDiscovery)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-signals-2024-04-15/StartDiscovery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/StartDiscovery)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-signals-2024-04-15/StartDiscovery)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-signals-2024-04-15/StartDiscovery)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-signals-2024-04-15/StartDiscovery)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/application-signals-2024-04-15/StartDiscovery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/StartDiscovery)

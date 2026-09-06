---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TimeBasedCanary.html
---

# TimeBasedCanary
<a name="API_TimeBasedCanary"></a>

A configuration that shifts traffic from one version of a Lambda function or Amazon ECS task set to another in two increments. The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.

## Contents
<a name="API_TimeBasedCanary_Contents"></a>

 ** canaryInterval **   <a name="CodeDeploy-Type-TimeBasedCanary-canaryInterval"></a>
The number of minutes between the first and second traffic shifts of a `TimeBasedCanary` deployment.
Type: Integer
Required: No

 ** canaryPercentage **   <a name="CodeDeploy-Type-TimeBasedCanary-canaryPercentage"></a>
The percentage of traffic to shift in the first increment of a `TimeBasedCanary` deployment.
Type: Integer
Required: No

## See Also
<a name="API_TimeBasedCanary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/TimeBasedCanary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/TimeBasedCanary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/TimeBasedCanary)

---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TimeBasedLinear.html
---

# TimeBasedLinear
<a name="API_TimeBasedLinear"></a>

A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in equal increments, with an equal number of minutes between each increment. The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.

## Contents
<a name="API_TimeBasedLinear_Contents"></a>

 ** linearInterval **   <a name="CodeDeploy-Type-TimeBasedLinear-linearInterval"></a>
The number of minutes between each incremental traffic shift of a `TimeBasedLinear` deployment.
Type: Integer
Required: No

 ** linearPercentage **   <a name="CodeDeploy-Type-TimeBasedLinear-linearPercentage"></a>
The percentage of traffic that is shifted at the start of each increment of a `TimeBasedLinear` deployment.
Type: Integer
Required: No

## See Also
<a name="API_TimeBasedLinear_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/TimeBasedLinear)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/TimeBasedLinear)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/TimeBasedLinear)

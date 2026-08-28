---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TrafficRoutingConfig.html
---

# TrafficRoutingConfig
<a name="API_TrafficRoutingConfig"></a>

The configuration that specifies how traffic is shifted from one version of a Lambda function to another version during an AWS Lambda deployment, or from one Amazon ECS task set to another during an Amazon ECS deployment.

## Contents
<a name="API_TrafficRoutingConfig_Contents"></a>

 ** timeBasedCanary **   <a name="CodeDeploy-Type-TrafficRoutingConfig-timeBasedCanary"></a>
A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in two increments. The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.
Type: [TimeBasedCanary](API_TimeBasedCanary.md) object
Required: No

 ** timeBasedLinear **   <a name="CodeDeploy-Type-TrafficRoutingConfig-timeBasedLinear"></a>
A configuration that shifts traffic from one version of a Lambda function or Amazon ECS task set to another in equal increments, with an equal number of minutes between each increment. The original and target Lambda function versions or Amazon ECS task sets are specified in the deployment's AppSpec file.
Type: [TimeBasedLinear](API_TimeBasedLinear.md) object
Required: No

 ** type **   <a name="CodeDeploy-Type-TrafficRoutingConfig-type"></a>
The type of traffic shifting (`TimeBasedCanary` or `TimeBasedLinear`) used by a deployment configuration.
Type: String
Valid Values: `TimeBasedCanary | TimeBasedLinear | TimeBasedFlexible | AllAtOnce`
Required: No

## See Also
<a name="API_TrafficRoutingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/TrafficRoutingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/TrafficRoutingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/TrafficRoutingConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

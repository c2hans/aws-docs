---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_InstanceDefinition.html
---

# InstanceDefinition
<a name="API_InstanceDefinition"></a>

An allowed instance type for a game server group. All game server groups must have at least two instance types defined for it. Amazon GameLift Servers FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

## Contents
<a name="API_InstanceDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** InstanceType **   <a name="gameliftservers-Type-InstanceDefinition-InstanceType"></a>
An Amazon EC2 instance type designation.
Type: String
Valid Values: `c4.large | c4.xlarge | c4.2xlarge | c4.4xlarge | c4.8xlarge | c5.large | c5.xlarge | c5.2xlarge | c5.4xlarge | c5.9xlarge | c5.12xlarge | c5.18xlarge | c5.24xlarge | c5a.large | c5a.xlarge | c5a.2xlarge | c5a.4xlarge | c5a.8xlarge | c5a.12xlarge | c5a.16xlarge | c5a.24xlarge | c6g.medium | c6g.large | c6g.xlarge | c6g.2xlarge | c6g.4xlarge | c6g.8xlarge | c6g.12xlarge | c6g.16xlarge | r4.large | r4.xlarge | r4.2xlarge | r4.4xlarge | r4.8xlarge | r4.16xlarge | r5.large | r5.xlarge | r5.2xlarge | r5.4xlarge | r5.8xlarge | r5.12xlarge | r5.16xlarge | r5.24xlarge | r5a.large | r5a.xlarge | r5a.2xlarge | r5a.4xlarge | r5a.8xlarge | r5a.12xlarge | r5a.16xlarge | r5a.24xlarge | r6g.medium | r6g.large | r6g.xlarge | r6g.2xlarge | r6g.4xlarge | r6g.8xlarge | r6g.12xlarge | r6g.16xlarge | m4.large | m4.xlarge | m4.2xlarge | m4.4xlarge | m4.10xlarge | m5.large | m5.xlarge | m5.2xlarge | m5.4xlarge | m5.8xlarge | m5.12xlarge | m5.16xlarge | m5.24xlarge | m5a.large | m5a.xlarge | m5a.2xlarge | m5a.4xlarge | m5a.8xlarge | m5a.12xlarge | m5a.16xlarge | m5a.24xlarge | m6g.medium | m6g.large | m6g.xlarge | m6g.2xlarge | m6g.4xlarge | m6g.8xlarge | m6g.12xlarge | m6g.16xlarge`
Required: Yes

 ** WeightedCapacity **   <a name="gameliftservers-Type-InstanceDefinition-WeightedCapacity"></a>
Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by Amazon GameLift Servers FleetIQ to calculate the instance type's cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see [Instance Weighting](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html) in the *Amazon Elastic Compute Cloud Auto Scaling User Guide*. Default value is "1".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 3.
Pattern: `^[\u0031-\u0039][\u0030-\u0039]{0,2}$`
Required: No

## See Also
<a name="API_InstanceDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/InstanceDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/InstanceDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/InstanceDefinition)

---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EnvironmentResourceDescription.html
---

# EnvironmentResourceDescription
<a name="API_EnvironmentResourceDescription"></a>

Describes the AWS resources in use by this environment. This data is live.

## Contents
<a name="API_EnvironmentResourceDescription_Contents"></a>

 ** AutoScalingGroups.member.N **
 The `AutoScalingGroups` used by this environment.
Type: Array of [AutoScalingGroup](API_AutoScalingGroup.md) objects
Required: No

 ** Cluster **
The Amazon EKS cluster that this environment runs on. This member is present only for environments in the *Cluster* tier.
Type: [Cluster](API_Cluster.md) object
Required: No

 ** EnvironmentName **
The name of the environment.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** Instances.member.N **
The Amazon EC2 instances used by this environment.
Type: Array of [Instance](API_Instance.md) objects
Required: No

 ** LaunchConfigurations.member.N **
The Auto Scaling launch configurations in use by this environment.
Type: Array of [LaunchConfiguration](API_LaunchConfiguration.md) objects
Required: No

 ** LaunchTemplates.member.N **
The Amazon EC2 launch templates in use by this environment.
Type: Array of [LaunchTemplate](API_LaunchTemplate.md) objects
Required: No

 ** LoadBalancers.member.N **
The LoadBalancers in use by this environment.
Type: Array of [LoadBalancer](API_LoadBalancer.md) objects
Required: No

 ** Queues.member.N **
The queues used by this environment.
Type: Array of [Queue](API_Queue.md) objects
Required: No

 ** Triggers.member.N **
The `AutoScaling` triggers in use by this environment.
Type: Array of [Trigger](API_Trigger.md) objects
Required: No

## See Also
<a name="API_EnvironmentResourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/EnvironmentResourceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/EnvironmentResourceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/EnvironmentResourceDescription)

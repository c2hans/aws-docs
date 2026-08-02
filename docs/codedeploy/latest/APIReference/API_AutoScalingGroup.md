---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_AutoScalingGroup.html
---

# AutoScalingGroup
<a name="API_AutoScalingGroup"></a>

Information about an Auto Scaling group.

## Contents
<a name="API_AutoScalingGroup_Contents"></a>

 ** hook **   <a name="CodeDeploy-Type-AutoScalingGroup-hook"></a>
The name of the launch hook that CodeDeploy installed into the Auto Scaling group.
For more information about the launch hook, see [How Amazon EC2 Auto Scaling works with CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors) in the * AWS CodeDeploy User Guide*.
Type: String
Required: No

 ** name **   <a name="CodeDeploy-Type-AutoScalingGroup-name"></a>
The Auto Scaling group name.
Type: String
Required: No

 ** terminationHook **   <a name="CodeDeploy-Type-AutoScalingGroup-terminationHook"></a>
The name of the termination hook that CodeDeploy installed into the Auto Scaling group.
For more information about the termination hook, see [Enabling termination deployments during Auto Scaling scale-in events](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-auto-scaling.html#integrations-aws-auto-scaling-behaviors-hook-enable) in the * AWS CodeDeploy User Guide*.
Type: String
Required: No

## See Also
<a name="API_AutoScalingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/AutoScalingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/AutoScalingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/AutoScalingGroup)

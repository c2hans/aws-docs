---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BlueInstanceTerminationOption.html
---

# BlueInstanceTerminationOption
<a name="API_BlueInstanceTerminationOption"></a>

Information about whether instances in the original environment are terminated when a blue/green deployment is successful. `BlueInstanceTerminationOption` does not apply to Lambda deployments.

## Contents
<a name="API_BlueInstanceTerminationOption_Contents"></a>

 ** action **   <a name="CodeDeploy-Type-BlueInstanceTerminationOption-action"></a>
The action to take on instances in the original environment after a successful blue/green deployment.
+  `TERMINATE`: Instances are terminated after a specified wait time.
+  `KEEP_ALIVE`: Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
Type: String
Valid Values: `TERMINATE | KEEP_ALIVE`
Required: No

 ** terminationWaitTimeInMinutes **   <a name="CodeDeploy-Type-BlueInstanceTerminationOption-terminationWaitTimeInMinutes"></a>
For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.
 For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set.
 The maximum setting is 2880 minutes (2 days).
Type: Integer
Required: No

## See Also
<a name="API_BlueInstanceTerminationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/BlueInstanceTerminationOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/BlueInstanceTerminationOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/BlueInstanceTerminationOption)

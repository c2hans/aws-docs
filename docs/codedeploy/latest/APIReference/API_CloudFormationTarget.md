---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CloudFormationTarget.html
---

# CloudFormationTarget
<a name="API_CloudFormationTarget"></a>

 Information about the target to be updated by an CloudFormation blue/green deployment. This target type is used for all deployments initiated by a CloudFormation stack update.

## Contents
<a name="API_CloudFormationTarget_Contents"></a>

 ** deploymentId **   <a name="CodeDeploy-Type-CloudFormationTarget-deploymentId"></a>
The unique ID of an CloudFormation blue/green deployment.
Type: String
Required: No

 ** lastUpdatedAt **   <a name="CodeDeploy-Type-CloudFormationTarget-lastUpdatedAt"></a>
 The date and time when the target application was updated by an CloudFormation blue/green deployment.
Type: Timestamp
Required: No

 ** lifecycleEvents **   <a name="CodeDeploy-Type-CloudFormationTarget-lifecycleEvents"></a>
 The lifecycle events of the CloudFormation blue/green deployment to this target application.
Type: Array of [LifecycleEvent](API_LifecycleEvent.md) objects
Required: No

 ** resourceType **   <a name="CodeDeploy-Type-CloudFormationTarget-resourceType"></a>
The resource type for the CloudFormation blue/green deployment.
Type: String
Required: No

 ** status **   <a name="CodeDeploy-Type-CloudFormationTarget-status"></a>
 The status of an CloudFormation blue/green deployment's target application.
Type: String
Valid Values: `Pending | InProgress | Succeeded | Failed | Skipped | Unknown | Ready`
Required: No

 ** targetId **   <a name="CodeDeploy-Type-CloudFormationTarget-targetId"></a>
 The unique ID of a deployment target that has a type of `CloudFormationTarget`.
Type: String
Required: No

 ** targetVersionWeight **   <a name="CodeDeploy-Type-CloudFormationTarget-targetVersionWeight"></a>
The percentage of production traffic that the target version of an CloudFormation blue/green deployment receives.
Type: Double
Required: No

## See Also
<a name="API_CloudFormationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/CloudFormationTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/CloudFormationTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/CloudFormationTarget)

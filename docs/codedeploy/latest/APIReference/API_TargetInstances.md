---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TargetInstances.html
---

# TargetInstances
<a name="API_TargetInstances"></a>

Information about the instances to be used in the replacement environment in a blue/green deployment.

## Contents
<a name="API_TargetInstances_Contents"></a>

 ** autoScalingGroups **   <a name="CodeDeploy-Type-TargetInstances-autoScalingGroups"></a>
The names of one or more Auto Scaling groups to identify a replacement environment for a blue/green deployment.
Type: Array of strings
Required: No

 ** ec2TagSet **   <a name="CodeDeploy-Type-TargetInstances-ec2TagSet"></a>
Information about the groups of Amazon EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment. Cannot be used in the same call as `tagFilters`.
Type: [EC2TagSet](API_EC2TagSet.md) object
Required: No

 ** tagFilters **   <a name="CodeDeploy-Type-TargetInstances-tagFilters"></a>
The tag filter key, type, and value used to identify Amazon EC2 instances in a replacement environment for a blue/green deployment. Cannot be used in the same call as `ec2TagSet`.
Type: Array of [EC2TagFilter](API_EC2TagFilter.md) objects
Required: No

## See Also
<a name="API_TargetInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/TargetInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/TargetInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/TargetInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

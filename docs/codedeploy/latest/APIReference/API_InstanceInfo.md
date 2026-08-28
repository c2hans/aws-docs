---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_InstanceInfo.html
---

# InstanceInfo
<a name="API_InstanceInfo"></a>

Information about an on-premises instance.

## Contents
<a name="API_InstanceInfo_Contents"></a>

 ** deregisterTime **   <a name="CodeDeploy-Type-InstanceInfo-deregisterTime"></a>
If the on-premises instance was deregistered, the time at which the on-premises instance was deregistered.
Type: Timestamp
Required: No

 ** iamSessionArn **   <a name="CodeDeploy-Type-InstanceInfo-iamSessionArn"></a>
The ARN of the IAM session associated with the on-premises instance.
Type: String
Required: No

 ** iamUserArn **   <a name="CodeDeploy-Type-InstanceInfo-iamUserArn"></a>
The user ARN associated with the on-premises instance.
Type: String
Required: No

 ** instanceArn **   <a name="CodeDeploy-Type-InstanceInfo-instanceArn"></a>
The ARN of the on-premises instance.
Type: String
Required: No

 ** instanceName **   <a name="CodeDeploy-Type-InstanceInfo-instanceName"></a>
The name of the on-premises instance.
Type: String
Required: No

 ** registerTime **   <a name="CodeDeploy-Type-InstanceInfo-registerTime"></a>
The time at which the on-premises instance was registered.
Type: Timestamp
Required: No

 ** tags **   <a name="CodeDeploy-Type-InstanceInfo-tags"></a>
The tags currently associated with the on-premises instance.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_InstanceInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/InstanceInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/InstanceInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/InstanceInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

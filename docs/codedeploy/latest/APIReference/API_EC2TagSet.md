---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_EC2TagSet.html
---

# EC2TagSet
<a name="API_EC2TagSet"></a>

Information about groups of Amazon EC2 instance tags.

## Contents
<a name="API_EC2TagSet_Contents"></a>

 ** ec2TagSetList **   <a name="CodeDeploy-Type-EC2TagSet-ec2TagSetList"></a>
A list that contains other lists of Amazon EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.
Type: Array of arrays of [EC2TagFilter](API_EC2TagFilter.md) objects
Required: No

## See Also
<a name="API_EC2TagSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/EC2TagSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/EC2TagSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/EC2TagSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

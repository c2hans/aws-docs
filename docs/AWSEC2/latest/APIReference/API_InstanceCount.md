---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceCount.html
---

# InstanceCount
<a name="API_InstanceCount"></a>

Describes a Reserved Instance listing state.

## Contents
<a name="API_InstanceCount_Contents"></a>

 ** instanceCount **
The number of listed Reserved Instances in the state specified by the `state`.
Type: Integer
Required: No

 ** state **
The states of the listed Reserved Instances.
Type: String
Valid Values: `available | sold | cancelled | pending`
Required: No

## See Also
<a name="API_InstanceCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceCount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

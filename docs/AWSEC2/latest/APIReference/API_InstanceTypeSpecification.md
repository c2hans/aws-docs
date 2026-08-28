---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceTypeSpecification.html
---

# InstanceTypeSpecification
<a name="API_InstanceTypeSpecification"></a>

Describes the instance type compatibility rules for an AMI, including lists of supported and unsupported instance type patterns.

## Contents
<a name="API_InstanceTypeSpecification_Contents"></a>

 ** SupportedInstanceTypeSet.N **
The instance types that the AMI supports.
Type: Array of [InstanceTypeItem](API_InstanceTypeItem.md) objects
Required: No

 ** UnsupportedInstanceTypeSet.N **
The instance types that the AMI does not support.
Type: Array of [InstanceTypeItem](API_InstanceTypeItem.md) objects
Required: No

## See Also
<a name="API_InstanceTypeSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InstanceTypeSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InstanceTypeSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InstanceTypeSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EbsStatusDetails.html
---

# EbsStatusDetails
<a name="API_EbsStatusDetails"></a>

Describes the attached EBS status check for an instance.

## Contents
<a name="API_EbsStatusDetails_Contents"></a>

 ** impairedSince **
The date and time when the attached EBS status check failed.
Type: Timestamp
Required: No

 ** name **
The name of the attached EBS status check.
Type: String
Valid Values: `reachability`
Required: No

 ** status **
The result of the attached EBS status check.
Type: String
Valid Values: `passed | failed | insufficient-data | initializing`
Required: No

## See Also
<a name="API_EbsStatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EbsStatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EbsStatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EbsStatusDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

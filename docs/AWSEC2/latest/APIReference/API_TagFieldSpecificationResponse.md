---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TagFieldSpecificationResponse.html
---

# TagFieldSpecificationResponse
<a name="API_TagFieldSpecificationResponse"></a>

A single resource's tag configuration associated with the Flow Logs Amazon EC2 Tags feature fields in your custom log format.

## Contents
<a name="API_TagFieldSpecificationResponse_Contents"></a>

 ** resourceType **
The resource type for the tag keys associated with the Flow Logs Amazon EC2 Tags feature fields in your custom log format.
Type: String
Valid Values: `network-interface | instance | auto-scaling-group`
Required: No

 ** TagKeySet.N **
The tag keys on your tagged resources to be displayed by the Flow Logs Amazon EC2 Tags feature fields in your custom log format.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_TagFieldSpecificationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TagFieldSpecificationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TagFieldSpecificationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TagFieldSpecificationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

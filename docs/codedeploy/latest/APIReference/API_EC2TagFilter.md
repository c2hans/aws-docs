---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_EC2TagFilter.html
---

# EC2TagFilter
<a name="API_EC2TagFilter"></a>

Information about an EC2 tag filter.

## Contents
<a name="API_EC2TagFilter_Contents"></a>

 ** Key **   <a name="CodeDeploy-Type-EC2TagFilter-Key"></a>
The tag filter key.
Type: String
Required: No

 ** Type **   <a name="CodeDeploy-Type-EC2TagFilter-Type"></a>
The tag filter type:
+  `KEY_ONLY`: Key only.
+  `VALUE_ONLY`: Value only.
+  `KEY_AND_VALUE`: Key and value.
Type: String
Valid Values: `KEY_ONLY | VALUE_ONLY | KEY_AND_VALUE`
Required: No

 ** Value **   <a name="CodeDeploy-Type-EC2TagFilter-Value"></a>
The tag filter value.
Type: String
Required: No

## See Also
<a name="API_EC2TagFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/EC2TagFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/EC2TagFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/EC2TagFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

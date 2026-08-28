---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_AssetInstanceTypeCapacity.html
---

# AssetInstanceTypeCapacity
<a name="API_AssetInstanceTypeCapacity"></a>

The capacity for each instance type.

## Contents
<a name="API_AssetInstanceTypeCapacity_Contents"></a>

 ** Count **   <a name="outposts-Type-AssetInstanceTypeCapacity-Count"></a>
The number of each instance type.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 9999.
Required: Yes

 ** InstanceType **   <a name="outposts-Type-AssetInstanceTypeCapacity-InstanceType"></a>
The type of instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-z0-9\-]+\.[a-z0-9\-]+$`
Required: Yes

## See Also
<a name="API_AssetInstanceTypeCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/AssetInstanceTypeCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/AssetInstanceTypeCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/AssetInstanceTypeCapacity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

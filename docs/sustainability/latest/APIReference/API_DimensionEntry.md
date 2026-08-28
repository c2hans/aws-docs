---
source_url: https://docs.aws.amazon.com/sustainability/latest/APIReference/API_DimensionEntry.html
---

# DimensionEntry
<a name="API_DimensionEntry"></a>

Represents a dimension and its corresponding value.

## Contents
<a name="API_DimensionEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dimension **   <a name="sustainability-Type-DimensionEntry-Dimension"></a>
The dimension type that categorizes this entry.
Type: String
Valid Values: `USAGE_ACCOUNT_ID | REGION | SERVICE`
Required: Yes

 ** Value **   <a name="sustainability-Type-DimensionEntry-Value"></a>
 The value for the specified dimension. Valid values vary based on the dimension type (e.g., `us-east-1` for the `REGION` dimension, `AmazonEC2` for the `SERVICE` dimension).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

## See Also
<a name="API_DimensionEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sustainability-2018-05-10/DimensionEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sustainability-2018-05-10/DimensionEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sustainability-2018-05-10/DimensionEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Sustainability. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sustainability` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

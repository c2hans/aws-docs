---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_Setting.html
---

# Setting
<a name="API_Setting"></a>

Represents a single network-level configuration setting with its name, value, and data type. Settings control network-wide behaviors and features.

## Contents
<a name="API_Setting_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** optionName **   <a name="wickr-Type-Setting-optionName"></a>
The name of the network setting (e.g., 'enableClientMetrics', 'dataRetention').
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** type **   <a name="wickr-Type-Setting-type"></a>
The data type of the setting value (e.g., 'boolean', 'string', 'number').
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** value **   <a name="wickr-Type-Setting-value"></a>
The current value of the setting as a string. Boolean values are represented as 'true' or 'false'.
Type: String
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_Setting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/Setting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/Setting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/Setting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

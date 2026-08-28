---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleExportJobThemeOverrideProperties.html
---

# AssetBundleExportJobThemeOverrideProperties
<a name="API_AssetBundleExportJobThemeOverrideProperties"></a>

Controls how a specific `Theme` resource is parameterized in the returned CloudFormation template.

## Contents
<a name="API_AssetBundleExportJobThemeOverrideProperties_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-AssetBundleExportJobThemeOverrideProperties-Arn"></a>
The ARN of the specific `Theme` resource whose override properties are configured in this structure.
Type: String
Required: Yes

 ** Properties **   <a name="QS-Type-AssetBundleExportJobThemeOverrideProperties-Properties"></a>
A list of `Theme` resource properties to generate variables for in the returned CloudFormation template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `Name`
Required: Yes

## See Also
<a name="API_AssetBundleExportJobThemeOverrideProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleExportJobThemeOverrideProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleExportJobThemeOverrideProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleExportJobThemeOverrideProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

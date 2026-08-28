---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ProviderConfig.html
---

# ProviderConfig
<a name="API_ProviderConfig"></a>

The provider-specific configuration for a DLP integration. This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Contents
<a name="API_ProviderConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** MicrosoftPurview **   <a name="QS-Type-ProviderConfig-MicrosoftPurview"></a>
The configuration for a Microsoft Purview DLP integration.
Type: [MicrosoftPurviewProviderConfig](API_MicrosoftPurviewProviderConfig.md) object
Required: No

## See Also
<a name="API_ProviderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ProviderConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ProviderConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ProviderConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_MicrosoftPurviewProviderConfig.html
---

# MicrosoftPurviewProviderConfig
<a name="API_MicrosoftPurviewProviderConfig"></a>

The full configuration for Microsoft Purview DLP integration, including the provider credentials and the label-action mappings that define the enforcement policy.

## Contents
<a name="API_MicrosoftPurviewProviderConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Credentials **   <a name="QS-Type-MicrosoftPurviewProviderConfig-Credentials"></a>
The credentials used to authenticate with Microsoft Purview.
Type: [MicrosoftPurviewCredentials](API_MicrosoftPurviewCredentials.md) object
Required: Yes

 ** LabelActionMappings **   <a name="QS-Type-MicrosoftPurviewProviderConfig-LabelActionMappings"></a>
The mappings from Microsoft Purview sensitivity labels to enforcement actions.
Type: Array of [LabelActionMapping](API_LabelActionMapping.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: Yes

 ** UnmappedAction **   <a name="QS-Type-MicrosoftPurviewProviderConfig-UnmappedAction"></a>
The default action to apply to content that has no sensitivity label or whose label is not mapped. Valid values are `ALLOW`, `BLOCK`, and `WARN`.
Type: String
Valid Values: `ALLOW | WARN | BLOCK`
Required: Yes

## See Also
<a name="API_MicrosoftPurviewProviderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/MicrosoftPurviewProviderConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/MicrosoftPurviewProviderConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/MicrosoftPurviewProviderConfig)

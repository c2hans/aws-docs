---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ConfigurationListItem.html
---

# ConfigurationListItem
<a name="API_ConfigurationListItem"></a>

Configuration list item with summary information.

## Contents
<a name="API_ConfigurationListItem_Contents"></a>

 ** arn **   <a name="omics-Type-ConfigurationListItem-arn"></a>
Unique resource identifier for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 190.
Pattern: `arn:.+`
Required: No

 ** creationTime **   <a name="omics-Type-ConfigurationListItem-creationTime"></a>
Configuration creation timestamp.
Type: Timestamp
Required: No

 ** description **   <a name="omics-Type-ConfigurationListItem-description"></a>
Description for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** name **   <a name="omics-Type-ConfigurationListItem-name"></a>
User-friendly name for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: No

 ** status **   <a name="omics-Type-ConfigurationListItem-status"></a>
Current configuration status.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | DELETED | FAILED`
Required: No

## See Also
<a name="API_ConfigurationListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ConfigurationListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ConfigurationListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ConfigurationListItem)

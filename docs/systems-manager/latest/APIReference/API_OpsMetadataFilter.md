---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsMetadataFilter.html
---

# OpsMetadataFilter
<a name="API_OpsMetadataFilter"></a>

A filter to limit the number of OpsMetadata objects displayed.

## Contents
<a name="API_OpsMetadataFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-OpsMetadataFilter-Key"></a>
A filter key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!\s*$).+`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-OpsMetadataFilter-Values"></a>
A filter value.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_OpsMetadataFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsMetadataFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsMetadataFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsMetadataFilter)

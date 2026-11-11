---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AliasOperations.html
---

# AliasOperations
<a name="API_AliasOperations"></a>

The aliases to add to and remove from a pipeline version. An alias can't appear in both lists. After the update, the version can have up to 10 aliases.

## Contents
<a name="API_AliasOperations_Contents"></a>

 ** Add **   <a name="sagemaker-Type-AliasOperations-Add"></a>
The aliases to add to the pipeline version. If you assigned an alias to another version of the same pipeline, you must remove it from that version before you add it here.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9._\-]{1,128}`
Required: No

 ** Remove **   <a name="sagemaker-Type-AliasOperations-Remove"></a>
The aliases to remove from the pipeline version.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9._\-]{1,128}`
Required: No

## See Also
<a name="API_AliasOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AliasOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AliasOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AliasOperations)

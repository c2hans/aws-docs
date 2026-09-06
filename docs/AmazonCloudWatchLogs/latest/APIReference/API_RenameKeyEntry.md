---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_RenameKeyEntry.html
---

# RenameKeyEntry
<a name="API_RenameKeyEntry"></a>

This object defines one key that will be renamed with the [ renameKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-renameKey) processor.

## Contents
<a name="API_RenameKeyEntry_Contents"></a>

 ** key **   <a name="CWL-Type-RenameKeyEntry-key"></a>
The key to rename
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** renameTo **   <a name="CWL-Type-RenameKeyEntry-renameTo"></a>
The string to use for the new key name
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** overwriteIfExists **   <a name="CWL-Type-RenameKeyEntry-overwriteIfExists"></a>
Specifies whether to overwrite the existing value if the destination key already exists. The default is `false`
Type: Boolean
Required: No

## See Also
<a name="API_RenameKeyEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/RenameKeyEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/RenameKeyEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/RenameKeyEntry)

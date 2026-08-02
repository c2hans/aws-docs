---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_HomeDirectoryMapEntry.html
---

# HomeDirectoryMapEntry
<a name="API_HomeDirectoryMapEntry"></a>

Represents an object that contains entries and targets for `HomeDirectoryMappings`.

The following is an `Entry` and `Target` pair example for `chroot`.

 `[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]`

## Contents
<a name="API_HomeDirectoryMapEntry_Contents"></a>

 ** Entry **   <a name="TransferFamily-Type-HomeDirectoryMapEntry-Entry"></a>
Represents an entry for `HomeDirectoryMappings`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `/.*`
Required: Yes

 ** Target **   <a name="TransferFamily-Type-HomeDirectoryMapEntry-Target"></a>
Represents the map target that is used in a `HomeDirectoryMapEntry`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `/.*`
Required: Yes

 ** Type **   <a name="TransferFamily-Type-HomeDirectoryMapEntry-Type"></a>
Specifies the type of mapping. Set the type to `FILE` if you want the mapping to point to a file, or `DIRECTORY` for the directory to point to a directory.
By default, home directory mappings have a `Type` of `DIRECTORY` when you create a Transfer Family server. You would need to explicitly set `Type` to `FILE` if you want a mapping to have a file target.
Type: String
Valid Values: `FILE | DIRECTORY`
Required: No

## See Also
<a name="API_HomeDirectoryMapEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/HomeDirectoryMapEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/HomeDirectoryMapEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/HomeDirectoryMapEntry)

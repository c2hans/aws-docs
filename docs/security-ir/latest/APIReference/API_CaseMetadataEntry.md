---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CaseMetadataEntry.html
---

# CaseMetadataEntry
<a name="API_CaseMetadataEntry"></a>

Represents a single metadata entry associated with a case. Each entry consists of a key-value pair that provides additional contextual information about the case, such as classification tags, custom attributes, or system-generated properties.

## Contents
<a name="API_CaseMetadataEntry_Contents"></a>

 ** key **   <a name="securityir-Type-CaseMetadataEntry-key"></a>
The identifier for the metadata field. This key uniquely identifies the type of metadata being stored, such as "severity", "category", or "assignee".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** value **   <a name="securityir-Type-CaseMetadataEntry-value"></a>
The value associated with the metadata key. This contains the actual data for the metadata field identified by the key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

## See Also
<a name="API_CaseMetadataEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/CaseMetadataEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/CaseMetadataEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/CaseMetadataEntry)

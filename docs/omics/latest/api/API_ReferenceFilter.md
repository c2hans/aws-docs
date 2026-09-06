---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ReferenceFilter.html
---

# ReferenceFilter
<a name="API_ReferenceFilter"></a>

A filter for references.

## Contents
<a name="API_ReferenceFilter_Contents"></a>

 ** createdAfter **   <a name="omics-Type-ReferenceFilter-createdAfter"></a>
The filter's start date.
Type: Timestamp
Required: No

 ** createdBefore **   <a name="omics-Type-ReferenceFilter-createdBefore"></a>
The filter's end date.
Type: Timestamp
Required: No

 ** md5 **   <a name="omics-Type-ReferenceFilter-md5"></a>
An MD5 checksum to filter on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{N}]+`
Required: No

 ** name **   <a name="omics-Type-ReferenceFilter-name"></a>
A name to filter on.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_ReferenceFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ReferenceFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ReferenceFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ReferenceFilter)

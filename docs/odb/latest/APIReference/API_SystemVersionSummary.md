---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_SystemVersionSummary.html
---

# SystemVersionSummary
<a name="API_SystemVersionSummary"></a>

Information about the compatible system versions that can be used with a specific Exadata shape and Grid Infrastructure (GI) version.

## Contents
<a name="API_SystemVersionSummary_Contents"></a>

 ** giVersion **   <a name="odb-Type-SystemVersionSummary-giVersion"></a>
The version of GI software.
Type: String
Required: No

 ** shape **   <a name="odb-Type-SystemVersionSummary-shape"></a>
The Exadata hardware model.
Type: String
Required: No

 ** systemVersions **   <a name="odb-Type-SystemVersionSummary-systemVersions"></a>
The Exadata system versions that are compatible with the specified Exadata shape and GI version.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1024 items.
Required: No

## See Also
<a name="API_SystemVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/SystemVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/SystemVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/SystemVersionSummary)

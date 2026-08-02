---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_PoAttributes.html
---

# PoAttributes
<a name="API_PoAttributes"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

The supported properties for a PO type data set.

## Contents
<a name="API_PoAttributes_Contents"></a>

 ** format **   <a name="m2-Type-PoAttributes-format"></a>
The format of the data set records.
Type: String
Required: Yes

 ** memberFileExtensions **   <a name="m2-Type-PoAttributes-memberFileExtensions"></a>
An array containing one or more filename extensions, allowing you to specify which files to be included as PDS member.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Pattern: `\S{1,20}`
Required: Yes

 ** encoding **   <a name="m2-Type-PoAttributes-encoding"></a>
The character set encoding of the data set.
Type: String
Required: No

## See Also
<a name="API_PoAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/PoAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/PoAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/PoAttributes)

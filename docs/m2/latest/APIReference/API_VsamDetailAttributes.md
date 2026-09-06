---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_VsamDetailAttributes.html
---

# VsamDetailAttributes
<a name="API_VsamDetailAttributes"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

The attributes of a VSAM type data set.

## Contents
<a name="API_VsamDetailAttributes_Contents"></a>

 ** alternateKeys **   <a name="m2-Type-VsamDetailAttributes-alternateKeys"></a>
The alternate key definitions, if any. A legacy dataset might not have any alternate key defined, but if those alternate keys definitions exist, provide them as some applications will make use of them.
Type: Array of [AlternateKey](API_AlternateKey.md) objects
Required: No

 ** cacheAtStartup **   <a name="m2-Type-VsamDetailAttributes-cacheAtStartup"></a>
If set to True, enforces loading the data set into cache before it’s used by the application.
Type: Boolean
Required: No

 ** compressed **   <a name="m2-Type-VsamDetailAttributes-compressed"></a>
Indicates whether indexes for this dataset are stored as compressed values. If you have a large data set (typically > 100 Mb), consider setting this flag to True.
Type: Boolean
Required: No

 ** encoding **   <a name="m2-Type-VsamDetailAttributes-encoding"></a>
The character set used by the data set. Can be ASCII, EBCDIC, or unknown.
Type: String
Pattern: `\S{1,20}`
Required: No

 ** primaryKey **   <a name="m2-Type-VsamDetailAttributes-primaryKey"></a>
The primary key of the data set.
Type: [PrimaryKey](API_PrimaryKey.md) object
Required: No

 ** recordFormat **   <a name="m2-Type-VsamDetailAttributes-recordFormat"></a>
The record format of the data set.
Type: String
Pattern: `\S{1,20}`
Required: No

## See Also
<a name="API_VsamDetailAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/VsamDetailAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/VsamDetailAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/VsamDetailAttributes)

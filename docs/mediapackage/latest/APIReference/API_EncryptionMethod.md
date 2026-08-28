---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_EncryptionMethod.html
---

# EncryptionMethod
<a name="API_EncryptionMethod"></a>

The encryption type.

## Contents
<a name="API_EncryptionMethod_Contents"></a>

 ** CmafEncryptionMethod **   <a name="mediapackage-Type-EncryptionMethod-CmafEncryptionMethod"></a>
The encryption method to use.
Type: String
Valid Values: `CENC | CBCS`
Required: No

 ** IsmEncryptionMethod **   <a name="mediapackage-Type-EncryptionMethod-IsmEncryptionMethod"></a>
The encryption method used for Microsoft Smooth Streaming (MSS) content. This specifies how the MSS segments are encrypted to protect the content during delivery to client players.
Type: String
Valid Values: `CENC`
Required: No

 ** TsEncryptionMethod **   <a name="mediapackage-Type-EncryptionMethod-TsEncryptionMethod"></a>
The encryption method to use.
Type: String
Valid Values: `AES_128 | SAMPLE_AES`
Required: No

## See Also
<a name="API_EncryptionMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/EncryptionMethod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/EncryptionMethod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/EncryptionMethod)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

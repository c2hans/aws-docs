---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CustomCodeSigning.html
---

# CustomCodeSigning
<a name="API_CustomCodeSigning"></a>

Describes a custom method used to code sign a file.

## Contents
<a name="API_CustomCodeSigning_Contents"></a>

 ** certificateChain **   <a name="iot-Type-CustomCodeSigning-certificateChain"></a>
The certificate chain.
Type: [CodeSigningCertificateChain](API_CodeSigningCertificateChain.md) object
Required: No

 ** hashAlgorithm **   <a name="iot-Type-CustomCodeSigning-hashAlgorithm"></a>
The hash algorithm used to code sign the file. You can use a string as the algorithm name if the target over-the-air (OTA) update devices are able to verify the signature that was generated using the same signature algorithm. For example, FreeRTOS uses `SHA256` or `SHA1`, so you can pass either of them based on which was used for generating the signature.
Type: String
Required: No

 ** signature **   <a name="iot-Type-CustomCodeSigning-signature"></a>
The signature for the file.
Type: [CodeSigningSignature](API_CodeSigningSignature.md) object
Required: No

 ** signatureAlgorithm **   <a name="iot-Type-CustomCodeSigning-signatureAlgorithm"></a>
The signature algorithm used to code sign the file. You can use a string as the algorithm name if the target over-the-air (OTA) update devices are able to verify the signature that was generated using the same signature algorithm. For example, FreeRTOS uses `ECDSA` or `RSA`, so you can pass either of them based on which was used for generating the signature.
Type: String
Required: No

## See Also
<a name="API_CustomCodeSigning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CustomCodeSigning)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CustomCodeSigning)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CustomCodeSigning)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

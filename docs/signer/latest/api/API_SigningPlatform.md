---
source_url: https://docs.aws.amazon.com/signer/latest/api/API_SigningPlatform.html
---

# SigningPlatform
<a name="API_SigningPlatform"></a>

Contains information about the signing configurations and parameters that are used to perform a code-signing job.

## Contents
<a name="API_SigningPlatform_Contents"></a>

 ** category **   <a name="signer-Type-SigningPlatform-category"></a>
The category of a signing platform.
Type: String
Valid Values: `AWSIoT`
Required: No

 ** displayName **   <a name="signer-Type-SigningPlatform-displayName"></a>
The display name of a signing platform.
Type: String
Required: No

 ** maxSizeInMB **   <a name="signer-Type-SigningPlatform-maxSizeInMB"></a>
The maximum size (in MB) of code that can be signed by a signing platform.
Type: Integer
Required: No

 ** partner **   <a name="signer-Type-SigningPlatform-partner"></a>
Any partner entities linked to a signing platform.
Type: String
Required: No

 ** platformId **   <a name="signer-Type-SigningPlatform-platformId"></a>
The ID of a signing platform.
Type: String
Required: No

 ** revocationSupported **   <a name="signer-Type-SigningPlatform-revocationSupported"></a>
Indicates whether revocation is supported for the platform.
Type: Boolean
Required: No

 ** signingConfiguration **   <a name="signer-Type-SigningPlatform-signingConfiguration"></a>
The configuration of a signing platform. This includes the designated hash algorithm and encryption algorithm of a signing platform.
Type: [SigningConfiguration](API_SigningConfiguration.md) object
Required: No

 ** signingImageFormat **   <a name="signer-Type-SigningPlatform-signingImageFormat"></a>
The image format of a AWS Signer platform or profile.
Type: [SigningImageFormat](API_SigningImageFormat.md) object
Required: No

 ** target **   <a name="signer-Type-SigningPlatform-target"></a>
The types of targets that can be signed by a signing platform.
Type: String
Required: No

## See Also
<a name="API_SigningPlatform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/SigningPlatform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/SigningPlatform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/SigningPlatform)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

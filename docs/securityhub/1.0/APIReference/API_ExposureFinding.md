---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ExposureFinding.html
---

# ExposureFinding
<a name="API_ExposureFinding"></a>

Provides details about an exposure finding and the effect the specific remediation target has on it.

## Contents
<a name="API_ExposureFinding_Contents"></a>

 ** Impact **   <a name="securityhub-Type-ExposureFinding-Impact"></a>
The impact resolving a remediation target has on the exposure finding.
+  `Reduces` specifies that resolving the remediation target lowers the severity of the exposure finding, but does not resolve it.
+  `Resolves` specifies that resolving the remediation target resolves the exposure finding.
+  `Unchanged` specifies that resolving the remediation target does not change the severity of the exposure finding.
Type: String
Valid Values: `Reduces | Resolves | Unchanged`
Required: Yes

 ** MetadataUid **   <a name="securityhub-Type-ExposureFinding-MetadataUid"></a>
The unique identifier (ID) of the Security Hub exposure finding, found under the `metadata.uid` field of the finding.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** PreviousSeverity **   <a name="securityhub-Type-ExposureFinding-PreviousSeverity"></a>
The severity of the exposure finding before the remediation target is resolved.
Type: String
Valid Values: `Informational | Low | Medium | High | Critical`
Required: Yes

 ** ProjectedSeverity **   <a name="securityhub-Type-ExposureFinding-ProjectedSeverity"></a>
The severity of the exposure finding after the remediation target is resolved.
Type: String
Valid Values: `Informational | Low | Medium | High | Critical`
Required: Yes

 ** Title **   <a name="securityhub-Type-ExposureFinding-Title"></a>
The title of the exposure finding.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_ExposureFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ExposureFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ExposureFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ExposureFinding)

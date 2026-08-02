---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingProviderSeverity.html
---

# FindingProviderSeverity
<a name="API_FindingProviderSeverity"></a>

The severity assigned to a finding by the finding provider. This object may include one or more of the following attributes:
+  `Label`
+  `Normalized`
+  `Original`
+  `Product`

If a [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html) request for a new finding only provides `Label` or only provides `Normalized`, AWS Security Hub CSPM automatically populates the value of the other field.

The `Normalized` and `Product` attributes are included in the `FindingProviderSeverity` structure to preserve the historical information associated with the finding, even if the top-level `Severity` object is later modified using the [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html) operation.

If the top-level `Finding.Severity` object is present, but `Finding.FindingProviderFields` isn't present, Security Hub CSPM creates the `FindingProviderFields.Severity` object and copies the entire `Finding.Severity` object into it. This ensures that the original, provider-supplied details are retained within the `FindingProviderFields.Severity` object, even if the top-level `Severity` object is overwritten.

## Contents
<a name="API_FindingProviderSeverity_Contents"></a>

 ** Label **   <a name="securityhub-Type-FindingProviderSeverity-Label"></a>
The severity label assigned to the finding by the finding provider.
Type: String
Valid Values: `INFORMATIONAL | LOW | MEDIUM | HIGH | CRITICAL`
Required: No

 ** Original **   <a name="securityhub-Type-FindingProviderSeverity-Original"></a>
The finding provider's original value for the severity.
Length Constraints: Minimum length of 1. Maximum length of 64.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_FindingProviderSeverity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FindingProviderSeverity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FindingProviderSeverity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FindingProviderSeverity)

---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RemediationOutcome.html
---

# RemediationOutcome
<a name="API_RemediationOutcome"></a>

The outcome from resolving the remediation target.

## Contents
<a name="API_RemediationOutcome_Contents"></a>

 ** ResolvedFindingsCount **   <a name="securityhub-Type-RemediationOutcome-ResolvedFindingsCount"></a>
The number of associated exposure findings that are resolved by remediating the target.
Type: Integer
Required: Yes

 ** SeverityReductionFindingsCount **   <a name="securityhub-Type-RemediationOutcome-SeverityReductionFindingsCount"></a>
The number of associated exposure findings whose severity is reduced by remediating the target.
Type: Integer
Required: Yes

 ** SeverityUnchangedCount **   <a name="securityhub-Type-RemediationOutcome-SeverityUnchangedCount"></a>
The number of associated exposure findings whose severity is unchanged by remediating the target.
Type: Integer
Required: Yes

## See Also
<a name="API_RemediationOutcome_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RemediationOutcome)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RemediationOutcome)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RemediationOutcome)

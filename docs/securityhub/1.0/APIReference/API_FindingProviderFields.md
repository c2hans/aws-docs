---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingProviderFields.html
---

# FindingProviderFields
<a name="API_FindingProviderFields"></a>

In a [`BatchImportFindings`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html) request, finding providers use `FindingProviderFields` to provide and update values for the following fields:
+  `Confidence`
+  `Criticality`
+  `RelatedFindings`
+  `Severity`
+  `Types`

The preceding fields are nested under the `FindingProviderFields` object, but also have analogues of the same name as top-level ASFF fields. When a new finding is sent to AWS Security Hub CSPM by a finding provider, Security Hub CSPM populates the `FindingProviderFields` object automatically, if it is empty, based on the corresponding top-level fields.

Finding providers can update `FindingProviderFields` only by using the `BatchImportFindings` operation. Finding providers can't update this object with the [`BatchUpdateFindings`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html) operation. Customers can update the top-level fields by using the `BatchUpdateFindings` operation. Customers can't update `FindingProviderFields`.

For information about how Security Hub CSPM handles updates from `BatchImportFindings` to `FindingProviderFields` and to the corresponding top-level attributes, see [Using `FindingProviderFields`](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-update-batchimportfindings.html#batchimportfindings-findingproviderfields) in the * AWS Security Hub CSPM User Guide*.

## Contents
<a name="API_FindingProviderFields_Contents"></a>

 ** Confidence **   <a name="securityhub-Type-FindingProviderFields-Confidence"></a>
A finding's confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.
Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Criticality **   <a name="securityhub-Type-FindingProviderFields-Criticality"></a>
The level of importance assigned to the resources associated with the finding.
A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** RelatedFindings **   <a name="securityhub-Type-FindingProviderFields-RelatedFindings"></a>
A list of findings that are related to the current finding.
Type: Array of [RelatedFinding](API_RelatedFinding.md) objects
Required: No

 ** Severity **   <a name="securityhub-Type-FindingProviderFields-Severity"></a>
The severity of a finding.
Type: [FindingProviderSeverity](API_FindingProviderSeverity.md) object
Required: No

 ** Types **   <a name="securityhub-Type-FindingProviderFields-Types"></a>
One or more finding types in the format of `namespace/category/classifier` that classify a finding.
Valid namespace values are: Software and Configuration Checks \| TTPs \| Effects \| Unusual Behaviors \| Sensitive Data Identifications
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_FindingProviderFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FindingProviderFields)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FindingProviderFields)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FindingProviderFields)

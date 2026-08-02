---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindingsV2UnprocessedFinding.html
---

# BatchUpdateFindingsV2UnprocessedFinding
<a name="API_BatchUpdateFindingsV2UnprocessedFinding"></a>

The list of findings that were not updated.

## Contents
<a name="API_BatchUpdateFindingsV2UnprocessedFinding_Contents"></a>

 ** ErrorCode **   <a name="securityhub-Type-BatchUpdateFindingsV2UnprocessedFinding-ErrorCode"></a>
Indicates the specific type of error preventing successful processing of a finding during a batch update operation.
Type: String
Valid Values: `ResourceNotFoundException | ValidationException | InternalServerException | ConflictException`
Required: No

 ** ErrorMessage **   <a name="securityhub-Type-BatchUpdateFindingsV2UnprocessedFinding-ErrorMessage"></a>
A detailed description of why a finding could not be processed during a batch update operation.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FindingIdentifier **   <a name="securityhub-Type-BatchUpdateFindingsV2UnprocessedFinding-FindingIdentifier"></a>
The finding identifier of an unprocessed finding.
Type: [OcsfFindingIdentifier](API_OcsfFindingIdentifier.md) object
Required: No

 ** MetadataUid **   <a name="securityhub-Type-BatchUpdateFindingsV2UnprocessedFinding-MetadataUid"></a>
The metadata.uid of an unprocessed finding.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_BatchUpdateFindingsV2UnprocessedFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchUpdateFindingsV2UnprocessedFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchUpdateFindingsV2UnprocessedFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchUpdateFindingsV2UnprocessedFinding)

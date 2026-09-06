---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationCodeGenerationSegment.html
---

# NetworkMigrationCodeGenerationSegment
<a name="API_NetworkMigrationCodeGenerationSegment"></a>

A segment of generated code representing a logical grouping of infrastructure resources.

## Contents
<a name="API_NetworkMigrationCodeGenerationSegment_Contents"></a>

 ** artifacts **   <a name="mgn-Type-NetworkMigrationCodeGenerationSegment-artifacts"></a>
A list of artifacts generated for this segment.
Type: Array of [NetworkMigrationCodeGenerationArtifact](API_NetworkMigrationCodeGenerationArtifact.md) objects
Required: No

 ** createdAt **   <a name="mgn-Type-NetworkMigrationCodeGenerationSegment-createdAt"></a>
The timestamp when the segment was created.
Type: Timestamp
Required: No

 ** jobID **   <a name="mgn-Type-NetworkMigrationCodeGenerationSegment-jobID"></a>
The unique identifier of the code generation job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** logicalID **   <a name="mgn-Type-NetworkMigrationCodeGenerationSegment-logicalID"></a>
The logical identifier for the segment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*`
Required: No

 ** mapperSegmentID **   <a name="mgn-Type-NetworkMigrationCodeGenerationSegment-mapperSegmentID"></a>
The ID of the mapper segment that this code generation segment was created from.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** networkMigrationDefinitionID **   <a name="mgn-Type-NetworkMigrationCodeGenerationSegment-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: No

 ** networkMigrationExecutionID **   <a name="mgn-Type-NetworkMigrationCodeGenerationSegment-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** referencedSegments **   <a name="mgn-Type-NetworkMigrationCodeGenerationSegment-referencedSegments"></a>
A list of other segments that this segment depends on or references.
Type: Array of strings
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** segmentID **   <a name="mgn-Type-NetworkMigrationCodeGenerationSegment-segmentID"></a>
The unique identifier of the segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** segmentType **   <a name="mgn-Type-NetworkMigrationCodeGenerationSegment-segmentType"></a>
The type of the segment.
Type: String
Valid Values: `WORKLOAD | APPLIANCE | NETWORK`
Required: No

## See Also
<a name="API_NetworkMigrationCodeGenerationSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationCodeGenerationSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationCodeGenerationSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationCodeGenerationSegment)

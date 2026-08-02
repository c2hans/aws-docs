---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationMapperSegment.html
---

# NetworkMigrationMapperSegment
<a name="API_NetworkMigrationMapperSegment"></a>

## Contents
<a name="API_NetworkMigrationMapperSegment_Contents"></a>

 ** checksum **   <a name="mgn-Type-NetworkMigrationMapperSegment-checksum"></a>
The checksum of the segment data for integrity verification.
Type: [Checksum](API_Checksum.md) object
Required: No

 ** createdAt **   <a name="mgn-Type-NetworkMigrationMapperSegment-createdAt"></a>
The timestamp when the segment was created.
Type: Timestamp
Required: No

 ** description **   <a name="mgn-Type-NetworkMigrationMapperSegment-description"></a>
A description of the segment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 600.
Pattern: `[^\x00]*`
Required: No

 ** jobID **   <a name="mgn-Type-NetworkMigrationMapperSegment-jobID"></a>
The unique identifier of the job that created this segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** logicalID **   <a name="mgn-Type-NetworkMigrationMapperSegment-logicalID"></a>
The logical identifier for the segment in the infrastructure code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*`
Required: No

 ** name **   <a name="mgn-Type-NetworkMigrationMapperSegment-name"></a>
The name of the segment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`
Required: No

 ** networkMigrationDefinitionID **   <a name="mgn-Type-NetworkMigrationMapperSegment-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: No

 ** networkMigrationExecutionID **   <a name="mgn-Type-NetworkMigrationMapperSegment-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** outputS3Configuration **   <a name="mgn-Type-NetworkMigrationMapperSegment-outputS3Configuration"></a>
The S3 location where segment artifacts are stored.
Type: [S3Configuration](API_S3Configuration.md) object
Required: No

 ** referencedSegments **   <a name="mgn-Type-NetworkMigrationMapperSegment-referencedSegments"></a>
A list of other segments that this segment depends on or references.
Type: Array of strings
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** scopeTags **   <a name="mgn-Type-NetworkMigrationMapperSegment-scopeTags"></a>
Scope tags for the segment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 40 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z0-9\s+\-=._:/@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s+\-=._:/@]*`
Required: No

 ** segmentID **   <a name="mgn-Type-NetworkMigrationMapperSegment-segmentID"></a>
The unique identifier of the segment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** segmentType **   <a name="mgn-Type-NetworkMigrationMapperSegment-segmentType"></a>
The type of the segment, such as VPC, subnet, or security group.
Type: String
Valid Values: `WORKLOAD | APPLIANCE`
Required: No

 ** targetAccount **   <a name="mgn-Type-NetworkMigrationMapperSegment-targetAccount"></a>
The target AWS account where this segment will be deployed.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** updatedAt **   <a name="mgn-Type-NetworkMigrationMapperSegment-updatedAt"></a>
The timestamp when the segment was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_NetworkMigrationMapperSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationMapperSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationMapperSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationMapperSegment)

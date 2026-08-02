---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationMapperSegmentConstruct.html
---

# NetworkMigrationMapperSegmentConstruct
<a name="API_NetworkMigrationMapperSegmentConstruct"></a>

Represents a construct within a mapper segment. A construct is an individual infrastructure component such as a VPC, subnet, security group, route table, or other network resource that is part of the network migration.

## Contents
<a name="API_NetworkMigrationMapperSegmentConstruct_Contents"></a>

 ** constructID **   <a name="mgn-Type-NetworkMigrationMapperSegmentConstruct-constructID"></a>
The unique identifier of the construct.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** constructType **   <a name="mgn-Type-NetworkMigrationMapperSegmentConstruct-constructType"></a>
The type of the construct, such as VPC, subnet, security group, or route table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 24.
Pattern: `AWS::([A-Z\d]){2,10}::[a-zA-Z\d]{2,30}`
Required: No

 ** createdAt **   <a name="mgn-Type-NetworkMigrationMapperSegmentConstruct-createdAt"></a>
The timestamp when the construct was created.
Type: Timestamp
Required: No

 ** description **   <a name="mgn-Type-NetworkMigrationMapperSegmentConstruct-description"></a>
A description of the construct.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 600.
Pattern: `[^\x00]*`
Required: No

 ** excluded **   <a name="mgn-Type-NetworkMigrationMapperSegmentConstruct-excluded"></a>
Whether this construct is excluded from the migration.
Type: Boolean
Required: No

 ** logicalID **   <a name="mgn-Type-NetworkMigrationMapperSegmentConstruct-logicalID"></a>
The logical identifier for the construct in the infrastructure code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*`
Required: No

 ** name **   <a name="mgn-Type-NetworkMigrationMapperSegmentConstruct-name"></a>
The name of the construct.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`
Required: No

 ** properties **   <a name="mgn-Type-NetworkMigrationMapperSegmentConstruct-properties"></a>
The properties and configuration of the construct.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 0. Maximum length of 24.
Value Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

 ** updatedAt **   <a name="mgn-Type-NetworkMigrationMapperSegmentConstruct-updatedAt"></a>
The timestamp when the construct was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_NetworkMigrationMapperSegmentConstruct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationMapperSegmentConstruct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationMapperSegmentConstruct)

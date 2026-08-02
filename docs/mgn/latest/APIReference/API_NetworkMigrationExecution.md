---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationExecution.html
---

# NetworkMigrationExecution
<a name="API_NetworkMigrationExecution"></a>

Details about a network migration execution instance.

## Contents
<a name="API_NetworkMigrationExecution_Contents"></a>

 ** activity **   <a name="mgn-Type-NetworkMigrationExecution-activity"></a>
The current activity being performed in the execution.
Type: String
Valid Values: `MAPPING | MAPPING_UPDATE | CODE_GENERATION | DEPLOY | DEPLOYED_STACKS_DELETION | ANALYZE`
Required: No

 ** createdAt **   <a name="mgn-Type-NetworkMigrationExecution-createdAt"></a>
The timestamp when the execution was created.
Type: Timestamp
Required: No

 ** networkMigrationDefinitionID **   <a name="mgn-Type-NetworkMigrationExecution-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition used by this execution.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: No

 ** networkMigrationExecutionID **   <a name="mgn-Type-NetworkMigrationExecution-networkMigrationExecutionID"></a>
The unique identifier of the execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** stage **   <a name="mgn-Type-NetworkMigrationExecution-stage"></a>
The current stage of the execution in the migration workflow.
Type: String
Valid Values: `MAPPING | CODE_GENERATION | DEPLOY | DEPLOYED_STACKS_DELETION | ANALYZE`
Required: No

 ** status **   <a name="mgn-Type-NetworkMigrationExecution-status"></a>
The current status of the execution.
Type: String
Valid Values: `PENDING | STARTED | SUCCEEDED | FAILED`
Required: No

 ** tags **   <a name="mgn-Type-NetworkMigrationExecution-tags"></a>
Tags assigned to the execution.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** updatedAt **   <a name="mgn-Type-NetworkMigrationExecution-updatedAt"></a>
The timestamp when the execution was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_NetworkMigrationExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationExecution)

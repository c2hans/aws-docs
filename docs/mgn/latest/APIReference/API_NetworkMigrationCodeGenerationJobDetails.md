---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationCodeGenerationJobDetails.html
---

# NetworkMigrationCodeGenerationJobDetails
<a name="API_NetworkMigrationCodeGenerationJobDetails"></a>

Details about a network migration code generation job.

## Contents
<a name="API_NetworkMigrationCodeGenerationJobDetails_Contents"></a>

 ** codeGenerationOutputFormatStatusDetailsMap **   <a name="mgn-Type-NetworkMigrationCodeGenerationJobDetails-codeGenerationOutputFormatStatusDetailsMap"></a>
A map of output format types to their status details.
Type: String to [CodeGenerationOutputFormatStatusDetails](API_CodeGenerationOutputFormatStatusDetails.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Valid Keys: `CDK_L1 | CDK_L2 | TERRAFORM | LZA`
Required: No

 ** createdAt **   <a name="mgn-Type-NetworkMigrationCodeGenerationJobDetails-createdAt"></a>
The timestamp when the job was created.
Type: Timestamp
Required: No

 ** endedAt **   <a name="mgn-Type-NetworkMigrationCodeGenerationJobDetails-endedAt"></a>
The timestamp when the job completed or failed.
Type: Timestamp
Required: No

 ** jobID **   <a name="mgn-Type-NetworkMigrationCodeGenerationJobDetails-jobID"></a>
The unique identifier of the code generation job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** networkMigrationDefinitionID **   <a name="mgn-Type-NetworkMigrationCodeGenerationJobDetails-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: No

 ** networkMigrationExecutionID **   <a name="mgn-Type-NetworkMigrationCodeGenerationJobDetails-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** status **   <a name="mgn-Type-NetworkMigrationCodeGenerationJobDetails-status"></a>
The current status of the code generation job.
Type: String
Valid Values: `PENDING | STARTED | SUCCEEDED | FAILED`
Required: No

 ** statusDetails **   <a name="mgn-Type-NetworkMigrationCodeGenerationJobDetails-statusDetails"></a>
Detailed status information about the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

## See Also
<a name="API_NetworkMigrationCodeGenerationJobDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationCodeGenerationJobDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationCodeGenerationJobDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationCodeGenerationJobDetails)

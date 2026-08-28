---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationDeployerJobDetails.html
---

# NetworkMigrationDeployerJobDetails
<a name="API_NetworkMigrationDeployerJobDetails"></a>

Details about a network migration deployer job.

## Contents
<a name="API_NetworkMigrationDeployerJobDetails_Contents"></a>

 ** createdAt **   <a name="mgn-Type-NetworkMigrationDeployerJobDetails-createdAt"></a>
The timestamp when the job was created.
Type: Timestamp
Required: No

 ** endedAt **   <a name="mgn-Type-NetworkMigrationDeployerJobDetails-endedAt"></a>
The timestamp when the job completed or failed.
Type: Timestamp
Required: No

 ** jobID **   <a name="mgn-Type-NetworkMigrationDeployerJobDetails-jobID"></a>
The unique identifier of the deployer job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** networkMigrationDefinitionID **   <a name="mgn-Type-NetworkMigrationDeployerJobDetails-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: No

 ** networkMigrationExecutionID **   <a name="mgn-Type-NetworkMigrationDeployerJobDetails-networkMigrationExecutionID"></a>
The unique identifier of the network migration execution.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** status **   <a name="mgn-Type-NetworkMigrationDeployerJobDetails-status"></a>
The current status of the deployer job.
Type: String
Valid Values: `PENDING | STARTED | SUCCEEDED | FAILED`
Required: No

 ** statusDetails **   <a name="mgn-Type-NetworkMigrationDeployerJobDetails-statusDetails"></a>
Detailed status information about the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

## See Also
<a name="API_NetworkMigrationDeployerJobDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationDeployerJobDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationDeployerJobDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationDeployerJobDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

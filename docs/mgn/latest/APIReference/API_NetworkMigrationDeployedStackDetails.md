---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_NetworkMigrationDeployedStackDetails.html
---

# NetworkMigrationDeployedStackDetails
<a name="API_NetworkMigrationDeployedStackDetails"></a>

Details about a CloudFormation stack that has been deployed as part of the network migration.

## Contents
<a name="API_NetworkMigrationDeployedStackDetails_Contents"></a>

 ** failedResources **   <a name="mgn-Type-NetworkMigrationDeployedStackDetails-failedResources"></a>
A list of resources that failed to deploy.
Type: Array of [NetworkMigrationFailedResourceDetails](API_NetworkMigrationFailedResourceDetails.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** segmentID **   <a name="mgn-Type-NetworkMigrationDeployedStackDetails-segmentID"></a>
The ID of the segment that this stack was deployed for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** stackLogicalID **   <a name="mgn-Type-NetworkMigrationDeployedStackDetails-stackLogicalID"></a>
The logical ID of the stack.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z][a-zA-Z0-9-]*`
Required: No

 ** stackPhysicalID **   <a name="mgn-Type-NetworkMigrationDeployedStackDetails-stackPhysicalID"></a>
The physical ID of the CloudFormation stack.
Type: String
Length Constraints: Minimum length of 86. Maximum length of 128.
Pattern: `arn:aws:cloudformation:[a-z0-9-]+:[0-9]{12}:stack/[a-zA-Z0-9-]+/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** status **   <a name="mgn-Type-NetworkMigrationDeployedStackDetails-status"></a>
The current status of the deployed stack.
Type: String
Valid Values: `CREATE_COMPLETE | CREATE_FAILED | CREATE_STARTED | DELETE_COMPLETE | DELETE_FAILED | DELETE_STARTED`
Required: No

 ** targetAccount **   <a name="mgn-Type-NetworkMigrationDeployedStackDetails-targetAccount"></a>
The target AWS account where the stack was deployed.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

## See Also
<a name="API_NetworkMigrationDeployedStackDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/NetworkMigrationDeployedStackDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/NetworkMigrationDeployedStackDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/NetworkMigrationDeployedStackDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

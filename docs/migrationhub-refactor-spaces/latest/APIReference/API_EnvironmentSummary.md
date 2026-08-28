---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_EnvironmentSummary.html
---

# EnvironmentSummary
<a name="API_EnvironmentSummary"></a>

The summary information for environments as a response to `ListEnvironments`.

## Contents
<a name="API_EnvironmentSummary_Contents"></a>

 ** Arn **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-Arn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** CreatedTime **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-CreatedTime"></a>
A timestamp that indicates when the environment is created.
Type: Timestamp
Required: No

 ** Description **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-Description"></a>
A description of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_\s\.\!\*\#\@\']+`
Required: No

 ** EnvironmentId **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-EnvironmentId"></a>
The unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: No

 ** Error **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-Error"></a>
Any error associated with the environment resource.
Type: [ErrorResponse](API_ErrorResponse.md) object
Required: No

 ** LastUpdatedTime **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-LastUpdatedTime"></a>
A timestamp that indicates when the environment was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-Name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!env-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`
Required: No

 ** NetworkFabricType **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-NetworkFabricType"></a>
The network fabric type of the environment.
Type: String
Valid Values: `TRANSIT_GATEWAY | NONE`
Required: No

 ** OwnerAccountId **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-OwnerAccountId"></a>
The AWS account ID of the environment owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** State **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-State"></a>
The current state of the environment.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`
Required: No

 ** Tags **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-Tags"></a>
The tags assigned to the environment.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** TransitGatewayId **   <a name="migrationhubrefactorspaces-Type-EnvironmentSummary-TransitGatewayId"></a>
The ID of the AWS Transit Gateway set up by the environment.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `tgw-[-a-f0-9]{17}`
Required: No

## See Also
<a name="API_EnvironmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/EnvironmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/EnvironmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/EnvironmentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub Refactor Spaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-refactor-spaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

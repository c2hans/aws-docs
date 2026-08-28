---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_DevEnvironmentSummary.html
---

# DevEnvironmentSummary
<a name="API_DevEnvironmentSummary"></a>

Information about a Dev Environment.

## Contents
<a name="API_DevEnvironmentSummary_Contents"></a>

 ** creatorId **   <a name="codecatalyst-Type-DevEnvironmentSummary-creatorId"></a>
The system-generated unique ID of the user who created the Dev Environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

 ** id **   <a name="codecatalyst-Type-DevEnvironmentSummary-id"></a>
The system-generated unique ID for the Dev Environment.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** inactivityTimeoutMinutes **   <a name="codecatalyst-Type-DevEnvironmentSummary-inactivityTimeoutMinutes"></a>
The amount of time the Dev Environment will run without any activity detected before stopping, in minutes. Dev Environments consume compute minutes when running.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1200.
Required: Yes

 ** instanceType **   <a name="codecatalyst-Type-DevEnvironmentSummary-instanceType"></a>
The Amazon EC2 instace type used for the Dev Environment.
Type: String
Valid Values: `dev.standard1.small | dev.standard1.medium | dev.standard1.large | dev.standard1.xlarge`
Required: Yes

 ** lastUpdatedTime **   <a name="codecatalyst-Type-DevEnvironmentSummary-lastUpdatedTime"></a>
The time when the Dev Environment was last updated, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp
Required: Yes

 ** persistentStorage **   <a name="codecatalyst-Type-DevEnvironmentSummary-persistentStorage"></a>
Information about the configuration of persistent storage for the Dev Environment.
Type: [PersistentStorage](API_PersistentStorage.md) object
Required: Yes

 ** repositories **   <a name="codecatalyst-Type-DevEnvironmentSummary-repositories"></a>
Information about the repositories that will be cloned into the Dev Environment. If no rvalue is specified, no repository is cloned.
Type: Array of [DevEnvironmentRepositorySummary](API_DevEnvironmentRepositorySummary.md) objects
Required: Yes

 ** status **   <a name="codecatalyst-Type-DevEnvironmentSummary-status"></a>
The status of the Dev Environment.
Type: String
Valid Values: `PENDING | RUNNING | STARTING | STOPPING | STOPPED | FAILED | DELETING | DELETED`
Required: Yes

 ** alias **   <a name="codecatalyst-Type-DevEnvironmentSummary-alias"></a>
The user-specified alias for the Dev Environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** ides **   <a name="codecatalyst-Type-DevEnvironmentSummary-ides"></a>
Information about the integrated development environment (IDE) configured for a Dev Environment.
Type: Array of [Ide](API_Ide.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** projectName **   <a name="codecatalyst-Type-DevEnvironmentSummary-projectName"></a>
The name of the project in the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: No

 ** spaceName **   <a name="codecatalyst-Type-DevEnvironmentSummary-spaceName"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: No

 ** statusReason **   <a name="codecatalyst-Type-DevEnvironmentSummary-statusReason"></a>
The reason for the status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** vpcConnectionName **   <a name="codecatalyst-Type-DevEnvironmentSummary-vpcConnectionName"></a>
The name of the connection used to connect to Amazon VPC used when the Dev Environment was created, if any.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: No

## See Also
<a name="API_DevEnvironmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/DevEnvironmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/DevEnvironmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/DevEnvironmentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

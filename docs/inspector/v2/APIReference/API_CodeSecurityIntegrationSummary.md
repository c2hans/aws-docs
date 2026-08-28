---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeSecurityIntegrationSummary.html
---

# CodeSecurityIntegrationSummary
<a name="API_CodeSecurityIntegrationSummary"></a>

A summary of information about a code security integration.

## Contents
<a name="API_CodeSecurityIntegrationSummary_Contents"></a>

 ** createdOn **   <a name="inspector2-Type-CodeSecurityIntegrationSummary-createdOn"></a>
The timestamp when the code security integration was created.
Type: Timestamp
Required: Yes

 ** integrationArn **   <a name="inspector2-Type-CodeSecurityIntegrationSummary-integrationArn"></a>
The Amazon Resource Name (ARN) of the code security integration.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration/[a-f0-9-]{36}`
Required: Yes

 ** lastUpdateOn **   <a name="inspector2-Type-CodeSecurityIntegrationSummary-lastUpdateOn"></a>
The timestamp when the code security integration was last updated.
Type: Timestamp
Required: Yes

 ** name **   <a name="inspector2-Type-CodeSecurityIntegrationSummary-name"></a>
The name of the code security integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[a-zA-Z0-9-_$:.]*`
Required: Yes

 ** status **   <a name="inspector2-Type-CodeSecurityIntegrationSummary-status"></a>
The current status of the code security integration.
Type: String
Valid Values: `PENDING | IN_PROGRESS | ACTIVE | INACTIVE | DISABLING`
Required: Yes

 ** statusReason **   <a name="inspector2-Type-CodeSecurityIntegrationSummary-statusReason"></a>
The reason for the current status of the code security integration.
Type: String
Required: Yes

 ** type **   <a name="inspector2-Type-CodeSecurityIntegrationSummary-type"></a>
The type of repository provider for the integration.
Type: String
Valid Values: `GITLAB_SELF_MANAGED | GITHUB`
Required: Yes

 ** tags **   <a name="inspector2-Type-CodeSecurityIntegrationSummary-tags"></a>
The tags associated with the code security integration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_CodeSecurityIntegrationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeSecurityIntegrationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeSecurityIntegrationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeSecurityIntegrationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

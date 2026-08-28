---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_MicrovmImageBuildSummary.html
---

# MicrovmImageBuildSummary
<a name="API_MicrovmImageBuildSummary"></a>

Contains summary information about a MicroVM image build.

## Contents
<a name="API_MicrovmImageBuildSummary_Contents"></a>

 ** architecture **   <a name="lambdamicrovm-Type-MicrovmImageBuildSummary-architecture"></a>
The target CPU architecture for the build. Supported value: ARM\_64.
Type: String
Valid Values: `ARM_64`
Required: Yes

 ** buildId **   <a name="lambdamicrovm-Type-MicrovmImageBuildSummary-buildId"></a>
The build request ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** buildState **   <a name="lambdamicrovm-Type-MicrovmImageBuildSummary-buildState"></a>
The current state of the build.
Type: String
Valid Values: `PENDING | IN_PROGRESS | SUCCESSFUL | FAILED`
Required: Yes

 ** chipset **   <a name="lambdamicrovm-Type-MicrovmImageBuildSummary-chipset"></a>
The target chipset for the build.
Type: String
Valid Values: `GRAVITON`
Required: Yes

 ** chipsetGeneration **   <a name="lambdamicrovm-Type-MicrovmImageBuildSummary-chipsetGeneration"></a>
The target chipset generation for the build.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** createdAt **   <a name="lambdamicrovm-Type-MicrovmImageBuildSummary-createdAt"></a>
The timestamp when the build was created.
Type: Timestamp
Required: Yes

 ** imageArn **   <a name="lambdamicrovm-Type-MicrovmImageBuildSummary-imageArn"></a>
The ARN of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** imageVersion **   <a name="lambdamicrovm-Type-MicrovmImageBuildSummary-imageVersion"></a>
The version of the MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** stateReason **   <a name="lambdamicrovm-Type-MicrovmImageBuildSummary-stateReason"></a>
The reason for the build state, if applicable.
Type: String
Required: No

## See Also
<a name="API_MicrovmImageBuildSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/MicrovmImageBuildSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/MicrovmImageBuildSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/MicrovmImageBuildSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda MicroVMs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_WorkGroupSummary.html
---

# WorkGroupSummary
<a name="API_WorkGroupSummary"></a>

The summary information for the workgroup, which includes its name, state, description, and the date and time it was created.

## Contents
<a name="API_WorkGroupSummary_Contents"></a>

 ** CreationTime **   <a name="athena-Type-WorkGroupSummary-CreationTime"></a>
The workgroup creation date and time.
Type: Timestamp
Required: No

 ** Description **   <a name="athena-Type-WorkGroupSummary-Description"></a>
The workgroup description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** EngineVersion **   <a name="athena-Type-WorkGroupSummary-EngineVersion"></a>
The engine version setting for all queries on the workgroup. Queries on the `AmazonAthenaPreviewFunctionality` workgroup run on the preview engine regardless of this setting.
Type: [EngineVersion](API_EngineVersion.md) object
Required: No

 ** IdentityCenterApplicationArn **   <a name="athena-Type-WorkGroupSummary-IdentityCenterApplicationArn"></a>
The ARN of the IAM Identity Center enabled application associated with the workgroup.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}$`
Required: No

 ** Name **   <a name="athena-Type-WorkGroupSummary-Name"></a>
The name of the workgroup.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: No

 ** State **   <a name="athena-Type-WorkGroupSummary-State"></a>
The state of the workgroup.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_WorkGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/WorkGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/WorkGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/WorkGroupSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

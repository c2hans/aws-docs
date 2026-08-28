---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_S3ReportOutputConfiguration.html
---

# S3ReportOutputConfiguration
<a name="API_S3ReportOutputConfiguration"></a>

S3 configuration for report output.

## Contents
<a name="API_S3ReportOutputConfiguration_Contents"></a>

 ** bucketOwner **   <a name="ngresiliencehub-Type-S3ReportOutputConfiguration-bucketOwner"></a>
Account ID of the bucket owner for cross-account access verification.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** bucketPath **   <a name="ngresiliencehub-Type-S3ReportOutputConfiguration-bucketPath"></a>
S3 bucket path where reports will be written (e.g., my-bucket/ngrh-reports/).
Type: String
Length Constraints: Minimum length of 3. Maximum length of 512.
Pattern: `(s3://)?[a-z0-9][a-z0-9.-]{1,61}[a-z0-9](/.*)?`
Required: Yes

## See Also
<a name="API_S3ReportOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/S3ReportOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/S3ReportOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/S3ReportOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

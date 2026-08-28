---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DefaultExportDestination.html
---

# DefaultExportDestination
<a name="API_DefaultExportDestination"></a>

The default s3 bucket where Audit Manager saves the files that you export from evidence finder.

## Contents
<a name="API_DefaultExportDestination_Contents"></a>

 ** destination **   <a name="auditmanager-Type-DefaultExportDestination-destination"></a>
The destination bucket where Audit Manager stores exported files.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(S|s)3:\/\/[a-zA-Z0-9\-\.\(\)\'\*\_\!\=\+\@\:\s\,\?\/]+$`
Required: No

 ** destinationType **   <a name="auditmanager-Type-DefaultExportDestination-destinationType"></a>
The destination type, such as Amazon S3.
Type: String
Valid Values: `S3`
Required: No

## See Also
<a name="API_DefaultExportDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/DefaultExportDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/DefaultExportDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/DefaultExportDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

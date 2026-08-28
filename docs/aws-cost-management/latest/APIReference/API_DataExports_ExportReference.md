---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ExportReference.html
---

# ExportReference
<a name="API_DataExports_ExportReference"></a>

The reference details for a given export.

## Contents
<a name="API_DataExports_ExportReference_Contents"></a>

 ** ExportArn **   <a name="awscostmanagement-Type-DataExports_ExportReference-ExportArn"></a>
The Amazon Resource Name (ARN) for this export.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:(bcm-data-exports):[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

 ** ExportName **   <a name="awscostmanagement-Type-DataExports_ExportReference-ExportName"></a>
The name of this specific data export.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9A-Za-z\-_]+`
Required: Yes

 ** ExportStatus **   <a name="awscostmanagement-Type-DataExports_ExportReference-ExportStatus"></a>
The status of this specific data export.
Type: [ExportStatus](API_DataExports_ExportStatus.md) object
Required: Yes

## See Also
<a name="API_DataExports_ExportReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/ExportReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/ExportReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/ExportReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

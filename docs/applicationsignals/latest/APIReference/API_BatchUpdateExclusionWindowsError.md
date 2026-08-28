---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchUpdateExclusionWindowsError.html
---

# BatchUpdateExclusionWindowsError
<a name="API_BatchUpdateExclusionWindowsError"></a>

An array of structures, where each structure includes an error indicating that one of the requests in the array was not valid.

## Contents
<a name="API_BatchUpdateExclusionWindowsError_Contents"></a>

 ** ErrorCode **   <a name="applicationsignals-Type-BatchUpdateExclusionWindowsError-ErrorCode"></a>
The error code.
Type: String
Required: Yes

 ** ErrorMessage **   <a name="applicationsignals-Type-BatchUpdateExclusionWindowsError-ErrorMessage"></a>
The error message.
Type: String
Required: Yes

 ** SloId **   <a name="applicationsignals-Type-BatchUpdateExclusionWindowsError-SloId"></a>
The SLO ID in the error.
Type: String
Pattern: `[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]$|^arn:(aws|aws-us-gov):application-signals:[^:]*:[^:]*:slo/[0-9A-Za-z][-._0-9A-Za-z ]{0,126}[0-9A-Za-z]`
Required: Yes

## See Also
<a name="API_BatchUpdateExclusionWindowsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/BatchUpdateExclusionWindowsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/BatchUpdateExclusionWindowsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/BatchUpdateExclusionWindowsError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

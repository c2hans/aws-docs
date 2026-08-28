---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_S3Parameters.html
---

# S3Parameters
<a name="API_S3Parameters"></a>

The parameters for S3.

## Contents
<a name="API_S3Parameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ManifestFileLocation **   <a name="QS-Type-S3Parameters-ManifestFileLocation"></a>
Location of the Amazon S3 manifest file. This is NULL if the manifest file was uploaded into Quick Sight.
Type: [ManifestFileLocation](API_ManifestFileLocation.md) object
Required: Yes

 ** RoleArn **   <a name="QS-Type-S3Parameters-RoleArn"></a>
Use the `RoleArn` structure to override an account-wide role for a specific S3 data source. For example, say an account administrator has turned off all S3 access with an account-wide role. The administrator can then use `RoleArn` to bypass the account-wide role and allow S3 access for the single S3 data source that is specified in the structure, even if the account-wide role forbidding S3 access is still active.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_S3Parameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/S3Parameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/S3Parameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/S3Parameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

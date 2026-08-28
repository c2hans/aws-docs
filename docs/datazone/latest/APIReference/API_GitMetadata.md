---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GitMetadata.html
---

# GitMetadata
<a name="API_GitMetadata"></a>

The Git metadata for a notebook sync operation in Amazon SageMaker Unified Studio. Contains information about the Git repository, branch, and commit associated with the notebook.

## Contents
<a name="API_GitMetadata_Contents"></a>

 ** branch **   <a name="datazone-Type-GitMetadata-branch"></a>
The name of the Git branch.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** commitHash **   <a name="datazone-Type-GitMetadata-commitHash"></a>
The commit hash in the Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** connectionId **   <a name="datazone-Type-GitMetadata-connectionId"></a>
The identifier of the Git connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** repository **   <a name="datazone-Type-GitMetadata-repository"></a>
The name of the Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** commitMessage **   <a name="datazone-Type-GitMetadata-commitMessage"></a>
The commit message associated with the Git commit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** committedAt **   <a name="datazone-Type-GitMetadata-committedAt"></a>
The timestamp of when the commit was made.
Type: Timestamp
Required: No

 ** fileName **   <a name="datazone-Type-GitMetadata-fileName"></a>
The name of the file in the Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_GitMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GitMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GitMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GitMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

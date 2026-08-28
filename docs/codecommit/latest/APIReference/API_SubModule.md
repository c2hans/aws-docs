---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_SubModule.html
---

# SubModule
<a name="API_SubModule"></a>

Returns information about a submodule reference in a repository folder.

## Contents
<a name="API_SubModule_Contents"></a>

 ** absolutePath **   <a name="CodeCommit-Type-SubModule-absolutePath"></a>
The fully qualified path to the folder that contains the reference to the submodule.
Type: String
Required: No

 ** commitId **   <a name="CodeCommit-Type-SubModule-commitId"></a>
The commit ID that contains the reference to the submodule.
Type: String
Required: No

 ** relativePath **   <a name="CodeCommit-Type-SubModule-relativePath"></a>
The relative path of the submodule from the folder where the query originated.
Type: String
Required: No

## See Also
<a name="API_SubModule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/SubModule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/SubModule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/SubModule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

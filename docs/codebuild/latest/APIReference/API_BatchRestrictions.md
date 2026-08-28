---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchRestrictions.html
---

# BatchRestrictions
<a name="API_BatchRestrictions"></a>

Specifies restrictions for the batch build.

## Contents
<a name="API_BatchRestrictions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** computeTypesAllowed **   <a name="CodeBuild-Type-BatchRestrictions-computeTypesAllowed"></a>
An array of strings that specify the compute types that are allowed for the batch build. See [Build environment compute types](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html) in the * AWS CodeBuild User Guide* for these values.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** fleetsAllowed **   <a name="CodeBuild-Type-BatchRestrictions-fleetsAllowed"></a>
An array of strings that specify the fleets that are allowed for the batch build. See [Run builds on reserved capacity fleets](https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.html) in the * AWS CodeBuild User Guide* for more information.
Type: Array of strings
Length Constraints: Minimum length of 1.
Required: No

 ** maximumBuildsAllowed **   <a name="CodeBuild-Type-BatchRestrictions-maximumBuildsAllowed"></a>
Specifies the maximum number of builds allowed.
Type: Integer
Required: No

## See Also
<a name="API_BatchRestrictions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/BatchRestrictions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/BatchRestrictions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/BatchRestrictions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

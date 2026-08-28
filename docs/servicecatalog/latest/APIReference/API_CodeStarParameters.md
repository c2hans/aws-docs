---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_CodeStarParameters.html
---

# CodeStarParameters
<a name="API_CodeStarParameters"></a>

The subtype containing details about the Codestar connection `Type`.

## Contents
<a name="API_CodeStarParameters_Contents"></a>

 ** ArtifactPath **   <a name="servicecatalog-Type-CodeStarParameters-ArtifactPath"></a>
The absolute path wehre the artifact resides within the repo and branch, formatted as "folder/file.json."
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** Branch **   <a name="servicecatalog-Type-CodeStarParameters-Branch"></a>
The specific branch where the artifact resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: Yes

 ** ConnectionArn **   <a name="servicecatalog-Type-CodeStarParameters-ConnectionArn"></a>
The CodeStar ARN, which is the connection between AWS Service Catalog and the external repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1224.
Pattern: `arn:[a-z0-9][-.a-z0-9]{0,62}:(codestar-connections|codeconnections):([a-z0-9][-.a-z0-9]{0,62})?:([a-z0-9][-.a-z0-9]{0,62})?:[^/].{0,1023}$`
Required: Yes

 ** Repository **   <a name="servicecatalog-Type-CodeStarParameters-Repository"></a>
The specific repository where the product’s artifact-to-be-synced resides, formatted as "Account/Repo."
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## See Also
<a name="API_CodeStarParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/CodeStarParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/CodeStarParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/CodeStarParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

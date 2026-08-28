---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ThirdPartySourceRepository.html
---

# ThirdPartySourceRepository
<a name="API_ThirdPartySourceRepository"></a>

Information about a third-party source repository connected to CodeGuru Reviewer.

## Contents
<a name="API_ThirdPartySourceRepository_Contents"></a>

 ** ConnectionArn **   <a name="reviewer-Type-ThirdPartySourceRepository-ConnectionArn"></a>
The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection. Its format is `arn:aws:codestar-connections:region-id:aws-account_id:connection/connection-id`. For more information, see [Connection](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_Connection.html) in the * AWS CodeStar Connections API Reference*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
Required: Yes

 ** Name **   <a name="reviewer-Type-ThirdPartySourceRepository-Name"></a>
The name of the third party source repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: Yes

 ** Owner **   <a name="reviewer-Type-ThirdPartySourceRepository-Owner"></a>
The owner of the repository. For a GitHub, GitHub Enterprise, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, this can be the username or AWS account ID
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: Yes

## See Also
<a name="API_ThirdPartySourceRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/ThirdPartySourceRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/ThirdPartySourceRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/ThirdPartySourceRepository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SignInDistribution.html
---

# SignInDistribution
<a name="API_SignInDistribution"></a>

The distribution of sign in traffic between the instance and its replica(s).

## Contents
<a name="API_SignInDistribution_Contents"></a>

 ** Enabled **   <a name="connect-Type-SignInDistribution-Enabled"></a>
Whether sign in distribution is enabled.
Type: Boolean
Required: Yes

 ** Region **   <a name="connect-Type-SignInDistribution-Region"></a>
The AWS Region of the sign in distribution.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 31.
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: Yes

## See Also
<a name="API_SignInDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SignInDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SignInDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SignInDistribution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

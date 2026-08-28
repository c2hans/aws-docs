---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EnvironmentResolvedAccount.html
---

# EnvironmentResolvedAccount
<a name="API_EnvironmentResolvedAccount"></a>

Specifies the account/Region that is to be used during project creation for a particular blueprint.

## Contents
<a name="API_EnvironmentResolvedAccount_Contents"></a>

 ** awsAccountId **   <a name="datazone-Type-EnvironmentResolvedAccount-awsAccountId"></a>
The ID of the resolved account.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** regionName **   <a name="datazone-Type-EnvironmentResolvedAccount-regionName"></a>
The name of the resolved Region.
Type: String
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`
Required: Yes

 ** sourceAccountPoolId **   <a name="datazone-Type-EnvironmentResolvedAccount-sourceAccountPoolId"></a>
The ID of the account pool.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## See Also
<a name="API_EnvironmentResolvedAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EnvironmentResolvedAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EnvironmentResolvedAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EnvironmentResolvedAccount)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

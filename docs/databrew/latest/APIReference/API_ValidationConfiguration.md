---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ValidationConfiguration.html
---

# ValidationConfiguration
<a name="API_ValidationConfiguration"></a>

Configuration for data quality validation. Used to select the Rulesets and Validation Mode to be used in the profile job. When ValidationConfiguration is null, the profile job will run without data quality validation.

## Contents
<a name="API_ValidationConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RulesetArn **   <a name="databrew-Type-ValidationConfiguration-RulesetArn"></a>
The Amazon Resource Name (ARN) for the ruleset to be validated in the profile job. The TargetArn of the selected ruleset should be the same as the Amazon Resource Name (ARN) of the dataset that is associated with the profile job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** ValidationMode **   <a name="databrew-Type-ValidationConfiguration-ValidationMode"></a>
Mode of data quality validation. Default mode is “CHECK\_ALL” which verifies all rules defined in the selected ruleset.
Type: String
Valid Values: `CHECK_ALL`
Required: No

## See Also
<a name="API_ValidationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ValidationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ValidationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ValidationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

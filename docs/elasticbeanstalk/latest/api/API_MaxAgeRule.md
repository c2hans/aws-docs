---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_MaxAgeRule.html
---

# MaxAgeRule
<a name="API_MaxAgeRule"></a>

A lifecycle rule that deletes application versions after the specified number of days.

## Contents
<a name="API_MaxAgeRule_Contents"></a>

 ** Enabled **
Specify `true` to apply the rule, or `false` to disable it.
Type: Boolean
Required: Yes

 ** DeleteSourceFromS3 **
Set to `true` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.
Type: Boolean
Required: No

 ** MaxAgeInDays **
Specify the number of days to retain an application versions.
Type: Integer
Required: No

## See Also
<a name="API_MaxAgeRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/MaxAgeRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/MaxAgeRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/MaxAgeRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

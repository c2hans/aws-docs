---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_MaxCountRule.html
---

# MaxCountRule
<a name="API_MaxCountRule"></a>

A lifecycle rule that deletes the oldest application version when the maximum count is exceeded.

## Contents
<a name="API_MaxCountRule_Contents"></a>

 ** Enabled **
Specify `true` to apply the rule, or `false` to disable it.
Type: Boolean
Required: Yes

 ** DeleteSourceFromS3 **
Set to `true` to delete a version's source bundle from Amazon S3 when Elastic Beanstalk deletes the application version.
Type: Boolean
Required: No

 ** MaxCount **
Specify the maximum number of application versions to retain.
Type: Integer
Required: No

## See Also
<a name="API_MaxCountRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/MaxCountRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/MaxCountRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/MaxCountRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplicationDescription.html
---

# ApplicationDescription
<a name="API_ApplicationDescription"></a>

Describes the properties of an application.

## Contents
<a name="API_ApplicationDescription_Contents"></a>

 ** ApplicationArn **
The Amazon Resource Name (ARN) of the application.
Type: String
Required: No

 ** ApplicationName **
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ConfigurationTemplates.member.N **
The names of the configuration templates associated with this application.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** DateCreated **
The date when the application was created.
Type: Timestamp
Required: No

 ** DateUpdated **
The date when the application was last modified.
Type: Timestamp
Required: No

 ** Description **
User-defined description of the application.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** ResourceLifecycleConfig **
The lifecycle settings for the application.
Type: [ApplicationResourceLifecycleConfig](API_ApplicationResourceLifecycleConfig.md) object
Required: No

 ** Versions.member.N **
The names of the versions for this application.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_ApplicationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ApplicationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ApplicationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ApplicationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

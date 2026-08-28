---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_EventDescription.html
---

# EventDescription
<a name="API_EventDescription"></a>

Describes an event.

## Contents
<a name="API_EventDescription_Contents"></a>

 ** ApplicationName **
The application associated with the event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** EnvironmentName **
The name of the environment associated with this event.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** EventDate **
The date when the event occurred.
Type: Timestamp
Required: No

 ** Message **
The event message.
Type: String
Required: No

 ** PlatformArn **
The ARN of the platform version.
Type: String
Required: No

 ** RequestId **
The web service request ID for the activity of this event.
Type: String
Required: No

 ** Severity **
The severity level of this event.
Type: String
Valid Values: `TRACE | DEBUG | INFO | WARN | ERROR | FATAL`
Required: No

 ** TemplateName **
The name of the configuration associated with this event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** VersionLabel **
The release label for the application version associated with this event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_EventDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/EventDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/EventDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/EventDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

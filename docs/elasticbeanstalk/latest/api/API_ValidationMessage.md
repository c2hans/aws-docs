---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ValidationMessage.html
---

# ValidationMessage
<a name="API_ValidationMessage"></a>

An error or warning for a desired configuration option value.

## Contents
<a name="API_ValidationMessage_Contents"></a>

 ** Message **
A message describing the error or warning.
Type: String
Required: No

 ** Namespace **
The namespace to which the option belongs.
Type: String
Required: No

 ** OptionName **
The name of the option.
Type: String
Required: No

 ** Severity **
An indication of the severity of this message:
+  `error`: This message indicates that this is not a valid setting for an option.
+  `warning`: This message is providing information you should take into account.
Type: String
Valid Values: `error | warning`
Required: No

## See Also
<a name="API_ValidationMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ValidationMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ValidationMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ValidationMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

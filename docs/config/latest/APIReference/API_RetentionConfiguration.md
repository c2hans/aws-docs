---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_RetentionConfiguration.html
---

# RetentionConfiguration
<a name="API_RetentionConfiguration"></a>

An object with the name of the retention configuration and the retention period in days. The object stores the configuration for data retention in AWS Config.

## Contents
<a name="API_RetentionConfiguration_Contents"></a>

 ** Name **   <a name="config-Type-RetentionConfiguration-Name"></a>
The name of the retention configuration object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w\-]+`
Required: Yes

 ** RetentionPeriodInDays **   <a name="config-Type-RetentionConfiguration-RetentionPeriodInDays"></a>
Number of days AWS Config stores your historical information.
Currently, only applicable to the configuration item history.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 2557.
Required: Yes

## See Also
<a name="API_RetentionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/RetentionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/RetentionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/RetentionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

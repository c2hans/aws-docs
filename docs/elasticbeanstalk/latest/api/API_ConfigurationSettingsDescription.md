---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ConfigurationSettingsDescription.html
---

# ConfigurationSettingsDescription
<a name="API_ConfigurationSettingsDescription"></a>

Describes the settings for a configuration set.

## Contents
<a name="API_ConfigurationSettingsDescription_Contents"></a>

 ** ApplicationName **
The name of the application associated with this configuration set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** DateCreated **
The date (in UTC time) when this configuration set was created.
Type: Timestamp
Required: No

 ** DateUpdated **
The date (in UTC time) when this configuration set was last modified.
Type: Timestamp
Required: No

 ** DeploymentStatus **
 If this configuration set is associated with an environment, the `DeploymentStatus` parameter indicates the deployment status of this configuration set:
+  `null`: This configuration is not associated with a running environment.
+  `pending`: This is a draft configuration that is not deployed to the associated environment but is in the process of deploying.
+  `deployed`: This is the configuration that is currently deployed to the associated running environment.
+  `failed`: This is a draft configuration that failed to successfully deploy.
Type: String
Valid Values: `deployed | pending | failed`
Required: No

 ** Description **
Describes this configuration set.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** EnvironmentName **
 If not `null`, the name of the environment for this configuration set.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** OptionSettings.member.N **
A list of the configuration options and their values in this configuration set.
Type: Array of [ConfigurationOptionSetting](API_ConfigurationOptionSetting.md) objects
Required: No

 ** PlatformArn **
The ARN of the platform version.
Type: String
Required: No

 ** SolutionStackName **
The name of the solution stack this configuration set uses.
Type: String
Required: No

 ** TemplateName **
 If not `null`, the name of the configuration template for this configuration set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_ConfigurationSettingsDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ConfigurationSettingsDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ConfigurationSettingsDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ConfigurationSettingsDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

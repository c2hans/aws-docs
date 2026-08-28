---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LaunchTemplateConfiguration.html
---

# LaunchTemplateConfiguration
<a name="API_LaunchTemplateConfiguration"></a>

Identifies an Amazon EC2 launch template to use for a specific account.

## Contents
<a name="API_LaunchTemplateConfiguration_Contents"></a>

 ** launchTemplateId **   <a name="imagebuilder-Type-LaunchTemplateConfiguration-launchTemplateId"></a>
Identifies the Amazon EC2 launch template to use.
Type: String
Pattern: `^lt-[a-z0-9-_]{17}$`
Required: Yes

 ** accountId **   <a name="imagebuilder-Type-LaunchTemplateConfiguration-accountId"></a>
The account ID that this configuration applies to.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** setDefaultVersion **   <a name="imagebuilder-Type-LaunchTemplateConfiguration-setDefaultVersion"></a>
Set the specified Amazon EC2 launch template as the default launch template for the specified account.
Type: Boolean
Required: No

## See Also
<a name="API_LaunchTemplateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LaunchTemplateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LaunchTemplateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LaunchTemplateConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for EC2 Image Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query imagebuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

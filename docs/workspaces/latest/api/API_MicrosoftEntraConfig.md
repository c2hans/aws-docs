---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_MicrosoftEntraConfig.html
---

# MicrosoftEntraConfig
<a name="API_MicrosoftEntraConfig"></a>

Specifies the configurations of the Microsoft Entra.

## Contents
<a name="API_MicrosoftEntraConfig_Contents"></a>

 ** ApplicationConfigSecretArn **   <a name="WorkSpaces-Type-MicrosoftEntraConfig-ApplicationConfigSecretArn"></a>
The Amazon Resource Name (ARN) of the application config.
Type: String
Pattern: `^arn:aws[a-z-]{0,7}:secretsmanager:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:secret:[A-Za-z0-9][A-za-z0-9_/.-]{8,519}$`
Required: No

 ** TenantId **   <a name="WorkSpaces-Type-MicrosoftEntraConfig-TenantId"></a>
The identifier of the tenant.
Type: String
Pattern: `^[a-zA-Z0-9-]{1,100}$`
Required: No

## See Also
<a name="API_MicrosoftEntraConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/MicrosoftEntraConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/MicrosoftEntraConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/MicrosoftEntraConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

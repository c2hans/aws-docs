---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-reference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# Transform reference
<a name="transform-reference"></a>

Transforms are macros hosted by CloudFormation. Unlike custom macros, a transform doesn't require any special permissions to use it because it is hosted by CloudFormation. Transforms can be used in templates in any account within CloudFormation. Also, there is no charge incurred when using transforms. CloudFormation treats a transform the same as any other macro in terms of evaluation order and scope.

For more information about how macros work, see [Using CloudFormation macros to perform custom processing on templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) in the *AWS CloudFormation User Guide*.

You can use the following transforms in your CloudFormation templates.

**Topics**
+ [`AWS::CodeDeployBlueGreen` transform](transform-aws-codedeploybluegreen.md)
+ [`AWS::Include` transform](transform-aws-include.md)
+ [`AWS::LanguageExtensions` transform](transform-aws-languageextensions.md)
+ [`AWS::SecretsManager` transform](transform-aws-secretsmanager.md)
+ [`AWS::Serverless` transform](transform-aws-serverless.md)
+ [`AWS::ServiceCatalog` transform](transform-aws-servicecatalog.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

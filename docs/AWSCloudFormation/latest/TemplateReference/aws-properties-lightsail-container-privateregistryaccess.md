---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-container-privateregistryaccess.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::Container PrivateRegistryAccess
<a name="aws-properties-lightsail-container-privateregistryaccess"></a>

Describes the configuration for an Amazon Lightsail container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.

For more information, see [Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access) in the *Amazon Lightsail Developer Guide*.

## Syntax
<a name="aws-properties-lightsail-container-privateregistryaccess-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-container-privateregistryaccess-syntax.json"></a>

```
{
  "[EcrImagePullerRole](#cfn-lightsail-container-privateregistryaccess-ecrimagepullerrole)" : {{EcrImagePullerRole}}
}
```

### YAML
<a name="aws-properties-lightsail-container-privateregistryaccess-syntax.yaml"></a>

```
  [EcrImagePullerRole](#cfn-lightsail-container-privateregistryaccess-ecrimagepullerrole): {{
    EcrImagePullerRole}}
```

## Properties
<a name="aws-properties-lightsail-container-privateregistryaccess-properties"></a>

`EcrImagePullerRole`  <a name="cfn-lightsail-container-privateregistryaccess-ecrimagepullerrole"></a>
An object that describes the activation status of the role that you can use to grant a Lightsail container service access to Amazon ECR private repositories. If the role is activated, the Amazon Resource Name (ARN) of the role is also listed.
*Required*: No
*Type*: [EcrImagePullerRole](aws-properties-lightsail-container-ecrimagepullerrole.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-serviceconnecttlscertificateauthority.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service ServiceConnectTlsCertificateAuthority
<a name="aws-properties-ecs-service-serviceconnecttlscertificateauthority"></a>

The certificate root authority that secures your service.

## Syntax
<a name="aws-properties-ecs-service-serviceconnecttlscertificateauthority-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-serviceconnecttlscertificateauthority-syntax.json"></a>

```
{
  "[AwsPcaAuthorityArn](#cfn-ecs-service-serviceconnecttlscertificateauthority-awspcaauthorityarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-serviceconnecttlscertificateauthority-syntax.yaml"></a>

```
  [AwsPcaAuthorityArn](#cfn-ecs-service-serviceconnecttlscertificateauthority-awspcaauthorityarn): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-serviceconnecttlscertificateauthority-properties"></a>

`AwsPcaAuthorityArn`  <a name="cfn-ecs-service-serviceconnecttlscertificateauthority-awspcaauthorityarn"></a>
The ARN of the AWS Private Certificate Authority certificate.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-service-serviceconnecttlscertificateauthority--seealso"></a>
+  [Associate an Application Load Balancer with a service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service--examples--Associate_an_Application_Load_Balancer_with_a_service)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-tenancyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function TenancyConfig
<a name="aws-properties-lambda-function-tenancyconfig"></a>

Specifies the tenant isolation mode configuration for a Lambda function. This allows you to configure specific tenant isolation strategies for your function invocations. Tenant isolation configuration cannot be modified after function creation.

## Syntax
<a name="aws-properties-lambda-function-tenancyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-tenancyconfig-syntax.json"></a>

```
{
  "[TenantIsolationMode](#cfn-lambda-function-tenancyconfig-tenantisolationmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-function-tenancyconfig-syntax.yaml"></a>

```
  [TenantIsolationMode](#cfn-lambda-function-tenancyconfig-tenantisolationmode): {{String}}
```

## Properties
<a name="aws-properties-lambda-function-tenancyconfig-properties"></a>

`TenantIsolationMode`  <a name="cfn-lambda-function-tenancyconfig-tenantisolationmode"></a>
Tenant isolation mode allows for invocation to be sent to a corresponding execution environment dedicated to a specific tenant ID.
*Required*: Yes
*Type*: String
*Allowed values*: `PER_TENANT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

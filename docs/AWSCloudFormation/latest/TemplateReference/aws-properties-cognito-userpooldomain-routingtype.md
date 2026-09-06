---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpooldomain-routingtype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolDomain RoutingType
<a name="aws-properties-cognito-userpooldomain-routingtype"></a>

Specifies routing configuration for user pool domains. Contains failover settings for multi-region deployments.

This data type is a request parameter of API\_CreateUserPoolDomain and API\_UpdateUserPoolDomain, and a response parameter of API\_DescribeUserPoolDomain.

## Syntax
<a name="aws-properties-cognito-userpooldomain-routingtype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpooldomain-routingtype-syntax.json"></a>

```
{
  "[Failover](#cfn-cognito-userpooldomain-routingtype-failover)" : {{FailoverType}}
}
```

### YAML
<a name="aws-properties-cognito-userpooldomain-routingtype-syntax.yaml"></a>

```
  [Failover](#cfn-cognito-userpooldomain-routingtype-failover): {{
    FailoverType}}
```

## Properties
<a name="aws-properties-cognito-userpooldomain-routingtype-properties"></a>

`Failover`  <a name="cfn-cognito-userpooldomain-routingtype-failover"></a>
The failover configuration that specifies the secondary region and health check settings.
*Required*: No
*Type*: [FailoverType](aws-properties-cognito-userpooldomain-failovertype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

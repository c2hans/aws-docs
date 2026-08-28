---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpooldomain-failovertype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolDomain FailoverType
<a name="aws-properties-cognito-userpooldomain-failovertype"></a>

Specifies failover configuration for multi-region user pool domains. Contains settings for the secondary region and health check configuration.

This data type is a request parameter of API\_CreateUserPoolDomain and API\_UpdateUserPoolDomain, and a response parameter of API\_DescribeUserPoolDomain.

## Syntax
<a name="aws-properties-cognito-userpooldomain-failovertype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpooldomain-failovertype-syntax.json"></a>

```
{
  "[PrimaryRoute53HealthCheckId](#cfn-cognito-userpooldomain-failovertype-primaryroute53healthcheckid)" : {{String}},
  "[SecondaryRegion](#cfn-cognito-userpooldomain-failovertype-secondaryregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpooldomain-failovertype-syntax.yaml"></a>

```
  [PrimaryRoute53HealthCheckId](#cfn-cognito-userpooldomain-failovertype-primaryroute53healthcheckid): {{String}}
  [SecondaryRegion](#cfn-cognito-userpooldomain-failovertype-secondaryregion): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpooldomain-failovertype-properties"></a>

`PrimaryRoute53HealthCheckId`  <a name="cfn-cognito-userpooldomain-failovertype-primaryroute53healthcheckid"></a>
The ID of the AWS Route53 healthcheck that controls routing. If the healthcheck is healthy, traffic will be routed to the primary replica, and if the healthcheck is unhealthy, traffic will be routed to the secondary region.
*Required*: Yes
*Type*: String
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryRegion`  <a name="cfn-cognito-userpooldomain-failovertype-secondaryregion"></a>
The secondary AWS Region to use for failover when the primary region becomes unavailable.
*Required*: Yes
*Type*: String
*Minimum*: `5`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

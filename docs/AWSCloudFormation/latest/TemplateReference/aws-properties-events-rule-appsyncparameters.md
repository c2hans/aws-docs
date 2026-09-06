---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-appsyncparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Rule AppSyncParameters
<a name="aws-properties-events-rule-appsyncparameters"></a>

Contains the GraphQL operation to be parsed and executed, if the event target is an AWS AppSync API.

## Syntax
<a name="aws-properties-events-rule-appsyncparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-rule-appsyncparameters-syntax.json"></a>

```
{
  "[GraphQLOperation](#cfn-events-rule-appsyncparameters-graphqloperation)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-rule-appsyncparameters-syntax.yaml"></a>

```
  [GraphQLOperation](#cfn-events-rule-appsyncparameters-graphqloperation): {{String}}
```

## Properties
<a name="aws-properties-events-rule-appsyncparameters-properties"></a>

`GraphQLOperation`  <a name="cfn-events-rule-appsyncparameters-graphqloperation"></a>
The GraphQL operation; that is, the query, mutation, or subscription to be parsed and executed by the GraphQL service.
For more information, see [Operations](https://docs.aws.amazon.com/appsync/latest/devguide/graphql-architecture.html#graphql-operations) in the *AWS AppSync User Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1048576`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

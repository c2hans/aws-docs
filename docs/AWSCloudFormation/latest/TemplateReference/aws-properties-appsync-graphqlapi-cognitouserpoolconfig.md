---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-graphqlapi-cognitouserpoolconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::GraphQLApi CognitoUserPoolConfig
<a name="aws-properties-appsync-graphqlapi-cognitouserpoolconfig"></a>

Describes an Amazon Cognito user pool configuration.

## Syntax
<a name="aws-properties-appsync-graphqlapi-cognitouserpoolconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-graphqlapi-cognitouserpoolconfig-syntax.json"></a>

```
{
  "[AppIdClientRegex](#cfn-appsync-graphqlapi-cognitouserpoolconfig-appidclientregex)" : {{String}},
  "[AwsRegion](#cfn-appsync-graphqlapi-cognitouserpoolconfig-awsregion)" : {{String}},
  "[UserPoolId](#cfn-appsync-graphqlapi-cognitouserpoolconfig-userpoolid)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-graphqlapi-cognitouserpoolconfig-syntax.yaml"></a>

```
  [AppIdClientRegex](#cfn-appsync-graphqlapi-cognitouserpoolconfig-appidclientregex): {{String}}
  [AwsRegion](#cfn-appsync-graphqlapi-cognitouserpoolconfig-awsregion): {{String}}
  [UserPoolId](#cfn-appsync-graphqlapi-cognitouserpoolconfig-userpoolid): {{String}}
```

## Properties
<a name="aws-properties-appsync-graphqlapi-cognitouserpoolconfig-properties"></a>

`AppIdClientRegex`  <a name="cfn-appsync-graphqlapi-cognitouserpoolconfig-appidclientregex"></a>
A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isn't set, no filtering is applied.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsRegion`  <a name="cfn-appsync-graphqlapi-cognitouserpoolconfig-awsregion"></a>
The AWS Region in which the user pool was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-appsync-graphqlapi-cognitouserpoolconfig-userpoolid"></a>
The user pool ID.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-api-cognitoconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Api CognitoConfig
<a name="aws-properties-appsync-api-cognitoconfig"></a>

Describes an Amazon Cognito configuration.

## Syntax
<a name="aws-properties-appsync-api-cognitoconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-api-cognitoconfig-syntax.json"></a>

```
{
  "[AppIdClientRegex](#cfn-appsync-api-cognitoconfig-appidclientregex)" : {{String}},
  "[AwsRegion](#cfn-appsync-api-cognitoconfig-awsregion)" : {{String}},
  "[UserPoolId](#cfn-appsync-api-cognitoconfig-userpoolid)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-api-cognitoconfig-syntax.yaml"></a>

```
  [AppIdClientRegex](#cfn-appsync-api-cognitoconfig-appidclientregex): {{String}}
  [AwsRegion](#cfn-appsync-api-cognitoconfig-awsregion): {{String}}
  [UserPoolId](#cfn-appsync-api-cognitoconfig-userpoolid): {{String}}
```

## Properties
<a name="aws-properties-appsync-api-cognitoconfig-properties"></a>

`AppIdClientRegex`  <a name="cfn-appsync-api-cognitoconfig-appidclientregex"></a>
A regular expression for validating the incoming Amazon Cognito user pool app client ID. If this value isn't set, no filtering is applied.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsRegion`  <a name="cfn-appsync-api-cognitoconfig-awsregion"></a>
The AWS Region in which the user pool was created.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-appsync-api-cognitoconfig-userpoolid"></a>
The user pool ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

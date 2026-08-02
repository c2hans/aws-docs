---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-authorizationcodegrantcredentialsdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector AuthorizationCodeGrantCredentialsDetails
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantcredentialsdetails"></a>

Details for OAuth 2.0 authorization code grant credentials.

## Syntax
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantcredentialsdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantcredentialsdetails-syntax.json"></a>

```
{
  "[AuthorizationCodeGrantDetails](#cfn-quicksight-actionconnector-authorizationcodegrantcredentialsdetails-authorizationcodegrantdetails)" : {{AuthorizationCodeGrantDetails}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantcredentialsdetails-syntax.yaml"></a>

```
  [AuthorizationCodeGrantDetails](#cfn-quicksight-actionconnector-authorizationcodegrantcredentialsdetails-authorizationcodegrantdetails): {{
    AuthorizationCodeGrantDetails}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-authorizationcodegrantcredentialsdetails-properties"></a>

`AuthorizationCodeGrantDetails`  <a name="cfn-quicksight-actionconnector-authorizationcodegrantcredentialsdetails-authorizationcodegrantdetails"></a>
The authorization code grant configuration details.
*Required*: Yes
*Type*: [AuthorizationCodeGrantDetails](aws-properties-quicksight-actionconnector-authorizationcodegrantdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

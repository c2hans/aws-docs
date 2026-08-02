---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-actionconnector-clientcredentialsdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector ClientCredentialsDetails
<a name="aws-properties-quicksight-actionconnector-clientcredentialsdetails"></a>

Details for OAuth 2.0 client credentials grant authentication.

## Syntax
<a name="aws-properties-quicksight-actionconnector-clientcredentialsdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-actionconnector-clientcredentialsdetails-syntax.json"></a>

```
{
  "[ClientCredentialsGrantDetails](#cfn-quicksight-actionconnector-clientcredentialsdetails-clientcredentialsgrantdetails)" : {{ClientCredentialsGrantDetails}}
}
```

### YAML
<a name="aws-properties-quicksight-actionconnector-clientcredentialsdetails-syntax.yaml"></a>

```
  [ClientCredentialsGrantDetails](#cfn-quicksight-actionconnector-clientcredentialsdetails-clientcredentialsgrantdetails): {{
    ClientCredentialsGrantDetails}}
```

## Properties
<a name="aws-properties-quicksight-actionconnector-clientcredentialsdetails-properties"></a>

`ClientCredentialsGrantDetails`  <a name="cfn-quicksight-actionconnector-clientcredentialsdetails-clientcredentialsgrantdetails"></a>
The OAuth2 client credentials grant configuration details for authentication.
*Required*: Yes
*Type*: [ClientCredentialsGrantDetails](aws-properties-quicksight-actionconnector-clientcredentialsgrantdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

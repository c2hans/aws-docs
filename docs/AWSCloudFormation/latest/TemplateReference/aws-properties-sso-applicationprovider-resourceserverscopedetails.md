---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sso-applicationprovider-resourceserverscopedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSO::ApplicationProvider ResourceServerScopeDetails
<a name="aws-properties-sso-applicationprovider-resourceserverscopedetails"></a>

A structure that describes details for an IAM Identity Center access scope that is associated with a resource server.

## Syntax
<a name="aws-properties-sso-applicationprovider-resourceserverscopedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sso-applicationprovider-resourceserverscopedetails-syntax.json"></a>

```
{
  "[DetailedTitle](#cfn-sso-applicationprovider-resourceserverscopedetails-detailedtitle)" : {{String}},
  "[LongDescription](#cfn-sso-applicationprovider-resourceserverscopedetails-longdescription)" : {{String}}
}
```

### YAML
<a name="aws-properties-sso-applicationprovider-resourceserverscopedetails-syntax.yaml"></a>

```
  [DetailedTitle](#cfn-sso-applicationprovider-resourceserverscopedetails-detailedtitle): {{String}}
  [LongDescription](#cfn-sso-applicationprovider-resourceserverscopedetails-longdescription): {{String}}
```

## Properties
<a name="aws-properties-sso-applicationprovider-resourceserverscopedetails-properties"></a>

`DetailedTitle`  <a name="cfn-sso-applicationprovider-resourceserverscopedetails-detailedtitle"></a>
The title of an access scope for a resource server.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LongDescription`  <a name="cfn-sso-applicationprovider-resourceserverscopedetails-longdescription"></a>
The description of an access scope for a resource server.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

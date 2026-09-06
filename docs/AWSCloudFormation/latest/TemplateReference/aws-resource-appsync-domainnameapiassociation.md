---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-domainnameapiassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DomainNameApiAssociation
<a name="aws-resource-appsync-domainnameapiassociation"></a>

The `AWS::AppSync::DomainNameApiAssociation` resource represents the mapping of your custom domain name to the assigned API URL.

## Syntax
<a name="aws-resource-appsync-domainnameapiassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appsync-domainnameapiassociation-syntax.json"></a>

```
{
  "Type" : "AWS::AppSync::DomainNameApiAssociation",
  "Properties" : {
      "[ApiId](#cfn-appsync-domainnameapiassociation-apiid)" : {{String}},
      "[DomainName](#cfn-appsync-domainnameapiassociation-domainname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-appsync-domainnameapiassociation-syntax.yaml"></a>

```
Type: AWS::AppSync::DomainNameApiAssociation
Properties:
  [ApiId](#cfn-appsync-domainnameapiassociation-apiid): {{String}}
  [DomainName](#cfn-appsync-domainnameapiassociation-domainname): {{String}}
```

## Properties
<a name="aws-resource-appsync-domainnameapiassociation-properties"></a>

`ApiId`  <a name="cfn-appsync-domainnameapiassociation-apiid"></a>
The API ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-appsync-domainnameapiassociation-domainname"></a>
The domain name.
*Required*: Yes
*Type*: String
*Pattern*: `^(\*[a-z\d-]*\.)?([a-z\d-]+\.)+[a-z\d-]+$`
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

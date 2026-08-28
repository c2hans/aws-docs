---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-domainname.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::DomainName
<a name="aws-resource-appsync-domainname"></a>

The `AWS::AppSync::DomainName` resource creates a `DomainNameConfig` object to configure a custom domain.

## Syntax
<a name="aws-resource-appsync-domainname-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appsync-domainname-syntax.json"></a>

```
{
  "Type" : "AWS::AppSync::DomainName",
  "Properties" : {
      "[CertificateArn](#cfn-appsync-domainname-certificatearn)" : {{String}},
      "[Description](#cfn-appsync-domainname-description)" : {{String}},
      "[DomainName](#cfn-appsync-domainname-domainname)" : {{String}},
      "[Tags](#cfn-appsync-domainname-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-appsync-domainname-syntax.yaml"></a>

```
Type: AWS::AppSync::DomainName
Properties:
  [CertificateArn](#cfn-appsync-domainname-certificatearn): {{String}}
  [Description](#cfn-appsync-domainname-description): {{String}}
  [DomainName](#cfn-appsync-domainname-domainname): {{String}}
  [Tags](#cfn-appsync-domainname-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-appsync-domainname-properties"></a>

`CertificateArn`  <a name="cfn-appsync-domainname-certificatearn"></a>
The Amazon Resource Name (ARN) of the certificate. This will be an AWS Certificate Manager certificate.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]*:acm:[a-z0-9-]*:\d{12}:certificate/[0-9A-Za-z_/-]*$`
*Minimum*: `3`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-appsync-domainname-description"></a>
The decription for your domain name.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-appsync-domainname-domainname"></a>
The domain name.
*Required*: Yes
*Type*: String
*Pattern*: `^(\*[a-z\d-]*\.)?([a-z\d-]+\.)+[a-z\d-]+$`
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-appsync-domainname-tags"></a>
A set of tags (key-value pairs) for this domain name.
*Required*: No
*Type*: Array of [Tag](aws-properties-appsync-domainname-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appsync-domainname-return-values"></a>

### Ref
<a name="aws-resource-appsync-domainname-return-values-ref"></a>

When you pass the logical ID of an `AWS::AppSync::DomainName` resource to the intrinsic `Ref` function, the function returns the domain name.

 For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref).

### Fn::GetAtt
<a name="aws-resource-appsync-domainname-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt).

####
<a name="aws-resource-appsync-domainname-return-values-fn--getatt-fn--getatt"></a>

`AppSyncDomainName`  <a name="AppSyncDomainName-fn::getatt"></a>
The domain name provided by AWS AppSync.

`DomainName`  <a name="DomainName-fn::getatt"></a>
The domain name.

`DomainNameArn`  <a name="DomainNameArn-fn::getatt"></a>
The Amazon resource name (ARN) of the domain name.

`HostedZoneId`  <a name="HostedZoneId-fn::getatt"></a>
The ID of your Amazon Route 53 hosted zone.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

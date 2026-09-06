---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-domainnameaccessassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::DomainNameAccessAssociation
<a name="aws-resource-apigateway-domainnameaccessassociation"></a>

The `AWS::ApiGateway::DomainNameAccessAssociation` resource creates a domain name access association between an access association source and a private custom domain name.

Use a domain name access association to invoke a private custom domain name while isolated from the public internet.

You can only create or delete a DomainNameAccessAssociation using CloudFormation. To reject a domain name access association, use the AWS CLI.

## Syntax
<a name="aws-resource-apigateway-domainnameaccessassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-apigateway-domainnameaccessassociation-syntax.json"></a>

```
{
  "Type" : "AWS::ApiGateway::DomainNameAccessAssociation",
  "Properties" : {
      "[AccessAssociationSource](#cfn-apigateway-domainnameaccessassociation-accessassociationsource)" : {{String}},
      "[AccessAssociationSourceType](#cfn-apigateway-domainnameaccessassociation-accessassociationsourcetype)" : {{String}},
      "[DomainNameArn](#cfn-apigateway-domainnameaccessassociation-domainnamearn)" : {{String}},
      "[Tags](#cfn-apigateway-domainnameaccessassociation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-apigateway-domainnameaccessassociation-syntax.yaml"></a>

```
Type: AWS::ApiGateway::DomainNameAccessAssociation
Properties:
  [AccessAssociationSource](#cfn-apigateway-domainnameaccessassociation-accessassociationsource): {{String}}
  [AccessAssociationSourceType](#cfn-apigateway-domainnameaccessassociation-accessassociationsourcetype): {{String}}
  [DomainNameArn](#cfn-apigateway-domainnameaccessassociation-domainnamearn): {{String}}
  [Tags](#cfn-apigateway-domainnameaccessassociation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-apigateway-domainnameaccessassociation-properties"></a>

`AccessAssociationSource`  <a name="cfn-apigateway-domainnameaccessassociation-accessassociationsource"></a>
The identifier of the domain name access association source. For a `VPCE`, the value is the VPC endpoint ID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AccessAssociationSourceType`  <a name="cfn-apigateway-domainnameaccessassociation-accessassociationsourcetype"></a>
The type of the domain name access association source. Only `VPCE` is currently supported.
*Required*: Yes
*Type*: String
*Allowed values*: `VPCE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainNameArn`  <a name="cfn-apigateway-domainnameaccessassociation-domainnamearn"></a>
The ARN of the domain name.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-apigateway-domainnameaccessassociation-tags"></a>
The collection of tags. Each tag element is associated with a given resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-apigateway-domainnameaccessassociation-tag.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-apigateway-domainnameaccessassociation-return-values"></a>

### Ref
<a name="aws-resource-apigateway-domainnameaccessassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the domain name access association ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-apigateway-domainnameaccessassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-apigateway-domainnameaccessassociation-return-values-fn--getatt-fn--getatt"></a>

`DomainNameAccessAssociationArn`  <a name="DomainNameAccessAssociationArn-fn::getatt"></a>
The access association ARN. For example: `arn:aws:apigateway:us-west-2:111122223333:/accessassociations/domainname/private.example.com+abcd1234/vpcesource/vpce-abcd1234efg`.

## Examples
<a name="aws-resource-apigateway-domainnameaccessassociation--examples"></a>

### Domain name access association example
<a name="aws-resource-apigateway-domainnameaccessassociation--examples--Domain_name_access_association_example"></a>

The following example creates a `DomainNameAccessAssociation` resource named `MyDomainNameAccessAssociation`.

#### JSON
<a name="aws-resource-apigateway-domainnameaccessassociation--examples--Domain_name_access_association_example--json"></a>

```
{
    "MyDomainNameAccessAssociation": {
        "Type": "AWS::ApiGateway::DomainNameAccessAssociation",
        "Properties": {
            "DomainNameArn": {
                "Fn::GetAtt": [
                    "MyDomainName",
                    "DomainNameArn"
                ]
            },
            "AccessAssociationSource": "vpce-abcd123456",
            "AccessAssociationSourceType": "VPCE"
        }
    }
}
```

#### YAML
<a name="aws-resource-apigateway-domainnameaccessassociation--examples--Domain_name_access_association_example--yaml"></a>

```
MyDomainNameAccessAssociation:
  Type: AWS::ApiGateway::DomainNameAccessAssociation
  Properties:
    DomainNameArn: !GetAtt MyDomainName.DomainNameArn
    AccessAssociationSource: vpce-abcd123456
    AccessAssociationSourceType: VPCE
```

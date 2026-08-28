---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pcaconnectorad-connector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorAD::Connector
<a name="aws-resource-pcaconnectorad-connector"></a>

Creates a connector between AWS Private CA and an Active Directory. You must specify the private CA, directory ID, and security groups.

## Syntax
<a name="aws-resource-pcaconnectorad-connector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pcaconnectorad-connector-syntax.json"></a>

```
{
  "Type" : "AWS::PCAConnectorAD::Connector",
  "Properties" : {
      "[CertificateAuthorityArn](#cfn-pcaconnectorad-connector-certificateauthorityarn)" : {{String}},
      "[DirectoryId](#cfn-pcaconnectorad-connector-directoryid)" : {{String}},
      "[Tags](#cfn-pcaconnectorad-connector-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[VpcInformation](#cfn-pcaconnectorad-connector-vpcinformation)" : {{VpcInformation}}
    }
}
```

### YAML
<a name="aws-resource-pcaconnectorad-connector-syntax.yaml"></a>

```
Type: AWS::PCAConnectorAD::Connector
Properties:
  [CertificateAuthorityArn](#cfn-pcaconnectorad-connector-certificateauthorityarn): {{String}}
  [DirectoryId](#cfn-pcaconnectorad-connector-directoryid): {{String}}
  [Tags](#cfn-pcaconnectorad-connector-tags): {{
    {{Key}}: {{Value}}}}
  [VpcInformation](#cfn-pcaconnectorad-connector-vpcinformation): {{
    VpcInformation}}
```

## Properties
<a name="aws-resource-pcaconnectorad-connector-properties"></a>

`CertificateAuthorityArn`  <a name="cfn-pcaconnectorad-connector-certificateauthorityarn"></a>
The Amazon Resource Name (ARN) of the certificate authority being used.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:acm-pca:[\w-]+:[0-9]+:certificate-authority\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$`
*Minimum*: `5`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DirectoryId`  <a name="cfn-pcaconnectorad-connector-directoryid"></a>
The identifier of the Active Directory.
*Required*: Yes
*Type*: String
*Pattern*: `^d-[0-9a-f]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-pcaconnectorad-connector-tags"></a>
Metadata assigned to a connector consisting of a key-value pair.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcInformation`  <a name="cfn-pcaconnectorad-connector-vpcinformation"></a>
Information of the VPC and security group(s) used with the connector.
*Required*: Yes
*Type*: [VpcInformation](aws-properties-pcaconnectorad-connector-vpcinformation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-pcaconnectorad-connector-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-pcaconnectorad-connector-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-pcaconnectorad-connector-return-values-fn--getatt-fn--getatt"></a>

`ConnectorArn`  <a name="ConnectorArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) that was returned when you called [CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

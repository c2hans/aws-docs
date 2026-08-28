---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-pcaconnectorad-serviceprincipalname.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCAConnectorAD::ServicePrincipalName
<a name="aws-resource-pcaconnectorad-serviceprincipalname"></a>

Creates a service principal name (SPN) for the service account in Active Directory. Kerberos authentication uses SPNs to associate a service instance with a service sign-in account.

## Syntax
<a name="aws-resource-pcaconnectorad-serviceprincipalname-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-pcaconnectorad-serviceprincipalname-syntax.json"></a>

```
{
  "Type" : "AWS::PCAConnectorAD::ServicePrincipalName",
  "Properties" : {
      "[ConnectorArn](#cfn-pcaconnectorad-serviceprincipalname-connectorarn)" : {{String}},
      "[DirectoryRegistrationArn](#cfn-pcaconnectorad-serviceprincipalname-directoryregistrationarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-pcaconnectorad-serviceprincipalname-syntax.yaml"></a>

```
Type: AWS::PCAConnectorAD::ServicePrincipalName
Properties:
  [ConnectorArn](#cfn-pcaconnectorad-serviceprincipalname-connectorarn): {{String}}
  [DirectoryRegistrationArn](#cfn-pcaconnectorad-serviceprincipalname-directoryregistrationarn): {{String}}
```

## Properties
<a name="aws-resource-pcaconnectorad-serviceprincipalname-properties"></a>

`ConnectorArn`  <a name="cfn-pcaconnectorad-serviceprincipalname-connectorarn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateConnector.html](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector(\/[\w-]+)$`
*Minimum*: `5`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DirectoryRegistrationArn`  <a name="cfn-pcaconnectorad-serviceprincipalname-directoryregistrationarn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateDirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:directory-registration(\/[\w-]+)$`
*Minimum*: `5`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

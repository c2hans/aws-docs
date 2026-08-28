---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchservice-domain-idp.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchService::Domain Idp
<a name="aws-properties-opensearchservice-domain-idp"></a>

The SAML Identity Provider's information.

## Syntax
<a name="aws-properties-opensearchservice-domain-idp-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchservice-domain-idp-syntax.json"></a>

```
{
  "[EntityId](#cfn-opensearchservice-domain-idp-entityid)" : {{String}},
  "[MetadataContent](#cfn-opensearchservice-domain-idp-metadatacontent)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchservice-domain-idp-syntax.yaml"></a>

```
  [EntityId](#cfn-opensearchservice-domain-idp-entityid): {{String}}
  [MetadataContent](#cfn-opensearchservice-domain-idp-metadatacontent): {{String}}
```

## Properties
<a name="aws-properties-opensearchservice-domain-idp-properties"></a>

`EntityId`  <a name="cfn-opensearchservice-domain-idp-entityid"></a>
The unique entity ID of the application in the SAML identity provider.
*Required*: Yes
*Type*: String
*Minimum*: `8`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataContent`  <a name="cfn-opensearchservice-domain-idp-metadatacontent"></a>
The metadata of the SAML application, in XML format.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1048576`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

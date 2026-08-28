---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Elasticsearch::Domain AdvancedSecurityOptionsInput
<a name="aws-properties-elasticsearch-domain-advancedsecurityoptionsinput"></a>

Specifies options for fine-grained access control.

**Important**
The `AWS::Elasticsearch::Domain` resource is being replaced by the [AWS::OpenSearchService::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchservice-domain.html) resource. While the legacy Elasticsearch resource and options are still supported, we recommend modifying your existing Cloudformation templates to use the new OpenSearch Service resource, which supports both OpenSearch and Elasticsearch. For more information about the service rename, see [New resource types](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rename.html#rename-resource) in the *Amazon OpenSearch Service Developer Guide*.

## Syntax
<a name="aws-properties-elasticsearch-domain-advancedsecurityoptionsinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticsearch-domain-advancedsecurityoptionsinput-syntax.json"></a>

```
{
  "[AnonymousAuthEnabled](#cfn-elasticsearch-domain-advancedsecurityoptionsinput-anonymousauthenabled)" : {{Boolean}},
  "[Enabled](#cfn-elasticsearch-domain-advancedsecurityoptionsinput-enabled)" : {{Boolean}},
  "[InternalUserDatabaseEnabled](#cfn-elasticsearch-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled)" : {{Boolean}},
  "[MasterUserOptions](#cfn-elasticsearch-domain-advancedsecurityoptionsinput-masteruseroptions)" : {{MasterUserOptions}}
}
```

### YAML
<a name="aws-properties-elasticsearch-domain-advancedsecurityoptionsinput-syntax.yaml"></a>

```
  [AnonymousAuthEnabled](#cfn-elasticsearch-domain-advancedsecurityoptionsinput-anonymousauthenabled): {{Boolean}}
  [Enabled](#cfn-elasticsearch-domain-advancedsecurityoptionsinput-enabled): {{Boolean}}
  [InternalUserDatabaseEnabled](#cfn-elasticsearch-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled): {{Boolean}}
  [MasterUserOptions](#cfn-elasticsearch-domain-advancedsecurityoptionsinput-masteruseroptions): {{
    MasterUserOptions}}
```

## Properties
<a name="aws-properties-elasticsearch-domain-advancedsecurityoptionsinput-properties"></a>

`AnonymousAuthEnabled`  <a name="cfn-elasticsearch-domain-advancedsecurityoptionsinput-anonymousauthenabled"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-elasticsearch-domain-advancedsecurityoptionsinput-enabled"></a>
True to enable fine-grained access control. You must also enable encryption of data at rest and node-to-node encryption.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InternalUserDatabaseEnabled`  <a name="cfn-elasticsearch-domain-advancedsecurityoptionsinput-internaluserdatabaseenabled"></a>
True to enable the internal user database.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MasterUserOptions`  <a name="cfn-elasticsearch-domain-advancedsecurityoptionsinput-masteruseroptions"></a>
Specifies information about the master user.
*Required*: No
*Type*: [MasterUserOptions](aws-properties-elasticsearch-domain-masteruseroptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-collection-fipsendpoints.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Collection FipsEndpoints
<a name="aws-properties-opensearchserverless-collection-fipsendpoints"></a>

FIPS-compliant endpoint URLs for an OpenSearch Serverless collection. These endpoints ensure all data transmission uses FIPS 140-3 validated cryptographic implementations, meeting federal security requirements for government workloads.

## Syntax
<a name="aws-properties-opensearchserverless-collection-fipsendpoints-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-collection-fipsendpoints-syntax.json"></a>

```
{
  "[CollectionEndpoint](#cfn-opensearchserverless-collection-fipsendpoints-collectionendpoint)" : {{String}},
  "[DashboardEndpoint](#cfn-opensearchserverless-collection-fipsendpoints-dashboardendpoint)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-collection-fipsendpoints-syntax.yaml"></a>

```
  [CollectionEndpoint](#cfn-opensearchserverless-collection-fipsendpoints-collectionendpoint): {{String}}
  [DashboardEndpoint](#cfn-opensearchserverless-collection-fipsendpoints-dashboardendpoint): {{String}}
```

## Properties
<a name="aws-properties-opensearchserverless-collection-fipsendpoints-properties"></a>

`CollectionEndpoint`  <a name="cfn-opensearchserverless-collection-fipsendpoints-collectionendpoint"></a>
FIPS-compliant collection endpoint used to submit index, search, and data upload requests to an OpenSearch Serverless collection. This endpoint uses FIPS 140-3 validated cryptography and is required for federal government workloads.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DashboardEndpoint`  <a name="cfn-opensearchserverless-collection-fipsendpoints-dashboardendpoint"></a>
FIPS-compliant endpoint used to access OpenSearch Dashboards. This endpoint uses FIPS 140-3 validated cryptography and is required for federal government workloads that need dashboard visualization capabilities.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

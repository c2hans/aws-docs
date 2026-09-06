---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-sapodatapaginationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow SAPODataPaginationConfig
<a name="aws-properties-appflow-flow-sapodatapaginationconfig"></a>

Sets the page size for each *concurrent process* that transfers OData records from your SAP instance. A concurrent process is query that retrieves a batch of records as part of a flow run. Amazon AppFlow can run multiple concurrent processes in parallel to transfer data faster.

## Syntax
<a name="aws-properties-appflow-flow-sapodatapaginationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-sapodatapaginationconfig-syntax.json"></a>

```
{
  "[maxPageSize](#cfn-appflow-flow-sapodatapaginationconfig-maxpagesize)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-appflow-flow-sapodatapaginationconfig-syntax.yaml"></a>

```
  [maxPageSize](#cfn-appflow-flow-sapodatapaginationconfig-maxpagesize): {{Integer}}
```

## Properties
<a name="aws-properties-appflow-flow-sapodatapaginationconfig-properties"></a>

`maxPageSize`  <a name="cfn-appflow-flow-sapodatapaginationconfig-maxpagesize"></a>
The maximum number of records that Amazon AppFlow receives in each page of the response from your SAP application. For transfers of OData records, the maximum page size is 3,000. For transfers of data that comes from an ODP provider, the maximum page size is 10,000.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

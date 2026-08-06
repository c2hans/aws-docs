---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-datashare-datashareassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::DataShare DataShareAssociation
<a name="aws-properties-redshift-datashare-datashareassociation"></a>

The association of a datashare from a producer account with a data consumer.

## Syntax
<a name="aws-properties-redshift-datashare-datashareassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-datashare-datashareassociation-syntax.json"></a>

```
{
  "[ConsumerIdentifier](#cfn-redshift-datashare-datashareassociation-consumeridentifier)" : {{String}},
  "[CreatedDate](#cfn-redshift-datashare-datashareassociation-createddate)" : {{String}},
  "[Status](#cfn-redshift-datashare-datashareassociation-status)" : {{String}},
  "[StatusChangeDate](#cfn-redshift-datashare-datashareassociation-statuschangedate)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-datashare-datashareassociation-syntax.yaml"></a>

```
  [ConsumerIdentifier](#cfn-redshift-datashare-datashareassociation-consumeridentifier): {{String}}
  [CreatedDate](#cfn-redshift-datashare-datashareassociation-createddate): {{String}}
  [Status](#cfn-redshift-datashare-datashareassociation-status): {{String}}
  [StatusChangeDate](#cfn-redshift-datashare-datashareassociation-statuschangedate): {{String}}
```

## Properties
<a name="aws-properties-redshift-datashare-datashareassociation-properties"></a>

`ConsumerIdentifier`  <a name="cfn-redshift-datashare-datashareassociation-consumeridentifier"></a>
The name of the consumer accounts that have an association with a producer datashare.
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedDate`  <a name="cfn-redshift-datashare-datashareassociation-createddate"></a>
The creation date of the datashare that is associated.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-redshift-datashare-datashareassociation-status"></a>
The status of the datashare that is associated.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | PENDING_AUTHORIZATION | AUTHORIZED | DEAUTHORIZED | REJECTED | AVAILABLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StatusChangeDate`  <a name="cfn-redshift-datashare-datashareassociation-statuschangedate"></a>
The status change data of the datashare that is associated.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

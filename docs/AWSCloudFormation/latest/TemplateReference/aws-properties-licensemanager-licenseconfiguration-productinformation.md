---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-licenseconfiguration-productinformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseConfiguration ProductInformation
<a name="aws-properties-licensemanager-licenseconfiguration-productinformation"></a>

Describes product information for a license configuration.

## Syntax
<a name="aws-properties-licensemanager-licenseconfiguration-productinformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-licenseconfiguration-productinformation-syntax.json"></a>

```
{
  "[ProductInformationFilterList](#cfn-licensemanager-licenseconfiguration-productinformation-productinformationfilterlist)" : {{[ ProductInformationFilter, ... ]}},
  "[ResourceType](#cfn-licensemanager-licenseconfiguration-productinformation-resourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-licensemanager-licenseconfiguration-productinformation-syntax.yaml"></a>

```
  [ProductInformationFilterList](#cfn-licensemanager-licenseconfiguration-productinformation-productinformationfilterlist): {{
    - ProductInformationFilter}}
  [ResourceType](#cfn-licensemanager-licenseconfiguration-productinformation-resourcetype): {{String}}
```

## Properties
<a name="aws-properties-licensemanager-licenseconfiguration-productinformation-properties"></a>

`ProductInformationFilterList`  <a name="cfn-licensemanager-licenseconfiguration-productinformation-productinformationfilterlist"></a>
A Product information filter consists of a `ProductInformationFilterComparator` which is a logical operator, a `ProductInformationFilterName` which specifies the type of filter being declared, and a `ProductInformationFilterValue` that specifies the value to filter on.
Accepted values for `ProductInformationFilterName` are listed here along with descriptions and valid options for `ProductInformationFilterComparator`.
The following filters and are supported when the resource type is `SSM_MANAGED`:
+ `Application Name` - The name of the application. Logical operator is `EQUALS`.
+ `Application Publisher` - The publisher of the application. Logical operator is `EQUALS`.
+ `Application Version` - The version of the application. Logical operator is `EQUALS`.
+ `Platform Name` - The name of the platform. Logical operator is `EQUALS`.
+ `Platform Type` - The platform type. Logical operator is `EQUALS`.
+ `Tag:key` - The key of a tag attached to an AWS resource you wish to exclude from automated discovery. Logical operator is `NOT_EQUALS`. The key for your tag must be appended to `Tag:` following the example: `Tag:name-of-your-key`. `ProductInformationFilterValue` is optional if you are not using values for the key.
+ `AccountId` - The 12-digit ID of an AWS account you wish to exclude from automated discovery. Logical operator is `NOT_EQUALS`.
+ `License Included` - The type of license included. Logical operators are `EQUALS` and `NOT_EQUALS`. Possible values are: `sql-server-enterprise` \| `sql-server-standard` \| `sql-server-web` \| `windows-server-datacenter`.
The following filters and logical operators are supported when the resource type is `RDS`:
+ `Engine Edition` - The edition of the database engine. Logical operator is `EQUALS`. Possible values are: `oracle-ee` \| `oracle-se` \| `oracle-se1` \| `oracle-se2` \| `db2-se` \| `db2-ae`.
+ `License Pack` - The license pack. Logical operator is `EQUALS`. Possible values are: `data guard` \| `diagnostic pack sqlt` \| `tuning pack sqlt` \| `ols` \| `olap`.
*Required*: Yes
*Type*: Array of [ProductInformationFilter](aws-properties-licensemanager-licenseconfiguration-productinformationfilter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-licensemanager-licenseconfiguration-productinformation-resourcetype"></a>
Resource type. The possible values are `SSM_MANAGED` \| `RDS`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

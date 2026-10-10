---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-licenseconfiguration-productinformationfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::LicenseConfiguration ProductInformationFilter
<a name="aws-properties-licensemanager-licenseconfiguration-productinformationfilter"></a>

Describes product information filters.

## Syntax
<a name="aws-properties-licensemanager-licenseconfiguration-productinformationfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-licenseconfiguration-productinformationfilter-syntax.json"></a>

```
{
  "[ProductInformationFilterComparator](#cfn-licensemanager-licenseconfiguration-productinformationfilter-productinformationfiltercomparator)" : {{String}},
  "[ProductInformationFilterName](#cfn-licensemanager-licenseconfiguration-productinformationfilter-productinformationfiltername)" : {{String}},
  "[ProductInformationFilterValue](#cfn-licensemanager-licenseconfiguration-productinformationfilter-productinformationfiltervalue)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-licensemanager-licenseconfiguration-productinformationfilter-syntax.yaml"></a>

```
  [ProductInformationFilterComparator](#cfn-licensemanager-licenseconfiguration-productinformationfilter-productinformationfiltercomparator): {{String}}
  [ProductInformationFilterName](#cfn-licensemanager-licenseconfiguration-productinformationfilter-productinformationfiltername): {{String}}
  [ProductInformationFilterValue](#cfn-licensemanager-licenseconfiguration-productinformationfilter-productinformationfiltervalue): {{
    - String}}
```

## Properties
<a name="aws-properties-licensemanager-licenseconfiguration-productinformationfilter-properties"></a>

`ProductInformationFilterComparator`  <a name="cfn-licensemanager-licenseconfiguration-productinformationfilter-productinformationfiltercomparator"></a>
Logical operator.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProductInformationFilterName`  <a name="cfn-licensemanager-licenseconfiguration-productinformationfilter-productinformationfiltername"></a>
Filter name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProductInformationFilterValue`  <a name="cfn-licensemanager-licenseconfiguration-productinformationfilter-productinformationfiltervalue"></a>
Filter value.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

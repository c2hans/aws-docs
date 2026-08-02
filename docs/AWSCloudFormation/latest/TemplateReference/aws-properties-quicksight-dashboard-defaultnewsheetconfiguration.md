---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-defaultnewsheetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DefaultNewSheetConfiguration
<a name="aws-properties-quicksight-dashboard-defaultnewsheetconfiguration"></a>

The configuration for default new sheet settings.

## Syntax
<a name="aws-properties-quicksight-dashboard-defaultnewsheetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-defaultnewsheetconfiguration-syntax.json"></a>

```
{
  "[InteractiveLayoutConfiguration](#cfn-quicksight-dashboard-defaultnewsheetconfiguration-interactivelayoutconfiguration)" : {{DefaultInteractiveLayoutConfiguration}},
  "[PaginatedLayoutConfiguration](#cfn-quicksight-dashboard-defaultnewsheetconfiguration-paginatedlayoutconfiguration)" : {{DefaultPaginatedLayoutConfiguration}},
  "[SheetContentType](#cfn-quicksight-dashboard-defaultnewsheetconfiguration-sheetcontenttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-defaultnewsheetconfiguration-syntax.yaml"></a>

```
  [InteractiveLayoutConfiguration](#cfn-quicksight-dashboard-defaultnewsheetconfiguration-interactivelayoutconfiguration): {{
    DefaultInteractiveLayoutConfiguration}}
  [PaginatedLayoutConfiguration](#cfn-quicksight-dashboard-defaultnewsheetconfiguration-paginatedlayoutconfiguration): {{
    DefaultPaginatedLayoutConfiguration}}
  [SheetContentType](#cfn-quicksight-dashboard-defaultnewsheetconfiguration-sheetcontenttype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-defaultnewsheetconfiguration-properties"></a>

`InteractiveLayoutConfiguration`  <a name="cfn-quicksight-dashboard-defaultnewsheetconfiguration-interactivelayoutconfiguration"></a>
The options that determine the default settings for interactive layout configuration.
*Required*: No
*Type*: [DefaultInteractiveLayoutConfiguration](aws-properties-quicksight-dashboard-defaultinteractivelayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PaginatedLayoutConfiguration`  <a name="cfn-quicksight-dashboard-defaultnewsheetconfiguration-paginatedlayoutconfiguration"></a>
The options that determine the default settings for a paginated layout configuration.
*Required*: No
*Type*: [DefaultPaginatedLayoutConfiguration](aws-properties-quicksight-dashboard-defaultpaginatedlayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetContentType`  <a name="cfn-quicksight-dashboard-defaultnewsheetconfiguration-sheetcontenttype"></a>
The option that determines the sheet content type.
*Required*: No
*Type*: String
*Allowed values*: `PAGINATED | INTERACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

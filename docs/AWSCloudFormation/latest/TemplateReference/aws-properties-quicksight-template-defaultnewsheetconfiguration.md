---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-defaultnewsheetconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DefaultNewSheetConfiguration
<a name="aws-properties-quicksight-template-defaultnewsheetconfiguration"></a>

The configuration for default new sheet settings.

## Syntax
<a name="aws-properties-quicksight-template-defaultnewsheetconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-defaultnewsheetconfiguration-syntax.json"></a>

```
{
  "[InteractiveLayoutConfiguration](#cfn-quicksight-template-defaultnewsheetconfiguration-interactivelayoutconfiguration)" : {{DefaultInteractiveLayoutConfiguration}},
  "[PaginatedLayoutConfiguration](#cfn-quicksight-template-defaultnewsheetconfiguration-paginatedlayoutconfiguration)" : {{DefaultPaginatedLayoutConfiguration}},
  "[SheetContentType](#cfn-quicksight-template-defaultnewsheetconfiguration-sheetcontenttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-defaultnewsheetconfiguration-syntax.yaml"></a>

```
  [InteractiveLayoutConfiguration](#cfn-quicksight-template-defaultnewsheetconfiguration-interactivelayoutconfiguration): {{
    DefaultInteractiveLayoutConfiguration}}
  [PaginatedLayoutConfiguration](#cfn-quicksight-template-defaultnewsheetconfiguration-paginatedlayoutconfiguration): {{
    DefaultPaginatedLayoutConfiguration}}
  [SheetContentType](#cfn-quicksight-template-defaultnewsheetconfiguration-sheetcontenttype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-defaultnewsheetconfiguration-properties"></a>

`InteractiveLayoutConfiguration`  <a name="cfn-quicksight-template-defaultnewsheetconfiguration-interactivelayoutconfiguration"></a>
The options that determine the default settings for interactive layout configuration.
*Required*: No
*Type*: [DefaultInteractiveLayoutConfiguration](aws-properties-quicksight-template-defaultinteractivelayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PaginatedLayoutConfiguration`  <a name="cfn-quicksight-template-defaultnewsheetconfiguration-paginatedlayoutconfiguration"></a>
The options that determine the default settings for a paginated layout configuration.
*Required*: No
*Type*: [DefaultPaginatedLayoutConfiguration](aws-properties-quicksight-template-defaultpaginatedlayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetContentType`  <a name="cfn-quicksight-template-defaultnewsheetconfiguration-sheetcontenttype"></a>
The option that determines the sheet content type.
*Required*: No
*Type*: String
*Allowed values*: `PAGINATED | INTERACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

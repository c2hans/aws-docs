---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-theme.html
---

# CreateTheme
<a name="create-theme"></a>

Use the `CreateTheme` operation to create a theme. The `base-theme-id` is the ID of the theme that you want to base the new theme off of. You can use the `ListThemes` operation to list all themes and their corresponding theme IDs.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-theme
    --aws-account-id {{AWSACCOUNTID}}
    --theme-id {{THEMEID}}
    --name {{NAME}}
    --base-theme-id {{THEMEID}}
    --configuration '{"Configuration":{"DataColorPalette":{"Colors":[""],"MinMaxGradient":[""],"EmptyFillColor":""},"UIColorPalette":{"PrimaryForeground":"","PrimaryBackground": "","SecondaryForeground":"","SecondaryBackground":"","Accent":"","AccentForeground":"","Danger":"","DangerForeground":"","Warning":"","WarningForeground":"","Success":"","SuccessForeground":"","Dimension":"","DimensionForeground":"","Measure":"","MeasureForeground":""},"Sheet":{"Tile":{"Border":{"Show":true}},"TileLayout":{"Gutter":{"Show":true},"Margin":{"Show":true}}}}'
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-theme
    --cli-input-json file//:{{createtheme}}.json
```

------

For more information about the `CreateTheme` operation, see [CreateTheme](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTheme.html) in the*Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

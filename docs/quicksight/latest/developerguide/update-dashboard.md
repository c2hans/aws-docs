---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/update-dashboard.html
---

# UpdateDashboard
<a name="update-dashboard"></a>

Use the `UpdateDashboard` API operation to update a dashboard in an AWS account. To use this operation, you need the ID of the dashboard that you want to update. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight update-dashboard
    --aws-account-id {{555555555555}}
    --dashboard-id {{DASHBOARDID}}
    --name {{Dashboard}}
    --source-entity '{"SourceTemplate":{"DataSetReferences":[{"DataSetPlaceholder": "{{PLACEHOLDER}}","DataSetArn": "arn:aws:quicksight:<region>:<awsaccountid>:dataset/<datasetid>"}],"Arn": "arn:aws:quicksight:<{{region}}>:<{{awsaccountid}}>:template/<{{templateid}}>"}}'
    --version-description {{VERSION}}
    --dashboard-publish-options AdHocFilteringOption={AvailabilityStatus=ENABLED},ExportToCSVOption={AvailabilityStatus=ENABLED},SheetControlsOption={VisibilityState=EXPANDED} /
    --theme-arn {{THEMEARN}}
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight update-dashboard
    --cli-input-json file://{{updatedashboard}}.json
```

------

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `UpdateDashboard` API operation, see [UpdateDashboard](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboard.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

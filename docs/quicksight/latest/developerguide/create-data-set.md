---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/create-data-set.html
---

# CreateDataSet
<a name="create-data-set"></a>

Use the `CreateDataSet` API operation to create a dataset. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight create-data-set
    --aws-account-id {{AWSACCOUNTID}}
    --data-set-id {{DATASETID}}
    --name {{NAME}}
    --physical-table-map '{"PhysicalTableMap":{"{{string}}":{"CustomSql":{"Columns":[{"Name":"{{string}}","Type":"{{string}}"}],"DataSourceArn":"{{string}}","Name":"{{string}}","SqlQuery":"{{string}}"},"RelationalTable":{"Catalog":"{{string}}","DataSourceArn":"{{string}}","InputColumns":[{"Name":"{{string}}","Type":"{{string}}"}],"Name":"{{string}}","Schema":"{{string}}"},"S3Source":{"DataSourceArn":"{{string}}","InputColumns":[{"Name":"{{string}}","Type":"{{string}}"}],"UploadSettings":{"ContainsHeader":boolean,"Delimiter":"{{string}}","Format":"{{string}}","StartFromRow":number,"TextQualifier":"{{string}}"}}}}'
    --import-mode DIRECT_QUERY
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md).

```
aws quicksight create-data-set
    --cli-input-json file://{{createdataset}}.json
```

------

For more information about the `CreateDataSet` API operation, see [CreateDataSet](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSet.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/proton/latest/userguide/delete-template-sync.html
---

End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October 7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure will remain intact. For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# Delete a template sync configuration
<a name="delete-template-sync"></a>

Delete a template sync configuration using the console or CLI.

------
#### [ AWS Management Console ]

**Delete a template sync configuration using the console.**

1. In the template details page, choose the **Sync** tab.

1. In the **Sync details** section, choose **Disconnect**.

------
#### [ AWS CLI ]

**The following example commands and responses show how to use the AWS CLI to delete synced template configurations.**

Run the following command.

```
$ aws proton delete-template-sync-config \
    --template-name "{{env-template}}" \
    --template-type "{{ENVIRONMENT}}"
```

The response is as follows.

```
{
    "templateSyncConfig": {
        "templateName": "{{env-template}}",
        "templateType": "{{ENVIRONMENT}}"
    }
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

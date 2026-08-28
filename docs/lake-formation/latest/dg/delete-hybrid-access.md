---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/delete-hybrid-access.html
---

# Removing principals and resources from hybrid access mode
<a name="delete-hybrid-access"></a>

 Follow these steps to remove databases, tables, and principals from hybrid access mode.

------
#### [ Console ]

1. Sign in to the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. Under **Permissions**, choose **Hybrid access mode**.

1.  On the **Hybrid access mode** page, select the checkbox next to the database or table name and choose `Remove`.

1. A warning message prompts you to confirm the action. Choose **Remove**.

   Lake Formation no longer enforces permissions for those resources, and access to this resource will be controlled using IAM and AWS Glue permissions. This may cause the user to no longer have access to this resource if they don't have the appropriate IAM permissions.

------
#### [ AWS CLI ]

 The following example shows how to remove resources from hybrid access mode.

```
aws lakeformation delete-lake-formation-opt-in --cli-input-json file://{{file path}}

json:
{
    "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:iam::{{<123456789012>}}:role/{{role name}}"
    },
    "Resource": {
        "Table": {
            "CatalogId": "{{<123456789012>}}",
            "DatabaseName": "{{<database name>}}",
            "Name": "{{<table name>}}"
          }
    }
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/view-hybrid-access.html
---

# Viewing principals and resources in hybrid access mode
<a name="view-hybrid-access"></a>

 Follow these steps to view databases, tables, and principals in hybrid access mode.

------
#### [ Console ]

1. Sign in to the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. Under **Permissions**, choose **Hybrid access mode**.

1.  The **Hybrid access mode** page shows the resources and principals that are currently in hybrid access mode..

------
#### [ AWS CLI ]

 The following example shows how to list all opt in principals and resources that are in hybrid access mode.

```

aws lakeformation list-lake-formation-opt-ins
```

 The following example shows how to list opt in for a specific principal-resource pair.

```
aws lakeformation list-lake-formation-opt-ins --cli-input-json file://{{file path}}

json:
{
    "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:iam::{{<account-id>}}:role/{{<role name>}}"
    },
    "Resource": {
        "Table": {
            "CatalogId": "{{<account-id>}}",
            "DatabaseName": "{{<database name>}}",
            "Name": "{{<table name>}}"
          }
    }
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

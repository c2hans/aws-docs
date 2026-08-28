---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/row-filtering-prereqs.html
---

# Permissions required for querying tables with cell-level filtering
<a name="row-filtering-prereqs"></a>

The following AWS Identity and Access Management (IAM) permissions are required to run queries against tables with cell-level filtering.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lakeformation:StartQueryPlanning",
                "lakeformation:GetQueryState",
                "lakeformation:GetWorkUnits",
                "lakeformation:GetWorkUnitResults"
            ],
            "Resource": "*"
        }
    ]
}
```

------

For more information about Lake Formation permissions, see [Lake Formation personas and IAM permissions reference](permissions-reference.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

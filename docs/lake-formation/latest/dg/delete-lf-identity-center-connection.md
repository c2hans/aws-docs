---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/delete-lf-identity-center-connection.html
---

# Deleting a Lake Formation connection with IAM Identity Center
<a name="delete-lf-identity-center-connection"></a>

 If you would like to delete an existing IAM Identity Center integration, you can do it using Lake Formation console, AWS CLI, or [DeleteLakeFormationIdentityCenterConfiguration](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteLakeFormationIdentityCenterConfiguration.html) operation.

------
#### [ AWS Management Console ]

**To delete an existing IAM Identity Center connection with Lake Formation**

1. Sign in to the AWS Management Console, and open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. In the left navigation pane, select **IAM Identity Center integration**.

1. Select **Delete** on the **IAM Identity Center integration** page.

1. On the **Confirm integration** screen, confirm the action, and select **Delete**.

------
#### [ AWS CLI ]

You can delete IAM Identity Center integration by running the following AWS CLI command.

```
 aws lakeformation delete-lake-formation-identity-center-configuration \
     --catalog-id {{<123456789012>}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

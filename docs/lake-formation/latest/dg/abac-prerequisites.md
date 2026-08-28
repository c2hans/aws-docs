---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/abac-prerequisites.html
---

# Prerequisites for granting permissions using attributes
<a name="abac-prerequisites"></a>

To grant permissions using attribute-based access control (ABAC), you must complete the following prerequisites:
+ Update the **Data Catalog** **settings **to enable Lake Formation permissions for Data Catalog objects. For more information, see the [Change the default permission model or use hybrid access mode](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#setup-change-cat-settings) section.
+ Set the cross-account version settings to two or higher.
+ [Attach attributes](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) to the IAM entities that require access.
+ Only a data lake administrator or an IAM user with the required permissions can grant access on Data Catalog objects. For more information on required permissions, see [IAM permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/required-permissions-for-grant.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

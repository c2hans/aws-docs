---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-granting-tags.html
---

# Managing LF-Tag value permissions
<a name="TBAC-granting-tags"></a>

You can grant the `Drop`, `Alter` permissions on LF-Tags to principals to manage LF-Tag value expressions. You can also grant `Describe`, `Associate`, and `Grant with LF-Tag expressions` permissions on LF-Tags to principals to view the LF-Tags and assign them to Data Catalog resources (databases, tables, and columns). When LF-Tags are assigned to Data Catalog resources, you can use the Lake Formation tag-based access control (LF-TBAC) method to secure those resources. For more information, see [Lake Formation tag-based access control](tag-based-access-control.md).

You can grant these permissions with the grant option so that other principals can grant them. The `Grant with LF-Tag expressions`, `Describe`, and `Associate` permissions are explained in [Add LF-Tag creators](TBAC-adding-tag-creator.md#add-lf-tag-creator).

You can grant the `Describe` and `Associate` permissions on a LF-Tag to an external AWS account. A data lake administrator in that account can then grant those permissions to other principals in the account. Principals to whom the data lake administrator in the external account grants the `Associate` permission can then assign LF-Tags to Data Catalog resources that you shared with their account.

When granting to an external account, you must include the grant option.

You can grant permissions on LF-Tags by using the Lake Formation console, the API, or the AWS Command Line Interface (AWS CLI).

**Topics**
+ [Listing LF-Tag permissions using the console](TBAC-listing-tag-perms-console.md)
+ [Granting LF-Tag permissions using the console](TBAC-granting-tags-console.md)
+ [Managing LF-Tag permissions using the AWS CLI](TBAC-granting-revoking-tags-cli.md)

For more information see [Managing LF-Tags for metadata access control](managing-tags.md) and [Lake Formation tag-based access control](tag-based-access-control.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

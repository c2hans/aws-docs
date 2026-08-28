---
source_url: https://docs.aws.amazon.com/lake-formation/latest/dg/redshift-ds-prereqs.html
---

# Prerequisites for setting up permissions on Amazon Redshift datashares
<a name="redshift-ds-prereqs"></a>

**Update default Data Catalog settings**
To enable Lake Formation permissions for the Data Catalog resources, we recommend that you disable the default **Data Catalog settings** in Lake Formation. For more information, see [Change the default permission model or use hybrid access mode](initial-lf-config.md#setup-change-cat-settings).

**Update permissions**
 In addition to data lake administrator permissions (`AWSLakeFormationDataAdmin`), the following permissions are also required to accept an Amazon Redshift datashare in Lake Formation:
+ `glue:PassConnection on aws:redshift`
+ `redshift:AssociateDataShareConsumer`
+ `redshift:DescribeDataSharesForConsumer`
+ `redshift:DescribeDataShares`

The data lake administrator IAM user has the following permissions implicitly.
+ data\_location\_access
+ create\_database
+ lakefomation:registerResource

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

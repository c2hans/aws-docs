---
source_url: https://docs.aws.amazon.com/glue/latest/dg/crawler-configure-partition-indexes.html
---

# Generating partition indexes
<a name="crawler-configure-partition-indexes"></a>

The Data Catalog supports creating partition indexes to provide efficient lookup for specific partitions. For more information, see [Creating partition indexes](https://docs.aws.amazon.com/glue/latest/dg/partition-indexes.html). The AWS Glue crawler creates partition indexes for Amazon S3 and Delta Lake targets by default.

------
#### [ AWS Management Console ]

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/).

1. Choose **Crawlers** under the **Data Catalog**.

1. When you define a crawler, the option to **Create partition indexes automatically ** is enabled by default under **Advanced options** on the **Set output and scheduling** page.

   To disable this option, you can unselect the checkbox **Create partition indexes automatically ** in the console.

1. Complete the crawler configuration and choose **Create crawler**.

------
#### [ AWS CLI ]

 You can also disable this option by using the AWS CLI, set the `CreatePartitionIndex ` in the `configuration` parameter. The default value is true.

```
aws glue update-crawler \
    --name myCrawler \
    --configuration '{"Version": 1.0, "CreatePartitionIndex": false }'
```

------

## Usage notes for partition indexes
<a name="crawler-configure-partition-indexes-usage-notes"></a>
+ Tables created by the crawler do not have the variable `partition_filtering.enabled` by default. For more information, see [AWS Glue partition indexing and filtering](https://docs.aws.amazon.com/athena/latest/ug/glue-best-practices.html#glue-best-practices-partition-index).
+ Creating partition indexes for encrypted partitions is not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-existing-sources.html
---

# Create a Neptune graph from existing sources
<a name="gettingStarted-existing-sources"></a>

 You can load data into a Neptune graph from another Neptune database, Neptune database cluster snapshot, or from Amazon S3 files. Select the data sources and an IAM role for the data import accordingly. For more information about loading data, see [Create a graph from Amazon S3, a Neptune cluster, or a snapshot](bulk-import-into-a-graph.md).

------
#### [ AWS console ]

![Image showing the AWS console, with the available options and settings configurations.](http://docs.aws.amazon.com/neptune-analytics/latest/userguide/images/getting-started/gettingStartedExistingData.png)

------
#### [ AWS CLI ]

 The following example creates a graph and loads data from Amazon S3.

```
aws neptune-graph create-graph-using-import-task \
--graph-name "neptune-graph-from-s3-source" \
--region "us-east-1" \
--format "CSV" \
--role-arn "arn:aws:iam::1234567890124:role/GraphExecutionRole" \
--source "s3://neptune-demo-test-us-east-1/test-data-csv/" \
--public-connectivity \
--min-provisioned-memory 256 \
--max-provisioned-memory 256
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

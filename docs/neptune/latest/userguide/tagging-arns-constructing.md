---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/tagging-arns-constructing.html
---

# Constructing an ARN for Neptune
<a name="tagging-arns-constructing"></a>

You can construct an ARN for an Amazon Neptune resource using the following syntax. Note that Neptune shares the format of Amazon RDS ARNs.

 `arn:aws:rds:{{<region>}}:{{<account number>}}:{{<resourcetype>}}:{{<name>}}`

The following table shows the format that you should use when constructing an ARN for a particular Neptune administrative resource type.

| Resource Type | ARN Format |
| --- | --- |
| DB instance  | arn:aws:rds:{{<region>}}:{{<account>}}`:db:`{{<name>}}<br />For example:<pre>arn:aws:rds:{{us-east-2}}:{{123456789012}}:db:{{my-instance-1}}</pre> |
| DB cluster | arn:aws:rds:{{<region>}}:{{<account>}}`:cluster:`{{<name>}}<br />For example:<pre>arn:aws:rds:{{us-east-2}}:{{123456789012}}:cluster:{{my-cluster-1}}</pre> |
| Event subscription  | arn:aws:rds:{{<region>}}:{{<account>}}`:es:`{{<name>}}<br />For example:<pre>arn:aws:rds:{{us-east-2}}:{{123456789012}}:es:{{my-subscription}}</pre> |
| DB parameter group  | arn:aws:rds:{{<region>}}:{{<account>}}`:pg:`{{<name>}}<br />For example:<pre>arn:aws:rds:{{us-east-2}}:{{123456789012}}:pg:{{my-param-enable-logs}}</pre> |
| DB cluster parameter group  | arn:aws:rds:{{<region>}}:{{<account>}}`:cluster-pg:`{{<name>}}<br />For example:<pre>arn:aws:rds:{{us-east-2}}:{{123456789012}}:cluster-pg:{{my-cluster-param-timezone}}</pre> |
| DB cluster snapshot  | arn:aws:`rds:`{{<region>}}:{{<account>}}`:cluster-snapshot:`{{<name>}}<br />For example:<pre>arn:aws:rds:{{us-east-2}}:{{123456789012}}:cluster-snapshot:{{my-snap-20160809}}</pre> |
| DB subnet group  | arn:aws:`rds:`{{<region>}}:{{<account>}}`:subgrp:`{{<name>}}<br />For example:<pre>arn:aws:rds:{{us-east-2}}:{{123456789012}}:subgrp:{{my-subnet-10}}</pre> |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

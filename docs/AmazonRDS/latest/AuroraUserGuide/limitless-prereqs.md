---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-prereqs.html
---

# Prerequisites for using Aurora PostgreSQL Limitless Database
<a name="limitless-prereqs"></a>

To use Aurora PostgreSQL Limitless Database, you must first perform the following tasks.

**Topics**
+ [Enabling DB shard group operations](#limitless-enable-iam)

## Enabling DB shard group operations
<a name="limitless-enable-iam"></a>

Before you can create a DB shard group, you must enable DB shard group operations.
+ Add the following section to the IAM policy of the IAM role of the user that accesses Aurora PostgreSQL Limitless Database:

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Sid": "AllowDBShardGroup",
              "Effect": "Allow",
              "Action": [
                  "rds:CreateDBShardGroup",
                  "rds:DescribeDBShardGroups",
                  "rds:DeleteDBShardGroup",
                  "rds:ModifyDBShardGroup",
                  "rds:RebootDBShardGroup"
              ],
              "Resource": [
                  "arn:aws:rds:*:*:shard-group:*",
                  "arn:aws:rds:*:*:cluster:*"
              ]
          }
      ]
  }
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

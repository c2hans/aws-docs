---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.tag-based-policy.html
---

# Using tag-based access control for Database Insights
<a name="USER_PerfInsights.access-control.tag-based-policy"></a>

You can control access to Database Insights metrics using tags inherited from the parent DB instance. To control access to Database Insights operations, use IAM policies. These policies can check the tags on your DB instance to determine permissions.

## How tags work with Database Insights
<a name="USER_PerfInsights.access-control.tag-inheritance"></a>

Database Insights automatically applies your DB instance tags to authorize Database Insights metrics. When you add tags to your DB instance, you can immediately use those tags to control access to Database Insights data.
+ To add or update tags for Database Insights metrics, modify the tags on your DB instance.
+ To view tags for Database Insights metrics, call `ListTagsForResource` on the Database Insights metric resource. It will return the tags from the DB instance associated with the metric.

**Note**
The `TagResource` and `UntagResource` operations return an error if you try to use them directly on Database Insights metrics.

## Creating tag-based IAM policies
<a name="USER_PerfInsights.access-control.tag-based-policies"></a>

To control access to Database Insights operations, use the `aws:ResourceTag` condition key in your IAM policies. These policies check the tags on yourDB instance.

**Example**
This policy prevents access to Database Insights metrics for production databases. The policy denies the `pi:GetResourceMetrics` operation in Database Insights for any database resource tagged with `env:prod`.

```
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "pi:GetResourceMetrics",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/env": "prod"
                }
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

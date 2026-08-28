---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-tag-filters-aws-cli.html
---

# Use tags to filter Auto Scaling groups
<a name="use-tag-filters-aws-cli"></a>

The following examples show you how to use filters with the [describe-auto-scaling-groups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html) command to describe Auto Scaling groups with specific tags. Filtering by tags is limited to the AWS CLI or an SDK, and is not available from the console.

**Filtering considerations**
+ You can specify multiple filters and multiple filter values in a single request.
+ You cannot use wildcards with the filter values.
+ Filter values are case-sensitive.

**Example: Describe Auto Scaling groups with a specific tag key and value pair**
The following command shows how to filter results to show only Auto Scaling groups with the tag key and value pair of **`environment=production`**.

```
aws autoscaling describe-auto-scaling-groups \
  --filters Name=tag-key,Values={{environment}} Name=tag-value,Values={{production}}
```

The following is an example response.

```
{
    "AutoScalingGroups": [
        {
            "AutoScalingGroupName": "my-asg",
            "AutoScalingGroupARN": "{{arn}}",
            "LaunchTemplate": {
                "LaunchTemplateId": "lt-0b97f1e282EXAMPLE",
                "LaunchTemplateName": "my-launch-template",
                "Version": "$Latest"
            },
            "MinSize": 1,
            "MaxSize": 5,
            "DesiredCapacity": 1,
            ...
            "Tags": [
                {
                    "ResourceType": "auto-scaling-group",
                    "ResourceId": "my-asg",
                    "PropagateAtLaunch": true,
                    "Value": "production",
                    "Key": "environment"
                }
            ],
            ...
        },

    {{... additional groups ...}}

    ]
}
```

Alternatively, you can specify tags using a `tag:<key>` filter. For example, the following command shows how to filter results to show only Auto Scaling groups with a tag key and value pair of **`environment=production`**. This filter is formatted as follows: `Name=tag:<key>,Values=<value>`, with **<key>** and **<value>** representing a tag key and value pair.

```
aws autoscaling describe-auto-scaling-groups \
  --filters Name=tag:{{environment}},Values={{production}}
```

You can also filter AWS CLI output by using the `--query` option. The following example shows how to limit AWS CLI output for the previous command to the group name, minimum size, maximum size, and desired capacity attributes only.

```
aws autoscaling describe-auto-scaling-groups \
  --filters Name=tag:{{environment}},Values={{production}} \
  --query "AutoScalingGroups[].{AutoScalingGroupName: AutoScalingGroupName, MinSize: MinSize, MaxSize: MaxSize, DesiredCapacity: DesiredCapacity}"
```

The following is an example response.

```
[
    {
        "AutoScalingGroupName": "my-asg",
        "MinSize": 0,
        "MaxSize": 10,
        "DesiredCapacity": 1
    },

    {{... additional groups ...}}

]
```

For more information about filtering, see [Filtering AWS CLI output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html) in the *AWS Command Line Interface User Guide*.

**Example: Describe Auto Scaling groups with tags that match the tag key specified**
The following command shows how to filter results to show only Auto Scaling groups with the `environment` tag, regardless of the tag value.

```
aws autoscaling describe-auto-scaling-groups \
  --filters Name=tag-key,Values={{environment}}
```

**Example: Describe Auto Scaling groups with tags that match the set of tag keys specified**
The following command shows how to filter results to show only Auto Scaling groups with tags for `environment` and `project`, regardless of the tag values.

```
aws autoscaling describe-auto-scaling-groups \
  --filters Name=tag-key,Values={{environment}} Name=tag-key,Values={{project}}
```

**Example: Describe Auto Scaling groups with tags that match at least one of the tag keys specified**
The following command shows how to filter results to show only Auto Scaling groups with tags for `environment` or `project`, regardless of the tag values.

```
aws autoscaling describe-auto-scaling-groups \
  --filters Name=tag-key,Values={{environment}},{{project}}
```

**Example: Describe Auto Scaling groups with the specified tag value**
The following command shows how to filter results to show only Auto Scaling groups with a tag value of `production`, regardless of the tag key.

```
aws autoscaling describe-auto-scaling-groups \
  --filters Name=tag-value,Values={{production}}
```

**Example: Describe Auto Scaling groups with the set of tag values specified**
The following command shows how to filter results to show only Auto Scaling groups with the tag values `production` and `development`, regardless of the tag key.

```
aws autoscaling describe-auto-scaling-groups \
  --filters Name=tag-value,Values={{production}} Name=tag-value,Values={{development}}
```

**Example: Describe Auto Scaling groups with tags that match at least one of the tag values specified**
The following command shows how to filter results to show only Auto Scaling groups with a tag value of `production` or `development`, regardless of the tag key.

```
aws autoscaling describe-auto-scaling-groups \
  --filters Name=tag-value,Values={{production}},{{development}}
```

**Example: Describe Auto Scaling groups with tags that match multiple tag keys and values**
You can also combine filters to create custom AND and OR logic to do more complex filtering.

The following command shows how to filter results to show only Auto Scaling groups with a specific set of tags. One tag key is `environment` AND the tag value is (`production` OR `development`) AND the other tag key is `costcenter` AND the tag value is `cc123`.

```
aws autoscaling describe-auto-scaling-groups \
  --filters Name=tag:{{environment}},Values={{production}},{{development}} Name=tag:{{costcenter}},Values={{cc123}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

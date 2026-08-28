---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/capacity-tags-access-policy-example.html
---

# Example: Allow capacity tags for specific keys and values
<a name="capacity-tags-access-policy-example"></a>

The following identity-based policy, which you attach to an IAM user or role, allows a principal to create and update compute environments and to set capacity tags, but only when the `CostCenter` tag value is `engineering` or `ops` and no tag keys other than `CostCenter` and `Team` are used. Requests that include any other tag key or a different `CostCenter` value are denied.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowComputeEnvironmentManagement",
      "Effect": "Allow",
      "Action": [
        "batch:CreateComputeEnvironment",
        "batch:UpdateComputeEnvironment"
      ],
      "Resource": "arn:aws:batch:us-east-1:123456789012:compute-environment/*"
    },
    {
      "Sid": "AllowSetCapacityTagsForApprovedTags",
      "Effect": "Allow",
      "Action": "batch:SetCapacityTags",
      "Resource": "arn:aws:batch:us-east-1:123456789012:compute-environment/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/CostCenter": ["engineering", "ops"]
        },
        "ForAllValues:StringEquals": {
          "aws:TagKeys": ["CostCenter", "Team"]
        }
      }
    }
  ]
}
```

To deny capacity tagging entirely while still permitting compute environment creation and updates, attach a policy with an explicit `Deny` on `batch:SetCapacityTags`:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "batch:SetCapacityTags",
      "Resource": "*"
    }
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

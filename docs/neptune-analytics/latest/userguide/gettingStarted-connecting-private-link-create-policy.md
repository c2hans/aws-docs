---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-private-link-create-policy.html
---

# Creating an Amazon VPC endpoint policy for Neptune Analytics data plane
<a name="gettingStarted-connecting-private-link-create-policy"></a>

**Note**
 AWS PrivateLink for Neptune Analytics does not support VPC endpoint policies for the control plane service `neptune-graph`. VPC endpoint policies are only supported for the Neptune Analytics data plane service `neptune-graph-data`.

 You can attach an endpoint policy to your Amazon VPC endpoint that controls access to a Neptune Analytics graph. The policy specifies the following information:
+  The AWS Identity and Access Management (IAM) principal that can perform actions.
+  The actions that can be performed.
+  The resources on which actions can be performed.

 **Restricting access to a specific Neptune Analytics graph from an Amazon VPC endpoint.**

 You can create an endpoint policy that restricts access to only specific Neptune Analytics graphs. This type of policy is useful if you have other AWS services in your Amazon VPC that use graphs. The following policy only provides access to the `GetGraphSummary` action/API from the VPC endpoint.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Id": "Policy1216114807515",
  "Statement": [
    {
      "Sid": "Access-to-specific-graph-only",
      "Principal": "*",
      "Action": [
        "neptune-graph:GetGraphSummary"
      ],
      "Effect": "Allow",
      "Resource": [
        "arn:aws:neptune-graph:{{us-east-1}}:{{111122223333}}:graph/{{resource-id}}"
      ]
    }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

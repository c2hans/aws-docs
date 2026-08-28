---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-manage-subset-automatic.html
---

# Removing Runtime Monitoring from an Amazon ECS cluster
<a name="ecs-guard-duty-manage-subset-automatic"></a>

You might want to exclude certain clusters from protection, for example clusters that you use for testing. This causes GuardDuty to perform the following operations on resources in the cluster:
+ No longer deploy the GuardDuty security agent to new standalone Fargate tasks, or new service deployments.

  In order to preserve the immutability constraint, existing tasks and deployments with Runtime Monitoring enabled are not affected.
+ Stop billing and no longer accepts run time events for tasks.

## Procedure
<a name="ecs-guard-duty-manage-subset-automatic-procedure"></a>

Perform the following steps to remove Runtime Monitoring from a cluster.

1. Use the Amazon ECS console or AWS CLI to set the `GuardDutyManaged` tag key on the cluster to `false`. For more information, see [Updating a cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-cluster-v2.html) or [Working with tags using the CLI or API](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html#tag-resources-api-sdk). Use the following values for the tag.
**Note**
The Key and Value are case sensitive and must exactly match the strings.

   Key = `GuardDutyManaged`, Value = `false`

1. Delete the GuardDuty VPC endpoint for the cluster. For more information about how to delete VPC endpoints, see [Delete an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/delete-interface-endpoint.html) in the *AWS PrivateLink User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-endpoints-custom-deleting.html
---

# Deleting a custom endpoint
<a name="aurora-endpoints-custom-deleting"></a>

Delete a custom endpoint using the AWS Management Console, AWS CLI, or the Amazon RDS API.

## Console
<a name="aurora-delete-endpoint.console"></a>

To delete a custom endpoint with the AWS Management Console, go to the cluster detail page, select the appropriate custom endpoint, and select the **Delete** action.

![Delete custom endpoint page.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/AuroraDeleteCustomEndpoint.png)

## AWS CLI
<a name="aurora-delete-endpoint.cli"></a>

To delete a custom endpoint with the AWS CLI, run the [delete-db-cluster-endpoint](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-db-cluster-endpoint.html) command.

The following command deletes a custom endpoint. You don't need to specify the associated cluster, but you must specify the region.

For Linux, macOS, or Unix:

```
aws rds delete-db-cluster-endpoint --db-cluster-endpoint-identifier {{custom-end-point-id}} \
  --region {{region_name}}
```

For Windows:

```
aws rds delete-db-cluster-endpoint --db-cluster-endpoint-identifier {{custom-end-point-id}} ^
  --region {{region_name}}
```

## RDS API
<a name="aurora-delete-endpoint.api"></a>

To delete a custom endpoint with the RDS API, run the [DeleteDBClusterEndpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DeleteDBClusterEndpoint.html) operation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

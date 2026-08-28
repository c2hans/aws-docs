---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance-details-tags-external.html
---

# Adding tags to External container instances for Amazon ECS
<a name="instance-details-tags-external"></a>

You can associate tags with your external container instances for Amazon ECS by using one of the following methods.
+ Method 1 – Before running the installation script to register your external instance with your cluster, create or edit the Amazon ECS container agent configuration file at `/etc/ecs/ecs.config` and add the `ECS_CONTAINER_INSTANCE_TAGS` container agent configuration parameter. This creates tags that are associated with the external instance.

  The following is example syntax.

  ```
  ECS_CONTAINER_INSTANCE_TAGS={"{{tag_key}}": "{{tag_value}}"}
  ```
+ Method 2 – After your external instance is registered to your cluster, you can use the AWS Management Console to add tags. For more information, see [Adding tags to existing resources (Amazon ECS console)](tag-resources-console.md#adding-or-deleting-tags).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

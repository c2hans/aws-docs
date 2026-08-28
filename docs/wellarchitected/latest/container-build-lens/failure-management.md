---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/failure-management.html
---

# Failure management
<a name="failure-management"></a>

| CONTAINER\_BUILD\_REL\_05: How do you monitor the health of a container? |
| --- |
|   |

 **Plan for health checks in all containers builds and deployments**

It is common to initially develop container applications without thinking of the availability of the services in the container. When running container applications, there is no way of knowing whether the services running within a container are up or not. Adding a health check or probe to the container provides testing of the services in the container. Health check options are available in Docker using the `HEALTHCHECK` command, however, `containerd` does not have this option. Examine the orchestrations systems health check and probing options. This could include liveness and readiness probes within Amazon EKS or health checks within a definition file within Amazon ECS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

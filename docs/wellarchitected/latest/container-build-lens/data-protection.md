---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/data-protection.html
---

# Data protection
<a name="data-protection"></a>

| CONTAINER\_BUILD\_SEC\_05: How do you handle data within your containerized applications? |
| --- |
|   |

** Do not hardcode sensitive data into your container image**

 With respect to handling data in the build and design of the container, it is important that no sensitive information is stored in the container itself. For example, user credentials should never be hardcoded into your container image. Instead, consider using a secret management protocol that is compatible with the container orchestration system being used to manage the container workloads.

 **Ensure that persistent data is stored outside of the container**

 Also, if your containerized application writes or consumes persistent data, ensure that data is stored outside of the container. Since containers are intended to be ephemeral, use volumes to store persistent data that will remain intact long after a container’s lifecycle has completed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/software-and-architecture-patterns.html
---

# Software and architecture patterns
<a name="software-and-architecture-patterns"></a>

| CONTAINER\_BUILD\_SUSTAINABILITY\_01: How do you design your containerized application in a way that reduces the use of the underlying resources? |
| --- |
|   |

 When designing containerized application, you should keep your build manifests up-to-date and aligned with your application needs. A containerized application image starts from a Dockerfile. The Dockerfile includes all commands required to include the configuration and dependencies for the containerized application. If there are some dependencies that are no longer required, removing them from the Dockerfile can:
+  Reduce the time that it takes to build the container image. This affects host resource consumption by the build process.
+  Reduce the container image size and therefore reduce the time it takes for this image to be pulled to an instance. This affects host resources usage for running and storing the container images.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

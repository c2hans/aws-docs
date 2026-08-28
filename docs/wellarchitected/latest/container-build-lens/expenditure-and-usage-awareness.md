---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/expenditure-and-usage-awareness.html
---

# Expenditure and usage awareness
<a name="expenditure-and-usage-awareness"></a>

| CONTAINER\_BUILD\_COST\_02: How do you design your container build process to avoid unnecessary cost? |
| --- |
|   |

 **Designing efficient container build process**

 Building containers is a process that consumes compute and storage resources and can lead to unnecessary costs if not using it properly. The build process consumes resources for each build, and there are some considerations that have to be taken for it to be efficient from a cost perspective.

 **Application dependencies**

The container image is usually being built alongside with the application build step. During this build step, all necessary dependencies, libraries, and modules that are being used by the application code are downloaded to the container image. Using unnecessary dependencies will make the build time longer, and will result in wasting compute resources of the build system.

 **Common container image dependencies**

 Some operating system packages are needed for multiple applications in the organization for a specific runtime (for example, Python and Java). Building a parent container image that preinstalls all common operating system packages and dependencies for the specific runtime will result in a more efficient build process. Without this common image, each individual container image would be installing the same packages, thus wasting compute and network resources. This practice will also shorten the time for container images built from a specific runtime, since all of its common operating system packages and dependencies are already included in the parent container image. As a result, this will reduce costs for building all other container images that use this parent image.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

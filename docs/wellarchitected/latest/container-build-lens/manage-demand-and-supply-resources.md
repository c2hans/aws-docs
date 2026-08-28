---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/manage-demand-and-supply-resources.html
---

# Manage demand and supply resources
<a name="manage-demand-and-supply-resources"></a>

| CONTAINER\_BUILD\_COST\_07: How do you minimize cost for your containerized application during startup time? |
| --- |
|   |

Longer startup times for containerized applications can result in wasted compute resources. Shortening startup times can be done on the application-level (code optimization), or on the container level. For example, if the application needs external dependencies to be present in the container, it should be already installed during the build process, or it should be included in the parent image, and not downloaded at startup using an entrypoint script or `DOCKERFILE` commands.

| CONTAINER\_BUILD\_COST\_08: What systems are you using to create your container build process? |
| --- |
|   |

Creating any build process requires developing, maintaining, and operating a build system. This can be done by a variety of methods, such as using OSS tooling for job automation, or using self-developed systems that are able to run build scripts for your application. However, running and maintaining this kind of system involves software development costs, operational costs, compute, and storage costs for running the system. Alternatively you can use build and pipeline services, such as Amazon EC2 Image Builder, AWS CodeBuild, and AWS CodePipeline. Using managed services removes the operational overhead and allows developers to consume pipeline runs and build jobs on a pay-as-you-go basis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

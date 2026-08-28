---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/best-practices.html
---

# Best practices
<a name="best-practices"></a>

 Operational excellence is defined by the ability to run and monitor your systems to ensure they are delivering the business value as intended. Further, it can continuously improve support processes and procedures throughout the lifetime of the system. Operational excellence with regard to your containers and container images is no different. As your application evolves and matures, you must update your container images and running containers to provide additional features to your customers. With these updates and new container deployments, you must have the right mechanisms in place to validate that your workload is attaining its intended business goals. These mechanisms include container health checks and the collection of container logs external to the container. The following guidance is in addition to the best practice guidance laid out by the [Operational Excellence Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).

 To drive operational excellence in your containerized workloads, you must understand your container images. This includes the capabilities that are built into the container image, the container image build process, and deployment behavior expectations. You will then be able to design your images to provide insight into your container status and build procedures in order to build containers that best fit your workload.

**Topics**
+ [Organization](organization.md)
+ [Prepare](prepare.md)
+ [Operate](operate.md)
+ [Evolve](evolve.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

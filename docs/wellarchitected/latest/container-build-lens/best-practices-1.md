---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/best-practices-1.html
---

# Best practices
<a name="best-practices-1"></a>

One of the greatest benefits of building applications using container images is confidence that the application can run on any sort of infrastructure. Whether the container is deployed on a developer’s personal laptop or in public cloud infrastructure, the container will run as expected, because all the required dependencies are packaged within the image. With this in mind, alignment with security standards and best practices is of utmost importance as containers are deployed in different types of environments.

 The best practices laid out in this section of the whitepaper are designed to help you address vulnerabilities that may be introduced during the design and build of a container image.

This section defines how the security pillar relates to Container Build Lens specifically.

**Topics**
+ [Identity and access management](identity-and-access-management.md)
+ [Detective controls](detective-controls.md)
+ [Infrastructure protection](infrastructure-protection.md)
+ [Data protection](data-protection.md)
+ [Incident response](incident-response.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/architecture.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Architecture
<a name="architecture"></a>

**Recommended Production Architecture**

The diagram below shows Wickr Enterprise configured as recommended for production, with both MySQL and Object Storage services situated outside of the Kubernetes cluster.

![The architecture diagram.](http://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/images/wickr-enterprise-ha.png)

**Internal or Test Architecture**

The diagram below displays the configuration of Wickr Enterprise, utilizing the internal MYSQL and Object Storage services. Although it may satisfy the specific needs of certain deployments, it is not recommended for general production use.

![The architecture diagram.](http://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/images/wickr-enterprise-ha-mysql.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

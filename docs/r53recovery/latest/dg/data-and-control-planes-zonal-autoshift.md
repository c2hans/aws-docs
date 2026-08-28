---
source_url: https://docs.aws.amazon.com/r53recovery/latest/dg/data-and-control-planes-zonal-autoshift.html
---

# Data and control planes for zonal autoshift
<a name="data-and-control-planes-zonal-autoshift"></a>

As you plan for failover and disaster recovery, consider how resilient your failover mechanisms are. We recommend that you make sure that the mechanisms that you depend on during failover are highly available, so that you can use them when you need them in a disaster scenario. Typically, you should use data plane functions for your mechanisms whenever you can, for the greatest reliability and fault tolerance. With that in mind, it's important to understand how the functionality of a service is divided between control planes and data planes, and when you can rely on an expectation of extreme reliability with a service's data plane.

In general, a *control plane* enables you to do basic management functions, such as create, update, and delete resources in the service. A *data plane* provides a service's core functionality.

For more information about data planes, control planes, and how AWS builds services to meet high availability targets, see the [Static stability using Availability Zones paper](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) in the Amazon Builders' Library.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query r53recovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

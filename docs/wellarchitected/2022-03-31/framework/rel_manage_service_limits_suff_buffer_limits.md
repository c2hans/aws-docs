---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_manage_service_limits_suff_buffer_limits.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL01-BP06 Ensure that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover
<a name="rel_manage_service_limits_suff_buffer_limits"></a>

 When a resource fails, it might still be counted against quotas until it’s successfully terminated. Ensure that your quotas cover the overlap of all failed resources with replacements before the failed resources are terminated. You should consider an Availability Zone failure when calculating this gap.

 **Common anti-patterns:**
+  Setting service quotas based on current needs without accounting for failover scenarios.

 **Benefits of establishing this best practice:** When events potentially impact availability, the cloud allows you to implement strategies to mitigate or recover from these events. Such strategies often include creating additional resources to replace failed ones. Your quota strategy must accommodate these additional resources.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Ensure that there is enough gap between your service quota and your maximum usage to accommodate for a failover.
  +  Determine your service quotas, accounting for your deployment patterns, availability requirements, and consumption growth.
  +  Request quota increases if necessary. Plan for necessary time for quota increase requests to be fulfilled.
    +  Determine your reliability requirements (also known as your number of 9's).
    +  Establish your fault scenarios (for example, loss of a component, an Availability Zone, or a Region).
    +  Establish your deployment methodology (for example, canary, blue/green, red/black, or rolling).
    +  Include an appropriate buffer (for example, 15%) to the current limit.
    +  Plan consumption growth (for example, monitor your trends in consumption).

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Marketplace: CMDB products that help track limits](https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB)
+  [AWS Service Quotas (formerly referred to as service limits)](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
+  [AWS Trusted Advisor Best Practice Checks (see the Service Limits section)](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/)
+  [Amazon EC2 Service Limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
+  [What Is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)

 **Related videos:**
+  [AWS Live re:Inforce 2019 - Service Quotas](https://youtu.be/O9R5dWgtrVo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_user_a3.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS02-BP02 Align SLAs with sustainability goals
<a name="sus_sus_user_a3"></a>

 Define and update Service Level Agreements (SLAs) such as availability or data retention periods to minimize the number of resources required to support your workload while continuing to meet business requirements.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Define SLAs that support your sustainability goals while meeting your business requirements.
+  Redefine SLAs to meet business requirements, not exceed them.
+  Make trade-offs that significantly reduce sustainability impacts in exchange for acceptable decreases in service levels.
+  Use design patterns that prioritize business-critical functions, and allow lower service levels (such as response time or recovery time objectives) for non-critical functions.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Service Level Agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/?aws-sla-cards.sort-by=item.additionalFields.serviceNameLower&aws-sla-cards.sort-order=asc&awsf.tech-category-filter=*all)
+  [Importance of Service Level Agreement for SaaS Providers](https://aws.amazon.com/blogs/apn/importance-of-service-level-agreement-for-saas-providers/)

 **Related videos:**
+  [Building Sustainably on AWS](https://www.youtube.com/watch?v=ARAitMSIxc8)

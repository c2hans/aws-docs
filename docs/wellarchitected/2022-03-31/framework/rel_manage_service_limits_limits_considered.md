---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_manage_service_limits_limits_considered.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL01-BP02 Manage service quotas across accounts and regions
<a name="rel_manage_service_limits_limits_considered"></a>

 If you are using multiple AWS accounts or AWS Regions, ensure that you request the appropriate quotas in all environments in which your production workloads run.

 Service quotas are tracked per account. Unless otherwise noted, each quota is AWS Region-specific. In addition to the production environments, also manage quotas in all applicable non-production environments, so that testing and development are not hindered.

 **Common anti-patterns:**
+  Allowing resource utilization in one isolation zone to grow with no mechanism to maintain capacity in the other ones.
+  Manually setting all quotas independently in isolation zones.
+  Not ensuring Regionally isolated deployments are sized to accommodate the increase in traffic from another Region if a deployment is lost.

 **Benefits of establishing this best practice:** Ensuring that you can handle your current load if an isolation zone is unavailable can help reduce the number of errors that occur during failover, instead of causing a denial of service to your customers.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Select relevant accounts and Regions based on your service requirements, latency, regulatory, and disaster recovery (DR) requirements.
+  Identify service quotas across all relevant accounts, Regions, and Availability Zones. The limits are scoped to account and Region.
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Marketplace: CMDB products that help track limits](https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB)
+  [AWS Service Quotas (formerly referred to as service limits)](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
+  [AWS Trusted Advisor Best Practice Checks (see the Service Limits section)](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/)
+  [AWS limit monitor on AWS answers](https://aws.amazon.com/answers/account-management/limit-monitor/)
+  [Amazon EC2 Service Limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)

 **Related videos:**
+  [AWS Live re:Inforce 2019 - Service Quotas](https://youtu.be/O9R5dWgtrVo)

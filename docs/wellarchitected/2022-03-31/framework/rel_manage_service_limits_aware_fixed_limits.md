---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_manage_service_limits_aware_fixed_limits.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL01-BP03 Accommodate fixed service quotas and constraints through architecture
<a name="rel_manage_service_limits_aware_fixed_limits"></a>

 Be aware of unchangeable service quotas and physical resources, and architect to prevent these from impacting reliability.

 Examples include network bandwidth, AWS Lambda payload size, throttle burst rate for API Gateway, and concurrent user connections to an Amazon Redshift cluster.

 **Common anti-patterns:**
+  Performing benchmarking for too short of time, utilizing the burst limit, but then expecting the service to perform at that capacity for sustained periods.
+  Choosing a design that uses one resource of a service per user or customer, unaware that there are design constraints that will cause this design to fail as you scale.

 **Benefits of establishing this best practice:** Tracking fixed quotes in AWS services and constraints in other parts of your workload, such as connectivity constraints, IP address constraints, and constraints in third-party services, allows you to detect when you are trending toward a quota and gives you the ability to address the quota before it's exceeded.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Be aware of fixed service quotas Be aware of fixed service quotas and constraints and architect around these.
  +  [AWS Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Marketplace: CMDB products that help track limits](https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB)
+  [AWS Service Quotas (formerly referred to as service limits)](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
+  [AWS Trusted Advisor Best Practice Checks (see the Service Limits section)](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/)
+  [AWS limit monitor on AWS answers](https://aws.amazon.com/answers/account-management/limit-monitor/)
+  [Amazon EC2 Service Limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
+  [What Is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)

 **Related videos:**
+  [AWS Live re:Inforce 2019 - Service Quotas](https://youtu.be/O9R5dWgtrVo)

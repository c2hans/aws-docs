---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_manage_service_limits_monitor_manage_limits.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL01-BP04 Monitor and manage quotas
<a name="rel_manage_service_limits_monitor_manage_limits"></a>

 Evaluate your potential usage and increase your quotas appropriately, allowing for planned growth in usage.

 For supported services, you can manage your quotas by configuring CloudWatch alarms to monitor usage and alert you to approaching quotas. These alarms can be triggered from Service Quotas or from Trusted Advisor. You can also use metric filters on CloudWatch Logs to search and extract patterns in logs to determine if usage is approaching quota thresholds.

 **Common anti-patterns:**
+  Configuring alarms for when Service Quotas are being approached, but having no process on how to respond to an alert.
+  Only configuring alarms for services supported by Service Quotas and not monitoring other services.

 **Benefits of establishing this best practice:** Automatic tracking of the AWS service quotas and monitoring your usage against those quotas will allow you to see when you are approaching a quota limit. You can also use this monitoring data to assess when you might lower quotas to save costs.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Monitor and manage your quotas Evaluate your potential usage on AWS, increase your regional service quotas appropriately, and allow planned growth in usage.
  +  Capture current resource consumption (for example, buckets, instances). Use service API operations, such as the Amazon EC2 DescribeInstances API, to collect current resource consumption.
  +  Capture your current quotas Use AWS Service Quotas, AWS Trusted Advisor, and AWS documentation.
    +  Use AWS Service Quotas, an AWS service that helps you manage your quotas for over 100 AWS services from one location.
    +  Use Trusted Advisor service limits to determine your current service limits.
    +  Use service API operations to determine current service quotas where supported.
    +  Keep a record of quota increases that have been requested, and their status After a quota increase has been approved, ensure that you update your records to reflect the change to the quota.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Marketplace: CMDB products that help track limits](https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB)
+  [AWS Service Quotas (formerly referred to as service limits)](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
+  [AWS Trusted Advisor Best Practice Checks for Service Limits](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html)
+  [AWS limit monitor on AWS answers](https://aws.amazon.com/answers/account-management/limit-monitor/)
+  [Amazon EC2 Service Limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
+  [What Is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
+  [Monitor Service Quotas using Amazon CloudWatch alarms](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html)

 **Related videos:**
+  [AWS Live re:Inforce 2019 - Service Quotas](https://youtu.be/O9R5dWgtrVo)

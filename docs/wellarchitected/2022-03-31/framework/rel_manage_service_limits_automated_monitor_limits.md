---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_manage_service_limits_automated_monitor_limits.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL01-BP05 Automate quota management
<a name="rel_manage_service_limits_automated_monitor_limits"></a>

 Implement tools to alert you when thresholds are being approached. You can automate quota increase requests by using AWS Service Quotas APIs.

 If you integrate your Configuration Management Database (CMDB) or ticketing system with Service Quotas, you can automate the tracking of quota increase requests and current quotas. In addition to the AWS SDK, Service Quotas offers automation using the AWS Command Line Interface (AWS CLI).

 **Common anti-patterns:**
+  Tracking the quotas and usage in spreadsheets.
+  Running reports on usage daily, weekly, or monthly, and then comparing usage to the quotas.

 **Benefits of establishing this best practice:** Automated tracking of the AWS service quotas and monitoring of your usage against that quota allows you to see when you are approaching a quota. You can set up automation to assist you in requesting a quota increase when needed. You might want to consider lowering some quotas when your usage trends in the opposite direction to realize the benefits of lowered risk (in case of compromised credentials) and cost savings.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Set up automated monitoring Implement tools using SDKs to alert you when thresholds are being approached.
  +  Use Service Quotas and augment the service with an automated quota monitoring solution, such as AWS Limit Monitor or an offering from AWS Marketplace.
    +  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
    +  [Quota Monitor on AWS - AWS Solution](https://aws.amazon.com/answers/account-management/limit-monitor/)
  +  Set up triggered responses based on quota thresholds, using Amazon SNS and AWS Service Quotas APIs.
  +  Test automation.
    +  Configure limit thresholds.
    +  Integrate with change events from AWS Config, deployment pipelines, Amazon EventBridge, or third parties.
    +  Artificially set low quota thresholds to test responses.
    +  Set up triggers to take appropriate action on notifications and contact AWS Support when necessary.
    +  Manually trigger change events.
    +  Run a game day to test the quota increase change process.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help with configuration management](https://aws.amazon.com/partners/find/results/?keyword=Configuration+Management)
+  [AWS Marketplace: CMDB products that help track limits](https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB)
+  [AWS Service Quotas (formerly referred to as service limits)](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
+  [AWS Trusted Advisor Best Practice Checks (see the Service Limits section)](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/)
+  [Quota Monitor on AWS - AWS Solution](https://aws.amazon.com/answers/account-management/limit-monitor/)
+  [Amazon EC2 Service Limits](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html)
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)

 **Related videos:**
+  [AWS Live re:Inforce 2019 - Service Quotas](https://youtu.be/O9R5dWgtrVo)

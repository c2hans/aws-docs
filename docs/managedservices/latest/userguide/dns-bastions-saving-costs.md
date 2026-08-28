---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/dns-bastions-saving-costs.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Saving costs on Single-account landing zone (SALZ) bastions
<a name="dns-bastions-saving-costs"></a>

AMS provides two SSH bastions and two RDP bastions in the default configuration for you to connect to your Amazon EC2 instances, and also deploys two DMZ bastions in the default configuration for service operations. The bastions use m4. large Amazon EC2 instances by default. You have an option to change the Amazon EC2 instances used for bastions to t3.small, and save cost.

If you are using on-demand instances, or spot instances, or a savings plan, you should consider this feature, and save costs. If you use Reserved Instances consider if using t3.small instances might lower your costs. To change the instance type, submit an RFC with Management \| Advanced stack components \| EC2 instance stack \| Resize (ct-15mazjj88xc69) CT from your AMS account.

Contact your cloud service delivery manager (CSDM) for additional questions, or to check if you can benefit from this feature.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

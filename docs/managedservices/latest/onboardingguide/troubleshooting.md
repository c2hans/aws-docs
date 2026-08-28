---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/troubleshooting.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Troubleshooting
<a name="troubleshooting"></a>

Some things to try if you run into trouble:
+ The AMS-managed Active Directory outbound security group needs to be allowed connection through your CIDR block (e.g. 10.27.0.0/16) to your domain controller.
+ Trace the route in the AWS Console from domain controller to domain controller checking all security groups along the way.
+ Make sure you can ping the AMS-managed Active Directory Domain Controllers if Internet Control Message Protocol (ICMP) is allowed.
+ Make sure your Domain Controller can communicate with AWS Directory Services.
+ Make sure the conditional forwarders resolve and are validated.
+ If you do not see **Forest Trust** in the New Trust wizard, then your conditional forwarders may not be working correctly:
  + Use nslookup to test resolution
  + Try rebooting the Domain Controller

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

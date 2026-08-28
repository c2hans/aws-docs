---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/salz-shared-services.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# AMS Single-account landing zone shared services
<a name="salz-shared-services"></a>

Shared services subnets contain AMS Directory Services, the Management Host that automates provisioning and common tasks, antivirus (TrendMicro) management server, and internal bastion hosts:
+ AMS Directory Services = AD Domain Controller

  Creates an Active Directory in AMS accounts, creates the AMS domain, joins managed stacks to the domain on launch.
+ Management hosts = AMS Management Host (automate provisioning and common tasks)

  Act as an API endpoint to modify Directory Service, interact with Directory Service domain controllers.
+ Security services: Antivirus (TrendMicro) management server = EPS DSM \+ EPS Relay

  Leverages Trend Micro™ Deep Security software (DSM), operates in a client-server model and has a back-end database, includes Deep Security managers, agents, and relays.
+ Internal bastion hosts = Customer bastions

  Special purpose servers designed to be the primary access point from the Internet and act as a proxy to your other Amazon EC2 instances.

![The Shared Services Subnet includes an active directory, an internal bastion, a management host, an EPS DSM, an EPS relay, and a controller.](http://docs.aws.amazon.com/managedservices/latest/userguide/images/AMS_VPC_Shared_Services_diagram.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

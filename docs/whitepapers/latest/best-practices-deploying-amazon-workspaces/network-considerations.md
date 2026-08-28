---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/network-considerations.html
---

# Network considerations
<a name="network-considerations"></a>

 Each WorkSpace is associated with the specific Amazon VPC and AWS Directory Service construct that you used to create it. All AWS Directory Service constructs (Simple AD, AD Connector, and Microsoft AD) require two subnets to operate, each in different Availability Zones (AZs). Subnets are permanently affiliated with a Directory Service construct and can’t be modified after it is created. Because of this, it’s imperative that you determine the right subnet sizes before you create the Directory Services construct. Carefully consider the following before you create the subnets:
+  How many WorkSpaces will you need over time?
+  What is the expected growth?
+  What types of users will you need to accommodate?
+  How many AD domains will you connect?
+  Where do your enterprise accounts reside?

 Amazon recommends defining user groups, or personas, based on the type of access and the user authentication you require as part of your planning process. Answers to these questions are helpful when you need to limit access to certain applications or resources. Defined user personas can help you segment and restrict access using AWS Directory Service, network access control lists, routing tables, and VPC security groups. Each AWS Directory Service construct uses two subnets and applies the same settings to all WorkSpaces that launch from that construct. For example, you can use a security group that applies to all WorkSpaces attached to an AD Connector to specify whether MFA is required, or whether an end-user can have local administrator access on their WorkSpace.

**Note**
 Each AD Connector connects to your existing Enterprise Microsoft AD. To take advantage of this capability and specify an Organizational Unit (OU), you must construct your Directory Service to take your user personas into consideration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

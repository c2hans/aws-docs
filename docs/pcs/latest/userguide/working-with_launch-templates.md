---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_launch-templates.html
---

# Using Amazon EC2 launch templates with AWS PCS
<a name="working-with_launch-templates"></a>

In Amazon EC2, a launch template can store a set of preferences so that you don't have to specify them individually when you launch instances. AWS PCS incorporates launch templates as a flexible way to configure compute node groups. When you create a node group, you provide a launch template. AWS PCS creates a derived launch template from it that includes transformations to help ensure it works with the service.

Understanding what the options and considerations are when writing a custom launch template can help you write one for use with AWS PCS. For more information on launch templates, see Launching an Instance from a [Launch an instance from a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.

**Topics**
+ [Overview of launch templates in AWS PCS](working-with_launch-templates_overview.md)
+ [Create a basic launch template](working-with_launch-templates_create.md)
+ [Working with Amazon EC2 user data for AWS PCS](working-with_ec2-user-data.md)
+ [Capacity Reservations in AWS PCS](working-with_capacity-reservations.md)
+ [Useful launch template parameters](working-with_launch-templates_parameters.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

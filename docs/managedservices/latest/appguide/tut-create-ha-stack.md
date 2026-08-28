---
source_url: https://docs.aws.amazon.com/managedservices/latest/appguide/tut-create-ha-stack.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# CLI Tutorial: High Availability Two-Tier Stack (Linux/RHEL)
<a name="tut-create-ha-stack"></a>

This section describes how to deploy a high availability (HA) two-tier stack into an AMS environment using the AMS CLI.

**Note**
This deployment walkthrough has been tested in AMZN Linux and RHEL environments.

Summary of tasks and required RFCs:

1. Create infrastructure (HA two-tier stack)

1. Create an S3 bucket for CodeDeploy applications

1. Create the WordPress application bundle and upload it to the S3 bucket

1. Deploy the application with CodeDeploy

1. Access the WordPress site and log in to validate the deployment

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

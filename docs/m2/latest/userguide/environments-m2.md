---
source_url: https://docs.aws.amazon.com/m2/latest/userguide/environments-m2.html
---

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

# Managed runtime environments in AWS Mainframe Modernization
<a name="environments-m2"></a>

If you're new to AWS Mainframe Modernization see the following topics to get started:
+ [What is AWS Mainframe Modernization?](what-is-m2.md)
+ [Set up for AWS Mainframe Modernization](setting-up.md)
+ [Get started with AWS Mainframe Modernization](getting-started.md)
+ [Tutorial: Set up managed runtime for AWS Transform for mainframe](tutorial-runtime-ba.md)
+ [Tutorial: Set up managed runtime for Rocket Software (formerly Micro Focus)](tutorial-runtime-mf.md)

A runtime environment in AWS Mainframe Modernization is a named combination of AWS compute resources, a runtime engine, and the configuration details that you specify. The runtime environment hosts one or more applications. Applications in AWS Mainframe Modernization contain migrated mainframe workloads. You can choose the runtime engine for the environments that you create. Choose AWS Transform for mainframe if you are using the automated refactoring pattern, and Rocket Software (formerly Micro Focus) if you are using the replatforming pattern. You can also choose the amount of compute resources that are right for your application and optionally attach storage to runtime environments. AWS Mainframe Modernization enables Amazon CloudWatch metrics and logging for you so that you can monitor your runtime environment.

**Topics**
+ [Create an AWS Mainframe Modernization runtime environment](create-environments-m2.md)
+ [Update an AWS Mainframe Modernization runtime environment](update-environments-m2.md)
+ [Stop an AWS Mainframe Modernization runtime environment](stop-environments-m2.md)
+ [Restart an AWS Mainframe Modernization runtime environment](restart-environments-m2.md)
+ [Delete an AWS Mainframe Modernization runtime environment](delete-environments-m2.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

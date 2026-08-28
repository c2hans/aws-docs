---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/AMI-minimal-and-standard-differences.html
---

# Comparing AL2023 standard and minimal AMIs
<a name="AMI-minimal-and-standard-differences"></a>

You can launch an Amazon EC2 instance with either a standard (default) or minimal AL2023 AMI. For instructions on how to launch an Amazon EC2 instance with the standard or minimal AMI type, see [AL2023 on Amazon EC2](ec2.md).

The standard AL2023 AMI comes with all of the most commonly used applications and tools installed. We recommend the standard AMI if you want to get started quickly and aren't interested in customizing the AMI.

The minimal AL2023 AMI is the basic, streamlined version that contains only the most basic tools and utilities necessary to run the operating system (OS). We recommend the minimal AMI if you want to have the smallest OS footprint possible. The minimal AMI offers slightly reduced disk space utilization and better long-term cost efficiency. The minimal AMI is suitable if you want a smaller OS and don't mind manually installing tools and applications.

The Container image is closer to the AL2023 minimal AMI in package set.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

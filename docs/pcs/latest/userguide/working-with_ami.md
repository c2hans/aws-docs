---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_ami.html
---

# Amazon Machine Images (AMIs) for AWS PCS
<a name="working-with_ami"></a>

AWS PCS works with AMIs that you provide, affording great flexibility in the software and configuration found on nodes in your cluster. For production AI/ML and HPC workloads, you can use the AWS-maintained PCS-ready DLAMI. If you are evaluating AWS PCS, you can use a sample AMI provided by AWS. You can also build your own customized AMIs for full control over the software and configuration on your nodes.

**Topics**
+ [Using PCS-ready DLAMI with AWS PCS](working-with_ami_pcs-ready-dlami.md)
+ [Using sample Amazon Machine Images (AMIs) with AWS PCS](working-with_ami_samples.md)
+ [Custom Amazon Machine Images (AMIs) for AWS PCS](working-with_ami_custom.md)
+ [Software installers to build custom AMIs for AWS PCS](working-with_ami_installers.md)
+ [Release notes for AWS PCS sample AMIs](ami-release-notes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

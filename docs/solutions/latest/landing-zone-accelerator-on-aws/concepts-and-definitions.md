---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to this solution.

 **AWSAccelerator** and **aws-accelerator**

As of version 1.4.0, this solution allows for a user-defined resource name prefix in the [Installer stack parameters](step-1.-launch-the-stack.md). This guide uses the default prefix values `AWSAccelerator` and `aws-accelerator` for the named resource it describes. If you input a custom prefix, your solution-deployed CloudFormation stacks and Amazon S3 buckets use your custom prefix value.

 **landing zone**

A cloud environment that offers a recommended starting point—​including default accounts, account structure, core networking infrastructure, and security configurations. Using a landing zone as a foundation, you can deploy your mission-critical application workloads and solutions across a centrally-governed multi-account environment.

 **Installer pipeline (`AWSAccelerator-Installer`)**

Deploys an installer that, in turn, deploys the solution’s core features. Because this installer functions separately from the Core pipeline, you can update to future versions of the solution with a single parameter through the AWS CloudFormation console.

 **Core pipeline (`AWSAccelerator-Pipeline`)**

Deploys the solution’s core features.

**Note**
For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

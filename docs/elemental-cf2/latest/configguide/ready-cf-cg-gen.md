---
source_url: https://docs.aws.amazon.com/elemental-cf2/latest/configguide/ready-cf-cg-gen.html
---

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# General Information
<a name="ready-cf-cg-gen"></a>

**CPU-only and GPU-enabled**
There are two processing architectures for AWS Elemental Server: CPU-only and GPU-enabled.

In an AWS Elemental Conductor File cluster, the Conductor File nodes and the AWS Elemental Server nodes must be either all running CPU-only versions of software, or all running GPU-enabled versions of software. So both Conductor File and all AWS Elemental Server nodes must all be running CPU-only software versions, or all be running GPU-enabled software.

**Redundancy and Non-Redundant Clusters**
The AWS Elemental Conductor File cluster can be set up in a redundant or non-redundant Conductor configuration.
+ A redundant configuration involves setting up two Conductor File nodes. Only one Conductor node controls the cluster at a time, but both are active and performing database replication.
+ In a non-redundant configuration, there is only one Conductor node.

This table summarizes the available cluster options for AWS Elemental Conductor File:

| Workers | Conductor |
| --- | --- |
| Non-redundant | Non-redundant (only one Conductor node) |
| Non-redundant | Redundant (two Conductor nodes) |

This guide describes how to set-up all of these configurations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor File. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cf2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

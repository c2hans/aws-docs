---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/post-deployment-plugin-points.html
---

# Post deployment: Plugin points
<a name="post-deployment-plugin-points"></a>

The Guidance is designed to be an orchestrator and therefore allows the following plugin points where you can replace existing tooling with your preferred tool of choice. The Guidance leverages [LiME](https://github.com/504ensicsLabs/LiME) for memory capture and [Volatility 3](https://github.com/volatilityfoundation/volatility3) for memory investigation.

1. A LiME module and volatility symbol table for the EC2 instance must be prebuilt and available for forensic memory investigation and investigation for the EC2 instances OS and kernel version. Refer to Plugin points to build the LiME module and volatility symbol table.

1. The prebuilt LiME module and volatility symbol table must be stored in the Guidance’s S3 bucket. The artifacts can be stored in the bucket created by the forensic Guidance in `cdk.json`. The prefix to the artifacts and the S3 bucket can be configured in `cdk.json` as context variable.

## Memory forensics analysis using LiME and Volatility 3
<a name="memory-forensics-analysis-using-lime-and-volatility3"></a>

As described in [Memory forensics acquisition workflow implementation](forensic-memory-and-disk-acquisition-service.md#memory-forensics-acquisition-workflow-implementation), memory forensics is implemented using Step Functions, which provides the orchestration mechanism and tuns the AWS Systems Manager automation documents. These automation documents can be partially or fully replaced. In the example below, we have bootstrapped our memory forensics implementation to acquire memory using [LiME](https://github.com/504ensicsLabs/LiME), and to use the * [Volatility 3](https://github.com/volatilityfoundation/volatility3) * profile. LiME is used to extract the volatile memory, which is then analyzed downstream by the Forensics investigation workflow.

When memory is investigated using Volatility 3 (and other tools) it is important for the tool to understand the structure of the memory. In Volatility 3, that is done using symbol tables which is comprised of two parts: a Debugging With Attribute Record Formats (DWARF) and a map (symbol table used by the kernel) file. The section below demonstrates how the process flow works and ensures that it can be extended by creating a new profile and dropping it into a configurable location (bucket).

**Note**
As every OS and kernel versions have slight variations, you must create LiME and Volatility artifacts specific to the EC2 instance or EKS cluster, and make these artifacts available to the orchestrator during run-time.

In the section below, we walk through how you can build the LiME module and Volatility profile using an SSM document.

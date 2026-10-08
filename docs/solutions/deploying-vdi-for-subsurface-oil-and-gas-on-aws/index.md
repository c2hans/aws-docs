---
source_url: https://docs.aws.amazon.com/solutions/deploying-vdi-for-subsurface-oil-and-gas-on-aws/index.html
---

---
title: 'Guidance for Deploying VDI for Subsurface Oil and Gas on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-vdi-for-subsurface-oil-and-gas-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Deploying VDI for Subsurface Oil and Gas on AWS

## Overview

This Guidance demonstrates how Energy companies can migrate subsurface geoscience and geophysics data from on-premises storage to AWS, enabling secure access to graphics-intensive applications through managed virtual desktop infrastructure. The solution addresses key challenges in enterprise VDI management by providing scalable cloud-based environments for seismic interpretation and reservoir modeling workloads. By leveraging high-performance pixel streaming and flexible storage options, organizations can enhance productivity for G&G workflows while reducing the operational burden of managing complex IT infrastructure. The architecture supports seamless integration with existing applications and workflows, allowing IT departments to efficiently provision and manage virtual workstations for distributed teams requiring remote access to computationally intensive geoscience applications.

## Benefits

### Accelerate geoscience workflows

Deploy high-performance virtual desktops optimized for graphics-intensive seismic interpretation and reservoir modeling. Enable your geoscientists to access specialized applications from anywhere while maintaining secure connections to centralized data storage.

### Reduce infrastructure costs

Choose from multiple enterprise storage solutions to match your performance and budget requirements. Migrate existing subsurface projects seamlessly while maintaining compatibility with your current license management and application environments.

### Scale virtual desktop capacity

Provision and manage virtual workstations centrally using integrated third-party management tools. Adjust computing resources to support project peaks without maintaining excess infrastructure or hardware investments.

## How it works

### VDI and data migration to Amazon FSX for NetApp ONTAP

This architecture diagram illustrates a secure migration and virtualization solution for geoscience and geophysics applications, moving subsurface data from on-premisesstorage to Amazon FSx for NetApp ONTAP via AWS DataSync, enabling users to access graphics-intensive applications through managed virtual desktop infrastructure.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploying-vdi-for-subsurface-oil-and-gas-on-aws.pdf)Step 1Subsurface projects, files, and documents reside in on premises shared file storage, accessible by all users.Step 2AWS DataSync (or NetApp Snap Mirror) moves files and data securely over AWS Direct Connect. Optionally, Interica OneView migrates on the project level of each Subsurface application.Step 3Amazon FSx for NetApp ONTAP hosts projects, files, and documents migrated from the on-premises file system.Step 4Users run graphics-intensive G&G applications on virtual workstations using Amazon DCV, a high-performance display protocol.

Step 5Partner Remote Desktop Management and Access software powered by Amazon WorkSpaces Core enables provisioning, deployment, and management of virtual desktop infrastructure (VDI).Step 6Amazon WorkSpaces Core provides managed VDI that integrates with third-party management solutions. It provide flexibility to run any Amazon Elastic Compute Cloud (Amazon EC2) instance.Step 7Applications access Amazon FSx for NetApp ONTAP file system using the SMB or NFS protocol, depending on the operating system of the VDI workstation.Step 8IT department prepares and provides Golden Image, which contains G&G applications that users need for work.

### AWS Partner Solution for Subsurface Data Storage

This architecture diagram illustrates a secure migration and virtualization solution for geoscience and geophysics applications, moving subsurface data from on-premisesstorage to AWS Partner storage solutions via AWS DataSync, enabling users to access graphics-intensive applications through managed virtual desktop infrastructure.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/deploying-vdi-for-subsurface-oil-and-gas-on-aws.pdf)Step 1Subsurface projects, files, and documents reside in on premises shared file storage, accessible by all users.Step 2AWS DataSync (or NetApp Snap Mirror) moves files and data securely over AWS Direct Connect. Optionally, Interica OneView migrates on the project level of each Subsurface application.Step 3AWS Partner Solutions such as WEKA Cluster, Nasuni Storage, and Qumulo CNQ host projects, files, and documents migrated from the on-premises file system.Step 4Users run graphics-intensive G&G applications on virtual workstations using Amazon DCV, a high-performance display protocol.

Step 5Partner Remote Desktop Management and Access software powered by Amazon WorkSpaces Core enables provisioning, deployment, and management of virtual desktop infrastructure (VDI).Step 6Amazon WorkSpaces Core provides managed VDI that integrates with third-party management solutions. It provide flexibility to run any Amazon Elastic Compute Cloud (Amazon EC2) instance.Step 7Applications access AWS Partner solutions using SMB or NFS protocol, depending on the operating system of the VDI workstation.Step 8IT department prepares and provides Golden Image, which contains G&G applications that users need for work.

## Related content

- **Energy Data Insights on AWS - OSDU® Data Platform**: This page describes Energy Data Insights on AWS (EDI), a fully managed cloud-based OSDU Data Platform for upstream energy data management.

[Learn more](https://aws.amazon.com/energy-utilities/osdu-data-platform/)

- **Halliburton Landmark improves user experience with Amazon AppStream 2.0**: This blog post demonstrates how Halliburton Landmark migrated to Amazon AppStream 2.0 to improve user experience for its Geosciences Suite.

[Learn more](https://aws.amazon.com/blogs/desktop-and-application-streaming/halliburton-landmark-improves-user-experience-with-amazon-appstream-2-0/)

[Read usage guidelines](/solutions/guidance-disclaimers/)

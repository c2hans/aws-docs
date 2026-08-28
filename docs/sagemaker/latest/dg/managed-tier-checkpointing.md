---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/managed-tier-checkpointing.html
---

# HyperPod managed tiered checkpointing
<a name="managed-tier-checkpointing"></a>

This section explains how managed tiered checkpointing works and the benefits it provides for large-scale model training.

Amazon SageMaker HyperPod managed tiered checkpointing helps you train large-scale generative AI models more efficiently. It uses multiple storage tiers, including your cluster’s CPU memory. This approach reduces your time to recovery and minimizes loss in training progress. It also uses underutilized memory resources in your training infrastructure.

Managed tiered checkpointing enables saving checkpoints at a higher frequency to memory. It periodically persists them to durable storage. This maintains both performance and reliability during your training process.

This guide covers how to set up, configure, and use managed tiered checkpointing with PyTorch frameworks on Amazon EKS HyperPod clusters.

## How managed tiered checkpointing works
<a name="managed-tier-checkpointing-works"></a>

Managed tiered checkpointing uses a multi-tier storage approach. CPU memory serves as the primary tier to store model checkpoints. Secondary tiers include persistent storage options like Amazon S3.

When you save a checkpoint, the system stores it in allocated memory space across your cluster nodes. It automatically replicates data across adjacent compute nodes for enhanced reliability. This replication strategy protects against single or multiple node failures while providing fast access for recovery operations.

The system also periodically saves checkpoints to persistent storage according to your configuration. This ensures long-term durability of your training progress.

Key components include:
+ **Memory management system**: A memory management daemon that provides disaggregated memory as a service for checkpoint storage
+ **HyperPod Python library**: Interfaces with the disaggregated storage APIs and provides utilities for saving, loading, and managing checkpoints across tiers
+ **Checkpoint replication**: Automatically replicates checkpoints across multiple nodes for fault tolerance

The system integrates seamlessly with PyTorch training loops through simple API calls. It requires minimal changes to your existing code.

## Benefits
<a name="managed-tier-checkpointing-benefits"></a>

Managed tiered checkpointing delivers several advantages for large-scale model training:
+ **Improved usability**: Manages checkpoint save, replication, persistence, and recovery
+ **Faster checkpoint operations**: Memory-based storage provides faster save and load times compared to disk-based checkpointing, leading to faster recovery
+ **Fault tolerance**: Automatic checkpoint replication across nodes protects against hardware node failures
+ **Minimal code changes**: Simple API integration requires only minor modifications to existing training scripts
+ **Improved training throughput**: Reduced checkpoint overhead means more time spent on actual training

**Topics**
+ [How managed tiered checkpointing works](#managed-tier-checkpointing-works)
+ [Benefits](#managed-tier-checkpointing-benefits)
+ [Set up managed tiered checkpointing](managed-tier-checkpointing-setup.md)
+ [Removing managed tiered checkpointing](managed-tier-checkpointing-remove.md)
+ [Security considerations for managed tiered checkpointing](managed-tier-security-considerations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

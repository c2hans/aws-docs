---
source_url: https://docs.aws.amazon.com/solutions/streaming-audio-quality-monitoring-with-tag-vs-on-aws/index.html
---

---
title: 'Guidance for Streaming Audio Quality Monitoring with TAG-VS on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/streaming-audio-quality-monitoring-with-tag-vs-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Streaming Audio Quality Monitoring with TAG-VS on AWS

## Overview

This Guidance demonstrates how to implement a comprehensive near real-time audio quality monitoring system using AWS infrastructure and TAG partner solutions. It helps broadcasters maintain high-quality audio delivery by providing unified visibility across multiple broadcast channels through a single dashboard interface. The solution shows how to proactively detect and prevent audio quality issues like double audio and phase problems before they impact listener experience, while ensuring compliance with professional broadcast standards. Furthermore, it demonstrates how to optimize operational efficiency and infrastructure costs through Transit Gateway networking, while enabling rapid issue identification and resolution through detailed quality metrics and monitoring capabilities.

## Benefits

### Ensure broadcast-quality audio delivery

Monitor professional audio streams in real-time with multi-AZ redundancy for continuous operations. Detect quality issues instantly to maintain audience experience and regulatory compliance.

### Reduce operational monitoring costs

Consolidate multiple audio channels into unified dashboards with automated alerting and historical analytics. Replace expensive hardware monitoring solutions with scalable cloud infrastructure.

### Accelerate incident response time

Visualize audio metrics and anomalies through integrated dashboards for immediate issue identification. Enable remote monitoring teams to troubleshoot problems before they impact viewers.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/streaming-audio-quality-monitoring-with-tag-vs-on-aws.pdf)

![Architecture diagram](/images/solutions/streaming-audio-quality-monitoring-with-tag-vs-on-aws/images/streaming-audio-quality-monitoring-with-tag-vs-on-aws-1.png)

1. **Step 1**: Use AWS Elemental MediaConnect Gateway to transport AES67 source audio streams using SMPTE2110-22 transport to the AWS Cloud.
1. **Step 2**: Contribute the multicast streams from the gateway instances across primary and secondary AWS Elemental MediaConnect Flows. Connect outputs from each Flow into TAG's Multi Channel Monitor (MCM) running on Amazon Elastic Compute Cloud (Amazon EC2) instances.
1. **Step 3**: The TAG Media Control System (MCS) serves as the orchestration layer, coordinating multiple MCM instances while providing enterprise-grade integration capabilities.
1. **Step 4**: From TAG MCS instances, send playout and monitoring metrics, as well as logs and other metadata to an Amazon OpenSearch Service.
1. **Step 5**: Visualize the metadata and the audio output streams through an Amazon OpenSearch Service dashboard along with historical metrics for studio operators and monitoring professionals.
1. **Step 6**: Deliver a multi-viewer output, combining multiple channels into one live view, from the MCM to operators via an AWS Elemental MediaConnect Flow using SRT to minimize latency.
1. **Step 7**: Distribute the monitored content through AWS Elemental MediaConnect Flow Outputs to downstream consumers.
## Related content

- **Introducing: Guidance for audio quality control with TAG Video Systems and AWS**: This blog post demonstrates how to implement automated audio quality control using TAG Video Systems and AWS services to detect and monitor audio-related issues in broadcast media workflows.

[Learn more](https://aws.amazon.com/blogs/media/introducing-guidance-for-audio-quality-control-with-tag-video-system-and-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)

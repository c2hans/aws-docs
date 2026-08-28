---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-mysql-on-ec2-using-amazon-ebs/terminology.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Terminology
<a name="terminology"></a>

 The following definitions are for the common terms that will be referenced throughout this paper:
+  **IOPS** — Input/output (I/O) operations per second (Ops/s).
+  **Throughput** — Read/write transfer rate to storage (MB/s).
+  **Latency** — Delay between sending an I/O request and receiving an acknowledgment (ms).
+  **Block size** — Size of each I/O (KB).
+  **Page size** — Internal basic structure to organize the data in the database files (KB).
+  **[Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) volume** — Persistent block-level storage devices for use with [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instances. This whitepaper focuses on solid state drive (SSD) EBS volume types optimized for transactional workloads involving frequent read/write operations with small I/O size, where the dominant performance attribute is IOPS.
+  **Amazon EBS General Purpose SSD volume** — General Purpose SSD volume that provides a balance of price and performance. AWS recommends these volumes for most workloads. Currently, AWS offer two types of General Purpose SSD volumes: gp2 and gp3.
+  **Amazon EBS Provisioned IOPS SSD volume** — Highest performance SSD volume designed for high performance for mission-critical, low-latency, or high-throughput workloads. Currently AWS offer two types of Provisioned IOPS SSD volumes: io1 and io2.
+  **Amazon EBS Throughput Optimized hard disk drive (HDD) (st1) volume** — Low- cost HDD volume designed for frequently accessed, throughput-intensive workloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

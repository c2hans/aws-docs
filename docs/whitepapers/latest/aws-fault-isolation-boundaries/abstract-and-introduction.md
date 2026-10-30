---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html
---

# AWS Fault Isolation Boundaries
<a name="abstract-and-introduction"></a>

Publication date: **October 29, 2026** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Amazon Web Services (AWS) provides multiple isolation boundaries including Availability Zones (AZ), AWS Regions, control planes, and data planes. This paper explains how AWS uses these boundaries to create zonal, Regional, and global services. It also provides prescriptive guidance for managing AWS service dependencies to improve application resilience.

## Introduction
<a name="introduction"></a>

 AWS designs and operates its global infrastructure and cloud services using multiple fault isolation boundaries that contain the scope of impact when failures occur. Because these boundaries give you a predictable scope of impact, you can use them to achieve consistent, bounded recovery times during service disruptions. This paper explains the fault isolation boundaries AWS provides, how our services are built using them, and how to design your applications to depend on AWS services reliably while avoiding single points of failure.

By the end of this paper, you’ll understand:
+ How AWS infrastructure boundaries (Availability Zones, AWS Regions, and partitions) limit the scope of impact when failures occur
+ The difference between control planes and data planes, and why it matters for resilience
+ How to design statically stable applications that recover predictably, without depending on control planes during recovery
+ Best practices for using zonal, Regional, and global AWS services

 With this foundation, you can make informed, intentional choices about your AWS dependencies and design applications that recover predictably.

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/appstream-well-architected-framework/sustainability.html
---

# Sustainability pillar
<a name="sustainability"></a>

The [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/sustainability.html) of the AWS Well-Architected Framework emphasizes minimizing your environmental footprint and optimizing energy usage and efficiency. It guides architects to make environmentally conscious decisions in their system designs and resource allocation strategies.

Key focus areas for applying this pillar to your WorkSpaces Applications streaming environment:
+ Understanding and optimizing resource allocation to match actual demand and minimize waste in streaming environments
+ Analyzing and adapting to user consumption patterns to improve efficiency of application delivery and streaming sessions
+ Selecting and using appropriate hardware configurations to maximize energy efficiency while meeting performance requirements
+ Using AWS managed service capabilities to benefit from the economies of scale and built-in efficiency features offered by these services

## Understand your impact
<a name="sustainability-impact"></a>

Monitor and optimize your workload's environmental impact by measuring resource efficiency and emissions per unit of output. Use this data to establish KPIs and guide sustainability improvements.
+ Monitor fleet utilization patterns.
+ Track streaming hours per user.
+ Analyze fleet capacity usage trends.

## Establish sustainability goals
<a name="sustainability-goals"></a>

Set measurable sustainability goals for each workload that align with organizational objectives. Focus on reducing resource intensity per transaction as you scale.
+ Set targets for fleet utilization rates, instance type efficiency, and streaming hours optimization.
+ Plan capacity based on actual usage patterns.

## Maximize utilization
<a name="sustainability-utilization"></a>

Optimize workload efficiency by right-sizing resources and maximizing utilization. Reduce idle capacity to minimize energy consumption and improve sustainability.
+ Configure automatic scaling to match actual demand.
+ Right-size fleet capacity based on usage patterns.
+ Implement appropriate minimum and maximum capacity limits.
+ Choose appropriate instance types for workloads.
+ Monitor and optimize streaming session density.
+ Reduce idle capacity during off-peak hours.

## Anticipate and adopt new, more efficient hardware and software offerings
<a name="sustainability-hw-sw"></a>

Stay informed about, and quickly adopt, new efficient technologies from partners and suppliers to continuously improve your workload's environmental impact.
+ Use current generation instance types.
+ Upgrade to newer instance types when available.
+ Optimize application streaming settings.
+ Configure appropriate streaming protocols.
+ Update to the latest WorkSpaces Applications features.

## Used managed services
<a name="sustainability-services"></a>

Take advantage of shared cloud services and managed solutions to maximize resource utilization efficiency while minimizing environmental impact through automated scaling and lifecycle management.
+ Use [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) for user storage for Windows-based fleets and [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) for shared file systems for Linux-based fleets.
+ Implement [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for monitoring.
+ Configure [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) for access management.

## Reduce the downstream impact of your cloud workloads
<a name="sustainability-downstream-impact"></a>

Design services to minimize client-side resource requirements, to reduce energy consumption and extend device lifespans for users.
+ Adjust maximum session duration to prevent unnecessary resource consumption.
+ Configure appropriate session timeouts.
+ Set disconnect timeout policies.
+ Implement session persistence policies where needed.

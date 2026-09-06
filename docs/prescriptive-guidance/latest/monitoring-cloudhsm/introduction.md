---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/monitoring-cloudhsm/introduction.html
---

# Monitoring AWS CloudHSM by using metrics, audit logs, and alarms
<a name="introduction"></a>

*Shubhansu Sawaria, Amazon Web Services*

This guide outlines observability and monitoring tools and best practices for managing an [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) cluster. To monitor an AWS CloudHSM cluster, you measure, track, and assess its availability, performance, security, and functionality.

On AWS, you can analyze workload logs, metrics, events, and traces to understand workload health. This helps you gain operational insights over time. Monitoring helps make sure that resources perform as expected so that you can detect and proactively address issues. Use monitored metrics, logs, and events to set alarms when thresholds are exceeded.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for solutions architects, senior DevOps engineers, and team members who design, implement, or manage monitoring and observability solutions for AWS CloudHSM workloads.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

By implementing monitoring and alerting best practices, you can help achieve a high-performing, resilient, efficient, secure, and cost-optimized infrastructure for your applications and workloads. These best practices enable near real-time observation and analysis of the overall health and performance of your AWS CloudHSM cluster.

Monitoring and alerting helps you prevent degradation or disruption of associated IT services. In the event of unplanned degradation or service disruption, monitoring and alerting tools can facilitate timely detection, escalation, reaction, investigation, and resolution.

A robust monitoring and alerting solution contributes to the following key business outcomes:
+ Enhancing customer experience
+ Building customer trust
+ Mitigating financial losses associated with unplanned service disruptions
+ Increasing developer productivity by helping them identify and resolve issues more quickly
+ Enhancing operational effectiveness and efficiency by increasing availability

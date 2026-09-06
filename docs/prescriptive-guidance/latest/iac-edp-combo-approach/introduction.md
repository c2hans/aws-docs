---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iac-edp-combo-approach/introduction.html
---

# Synchronizing infrastructure as code (IaC) with event-driven programming (EDP)
<a name="introduction"></a>

*Ram Kandaswamy, Amazon Web Services*

The [infrastructure as code (IaC)](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) practice and [event-driven programming (EDP)](https://aws.amazon.com/what-is/eda/) practice (based on an event-driven architecture) are two different approaches to DevOps. Organizations often use some combination of each approach, but this can lead to unintentional consequences that are counterproductive and even harmful to the organization. This guide provides recommendations, best practices, and guidelines for combining IaC practices with EDP practices in the AWS Cloud in a way that's compatible, secure, and mutually beneficial for both IaC and EDP implementations.

You can use an IaC approach to provision and manage IT infrastructure resources by using code and creating configuration files (typically JSON or YAML files) that define your infrastructure specifications. An IaC approach is usually combined with a version control system such as Git to manage the configuration files. EDP is an approach where you develop code to run in response to events that you define. Typically, the code modifies a resource or its properties.

This guide is intended for technical roles that have a basic understanding of general DevOps principles, EDP architectures, and AWS Cloud services.

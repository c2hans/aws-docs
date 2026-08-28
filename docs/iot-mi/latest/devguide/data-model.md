---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/data-model.html
---

# Data models
<a name="data-model"></a>

A data model represents the organizational hierarchy of how data is organized within a system. Additionally, it supports end-to-end communication across your entire device implementation. For Managed Integrations, there are two data models used. The Managed Integrations data model and the AWS implementation of the Matter Data Model. They have similarities, but also have subtle differences that are outlined in the following topics.

For third-party devices, both data models are used for communication between the end user, Managed Integrations, and the third-party cloud provider. To translate messages such as device commands and device events from the two data models, the Cloud-to-Cloud Connector functionality is leveraged.

**Topics**
+ [Managed Integrations data model](managedintegrations-data-model.md)
+ [AWS implementation of the Matter data model](matter-data-model.md)
+ [Data model schemas](data-model-schemas.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

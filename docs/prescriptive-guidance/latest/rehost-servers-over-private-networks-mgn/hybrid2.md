---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/hybrid2.html
---

# Public HTTPS egress at the source and public staging area resources
<a name="hybrid2"></a>

In cases where staging area resources aren't required to be on a fully isolated subnet, you can use the hybrid alternative that's shown in the following diagram.

![Application Migration Service communications with public HTTPS and data replication over public channel](http://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/images/guide-img/db816b63-918e-424c-861e-0630fc54fedf/images/e9c699cc-909b-408c-a5fb-612a11cfd745.png)

In this scenario, only data replication traffic on TCP port 1500 goes over the private channel. The rest of the communication, both from the source subnet and the staging subnet, happen over the public network, to standard public HTTPS endpoints.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

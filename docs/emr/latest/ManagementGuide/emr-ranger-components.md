---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger-components.html
---

# Amazon EMR components for use with Apache Ranger
<a name="emr-ranger-components"></a>

Amazon EMR enables fine-grained access control with Apache Ranger through the following components. See the [architecture diagram](emr-ranger-architecture.md) for a visual representation of these Amazon EMR components with the Apache Ranger plugins.

**Secret agent** – The secret agent securely stores secrets and distributes secrets to other Amazon EMR components or applications. The secrets can include temporary user credentials, encryption keys, or Kerberos tickets. The secret agent runs on every node in the cluster and intercepts calls to the Instance Metadata Service. For requests to the instance profile role credentials, the Secret Agent vends credentials depending on the requesting user and requested resources after authorizing the request with the EMRFS S3 Ranger plugin. The secret agent runs as the *`emrsecretagent`* user, and it writes logs to the /emr/secretagent/log directory. The process relies on a specific set of `iptables` rules to function. It is important to ensure that `iptables` is not disabled. If you customize `iptables` configuration, the NAT table rules must be preserved and left unaltered.

**EMR record server** – The record server receives requests to access data from Spark. It then authorizes requests by forwarding the requested resources to the Spark Ranger plugin for Amazon EMR. The record server reads data from Amazon S3 and returns filtered data that the user is authorized to access based on Ranger policy. The record server runs on every node in the cluster as the emr\_record\_server user and writes logs to the /var/log/emr-record-server directory.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

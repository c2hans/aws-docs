---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/ldap-components.html
---

# LDAP components for Amazon EMR
<a name="ldap-components"></a>

You can use your LDAP server to authenticate with Amazon EMR and any applications that the user directly utilizes on the EMR cluster through the following components.

**Secret Agent**
The *Secret Agent* is an on-cluster process that authenticates all user requests. The Secret Agent creates the user bind to your LDAP server on behalf of the supported applications on the EMR cluster. The Secret Agent runs as the `emrsecretagent` user, and it writes logs to the `/emr/secretagent/log` directory. These logs provide details about the state of each user's authentication request and any errors that might surface during user authentication.

**System Security Services Daemon (SSSD)**
*SSSD* is a daemon that runs on each node of an LDAP-enabled EMR cluster. SSSD creates and manages a UNIX user to sync your remote corporate identity to each node. YARN-based applications such as Hive and Spark require that a local UNIX user exists on every node that runs a query for a user.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

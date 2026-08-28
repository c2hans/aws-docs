---
source_url: https://docs.aws.amazon.com/elemental-live/latest/configguide/auth-ref-type-auth.html
---

# Supported types of user authentication
<a name="auth-ref-type-auth"></a>

AWS Elemental Live supports the following types of user authentication:

**Local authentication**
An administrator creates and manages user credentials from the Elemental Live node.
Users logging in to nodes with local authentication enabled must enter valid credentials for access. They must also supply credentials when using the REST API.
The credentials that users enter are validated against credentials that are housed locally on the node that they're accessing.

**Privileged Access Management (PAM) authentication**
An administrator creates and manages user credentials from a Lightweight Directory Access Protocol (LDAP) server that's external from the AWS Elemental systems.
Users logging in to nodes with PAM authentication enabled must enter valid credentials for access. They must also supply credentials when using the REST API.
The credentials that users enter are validated against credentials that are housed on an external LDAP server.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

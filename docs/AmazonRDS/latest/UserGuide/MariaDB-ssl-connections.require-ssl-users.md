---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB-ssl-connections.require-ssl-users.html
---

# Requiring SSL/TLS for specific user accounts to a MariaDB DB instance on Amazon RDS
<a name="MariaDB-ssl-connections.require-ssl-users"></a>

You can require SSL/TLS encryption for specified user account connections to your MariaDB DB instances on Amazon RDS. Protecting sensitive information from unauthorized access or interception is crucial to enforce security policies where data confidentiality is a concern.

To require SSL/TLS connections for specific users' accounts, use one of the following statements, depending on your MySQL version, to require SSL/TLS connections on the user account `encrypted_user`.

To do so, use the following statement.

```
ALTER USER 'encrypted_user'@'%' REQUIRE SSL;
```

For more information on SSL/TLS connections with MariaDB, see [ Securing Connections for Client and Server](https://mariadb.com/kb/en/securing-connections-for-client-and-server/) in the MariaDB documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

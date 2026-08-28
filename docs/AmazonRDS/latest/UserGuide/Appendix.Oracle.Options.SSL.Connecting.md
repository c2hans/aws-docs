---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.Connecting.html
---

# Connecting to an RDS for Oracle DB instance using SSL
<a name="Appendix.Oracle.Options.SSL.Connecting"></a>

After you configure SQL\*Plus to use SSL as described previously, you can connect to the RDS for Oracle DB instance with the SSL option. Optionally, you can first export the `TNS_ADMIN` value that points to the directory that contains the tnsnames.ora and sqlnet.ora files. Doing so ensures that SQL\*Plus can find these files consistently. The following example exports the `TNS_ADMIN` value.

```
export TNS_ADMIN=${ORACLE_HOME}/network/admin
```

Connect to the DB instance. For example, you can connect using SQL\*Plus and a {{<net\_service\_name>}} in a tnsnames.ora file.

```
sqlplus {{mydbuser}}@{{net_service_name}}
```

You can also connect to the DB instance using SQL\*Plus without using a tnsnames.ora file by using the following command.

```
sqlplus '{{mydbuser}}@(DESCRIPTION = (ADDRESS = (PROTOCOL = TCPS)(HOST = {{endpoint}}) (PORT = {{ssl_port_number}}))(CONNECT_DATA = (SID = {{database_name}})))'
```

You can also connect to the RDS for Oracle DB instance without using SSL. For example, the following command connects to the DB instance through the clear text port without SSL encryption.

```
sqlplus '{{mydbuser}}@(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = {{endpoint}}) (PORT = {{port_number}}))(CONNECT_DATA = (SID = {{database_name}})))'
```

If you want to close Transmission Control Protocol (TCP) port access, create a security group with no IP address ingresses and add it to the instance. This addition closes connections over the TCP port, while still allowing connections over the SSL port that are specified from IP addresses within the range permitted by the SSL option security group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

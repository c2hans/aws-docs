---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.DML-support.html
---

# Supported and unsupported Data Manipulation Language (DML) and query processing SQL commands
<a name="limitless-reference.DML-support"></a>

The following table lists the DML commands that are supported and not supported by Aurora PostgreSQL Limitless Database, with references to limitations or more information.

| Command | Supported? | Limitations or more information |
| --- | --- | --- |
| ABORT | Yes | None |
| ANALYZE | Yes | [ANALYZE](limitless-reference.DML-limitations.md#limitless-reference.DML-limitations.ANALYZE) |
| BEGIN | Yes | None |
| CALL | Yes | None |
| CHECKPOINT | Yes | None |
| CLOSE | Yes | None |
| CLUSTER | Yes | [CLUSTER](limitless-reference.DML-limitations.md#limitless-reference.DML-limitations.CLUSTER) |
| COMMIT | Yes | None |
| COMMIT PREPARED | No | Not applicable |
| COPY | Yes | None |
| DEALLOCATE | Yes | None |
| DECLARE | Yes | None |
| DELETE | Yes | None |
| DISCARD | Yes | None |
| DO | Yes | None |
| END | Yes | None |
| EXECUTE | Yes | None |
| EXPLAIN | Yes | [EXPLAIN](limitless-reference.DML-limitations.md#limitless-reference.DML-limitations.EXPLAIN) |
| FETCH | Yes | None |
| IMPORT FOREIGN SCHEMA | No | Not applicable |
| INSERT | Yes | [INSERT](limitless-reference.DML-limitations.md#limitless-reference.DML-limitations.INSERT) |
| LISTEN | No | Not applicable |
| LOCK | Yes | None |
| MERGE | No | Not applicable |
| MOVE | Yes | None |
| NOTIFY | No | Not applicable |
| OPEN | Yes | None |
| PREPARE | Yes | None |
| PREPARE TRANSACTION | No | Not applicable |
| REFRESH MATERIALIZED VIEW | No | Not applicable |
| REINDEX | No | Not applicable |
| RELEASE SAVEPOINT | Yes | None |
| ROLLBACK | Yes | None |
| ROLLBACK PREPARED | No | Not applicable |
| ROLLBACK TO SAVEPOINT | Yes | None |
| SAVEPOINT | Yes | None |
| SELECT | Yes | None |
| SELECT INTO | Yes | None |
| SHOW | Yes | None |
| START TRANSACTION | Yes | None |
| UNLISTEN | No | None |
| UPDATE | Yes | [UPDATE](limitless-reference.DML-limitations.md#limitless-reference.DML-limitations.UPDATE) |
| UPDATE … WHERE CURRENT OF | No | Not applicable |
| VACUUM | Yes | [VACUUM](limitless-reference.DML-limitations.md#limitless-reference.DML-limitations.VACUUM) |
| VALUES | Yes | None |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

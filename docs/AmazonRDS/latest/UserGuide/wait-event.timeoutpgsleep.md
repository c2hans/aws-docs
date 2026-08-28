---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.timeoutpgsleep.html
---

# Timeout:PgSleep
<a name="wait-event.timeoutpgsleep"></a>

The `Timeout:PgSleep` event occurs when a server process has called the `pg_sleep` function and is waiting for the sleep timeout to expire.

**Topics**
+ [Supported engine versions](#wait-event.timeoutpgsleep.context.supported)
+ [Likely causes of increased waits](#wait-event.timeoutpgsleep.causes)
+ [Actions](#wait-event.timeoutpgsleep.actions)

## Supported engine versions
<a name="wait-event.timeoutpgsleep.context.supported"></a>

This wait event information is supported for all versions of RDS for PostgreSQL.

## Likely causes of increased waits
<a name="wait-event.timeoutpgsleep.causes"></a>

This wait event occurs when an application, stored function, or user issues a SQL statement that calls one of the following functions:
+ `pg_sleep`
+ `pg_sleep_for`
+ `pg_sleep_until`

The preceding functions delay execution until the specified number of seconds have elapsed. For example, `SELECT pg_sleep(1)` pauses for 1 second. For more information, see [Delaying Execution](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-DELAY) in the PostgreSQL documentation.

## Actions
<a name="wait-event.timeoutpgsleep.actions"></a>

Identify the statement that was running the `pg_sleep` function. Determine if the use of the function is appropriate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/managing-sessions-lifecycle-stop.html
---

# Stopping Amazon DCV sessions
<a name="managing-sessions-lifecycle-stop"></a>

A console session can only be stopped by the administrator on Windows Amazon DCV servers, and the root user on Linux and macOS Amazon DCV servers. A virtual session on a Linux Amazon DCV server can only be stopped by the root user or the Amazon DCV user who created it.

**Note**
Stopping a session closes all of the applications that are running in the session.

To stop a console or virtual session on a Windows, Linux, or macOS Amazon DCV server, use the `dcv close-session` command and specify the unique session ID.

**Topics**
+ [Syntax](#managing-sessions-lifecycle-stop-syntax)
+ [Example](#example)

## Syntax
<a name="managing-sessions-lifecycle-stop-syntax"></a>

```
dcv close-session {{session-id}}
```

## Example
<a name="example"></a>

For example, the following command stops a session with the unique ID of `my-session`.

```
dcv close-session {{my-session}}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

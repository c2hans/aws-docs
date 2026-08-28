---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/built-in-slot-number.html
---

# AMAZON.Number
<a name="built-in-slot-number"></a>

Converts words or numbers that express a number into digits, including decimal numbers. The following table shows how the `AMAZON.Number` slot type captures numeric words.

| Input | Response |
| --- | --- |
| one hundred twenty three point four five | 123.45 |
| one hundred twenty three dot four five | 123.45 |
| point four two | 0.42 |
| point forty two | 0.42 |
| 232.998 | 232.998 |
| 50 | 50 |
| -15 | -15 |
| minus 15 | -15 |
| minus fifteen point two four five | -15.245 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

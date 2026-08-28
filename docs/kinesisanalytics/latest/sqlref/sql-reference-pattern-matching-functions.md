---
source_url: https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-pattern-matching-functions.html
---

# Log Parsing Functions
<a name="sql-reference-pattern-matching-functions"></a>

Amazon Kinesis Data Analytics features the following functions for log parsing:
+ [FAST\_REGEX\_LOG\_PARSER](sql-reference-fast-regex-log-parser.md) works similarly to the regex parser, but takes several "shortcuts" to ensure faster results. For example, the fast regex parser stops at the first match it finds (known as "lazy" semantics.)
+ [FIXED\_COLUMN\_LOG\_PARSE](sql-reference-fixed-column-log-parse.md) parses fixed-width fields and automatically converts them to the given SQL types.
+ [REGEX\_LOG\_PARSE](sql-reference-regex-log-parse.md) uses the default Java regular expression parser. For more information about this parser, see [Pattern](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) in the Java Platform documentation on the Oracle website.
+ [SYS\_LOG\_PARSE](sql-reference-sys-log-parse.md) processes entries commonly found in UNIX/Linux system logs.
+ [VARIABLE\_COLUMN\_LOG\_PARSE](sql-reference-variable-column-log-parse.md) splits an input string (its first argument, <character-expression>) into fields separated by a delimiter character or delimiter string.
+ [W3C\_LOG\_PARSE](sql-reference-w3c-log-parse.md) processes entries in W3C-predefined-format logs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Kinesis Data Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesisanalytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

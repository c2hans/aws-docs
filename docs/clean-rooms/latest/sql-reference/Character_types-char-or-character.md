---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Character_types-char-or-character.html
---

# CHAR or CHARACTER
<a name="Character_types-char-or-character"></a>

Use a CHAR or CHARACTER column to store fixed-length strings. These strings are padded with blanks, so a CHAR(10) column always occupies 10 bytes of storage.

```
char(10)
```

 A CHAR column without a length specification results in a CHAR(1) column.

CHAR and VARCHAR data types are defined in terms of bytes, not characters. A CHAR column can only contain single-byte characters, so a CHAR(10) column can contain a string with a maximum length of 10 bytes.

| Name  | Storage  | Range (width of column)  |
| --- | --- | --- |
| CHAR or CHARACTER | Length of string, including trailing blanks (if any)  | 4096 bytes |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

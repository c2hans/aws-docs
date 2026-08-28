---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Character_types-varchar-or-character-varying.html
---

# VARCHAR or CHARACTER VARYING
<a name="Character_types-varchar-or-character-varying"></a>

Use a VARCHAR or CHARACTER VARYING column to store variable-length strings with a fixed limit. These strings are not padded with blanks, so a VARCHAR(120) column consists of a maximum of 120 single-byte characters, 60 two-byte characters, 40 three-byte characters, or 30 four-byte characters.

```
varchar(120)
```

VARCHAR data types are defined in terms of bytes, not characters. A VARCHAR can contain multibyte characters, up to a maximum of four bytes per character. For example, a VARCHAR(12) column can contain 12 single-byte characters, 6 two-byte characters, 4 three-byte characters, or 3 four-byte characters.

| Name  | Storage  | Range (width of column)  |
| --- | --- | --- |
| VARCHAR or CHARACTER VARYING  | 4 bytes \+ total bytes for characters, where each character can be 1 to 4 bytes.  | 65535 bytes (64K -1)  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

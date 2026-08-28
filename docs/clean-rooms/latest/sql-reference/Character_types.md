---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/Character_types.html
---

# Character types
<a name="Character_types"></a>

Character data types include CHAR (character) and VARCHAR (character varying).

**Topics**
+ [CHAR or CHARACTER](Character_types-char-or-character.md)
+ [VARCHAR or CHARACTER VARYING](Character_types-varchar-or-character-varying.md)
+ [Significance of trailing blanks](#Character_types-significance-of-trailing-blanks)

## Significance of trailing blanks
<a name="Character_types-significance-of-trailing-blanks"></a>

Both CHAR and VARCHAR data types store strings up to *n* bytes in length. An attempt to store a longer string into a column of these types results in an error. However, if the extra characters are all spaces (blanks), the string is truncated to the maximum length. If the string is shorter than the maximum length, CHAR values are padded with blanks, but VARCHAR values store the string without blanks.

Trailing blanks in CHAR values are always semantically insignificant. They are disregarded when you compare two CHAR values, not included in LENGTH calculations, and removed when you convert a CHAR value to another string type.

Trailing spaces in VARCHAR and CHAR values are treated as semantically insignificant when values are compared.

Length calculations return the length of VARCHAR character strings with trailing spaces included in the length. Trailing blanks are not counted in the length for fixed-length character strings.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

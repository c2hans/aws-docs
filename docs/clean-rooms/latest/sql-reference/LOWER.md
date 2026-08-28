---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/LOWER.html
---

# LOWER function
<a name="LOWER"></a>

Converts a string to lowercase. LOWER supports UTF-8 multibyte characters, up to a maximum of four bytes per character.

## Syntax
<a name="LOWER-synopsis"></a>

```
LOWER(string)
```

## Argument
<a name="LOWER-argument"></a>

 *string*
The input parameter is a VARCHAR string (or any other data type, such as CHAR, that can be implicitly converted to VARCHAR).

## Return type
<a name="LOWER-return-type"></a>

The LOWER function returns a character string that is the same data type as the input string.

## Examples
<a name="LOWER-examples"></a>

The following example converts the CATNAME field to lowercase:

```
select catname, lower(catname) from category order by 1,2;

 catname  |   lower
----------+-----------
Classical | classical
Jazz      | jazz
MLB       | mlb
MLS       | mls
Musicals  | musicals
NBA       | nba
NFL       | nfl
NHL       | nhl
Opera     | opera
Plays     | plays
Pop       | pop
(11 rows)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

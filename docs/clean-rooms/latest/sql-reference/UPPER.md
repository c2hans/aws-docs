---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/UPPER.html
---

# UPPER function
<a name="UPPER"></a>

Converts a string to uppercase. UPPER supports UTF-8 multibyte characters, up to a maximum of four bytes per character.

## Syntax
<a name="UPPER-synopsis"></a>

```
UPPER(string)
```

## Arguments
<a name="UPPER-arguments"></a>

 *string*
The input parameter is a VARCHAR string (or any other data type, such as CHAR, that can be implicitly converted to VARCHAR).

## Return type
<a name="UPPER-return-type"></a>

The UPPER function returns a character string that is the same data type as the input string.

## Examples
<a name="UPPER-examples"></a>

The following example converts the CATNAME field to uppercase:

```
select catname, upper(catname) from category order by 1,2;

 catname  |   upper
----------+-----------
Classical | CLASSICAL
Jazz      | JAZZ
MLB       | MLB
MLS       | MLS
Musicals  | MUSICALS
NBA       | NBA
NFL       | NFL
NHL       | NHL
Opera     | OPERA
Plays     | PLAYS
Pop       | POP
(11 rows)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

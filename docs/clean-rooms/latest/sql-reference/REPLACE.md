---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/REPLACE.html
---

# REPLACE function
<a name="REPLACE"></a>

Replaces all occurrences of a set of characters within an existing string with other specified characters.

REPLACE is similar to the [TRANSLATE function](TRANSLATE.md) and the [REGEXP\_REPLACE function](REGEXP_REPLACE.md), except that TRANSLATE makes multiple single-character substitutions and REGEXP\_REPLACE lets you search a string for a regular expression pattern, while REPLACE substitutes one entire string with another string.

## Syntax
<a name="REPLACE-synopsis"></a>

```
REPLACE(string1, old_chars, new_chars)
```

## Arguments
<a name="REPLACE-arguments"></a>

 *string*
CHAR or VARCHAR string to be searched search

 *old\_chars*
CHAR or VARCHAR string to replace.

 *new\_chars*
New CHAR or VARCHAR string replacing the *old\_string*.

## Return type
<a name="REPLACE-return-type"></a>

VARCHAR

If either *old\_chars* or *new\_chars* is NULL, the return is NULL.

## Examples
<a name="REPLACE-examples"></a>

The following example converts the string `Shows` to `Theatre` in the CATGROUP field:

```
select catid, catgroup,
replace(catgroup, 'Shows', 'Theatre')
from category
order by 1,2,3;

 catid | catgroup | replace
-------+----------+----------
     1 | Sports   | Sports
     2 | Sports   | Sports
     3 | Sports   | Sports
     4 | Sports   | Sports
     5 | Sports   | Sports
     6 | Shows    | Theatre
     7 | Shows    | Theatre
     8 | Shows    | Theatre
     9 | Concerts | Concerts
    10 | Concerts | Concerts
    11 | Concerts | Concerts
(11 rows)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

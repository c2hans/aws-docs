---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/s_SHA1.html
---

# SHA1 function
<a name="s_SHA1"></a>

The SHA1 function uses the SHA1 cryptographic hash function to convert a variable-length string into a 40-character string that is a text representation of the hexadecimal value of a 160-bit checksum.

## Syntax
<a name="s_SHA1-syntax"></a>

SHA1 is a synonym of [SHA function](s_SHA.md).

```
SHA1(string)
```

## Arguments
<a name="s_SHA1-arguments"></a>

 *string*
A variable-length string.

## Return type
<a name="s_SHA1-returm-type"></a>

The SHA1 function returns a 40-character string that is a text representation of the hexadecimal value of a 160-bit checksum.

## Example
<a name="s_SHA1-example"></a>

The following example returns the 160-bit value for the word 'AWS Clean Rooms':

```
select sha1('AWS Clean Rooms');
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

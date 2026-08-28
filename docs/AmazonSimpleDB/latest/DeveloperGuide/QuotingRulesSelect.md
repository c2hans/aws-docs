---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/QuotingRulesSelect.html
---

# Select Quoting Rules
<a name="QuotingRulesSelect"></a>

Attribute values must be quoted with a single or double quote. If a quote appears within the attribute value, it must be escaped with the same quote symbol. These following two expressions are equivalent:

```
select * from mydomain where attr1 = 'He said, "That''s the ticket!"'
select * from mydomain where attr1 = "He said, ""That's the ticket!"""
```

Attribute and domain names may appear without quotes if they contain only letters, numbers, underscores (\_), or dollar symbols ($) and do not start with a number. You must quote all other attribute and domain names with the backtick (`).

```
select * from mydomain where `timestamp-1` > '1194393600'
```

You must escape the backtick when it appears in the attribute or domain name by replacing it with two backticks. For example, we can retrieve any items that have the attribute abc`123 set to the value 1 with this select expression:

```
select * from mydomain where `abc``123` = '1'
```

The following is the list of reserved keywords that are valid identifiers that must be backtick quoted if used as an attribute or domain name in the Select syntax.
+ or
+ and
+ not
+ from
+ where
+ select
+ like
+ null
+ is
+ order
+ by
+ asc
+ desc
+ in
+ between
+ intersection
+ limit
+ every

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

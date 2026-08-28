---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/NegativeNumbersOffsets.html
---

# Negative Numbers Offsets
<a name="NegativeNumbersOffsets"></a>

When choosing a numerical range, ensure that every number is positive. To do this, choose an offset that is larger than the smallest expected negative number in your data set. For example, if the smallest expected number in your data set is -12,000, choosing offset = 100,000 might be safe.

The following is a sample original data set.

```
14.58, -12536.791, 20071109, 655378.34, -23
```

If you apply an offset of 100,000, the following is the resulting data set.

```
100014.58, 87463.209, 20171109, 755378.34, 99977
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

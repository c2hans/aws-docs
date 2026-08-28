---
source_url: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/NumericalData.html
---

# Working with Numerical Data
<a name="NumericalData"></a>

**Topics**
+ [Negative Numbers Offsets](NegativeNumbersOffsets.md)
+ [Zero Padding](ZeroPadding.md)
+ [Dates](Dates.md)

Amazon SimpleDB is a schema-less data store and everything is stored as a UTF-8 string value. This provides application designers with the flexibility of enforcing data restrictions at the application layer without the data store enforcing constraints.

All comparisons are performed lexicographically. As a result, we highly recommend that you use negative number offsets, zero padding, and store dates in an appropriate format.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SimpleDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSimpleDB` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

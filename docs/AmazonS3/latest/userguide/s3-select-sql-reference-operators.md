---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-select-sql-reference-operators.html
---

# Operators
<a name="s3-select-sql-reference-operators"></a>

**Important**
Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can continue to use the feature as usual. [Learn more](https://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/)

Amazon S3 Select supports the following operators.

## Logical operators
<a name="s3-select-sql-reference-loical-ops"></a>
+ `AND`
+ `NOT`
+ `OR`

## Comparison operators
<a name="s3-select-sql-reference-compare-ops"></a>
+ `<`
+ `>`
+ `<=`
+ `>=`
+ `=`
+ `<>`
+ `!=`
+ `BETWEEN`
+ `IN` – For example: `IN ('a', 'b', 'c')`

## Pattern-matching operators
<a name="s3-select-sql-reference-pattern"></a>
+ `LIKE`
+ `_` (Matches any character)
+ `%` (Matches any sequence of characters)

## Unitary operators
<a name="s3-select-sql-reference-unitary-ops"></a>
+ `IS NULL`
+ `IS NOT NULL`

## Math operators
<a name="s3-select-sql-referencemath-ops"></a>

Addition, subtraction, multiplication, division, and modulo are supported, as follows:
+ \+
+ -
+ \*
+ /
+ %

## Operator precedence
<a name="s3-select-sql-reference-op-Precedence"></a>

The following table shows the operators' precedence in decreasing order.

|  Operator or element  |  Associativity |  Required  |
| --- | --- | --- |
| `-`  | right  | unary minus  |
| `*`, `/`, `%`  | left  | multiplication, division, modulo  |
| `+`, `-`  | left  | addition, subtraction  |
| `IN` |  | set membership  |
| `BETWEEN` |  | range containment  |
| `LIKE` |  | string pattern matching  |
| `<``>` |  | less than, greater than  |
| `=` | right  | equality, assignment |
| `NOT` | right | logical negation  |
| `AND` | left | logical conjunction  |
| `OR` | left | logical disjunction  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

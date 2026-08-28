---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/query-components.html
---

# Query Components for AWS Config
<a name="query-components"></a>

The SQL `SELECT` query components for AWS Config advanced queries are as follows.

## Synopsis
<a name="synopsis"></a>

```
SELECT property [, ...]
[ WHERE condition ]
[ GROUP BY property ]
[ ORDER BY property [ ASC | DESC ] [, property [ ASC | DESC ] ...] ]
```

## Parameters
<a name="parameters"></a>

**[ WHERE condition ]**
Filters results according to the `condition` you specify.
**Comparison operators**
+ `=` (equals)
+ `IN` (list membership)
+ `BETWEEN` (range check)
**Logic operators**
+ `AND`
+ `OR`
+ `NOT`

**[ GROUP BY property ]**
Aggregates the result set into groups of rows with matching values for the given property.
The GROUP BY clause is applicable to aggregations.

**[ ORDER BY property [ ASC \| DESC ] [, property [ ASC \| DESC ] ...] ]**
Sorts a result set by one or more output `properties`.
When the clause contains multiple properties, the result set is sorted according to the first `property`, then according to the second `property` for rows that have matching values for the first property, and so on.

## Examples
<a name="examples"></a>

```
SELECT resourceId WHERE resourceType='AWS::EC2::Instance'
```

```
SELECT configuration.complianceType, COUNT(*) WHERE resourceType = 'AWS::Config::ResourceCompliance' GROUP BY configuration.complianceType
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

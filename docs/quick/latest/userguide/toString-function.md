---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/toString-function.html
---

# toString
<a name="toString-function"></a>

`toString` formats the input expression as a string. `toString` skips rows containing null values.

## Syntax
<a name="toString-function-syntax"></a>

```
toString({{expression}})
```

## Arguments
<a name="toString-function-arguments"></a>

 *expression*
 An expression can be a field of any data type, a literal value like **14.62**, or a call to another function that returns any data type.

## Return type
<a name="toString-function-return-type"></a>

String

## Example
<a name="toString-function-example"></a>

The following example returns the values from `payDate` (which uses the `date` data type) as strings.

```
toString(payDate)
```

The following are the given field values.

```
payDate
--------
1992-11-14T00:00:00.000Z
2012-10-12T00:00:00.000Z
1973-04-08T00:00:00.000Z
```

For these field values, the following rows are returned.

```
1992-11-14T00:00:00.000Z
2012-10-12T00:00:00.000Z
1973-04-08T00:00:00.000Z
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

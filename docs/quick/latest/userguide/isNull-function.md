---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/isNull-function.html
---

# isNull
<a name="isNull-function"></a>

`isNull` evaluates an expression to see if it is null. If the expression is null, `isNull` returns true, and otherwise it returns false.

## Syntax
<a name="isNull-function-syntax"></a>

```
isNull({{expression}})
```

## Arguments
<a name="isNull-function-arguments"></a>

 *expression*
The expression to be evaluated as null or not. It can be a field name like **address1** or a call to another function that outputs a string.

## Return type
<a name="isNull-function-return-type"></a>

Boolean

## Example
<a name="isNull-function-example"></a>

The following example evaluates the sales\_amount field for null values.

```
isNull(salesAmount)
```

The following are the given field values.

```
20.13
(null)
57.54
```

For these field values, the following values are returned.

```
false
true
false
```

The following example tests for a NULL value in an `ifelse` statement, and returns a human-readable value instead.

```
ifelse( isNull({ActiveFlag}) , 'Inactive',  'Active')
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

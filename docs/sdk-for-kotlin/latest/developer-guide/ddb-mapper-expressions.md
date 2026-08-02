---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-expressions.html
---

# Use expressions
<a name="ddb-mapper-expressions"></a>

**Important**
DynamoDB Mapper is a Developer Preview release. It is not feature complete and is subject to change.

Certain DynamoDB operations accept [expressions](/amazondynamodb/latest/developerguide/Expressions.html) that you can use to specify constraints or conditions. DynamoDB Mapper provides an idiomatic Kotlin DSL to create expressions. The DSL brings greater structure and readability to your code and also makes it easier to write expressions.

This section describes the DSL syntax and provides various examples.

## Use expressions in operations
<a name="ddb-mapper-expressions-basic-usage"></a>

You use expressions in operations like `scan`, where they filter the returned items based on criteria that you define. To use expressions with DynamoDB Mapper, add the expression component in the operation request.

The following snippet shows an example of a filter expression that is used in a `scan` operation. It uses a lambda argument to describe the filter criteria that limits the items to be returned to those with a `year` attribute value of 2001:

```
val table = // A table instance.

table.scanPaginated {
    filter {
        attr("year") eq 2001
    }
}
```

The following example shows a `query` operation that supports expressions in two places—sort key filtering and non-key filtering:

```
table.queryPaginated {
    keyCondition = KeyFilter(partitionKey = 1000) { sortKey startsWith "M" }
    filter {
        attr("year") eq 2001
    }
}
```

The previous code filters results to those that meet all three criteria:
+ Partition key attribute value is 1000 *-AND-*
+ Sort key attribute value starts with the letter *M* *-AND-*
+ year attribute value is 2001

## DSL components
<a name="ddb-mapper-expressions-dsl"></a>

The DSL syntax exposes several types of components—described below—that you use to build expressions.

### Attributes
<a name="ddb-mapper-expressions-dsl-attrs"></a>

Most conditions reference attributes, which are identified by their key or document path. With the DSK, you create all attribute references by using the `attr` function and optionally make additional modifications.

The following code shows a range of example attribute references from simple to complex, such as list dereferencing by index and map dereferencing by key

```
attr("foo")           // Refers to the value of top-level attribute `foo`.

attr("foo")[3]        // Refers to the value at index 3 in the list value of
                      // attribute `foo`.

attr("foo")[3]["bar"] // Refers to the value of key `bar` in the map value at
                      // index 3 of the list value of attribute `foo`.
```

### Equalities and inequalities
<a name="ddb-mapper-expressions-dsl-eq-and-ineq"></a>

You can compare attribute values in an expression by equalities and inequalities. You can compare attribute values to literal values or other attribute values. The functions that you use to specify the conditions are:
+  `eq`: is equal to (equivalent to `==`)
+  `neq`: is not equal to (equivalent to `!=`)
+  `gt`: is greater than (equivalent to `>`)
+  `gte`: is greater than or equal to (equivalent to `>=`)
+  `lt`: is less than (equivalent to `<`)
+  `lte`: is less than or equal to (equivalent to `⇐`)

You combine the comparison function with arguments by using infix notation as shown in the following examples:

```
attr("foo") eq 42           // Uses a literal. Specifies that the attribute value `foo` must be
                            // equal to 42.

attr("bar") gte attr("baz") // Uses another attribute value. Specifies that the attribute
                            // value `bar` must be greater than or equal to the
                            // attribute value of `baz`.
```

### Ranges and sets
<a name="ddb-mapper-expressions-dsl-ranges-sets"></a>

In addition to single values, you can compare attribute values to multiple values in ranges or sets. You use the infix `isIn` function to do the comparison as shown in the following examples:

```
attr("foo") isIn 0..99  // Specifies that the attribute value `foo` must be
                        // in the range of `0` to `99` (inclusive).

attr("foo") isIn setOf( // Specifies that the attribute value `foo` must be
    "apple",            // one of `apple`, `banana`, or `cherry`.
    "banana",
    "cherry",
)
```

The `isIn` function provides overloads for collections (such as `Set<String>`) and for bounds that you can express as a Kotlin `ClosedRange<T>` (such as `IntRange`). For bounds that you cannot express as a `ClosedRange<T>` (such as byte arrays or other attribute references), you can use the `isBetween` function:

```
val lowerBytes = byteArrayOf(0x48, 0x65, 0x6c)  // Specifies that the attribute value
val upperBytes = byteArrayOf(0x6c, 0x6f, 0x21)  // `foo` is between the values
attr("foo").isBetween(lowerBytes, upperBytes)   // `0x48656c` and `0x6c6f21`

attr("foo").isBetween(attr("bar"), attr("baz")) // Specifies that the attribute value
                                                // `foo` is between the values of
                                                // attributes `bar` and `baz`.
```

### Boolean logic
<a name="ddb-mapper-expressions-dsl-boolean"></a>

You can combine individual conditions or altered using boolean logic by using the following functions:
+  `and`: every condition must be true (equivalent to `&&`)
+  `or`: at least one condition must be true (equivalent to `||`)
+  `not`: the given condition must be false (equivalent to `!`)

The follow examples show each function:

```
and(                           // Both conditions must be met:
    attr("foo") eq "banana",   // * attribute value `foo` must equal `banana`
    attr("bar") isIn 0..99,    // * attribute value `bar` must be between
)                              //   0 and 99 (inclusive)

or(                            // At least one condition must be met:
    attr("foo") eq "cherry",   // * attribute value `foo` must equal `cherry`
    attr("bar") isIn 100..199, // * attribute value `bar` must be between
)                              //   100 and 199 (inclusive)

not(                           // The attribute value `foo` must *not* be
    attr("baz") isIn setOf(    // one of `apple`, `banana`, or `cherry`.
        "apple",               // Stated another way, the attribute value
        "banana",              // must be *anything except* `apple`, `banana`,
        "cherry",              // or `cherry`--including potentially a
    ),                         // non-string value or no value at all.
)
```

You can further combine boolean conditions by boolean functions to create nested logic as shown in the following expression:

```
or(
    and(
        attr("foo") eq 123,
        attr("bar") eq "abc",
    ),
    and(
        attr("foo") eq 234,
        attr("bar") eq "bcd",
    ),
)
```

The previous expression filters results to those that meet either of these conditions:
+ Both of these conditions are true:
  +  `foo` attribute value is 123 *-AND-*
  +  `bar` attribute value is "abc"
+ Both of these conditions are true:
  +  `foo` attribute value is 234 *-AND-*
  +  `bar` attribute value is "bcd"

This is equivalent to the following Kotlin boolean expression:

```
(foo == 123 && bar == "abc") || (foo == 234 && bar == "bcd")
```

### Functions and properties
<a name="ddb-mapper-expressions-dsl-functions"></a>

The following functions and properties provide additional expression capabilities:
+  `contains`: checks if a string/list attribute value contains a given value
+  `exists`: checks if an attribute is defined and holds any value (including `null`)
+  `notExists`: checks if an attribute is undefined
+  `isOfType`: checks if an attribute value is of a given type, such as string, number, boolean, and so on
+  `size`: gets the size of an attribute, such as the number of elements in a collection or the length of a string
+  `startsWith`: checks if a string attribute value starts with a given substring

The following examples show use of additional functions and properties that you can use in expressions:

```
attr("foo") contains "apple" // Specifies that the attribute value `foo` must be
                             // a list that contains an `apple` element or a string
                             // which contains the substring `apple`.

attr("bar").exists()         // Specifies that the `bar` must exist and have a
                             // value (including potentially `null`).

attr("baz").size lt 100      // Specifies that the attribute value `baz` must have
                             // a size of less than 100.

attr("qux") isOfType AttributeType.String // Specifies that the attribute `qux`
                                          // must have a string value.
```

### Sort key filters
<a name="ddb-mapper-expressions-dsl-sort-key"></a>

Filter expressions on sort keys (such as in the `query` operation’s `keyCondition` parameter) do not use named attribute values. To use a sort key in a filter, you must use the keyword `sortKey` in all comparisons. The `sortKey` keyword replaces `attr("<sort key name>")` as shown in the following examples:

```
sortKey startsWith "abc" // The sort key attribute value must begin with the
                         // substring `abc`.

sortKey isIn 0..99       // The sort key attribute value must be between 0
                         // and 99 (inclusive).
```

You cannot combine sort key filters with boolean logic and they support only a subset of the comparisons described above:
+  [Equalities and inequalities](#ddb-mapper-expressions-dsl-eq-and-ineq): all comparisons supported
+  [Ranges and sets](#ddb-mapper-expressions-dsl-ranges-sets): all comparisons supported
+  [Boolean logic](#ddb-mapper-expressions-dsl-boolean): not supported
+  [Functions and properties](#ddb-mapper-expressions-dsl-functions): only `startsWith` is supported

---
source_url: https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/ddb-mapper-expressions.html
---

# Use expressions
<a name="ddb-mapper-expressions"></a>

DynamoDB Mapper provides Kotlin DSLs for building the two kinds of [DynamoDB expressions](/amazondynamodb/latest/developerguide/Expressions.html) you use most:
+  **Filter and condition expressions**: boolean conditions that narrow the results of a [`query`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) or [`scan`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html), or that gate a write. You build these in a `filter { }` block.
+  **Update expressions**: instructions that describe how [`updateItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) modifies an item. You build these in an `update { }` block.

This topic uses the `Order` item type (partition key `customerId`, sort key `orderId`) for its examples.

**Important**
These DSLs build **low-level** expressions: they are not restricted by or adherent to any defined schema. Instead, they are a convenience layer over literal DynamoDB expression strings and expression attribute value maps. As such they provide **minimal type correctness** and might allow you to form expressions that are invalid given the shape of your data, such as referencing attributes that don’t exist or comparing mismatched data types. Because they’re schema-unaware, expressions reference **stored attribute names**, not Kotlin property names. For example, a property annotated with [`@DynamoDbAttribute`](ddb-mapper-anno-index.md) (such as `@DynamoDbAttribute("created_at")`) is referenced by its stored name: `attr["created_at"]`.

## Reference attributes
<a name="ddb-mapper-expressions-attributes"></a>

Every expression references at least one attribute through the `attr` accessor. A top-level attribute is `attr["name"]`. Nested values inside maps and lists are reached by chaining the `[]` operator with string keys and integer indexes:

```
attr["status"]              // a top-level attribute
attr["shipping"]["city"]    // the "city" entry of the "shipping" map attribute
attr["productSkus"][0]      // the first element of the "productSkus" list attribute
```

## Filter expressions
<a name="ddb-mapper-expressions-filter"></a>

Set a `filter { }` on a [`query`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) or [`scan`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) to drop items that don’t match a condition. The filter is applied by DynamoDB after items are read, so it narrows results but doesn’t reduce read cost.

```
import aws.sdk.kotlin.hll.dynamodbmapper.expressions.KeyFilter

val largeShipped = ordersTable
    .queryPaginated {
        keyCondition = KeyFilter("customer-123")
        filter {
            and(
                attr["status"] eq "SHIPPED",
                attr["totalCents"] gt 10_000L,
            )
        }
    }
    .items()
```

### Operators and functions
<a name="ddb-mapper-expressions-operators"></a>

Inside a `filter { }` block, the following are available on attribute references.

#### Comparisons
<a name="ddb-mapper-expressions-comparisons"></a>

The following equality/inequality comparison operators are available:
+  `A eq B`: true if `A` is equal to `B`
+  `A gt B`: true if `A` is greater than `B`
+  `A gte B`: true if `A` is greater than or equal to `B`
+  `A lt B`: true if `A` is less than `B`
+  `A lte B`: true if `A` is less than or equal to `B`
+  `A neq B`: true if `A` is not equal to `B`

```
filter { attr["totalCents"] gte 5_000L } // totalCents is greater than or equal to 5,000
```

#### Ranges and membership
<a name="ddb-mapper-expressions-ranges-memberships"></a>

The following operators work on ranges and collections:
+  `A.isBetween(B, C)`: true if `A` is greater than or equal to `B` **and** less than or equal to `C`
+  `A isIn B`: true if `A` is an element in the collection/range `B`

```
filter { attr["totalCents"] isIn 1_000L..5_000L }       // totalCents is between 1,000 and 5,000
filter { attr["status"] isIn setOf("PAID", "SHIPPED") } // status is either PAID or SHIPPED
```

#### Functions
<a name="ddb-mapper-expressions-functions"></a>

The following functions are available:
+  `A contains B`: true if `A` contains `B` as an element or substring
+  `A.exists()`: true if the item contains attribute `A`
+  `A isOfType B`: true if `A`'s attribute type is `B`
+  `A.notExists()`: true if the item *does not* contain attribute `A`
+  `A.size`: computes the string length or collection size of `A`. Note that this is not a boolean expression and must be combined with another operator or function to form a valid filter expression.
+  `A startsWith B`: true if `A` begins with `B`

```
filter { attr["productSkus"] contains "SKU-1" }    // SKU-1 is an element in productSkus
filter { attr["couponCode"].exists() }             // the item has a couponCode
filter { attr["orderId"] startsWith "ORDER#2026" } // orderId begins with ORDER#2026
filter { attr["productSkus"].size gte 2 }          // there are at least 2 productSkus
```

#### Boolean logic
<a name="ddb-mapper-expressions-boolean-logic"></a>

The following boolean logic operations are available:
+  `and(A, B, C, …​)`: true if all of `A`, `B`, `C`, `…​` are true
+  `or(A, B, C, …​)`: true if at least one of `A`, `B`, `C`, `…​` is true
+  `not(A)`: true if `A` is false; false if `A` is true

```
filter {
    or(
        attr["status"] eq "PENDING",
        and(
            attr["status"] eq "PAID",
            not(attr["couponCode"].exists()),
        ),
    )
}
```

### Key conditions
<a name="ddb-mapper-expressions-key-conditions"></a>

A [`query`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) also takes a `keyCondition`, built with `KeyFilter`. Unlike a filter, a key condition is evaluated by DynamoDB to select which items to read. It always specifies the partition key and can add a condition on the sort key through a lambda argument:

```
// All orders for a customer:
keyCondition = KeyFilter("customer-123")

// Orders for a customer whose orderId begins with a prefix:
keyCondition = KeyFilter("customer-123", { sortKey startsWith "ORDER#2026" })
```

Within the sort-key lambda you can use the following operators and functions:
+  [Comparisons](#ddb-mapper-expressions-comparisons): `eq`, `gt`, `gte`, `lt`, `lte`, `neq`
+  [Ranges and membership](#ddb-mapper-expressions-ranges-memberships): `isBetween` and `isIn`
+  [Functions](#ddb-mapper-expressions-functions): `startsWith`

## Update expressions
<a name="ddb-mapper-expressions-update"></a>

Set an `update { }` on [`updateItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) to modify an item in place without reading and rewriting it. An update expression contains one or more of four clauses, which may appear in any order:
+  `add { }`: increment numbers or add elements to sets
+  `delete { }`: remove elements from sets
+  `remove { }`: delete attributes or elements
+  `set { }`: add or modify attributes

```
import aws.sdk.kotlin.hll.dynamodbmapper.items.Key

ordersTable.updateItem {
    partitionKey = Key("customer-123")
    sortKey = Key("ORDER#2026-06-25#0042")
    update {
        set {
            attr["status"] = "SHIPPED"
            attr["totalCents"] = attr["totalCents"] - 500 // apply a $5.00 discount
            attr["notes"] = attr["notes"] orElse "none"   // set only if not already present
        }
        remove {
            -attr["couponCode"]                           // remove the coupon code
        }
        add {
            attr["tags"] += setOf("priority")             // add elements to the "tags" set
        }
        delete {
            attr["tags"] -= setOf("gift")                 // remove an element from the "tags" set
        }
    }
}
```

### Clause details
<a name="ddb-mapper-expressions-clause-details"></a>

 ** `add` ** increments a number or adds elements to a set with `+=`. Unlike a `set` increment, this maps to the low-level `ADD` action, which also creates the attribute if it’s absent.

```
add {
    attr["tags"] += setOf("backordered")
}
```

 ** `delete` ** removes elements from a set with `-=`:

```
delete {
    attr["tags"] -= setOf("gift", "priority")
}
```

 ** `remove` ** deletes attributes, map entries, or list elements with the unary `-` operator:

```
remove {
    -attr["couponCode"]
    -attr["productSkus"][0]
}
```

 ** `set` ** adds or replaces attributes and elements. Assign a literal value or an expression with `=`. Derive numeric values with `+`/`-` (or `+=`/`-=`), fall back to a default for a missing attribute with `orElse`, and concatenate lists with `appending`:

```
set {
    attr["status"] = "PAID"
    attr["totalCents"] += 250
    attr["productSkus"] = attr["productSkus"] appending listOf("SKU-9")
}
```

## Related topics
<a name="ddb-mapper-expressions-related"></a>
+  [Operations overview](ddb-mapper-operations.md): the [`query`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html), [`scan`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html), and [`updateItem`](/sdk-for-kotlin/api/latest/dynamodb-mapper/aws.sdk.kotlin.hll.dynamodbmapper.operations/index.html) operations these expressions feed.
+  [Use secondary indexes with DynamoDB Mapper](ddb-mapper-secondary-indexes.md): key conditions and filters on indexes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Kotlin. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-kotlin` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

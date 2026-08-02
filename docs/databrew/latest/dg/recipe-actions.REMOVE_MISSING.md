---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.REMOVE_MISSING.html
---

# REMOVE\_MISSING
<a name="recipe-actions.REMOVE_MISSING"></a>

Returns only the rows in which a specified column isn't missing data.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "REMOVE_MISSING",
        "Parameters": {
            "sourceColumn": "last_name"
        }
    }
}
```

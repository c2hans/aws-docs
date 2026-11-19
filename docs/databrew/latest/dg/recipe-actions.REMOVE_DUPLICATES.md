---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.REMOVE_DUPLICATES.html
---

# REMOVE\_DUPLICATES

Deletes an entire row, if a duplicate value is encountered in a selected source column.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "REMOVE_DUPLICATES",
        "Parameters": {
            "sourceColumn": "nationality"
        }
    }
}
```

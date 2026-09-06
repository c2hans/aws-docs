---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.MOVE_TO_START.html
---

# MOVE\_TO\_START
<a name="recipe-actions.MOVE_TO_START"></a>

Moves a column to the beginning position (first column) in the dataset.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "MOVE_TO_START",
        "Parameters": {
            "sourceColumn": "first_name"
        }
    }
}
```

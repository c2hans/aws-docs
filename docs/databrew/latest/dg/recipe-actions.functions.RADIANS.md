---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.RADIANS.html
---

# RADIANS
<a name="recipe-actions.functions.RADIANS"></a>

Converts degrees to radians (divides by 180/pi) and returns the value in a new column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.

**Example**

```
{
    "RecipeAction": {
        "Operation": "RADIANS",
        "Parameters": {
            "sourceColumn": "weight_kg",
            "targetColumn": "weight_kg_RADIANS"
        }
    }
}
```

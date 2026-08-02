---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.DEGREES.html
---

# DEGREES
<a name="recipe-actions.functions.DEGREES"></a>

Converts radians for an angle to degrees and returns the result in a new column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.

**Example**

```
{
    "RecipeAction": {
        "Operation": "DEGREES",
        "Parameters": {
            "sourceColumn": "height_cm",
            "targetColumn": "height_cm_DEGREES"
        }
    }
}
```

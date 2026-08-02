---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.FILL_WITH_EMPTY.html
---

# FILL\_WITH\_EMPTY
<a name="recipe-actions.FILL_WITH_EMPTY"></a>

Returns a column with missing data replaced by an empty string.

**Parameters**
+ `sourceColumn` – The name of an existing column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "FILL_WITH_EMPTY",
        "Parameters": {
            "sourceColumn": "wind_direction"
        }
    }
}
```

---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.GET_ADVANCED_DATATYPE.html
---

# GET\_ADVANCED\_DATATYPE

Given a string column, identifies the advanced data type of the column, if any.

**Parameters**
+ `columnName` – The name of the string column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "GET_ADVANCED_DATATYPE",
        "Parameters": {
            "sourceColumn": "columnName"
        }
    }
}
```

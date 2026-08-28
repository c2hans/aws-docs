---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.EXTRACT_VALUE.html
---

# EXTRACT\_VALUE
<a name="recipe-actions.EXTRACT_VALUE"></a>

Creates a new column with an extracted value from a user-specified path. If the source column is of the Map, Array, or Struct type, each field in the path should be escaped using back ticks (for example, `name`).

**Parameters**
+ `targetColumn` – The name of the target column.
+ `sourceColumn` – Name of the source column from which the value is to be extracted.
+ `path` – The path to the specific key that the user wants to extract. If the source column is of the Map, Array, or Struct type, each field in the path should be escaped using back ticks (for example, `name`).

  Consider the following example of user information:

  ```
                     user {
                        name: “Ammy”
                        address: {
                           state: "CA",
                           zipcode: 12345
                        },
                        phoneNumber:{"home": "123123123", "work": "456456456"}
                        citizenship: ["Canada", "USA", "Mexico", "India"]
                     }
  ```

  The following are examples of the paths you would provide, depending on the type of the source column:
  + If the source column is of the type **map**, the path for extracting the home phone number is:

    ``user`.`phoneNumber`.`home``
  + If the source column is of the type **array**, the path for extracting the second "citizenship" value is:

    ``user`.`citizenship`[1]`
  + If the source column is of the type **struct**, the path for extracting the zip code is:

    ``user`.`address`.`zipcode``

**Example**

```
{
    "RecipeAction": {
        "Operation": "EXTRACT_VALUE",
        "Parameters": {
            "sourceColumn": "age",
            "targetColumn": "columnName",
            "path": "`age`.`name`",
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

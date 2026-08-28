---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.MASK_DELIMITER.html
---

# MASK\_DELIMITER
<a name="recipe-actions.MASK_DELIMITER"></a>

Masks characters between two delimiters with a user-specified masking symbol.

**Parameters**
+ `sourceColumns` – A list of existing column names.
+ `maskSymbol` – A symbol that will be used to replace specified characters.
+ `startDelimiter` – A character indicating where masking is to begin. Omitting this parameter will apply the mask starting from the start of the string.
+ `endDelimiter` – A character indicating where masking is to end. Omitting this parameter will apply the masking from the startDelimiter to the end of the string.
+ `preserveDelimiters` – If true, applies mask to delimiters.
+ `alphabet` – An array of character sets to preserve during masking. Valid enum values: SYMBOLS, WHITESPACE.
+ `entityTypeFilter` – Optional array of [entity types](https://docs.aws.amazon.com/databrew/latest/APIReference/API_EntityDetectorConfiguration.html#databrew-Type-EntityDetectorConfiguration-EntityTypes). Can be used to encrypt only detected PII in free-text column.

**Example**

```
// Mask string between '<' and '>', ignoring white spaces, symbols, and lowercase letters
{
    "RecipeAction": {
        "Operation": "MASK_DELIMITER",
        "Parameters": {
            "sourceColumns": ["name"],
            "maskSymbol": "#",
            "startDelimiter": "<",
            "endDelimiter": ">",
            "preserveDelimiters": false,
            "alphabet": ["WHITESPACE", "SYMBOLS"]
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

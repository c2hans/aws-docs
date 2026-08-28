---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.TOKENIZATION.html
---

# TOKENIZATION
<a name="recipe-actions.TOKENIZATION"></a>

Splits text into smaller units, or tokens, such as individual words or terms.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `delimiter` — A custom delimiter that appears between tokenized words. (The default behavior is to separate each token by a space.)
+ `expandContractions` — If `ENABLED`, expands contracted words. For example: "don't" becomes "do not".
+ `stemmingMode` — Splits text into smaller units or tokens, such as individual lowercase words or terms. Two stemming modes are available: `PORTER` \| `LANCASTER`.
+ `stopWordRemovalMode` — Removes common words like a, an, the, and more.
+ `customStopWords` — For `StopWordRemovalMode`, allows you to specify a custom list of stop words.
+ `targetColumn` — The name of a column to contain the results.

**Example**

```
{
    "Action": {
        "Operation": "TOKENIZATION",
        "Parameters": {
            "customStopWords": "[]",
            "delimiter": "- ",
            "expandContractions": "ENABLED",
            "sourceColumn": "dimensions",
            "stemmingMode": "PORTER",
            "stopWordRemovalMode": "DEFAULT",
            "targetColumn": "dimensions_tokenized"
        }
    }

}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

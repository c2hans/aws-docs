---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_Recipe.html
---

# Recipe
<a name="API_Recipe"></a>

Represents one or more actions to be performed on a DataBrew dataset.

## Contents
<a name="API_Recipe_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="databrew-Type-Recipe-Name"></a>
The unique name for the recipe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** CreateDate **   <a name="databrew-Type-Recipe-CreateDate"></a>
The date and time that the recipe was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="databrew-Type-Recipe-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the recipe.
Type: String
Required: No

 ** Description **   <a name="databrew-Type-Recipe-Description"></a>
The description of the recipe.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** LastModifiedBy **   <a name="databrew-Type-Recipe-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last modified the recipe.
Type: String
Required: No

 ** LastModifiedDate **   <a name="databrew-Type-Recipe-LastModifiedDate"></a>
The last modification date and time of the recipe.
Type: Timestamp
Required: No

 ** ProjectName **   <a name="databrew-Type-Recipe-ProjectName"></a>
The name of the project that the recipe is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** PublishedBy **   <a name="databrew-Type-Recipe-PublishedBy"></a>
The Amazon Resource Name (ARN) of the user who published the recipe.
Type: String
Required: No

 ** PublishedDate **   <a name="databrew-Type-Recipe-PublishedDate"></a>
The date and time when the recipe was published.
Type: Timestamp
Required: No

 ** RecipeVersion **   <a name="databrew-Type-Recipe-RecipeVersion"></a>
The identifier for the version for the recipe. Must be one of the following:
+ Numeric version (`X.Y`) - `X` and `Y` stand for major and minor version numbers. The maximum length of each is 6 digits, and neither can be negative values. Both `X` and `Y` are required, and "0.0" isn't a valid version.
+  `LATEST_WORKING` - the most recent valid version being developed in a DataBrew project.
+  `LATEST_PUBLISHED` - the most recent published version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

 ** ResourceArn **   <a name="databrew-Type-Recipe-ResourceArn"></a>
The Amazon Resource Name (ARN) for the recipe.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** Steps **   <a name="databrew-Type-Recipe-Steps"></a>
A list of steps that are defined by the recipe.
Type: Array of [RecipeStep](API_RecipeStep.md) objects
Required: No

 ** Tags **   <a name="databrew-Type-Recipe-Tags"></a>
Metadata tags that have been applied to the recipe.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Recipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/Recipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/Recipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/Recipe)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

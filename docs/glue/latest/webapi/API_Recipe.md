---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Recipe.html
---

# Recipe
<a name="API_Recipe"></a>

A AWS Glue Studio node that uses a AWS Glue DataBrew recipe in AWS Glue jobs.

## Contents
<a name="API_Recipe_Contents"></a>

 ** Inputs **   <a name="Glue-Type-Recipe-Inputs"></a>
The nodes that are inputs to the recipe node, identified by id.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-Recipe-Name"></a>
The name of the AWS Glue Studio node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** RecipeReference **   <a name="Glue-Type-Recipe-RecipeReference"></a>
A reference to the DataBrew recipe used by the node.
Type: [RecipeReference](API_RecipeReference.md) object
Required: No

 ** RecipeSteps **   <a name="Glue-Type-Recipe-RecipeSteps"></a>
Transform steps used in the recipe node.
Type: Array of [RecipeStep](API_RecipeStep.md) objects
Required: No

## See Also
<a name="API_Recipe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Recipe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Recipe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Recipe)

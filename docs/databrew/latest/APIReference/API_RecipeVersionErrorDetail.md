---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_RecipeVersionErrorDetail.html
---

# RecipeVersionErrorDetail
<a name="API_RecipeVersionErrorDetail"></a>

Represents any errors encountered when attempting to delete multiple recipe versions.

## Contents
<a name="API_RecipeVersionErrorDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorCode **   <a name="databrew-Type-RecipeVersionErrorDetail-ErrorCode"></a>
The HTTP status code for the error.
Type: String
Pattern: `^[1-5][0-9][0-9]$`
Required: No

 ** ErrorMessage **   <a name="databrew-Type-RecipeVersionErrorDetail-ErrorMessage"></a>
The text of the error message.
Type: String
Required: No

 ** RecipeVersion **   <a name="databrew-Type-RecipeVersionErrorDetail-RecipeVersion"></a>
The identifier for the recipe version associated with this error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

## See Also
<a name="API_RecipeVersionErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/RecipeVersionErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/RecipeVersionErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/RecipeVersionErrorDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

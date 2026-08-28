---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/use-the-rewrite-feature.html
---

# Use the rewrite feature
<a name="use-the-rewrite-feature"></a>

You can use this solution’s rewrite feature to migrate your current image request model to the Dynamic Image Transformation for Amazon CloudFront solution, without changing the applications to accommodate new image URLs.

The rewrite feature translates custom URL image requests into Thumbor-consumable formats, based on JavaScript-compatible regular expression match patterns and substitution strings. After the image request is converted into Thumbor-consumable form, it’s then processed as a Thumbor image request and edits are mapped to the new sharp image library.

This feature requires that you populate the following environment variables in the [image handler function](custom-image-requests.md). These environment variables are added to the function by default, but are left empty for user input if the rewrite feature is needed.

| Variable Key | Value Type | Description |
| --- | --- | --- |
|  **REWRITE\_MATCH\_PATTERN**  |  `Regex`  | By default, this parameter is empty. If you overwrite this default value, use a JavaScript-compatible regular expression for matching custom image requests using the rewrite function. This value should match the JavaScript compatible regular expression. For example, `/(filters-)/gm`. |
|  **REWRITE\_SUBSTITUTION**  |  `String`  | By default, this parameter is empty. If you overwrite this default value, use a substitution string for custom image requests using the rewrite function. For example, `filters:`. |

You can use any of the Thumbor-supported filters listed in this section with the rewrite feature. The following sections provide examples.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

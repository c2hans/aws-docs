---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_SpaceSummary.html
---

# SpaceSummary
<a name="API_SpaceSummary"></a>

Information about an space.

## Contents
<a name="API_SpaceSummary_Contents"></a>

 ** name **   <a name="codecatalyst-Type-SpaceSummary-name"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

 ** regionName **   <a name="codecatalyst-Type-SpaceSummary-regionName"></a>
The AWS Region where the space exists.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 16.
Pattern: `(us(?:-gov)?|af|ap|ca|cn|eu|sa)-(central|(?:north|south)?(?:east|west)?)-(\d+)`
Required: Yes

 ** description **   <a name="codecatalyst-Type-SpaceSummary-description"></a>
The description of the space.
Type: String
Required: No

 ** displayName **   <a name="codecatalyst-Type-SpaceSummary-displayName"></a>
The friendly name of the space displayed to users.
Type: String
Required: No

## See Also
<a name="API_SpaceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/SpaceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/SpaceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/SpaceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

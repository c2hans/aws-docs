---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_Exclusion.html
---

# Exclusion
<a name="API_Exclusion"></a>

Contains information about what was excluded from an assessment run.

## Contents
<a name="API_Exclusion_Contents"></a>

 ** arn **   <a name="Inspector-Type-Exclusion-arn"></a>
The ARN that specifies the exclusion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** description **   <a name="Inspector-Type-Exclusion-description"></a>
The description of the exclusion.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: Yes

 ** recommendation **   <a name="Inspector-Type-Exclusion-recommendation"></a>
The recommendation for the exclusion.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: Yes

 ** scopes **   <a name="Inspector-Type-Exclusion-scopes"></a>
The AWS resources for which the exclusion pertains.
Type: Array of [Scope](API_Scope.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** title **   <a name="Inspector-Type-Exclusion-title"></a>
The name of the exclusion.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: Yes

 ** attributes **   <a name="Inspector-Type-Exclusion-attributes"></a>
The system-defined attributes for the exclusion.
Type: Array of [Attribute](API_Attribute.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_Exclusion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/Exclusion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/Exclusion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/Exclusion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

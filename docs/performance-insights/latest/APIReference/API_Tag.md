---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_Tag.html
---

# Tag
<a name="API_Tag"></a>

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

## Contents
<a name="API_Tag_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Key **   <a name="performanceinsights-Type-Tag-Key"></a>
A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and can't be prefixed with `aws:` or `rds:`. The string can only contain only the set of Unicode letters, digits, white-space, '\_', '.', ':', '/', '=', '\+', '-', '@' (Java regex: `"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^.*$`
Required: Yes

 ** Value **   <a name="performanceinsights-Type-Tag-Value"></a>
A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and can't be prefixed with `aws:` or `rds:`. The string can only contain only the set of Unicode letters, digits, white-space, '\_', '.', ':', '/', '=', '\+', '-', '@' (Java regex: "^([\\\\p{L}\\\\p{Z}\\\\p{N}\_.:/=\+\\\\-@]\*)$").
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^.*$`
Required: Yes

## See Also
<a name="API_Tag_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/Tag)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/Tag)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/Tag)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

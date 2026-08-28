---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_Region.html
---

# Region
<a name="API_Region"></a>

The AWS Region.

## Contents
<a name="API_Region_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** regionName **   <a name="datazone-Type-Region-regionName"></a>
The AWS Region name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`
Required: No

 ** regionNamePath **   <a name="datazone-Type-Region-regionNamePath"></a>
The region name path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_Region_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/Region)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/Region)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/Region)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

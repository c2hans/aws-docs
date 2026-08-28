---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_Region.html
---

# Region
<a name="API_Region"></a>

An AWS Region in which AWS Control Tower expects to find the control deployed.

The expected Regions are based on the Regions that are governed by the landing zone. In certain cases, a control is not actually enabled in the Region as expected, such as during drift, or [mixed governance](https://docs.aws.amazon.com/controltower/latest/userguide/region-how.html#mixed-governance).

## Contents
<a name="API_Region_Contents"></a>

 ** name **   <a name="controltower-Type-Region-name"></a>
The AWS Region name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## See Also
<a name="API_Region_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/Region)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/Region)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/Region)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

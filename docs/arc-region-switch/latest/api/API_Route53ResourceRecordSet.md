---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Route53ResourceRecordSet.html
---

# Route53ResourceRecordSet
<a name="API_Route53ResourceRecordSet"></a>

The Amazon Route 53 record set.

## Contents
<a name="API_Route53ResourceRecordSet_Contents"></a>

 ** recordSetIdentifier **   <a name="regionswitch-Type-Route53ResourceRecordSet-recordSetIdentifier"></a>
The Amazon Route 53 record set identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** region **   <a name="regionswitch-Type-Route53ResourceRecordSet-region"></a>
The Amazon Route 53 record set Region.
Type: String
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: No

## See Also
<a name="API_Route53ResourceRecordSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Route53ResourceRecordSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Route53ResourceRecordSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Route53ResourceRecordSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

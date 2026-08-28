---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_CommonControlSummary.html
---

# CommonControlSummary
<a name="API_CommonControlSummary"></a>

A summary of metadata for a common control.

## Contents
<a name="API_CommonControlSummary_Contents"></a>

 ** Arn **   <a name="controlcatalog-Type-CommonControlSummary-Arn"></a>
The Amazon Resource Name (ARN) that identifies the common control.
Type: String
Length Constraints: Minimum length of 41. Maximum length of 2048.
Pattern: `arn:(aws(?:[-a-z]*)?):controlcatalog:::common-control/[0-9a-z]+`
Required: Yes

 ** CreateTime **   <a name="controlcatalog-Type-CommonControlSummary-CreateTime"></a>
The time when the common control was created.
Type: Timestamp
Required: Yes

 ** Description **   <a name="controlcatalog-Type-CommonControlSummary-Description"></a>
The description of the common control.
Type: String
Required: Yes

 ** Domain **   <a name="controlcatalog-Type-CommonControlSummary-Domain"></a>
The domain that the common control belongs to.
Type: [AssociatedDomainSummary](API_AssociatedDomainSummary.md) object
Required: Yes

 ** LastUpdateTime **   <a name="controlcatalog-Type-CommonControlSummary-LastUpdateTime"></a>
The time when the common control was most recently updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="controlcatalog-Type-CommonControlSummary-Name"></a>
The name of the common control.
Type: String
Required: Yes

 ** Objective **   <a name="controlcatalog-Type-CommonControlSummary-Objective"></a>
The objective that the common control belongs to.
Type: [AssociatedObjectiveSummary](API_AssociatedObjectiveSummary.md) object
Required: Yes

## See Also
<a name="API_CommonControlSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/CommonControlSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/CommonControlSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/CommonControlSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controlcatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

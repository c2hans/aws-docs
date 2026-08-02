---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ObjectiveSummary.html
---

# ObjectiveSummary
<a name="API_ObjectiveSummary"></a>

A summary of metadata for an objective.

## Contents
<a name="API_ObjectiveSummary_Contents"></a>

 ** Arn **   <a name="controlcatalog-Type-ObjectiveSummary-Arn"></a>
The Amazon Resource Name (ARN) that identifies the objective.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 2048.
Pattern: `arn:(aws(?:[-a-z]*)?):controlcatalog:::objective/[0-9a-z]+`
Required: Yes

 ** CreateTime **   <a name="controlcatalog-Type-ObjectiveSummary-CreateTime"></a>
The time when the objective was created.
Type: Timestamp
Required: Yes

 ** Description **   <a name="controlcatalog-Type-ObjectiveSummary-Description"></a>
The description of the objective.
Type: String
Required: Yes

 ** Domain **   <a name="controlcatalog-Type-ObjectiveSummary-Domain"></a>
The domain that the objective belongs to.
Type: [AssociatedDomainSummary](API_AssociatedDomainSummary.md) object
Required: Yes

 ** LastUpdateTime **   <a name="controlcatalog-Type-ObjectiveSummary-LastUpdateTime"></a>
The time when the objective was most recently updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="controlcatalog-Type-ObjectiveSummary-Name"></a>
The name of the objective.
Type: String
Required: Yes

## See Also
<a name="API_ObjectiveSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ObjectiveSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ObjectiveSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ObjectiveSummary)

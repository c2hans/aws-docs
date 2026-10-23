---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_CollectorSummary.html
---

# CollectorSummary
<a name="API_CollectorSummary"></a>

The collector Summary.

## Contents
<a name="API_CollectorSummary_Contents"></a>

 ** collectorArn **   <a name="continuum-Type-CollectorSummary-collectorArn"></a>
The Amazon Resource Name (ARN) of the collector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:[a-z0-9-]+:continuum:[a-z0-9-]+:[0-9]{12}:collectors/[a-z0-9]+`
Required: Yes

 ** collectorId **   <a name="continuum-Type-CollectorSummary-collectorId"></a>
The identifier of the collector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** createdAt **   <a name="continuum-Type-CollectorSummary-createdAt"></a>
The timestamp when the resource was created.
Type: Timestamp
Required: Yes

 ** status **   <a name="continuum-Type-CollectorSummary-status"></a>
The current status of the resource.
Type: String
Valid Values: `ACTIVE | PENDING_DELETION`
Required: Yes

 ** type **   <a name="continuum-Type-CollectorSummary-type"></a>
The type.
Type: String
Valid Values: `AWS_COLLECTOR`
Required: Yes

## See Also
<a name="API_CollectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/CollectorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/CollectorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/CollectorSummary)

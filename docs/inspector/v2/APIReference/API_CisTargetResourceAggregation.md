---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisTargetResourceAggregation.html
---

# CisTargetResourceAggregation
<a name="API_CisTargetResourceAggregation"></a>

The CIS target resource aggregation.

## Contents
<a name="API_CisTargetResourceAggregation_Contents"></a>

 ** scanArn **   <a name="inspector2-Type-CisTargetResourceAggregation-scanArn"></a>
The scan ARN for the CIS target resource.
Type: String
Pattern: `arn:aws(-us-gov|-cn)?:inspector2:[-.a-z0-9]{0,20}:\d{12}:owner/(\d{12}|o-[a-z0-9]{10,32})/cis-scan/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** accountId **   <a name="inspector2-Type-CisTargetResourceAggregation-accountId"></a>
The account ID for the CIS target resource.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** platform **   <a name="inspector2-Type-CisTargetResourceAggregation-platform"></a>
The platform for the CIS target resource.
Type: String
Required: No

 ** statusCounts **   <a name="inspector2-Type-CisTargetResourceAggregation-statusCounts"></a>
The target resource status counts.
Type: [StatusCounts](API_StatusCounts.md) object
Required: No

 ** targetResourceId **   <a name="inspector2-Type-CisTargetResourceAggregation-targetResourceId"></a>
The ID of the target resource.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `.*(^arn:.*:ecr:.*:\d{12}:repository\/[a-zA-Z0-9._\/-]+(\/sha256:[a-z0-9]{64})?$)|(^i-([a-z0-9]{8}|[a-z0-9]{17}|\\*)$|(^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$)|(^arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}\/project-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$))|(^\/subscriptions\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\/resourcegroups\/[a-z0-9_\-\.()]+\/providers\/(microsoft\.compute\/virtualmachines\/[a-z0-9_\-]+|microsoft\.web\/sites\/[a-z0-9_\-]+|microsoft\.containerregistry\/registries\/[a-z0-9_\-]+(\/repositories\/[a-z0-9_\-\/]+\/images?\/sha256:[a-f0-9]{64})?)$).*`
Required: No

 ** targetResourceTags **   <a name="inspector2-Type-CisTargetResourceAggregation-targetResourceTags"></a>
The tag for the target resource.
Type: String to array of strings map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{Z}\p{N}_.:/=\-@]*`
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** targetStatus **   <a name="inspector2-Type-CisTargetResourceAggregation-targetStatus"></a>
The status of the target resource.
Type: String
Valid Values: `TIMED_OUT | CANCELLED | COMPLETED`
Required: No

 ** targetStatusReason **   <a name="inspector2-Type-CisTargetResourceAggregation-targetStatusReason"></a>
The reason for the target resource.
Type: String
Valid Values: `SCAN_IN_PROGRESS | UNSUPPORTED_OS | SSM_UNMANAGED`
Required: No

## See Also
<a name="API_CisTargetResourceAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CisTargetResourceAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CisTargetResourceAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CisTargetResourceAggregation)

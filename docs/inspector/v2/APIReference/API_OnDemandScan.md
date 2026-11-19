---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_OnDemandScan.html
---

# OnDemandScan

Details of a single on-demand scan of a resource.

## Contents
<a name="API_OnDemandScan_Contents"></a>

 ** resourceId **   <a name="inspector2-Type-OnDemandScan-resourceId"></a>
The ID of the resource that was scanned.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `.*(^arn:.*:ecr:.*:\d{12}:repository\/[a-zA-Z0-9._\/-]+(\/sha256:[a-z0-9]{64})?$)|(^i-([a-z0-9]{8}|[a-z0-9]{17}|\\*)$|(^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$)|(^arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}\/project-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$))|(^\/subscriptions\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\/resourcegroups\/[a-z0-9_\-\.()]+\/providers\/(microsoft\.compute\/virtualmachines\/[a-z0-9_\-]+|microsoft\.web\/sites\/[a-z0-9_\-]+|microsoft\.containerregistry\/registries\/[a-z0-9_\-]+(\/repositories\/[a-z0-9_\-\/]+\/images?\/sha256:[a-f0-9]{64})?)$).*`
Required: Yes

 ** resourceType **   <a name="inspector2-Type-OnDemandScan-resourceType"></a>
The type of the resource that was scanned.
Type: String
Valid Values: `AMI`
Required: Yes

 ** scanId **   <a name="inspector2-Type-OnDemandScan-scanId"></a>
The unique identifier of the on-demand scan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** scanStatus **   <a name="inspector2-Type-OnDemandScan-scanStatus"></a>
The current status of the on-demand scan.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED`
Required: Yes

 ** startedAt **   <a name="inspector2-Type-OnDemandScan-startedAt"></a>
The date and time, in ISO 8601 format, when the on-demand scan started.
Type: Timestamp
Required: Yes

 ** completedAt **   <a name="inspector2-Type-OnDemandScan-completedAt"></a>
The date and time, in ISO 8601 format, when the on-demand scan completed. This field is absent if the scan has not completed.
Type: Timestamp
Required: No

 ** scanStatusReason **   <a name="inspector2-Type-OnDemandScan-scanStatusReason"></a>
The reason associated with the current on-demand scan status.
Type: String
Valid Values: `ACCESS_DENIED | INTERNAL_ERROR | STORAGE_LIMIT_EXCEEDED | EXTRACTION_COLLECTION_TIME_LIMIT_EXCEEDED | UNSUPPORTED_OS | RESOURCE_TERMINATED`
Required: No

## See Also
<a name="API_OnDemandScan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/OnDemandScan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/OnDemandScan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/OnDemandScan)

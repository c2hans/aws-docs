---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationVersionSummary.html
---

# ApplicationVersionSummary
<a name="API_ApplicationVersionSummary"></a>

The summary of the application version.

## Contents
<a name="API_ApplicationVersionSummary_Contents"></a>

 ** ApplicationStatus **   <a name="APIReference-Type-ApplicationVersionSummary-ApplicationStatus"></a>
The status of the application.
Type: String
Valid Values: `DELETING | STARTING | STOPPING | READY | RUNNING | UPDATING | AUTOSCALING | FORCE_STOPPING | ROLLING_BACK | MAINTENANCE | ROLLED_BACK`
Required: Yes

 ** ApplicationVersionId **   <a name="APIReference-Type-ApplicationVersionSummary-ApplicationVersionId"></a>
The ID of the application version. Managed Service for Apache Flink updates the `ApplicationVersionId` each time you update the application.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 999999999.
Required: Yes

## See Also
<a name="API_ApplicationVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationVersionSummary)

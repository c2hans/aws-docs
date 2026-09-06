---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_TargetAction.html
---

# TargetAction
<a name="API_TargetAction"></a>

A JSON format string of the Amazon Redshift Serverless API operation with input parameters. The following is an example of a target action.

 `"{"CreateSnapshot": {"NamespaceName": "sampleNamespace","SnapshotName": "sampleSnapshot", "retentionPeriod": "1"}}"`

## Contents
<a name="API_TargetAction_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** createSnapshot **   <a name="redshiftserverless-Type-TargetAction-createSnapshot"></a>
The parameters that you can use to configure a [scheduled action](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateScheduledAction.html) to create a snapshot. For more information about creating a scheduled action, see [CreateScheduledAction](https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_CreateScheduledAction.html).
Type: [CreateSnapshotScheduleActionParameters](API_CreateSnapshotScheduleActionParameters.md) object
Required: No

## See Also
<a name="API_TargetAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/TargetAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/TargetAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/TargetAction)

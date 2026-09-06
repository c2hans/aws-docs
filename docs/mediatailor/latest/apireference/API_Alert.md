---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_Alert.html
---

# Alert
<a name="API_Alert"></a>

Alert configuration parameters.

## Contents
<a name="API_Alert_Contents"></a>

 ** AlertCode **   <a name="mediatailor-Type-Alert-AlertCode"></a>
The code for the alert. For example, `NOT_PROCESSED`.
Type: String
Required: Yes

 ** AlertMessage **   <a name="mediatailor-Type-Alert-AlertMessage"></a>
If an alert is generated for a resource, an explanation of the reason for the alert.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="mediatailor-Type-Alert-LastModifiedTime"></a>
The timestamp when the alert was last modified.
Type: Timestamp
Required: Yes

 ** RelatedResourceArns **   <a name="mediatailor-Type-Alert-RelatedResourceArns"></a>
The Amazon Resource Names (ARNs) related to this alert.
Type: Array of strings
Required: Yes

 ** ResourceArn **   <a name="mediatailor-Type-Alert-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: Yes

 ** Category **   <a name="mediatailor-Type-Alert-Category"></a>
The category that MediaTailor assigns to the alert.
Type: String
Valid Values: `SCHEDULING_ERROR | PLAYBACK_WARNING | INFO`
Required: No

## See Also
<a name="API_Alert_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/Alert)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/Alert)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/Alert)

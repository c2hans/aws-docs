---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_LiveResourceDrift.html
---

# LiveResourceDrift
<a name="API_LiveResourceDrift"></a>

Contains drift information for a resource property, including actual value, previous deployment value, and drift detection timestamp.

## Contents
<a name="API_LiveResourceDrift_Contents"></a>

 ** ActualValue **
The current live configuration value of the resource property.
Type: String
Required: No

 ** DriftDetectionTimestamp **
The timestamp when drift was detected for this resource property.
Type: Timestamp
Required: No

 ** PreviousValue **
The configuration value from the previous CloudFormation deployment.
Type: String
Required: No

## See Also
<a name="API_LiveResourceDrift_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/LiveResourceDrift)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/LiveResourceDrift)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/LiveResourceDrift)

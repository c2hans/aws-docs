---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnsuccessfulSuppressionResponseObject.html
---

# UnsuccessfulSuppressionResponseObject
<a name="API_UnsuccessfulSuppressionResponseObject"></a>

Describes an unsuccessful application status check suppression.

## Contents
<a name="API_UnsuccessfulSuppressionResponseObject_Contents"></a>

 ** instanceId **
The ID of the instance.
Type: String
Required: No

 ** reason **
The reason the suppression failed.
Type: String
Required: No

 ** resumeAt **
The date and time when health checks would have resumed.
Type: Timestamp
Required: No

 ** suppressAt **
The date and time when suppression was attempted.
Type: Timestamp
Required: No

## See Also
<a name="API_UnsuccessfulSuppressionResponseObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/UnsuccessfulSuppressionResponseObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/UnsuccessfulSuppressionResponseObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/UnsuccessfulSuppressionResponseObject)

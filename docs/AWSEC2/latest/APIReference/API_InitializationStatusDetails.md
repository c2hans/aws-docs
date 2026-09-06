---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InitializationStatusDetails.html
---

# InitializationStatusDetails
<a name="API_InitializationStatusDetails"></a>

Information about the volume initialization. For more information, see [Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html).

## Contents
<a name="API_InitializationStatusDetails_Contents"></a>

 ** estimatedTimeToCompleteInSeconds **
The estimated remaining time, in seconds, for volume initialization to complete. Returns `0` when volume initialization has completed.
Only available for volumes created with Amazon EBS Provisioned Rate for Volume Initialization.
Type: Long
Required: No

 ** initializationType **
The method used for volume initialization. Possible values include:
+  `default` - Volume initialized using the default volume initialization rate or fast snapshot restore.
+  `provisioned-rate` - Volume initialized using an Amazon EBS Provisioned Rate for Volume Initialization.
+  `volume-copy` - Volume copy initialized at the rate for volume copies.
Type: String
Valid Values: `default | provisioned-rate | volume-copy`
Required: No

 ** progress **
The current volume initialization progress as a percentage (0-100). Returns `100` when volume initialization has completed.
Type: Long
Required: No

## See Also
<a name="API_InitializationStatusDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InitializationStatusDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InitializationStatusDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InitializationStatusDetails)

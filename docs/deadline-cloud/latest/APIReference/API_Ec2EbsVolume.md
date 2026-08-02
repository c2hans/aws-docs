---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Ec2EbsVolume.html
---

# Ec2EbsVolume
<a name="API_Ec2EbsVolume"></a>

Specifies the EBS volume.

## Contents
<a name="API_Ec2EbsVolume_Contents"></a>

 ** iops **   <a name="deadlinecloud-Type-Ec2EbsVolume-iops"></a>
The IOPS per volume.
Type: Integer
Valid Range: Minimum value of 3000. Maximum value of 16000.
Required: No

 ** sizeGiB **   <a name="deadlinecloud-Type-Ec2EbsVolume-sizeGiB"></a>
The EBS volume size in GiB.
Type: Integer
Required: No

 ** throughputMiB **   <a name="deadlinecloud-Type-Ec2EbsVolume-throughputMiB"></a>
The throughput per volume in MiB.
Type: Integer
Valid Range: Minimum value of 125. Maximum value of 1000.
Required: No

## See Also
<a name="API_Ec2EbsVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/Ec2EbsVolume)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/Ec2EbsVolume)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/Ec2EbsVolume)

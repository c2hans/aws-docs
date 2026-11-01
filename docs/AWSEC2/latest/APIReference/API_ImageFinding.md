---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImageFinding.html
---

# ImageFinding
<a name="API_ImageFinding"></a>

Describes an Amazon Inspector vulnerability finding for an AMI.

## Contents
<a name="API_ImageFinding_Contents"></a>

 ** firstObservedAt **
The date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), when Amazon Inspector first observed the finding.
Type: Timestamp
Required: No

 ** fixAvailable **
Specifies whether a fix is available for the finding. This value is `true` when Amazon Inspector reports a full or partial fix for the finding.
Type: Boolean
Required: No

 ** PathSet.N **
The file paths in the AMI that are affected by the finding. Amazon EC2 returns up to 10 file paths for each finding.
Type: Array of strings
Required: No

 ** score **
The Amazon Inspector score for the finding.
Type: Double
Required: No

 ** severityLabel **
The severity of the finding.
The valid values are the following Amazon Inspector severity levels, which correspond to CVSS score ranges:
+  `informational` - CVSS score of 0.
+  `low` - CVSS score of 0.1 to 3.9.
+  `medium` - CVSS score of 4.0 to 6.9.
+  `high` - CVSS score of 7.0 to 8.9.
+  `critical` - CVSS score of 9.0 to 10.0.
For more information, see [Software package vulnerability severity](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html#findings-understanding-package-score) in the *Amazon Inspector User Guide*.
Type: String
Valid Values: `informational | low | medium | high | critical`
Required: No

 ** snapshotId **
The ID of the Amazon EBS snapshot of the AMI in which the finding was detected.
Type: String
Required: No

 ** title **
The title of the finding.
Type: String
Required: No

 ** updatedAt **
The date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), when Amazon Inspector last updated the finding.
Type: Timestamp
Required: No

## See Also
<a name="API_ImageFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ImageFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ImageFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ImageFinding)

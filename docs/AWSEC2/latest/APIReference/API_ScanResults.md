---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ScanResults.html
---

# ScanResults
<a name="API_ScanResults"></a>

The Amazon Inspector scan results for an AMI. This information is present only for AMIs that Amazon Inspector has scanned.

When you share an AMI with other accounts, organizations, or organizational units (OUs), or make it public, its scan results are available to the accounts that can use the AMI.

The fix-available dates are specific to the AMI. Each date reflects when a fix became available for a finding on that AMI, not when the vendor released the fix. As a result, a date can be later than the vendor's release date, and AMIs with the same vulnerability can have different dates.

## Contents
<a name="API_ScanResults_Contents"></a>

 ** criticalFixAvailableSince **
The earliest date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), at which Amazon Inspector reported a fix as available for a `critical` severity finding on the AMI. This value is present only if the AMI has at least one `critical` severity finding with a fix available. Amazon Inspector recomputes this value on each scan.
Type: Timestamp
Required: No

 ** findingScanDate **
The date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), of the most recent Amazon Inspector scan of the AMI.
Type: Timestamp
Required: No

 ** highestFindingSeverityLabel **
The highest severity among the AMI's Amazon Inspector findings, whether or not a fix is available.
The valid values are the following Amazon Inspector severity levels, which correspond to CVSS score ranges:
+  `informational` - CVSS score of 0.
+  `low` - CVSS score of 0.1 to 3.9.
+  `medium` - CVSS score of 4.0 to 6.9.
+  `high` - CVSS score of 7.0 to 8.9.
+  `critical` - CVSS score of 9.0 to 10.0.
For more information, see [Software package vulnerability severity](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html#findings-understanding-package-score) in the *Amazon Inspector User Guide*.
This value is present only if the AMI has at least one finding.
Type: String
Valid Values: `informational | low | medium | high | critical`
Required: No

 ** highFixAvailableSince **
The earliest date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), at which Amazon Inspector reported a fix as available for a `high` severity finding on the AMI. This value is present only if the AMI has at least one `high` severity finding with a fix available. Amazon Inspector recomputes this value on each scan.
Type: Timestamp
Required: No

 ** informationalFixAvailableSince **
The earliest date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), at which Amazon Inspector reported a fix as available for an `informational` severity finding on the AMI. This value is present only if the AMI has at least one `informational` severity finding with a fix available. Amazon Inspector recomputes this value on each scan.
Type: Timestamp
Required: No

 ** lowFixAvailableSince **
The earliest date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), at which Amazon Inspector reported a fix as available for a `low` severity finding on the AMI. This value is present only if the AMI has at least one `low` severity finding with a fix available. Amazon Inspector recomputes this value on each scan.
Type: Timestamp
Required: No

 ** mediumFixAvailableSince **
The earliest date and time, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), at which Amazon Inspector reported a fix as available for a `medium` severity finding on the AMI. This value is present only if the AMI has at least one `medium` severity finding with a fix available. Amazon Inspector recomputes this value on each scan.
Type: Timestamp
Required: No

## See Also
<a name="API_ScanResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ScanResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ScanResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ScanResults)

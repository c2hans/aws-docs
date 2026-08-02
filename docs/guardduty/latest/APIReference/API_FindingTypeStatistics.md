---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FindingTypeStatistics.html
---

# FindingTypeStatistics
<a name="API_FindingTypeStatistics"></a>

Information about each finding type associated with the `groupedByFindingType` statistics.

## Contents
<a name="API_FindingTypeStatistics_Contents"></a>

 ** findingType **   <a name="guardduty-Type-FindingTypeStatistics-findingType"></a>
Name of the finding type.
Type: String
Required: No

 ** lastGeneratedAt **   <a name="guardduty-Type-FindingTypeStatistics-lastGeneratedAt"></a>
The timestamp at which this finding type was last generated in your environment.
Type: Timestamp
Required: No

 ** totalFindings **   <a name="guardduty-Type-FindingTypeStatistics-totalFindings"></a>
The total number of findings associated with generated for each distinct finding type.
Type: Integer
Required: No

## See Also
<a name="API_FindingTypeStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FindingTypeStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FindingTypeStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FindingTypeStatistics)

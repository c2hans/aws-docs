---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_FindingsStatistics.html
---

# FindingsStatistics
<a name="API_FindingsStatistics"></a>

Contains information about the aggregate statistics for an external or unused access analyzer. Only one parameter can be used in a `FindingsStatistics` object.

## Contents
<a name="API_FindingsStatistics_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** externalAccessFindingsStatistics **   <a name="accessanalyzer-Type-FindingsStatistics-externalAccessFindingsStatistics"></a>
The aggregate statistics for an external access analyzer.
Type: [ExternalAccessFindingsStatistics](API_ExternalAccessFindingsStatistics.md) object
Required: No

 ** internalAccessFindingsStatistics **   <a name="accessanalyzer-Type-FindingsStatistics-internalAccessFindingsStatistics"></a>
The aggregate statistics for an internal access analyzer. This includes information about active, archived, and resolved findings related to internal access within your AWS organization or account.
Type: [InternalAccessFindingsStatistics](API_InternalAccessFindingsStatistics.md) object
Required: No

 ** unusedAccessFindingsStatistics **   <a name="accessanalyzer-Type-FindingsStatistics-unusedAccessFindingsStatistics"></a>
The aggregate statistics for an unused access analyzer.
Type: [UnusedAccessFindingsStatistics](API_UnusedAccessFindingsStatistics.md) object
Required: No

## See Also
<a name="API_FindingsStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/FindingsStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/FindingsStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/FindingsStatistics)

---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_FixtureSummary.html
---

# FixtureSummary
<a name="API_FixtureSummary"></a>

Contains information about one fixture. It is used in the SearchFixtures response.

Elemental Inference relays the information in this structure from the data source, so that you can identify the fixture that matches your source media.

## Contents
<a name="API_FixtureSummary_Contents"></a>

 ** competitors **   <a name="elementalinference-Type-FixtureSummary-competitors"></a>
An array of the competitors (the teams or individuals) in the fixture.
Type: Array of [Competitor](API_Competitor.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: Yes

 ** fixtureId **   <a name="elementalinference-Type-FixtureSummary-fixtureId"></a>
The ID of the fixture. Specify this ID in the clipping output of a feed, to identify the fixture whose event data you want Elemental Inference to map onto the clipping metadata.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** name **   <a name="elementalinference-Type-FixtureSummary-name"></a>
The name of the fixture, as provided by the data source. For example, the names of the two competing teams.
Type: String
Required: Yes

 ** status **   <a name="elementalinference-Type-FixtureSummary-status"></a>
The status of the fixture in its lifecycle, as provided by the data source. For example, Scheduled or Completed.
Type: String
Required: Yes

 ** fixtureGroup **   <a name="elementalinference-Type-FixtureSummary-fixtureGroup"></a>
The group that the fixture belongs to, such as the competition, league, or tournament. The data source doesn't provide this information for every fixture.
Type: String
Required: No

 ** scheduledStart **   <a name="elementalinference-Type-FixtureSummary-scheduledStart"></a>
The scheduled start time of the fixture, as provided by the data source. The actual start time might differ.
Type: Timestamp
Required: No

## See Also
<a name="API_FixtureSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/FixtureSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/FixtureSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/FixtureSummary)

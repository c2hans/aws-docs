---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_MatchScoreDetails.html
---

# MatchScoreDetails
<a name="API_geoplaces_MatchScoreDetails"></a>

Details related to the match score.

## Contents
<a name="API_geoplaces_MatchScoreDetails_Contents"></a>

 ** Components **   <a name="location-Type-geoplaces_MatchScoreDetails-Components"></a>
Indicates how well the component input matches the returned. It is equal to 1 if all input tokens are recognized and matched.
Type: [ComponentMatchScores](API_geoplaces_ComponentMatchScores.md) object
Required: No

 ** Overall **   <a name="location-Type-geoplaces_MatchScoreDetails-Overall"></a>
Indicates how well the entire input matches the returned. It is equal to 1 if all input tokens are recognized and matched.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_geoplaces_MatchScoreDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/MatchScoreDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/MatchScoreDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/MatchScoreDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

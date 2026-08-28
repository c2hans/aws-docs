---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_AvailMatchingCriteria.html
---

# AvailMatchingCriteria
<a name="API_AvailMatchingCriteria"></a>

MediaTailor only places (consumes) prefetched ads if the ad break meets the criteria defined by the dynamic variables. This gives you granular control over which ad break to place the prefetched ads into.

As an example, let's say that you set `DynamicVariable` to `scte.event_id` and `Operator` to `EQUALS`, and your playback configuration has an ADS URL of `https://my.ads.server.com/path?&podId=[scte.avail_num]&event=[scte.event_id]&duration=[session.avail_duration_secs]`. And the prefetch request to the ADS contains these values `https://my.ads.server.com/path?&podId=3&event=my-awesome-event&duration=30`. MediaTailor will only insert the prefetched ads into the ad break if has a SCTE marker with an event id of `my-awesome-event`, since it must match the event id that MediaTailor uses to query the ADS.

You can specify up to five `AvailMatchingCriteria`. If you specify multiple `AvailMatchingCriteria`, MediaTailor combines them to match using a logical `AND`. You can model logical `OR` combinations by creating multiple prefetch schedules.

## Contents
<a name="API_AvailMatchingCriteria_Contents"></a>

 ** DynamicVariable **   <a name="mediatailor-Type-AvailMatchingCriteria-DynamicVariable"></a>
The dynamic variable(s) that MediaTailor should use as avail matching criteria. MediaTailor only places the prefetched ads into the avail if the avail matches the criteria defined by the dynamic variable. For information about dynamic variables, see [Using dynamic ad variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables.html) in the *MediaTailor User Guide*.
You can include up to 100 dynamic variables.
Type: String
Required: Yes

 ** Operator **   <a name="mediatailor-Type-AvailMatchingCriteria-Operator"></a>
For the `DynamicVariable` specified in `AvailMatchingCriteria`, the Operator that is used for the comparison.
Type: String
Valid Values: `EQUALS`
Required: Yes

## See Also
<a name="API_AvailMatchingCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/AvailMatchingCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/AvailMatchingCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/AvailMatchingCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

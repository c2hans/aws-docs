---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_GremlinQueryStatus.html
---

# GremlinQueryStatus
<a name="API_GremlinQueryStatus"></a>

Captures the status of a Gremlin query (see the [Gremlin query status API](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status.html) page).

## Contents
<a name="API_GremlinQueryStatus_Contents"></a>

 ** queryEvalStats **   <a name="neptunedata-Type-GremlinQueryStatus-queryEvalStats"></a>
The query statistics of the Gremlin query.
Type: [QueryEvalStats](API_QueryEvalStats.md) object
Required: No

 ** queryId **   <a name="neptunedata-Type-GremlinQueryStatus-queryId"></a>
The ID of the Gremlin query.
Type: String
Required: No

 ** queryString **   <a name="neptunedata-Type-GremlinQueryStatus-queryString"></a>
The query string of the Gremlin query.
Type: String
Required: No

## See Also
<a name="API_GremlinQueryStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/GremlinQueryStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/GremlinQueryStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/GremlinQueryStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Neptune Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

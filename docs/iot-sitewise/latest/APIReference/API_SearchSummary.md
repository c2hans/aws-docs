---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_SearchSummary.html
---

# SearchSummary
<a name="API_SearchSummary"></a>

A summary of a single search as returned by ListSearches.

## Contents
<a name="API_SearchSummary_Contents"></a>

 ** queryStatement **   <a name="iotsitewise-Type-SearchSummary-queryStatement"></a>
The natural-language query that was submitted for the search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Required: Yes

 ** searchId **   <a name="iotsitewise-Type-SearchSummary-searchId"></a>
The unique identifier of the search.
Type: String
Length Constraints: Minimum length of 23. Maximum length of 36.
Pattern: `[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*`
Required: Yes

 ** searchType **   <a name="iotsitewise-Type-SearchSummary-searchType"></a>
The search strategy used for the search.
Type: String
Valid Values: `DEEP | QUICK`
Required: Yes

 ** status **   <a name="iotsitewise-Type-SearchSummary-status"></a>
The current status of the search.
Type: String
Valid Values: `QUEUED | RUNNING | SUCCEEDED | FAILED`
Required: Yes

 ** workspaceName **   <a name="iotsitewise-Type-SearchSummary-workspaceName"></a>
The name of the workspace the search runs against.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** groupId **   <a name="iotsitewise-Type-SearchSummary-groupId"></a>
The group identifier associated with the search, if one was supplied on the request.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`
Required: No

 ** startedAt **   <a name="iotsitewise-Type-SearchSummary-startedAt"></a>
The time at which the search was started.
Type: Timestamp
Required: No

 ** statusReason **   <a name="iotsitewise-Type-SearchSummary-statusReason"></a>
A human-readable explanation of the current status. Populated when the search has `FAILED`.
Type: String
Required: No

## See Also
<a name="API_SearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/SearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/SearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/SearchSummary)

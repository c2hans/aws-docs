---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListTestGridSessionsRequest.html
---

# ListTestGridSessionsRequest
<a name="API_ListTestGridSessionsRequest"></a>

## Contents
<a name="API_ListTestGridSessionsRequest_Contents"></a>

 ** projectArn **   <a name="devicefarm-Type-ListTestGridSessionsRequest-projectArn"></a>
ARN of a [TestGridProject](API_TestGridProject.md).
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** creationTimeAfter **   <a name="devicefarm-Type-ListTestGridSessionsRequest-creationTimeAfter"></a>
Return only sessions created after this time.
Type: Timestamp
Required: No

 ** creationTimeBefore **   <a name="devicefarm-Type-ListTestGridSessionsRequest-creationTimeBefore"></a>
Return only sessions created before this time.
Type: Timestamp
Required: No

 ** endTimeAfter **   <a name="devicefarm-Type-ListTestGridSessionsRequest-endTimeAfter"></a>
Return only sessions that ended after this time.
Type: Timestamp
Required: No

 ** endTimeBefore **   <a name="devicefarm-Type-ListTestGridSessionsRequest-endTimeBefore"></a>
Return only sessions that ended before this time.
Type: Timestamp
Required: No

 ** maxResult **   <a name="devicefarm-Type-ListTestGridSessionsRequest-maxResult"></a>
Return only this many results at a time.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** nextToken **   <a name="devicefarm-Type-ListTestGridSessionsRequest-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

 ** status **   <a name="devicefarm-Type-ListTestGridSessionsRequest-status"></a>
Return only sessions in this state.
Type: String
Valid Values: `ACTIVE | CLOSED | ERRORED`
Required: No

## See Also
<a name="API_ListTestGridSessionsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListTestGridSessionsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListTestGridSessionsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListTestGridSessionsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

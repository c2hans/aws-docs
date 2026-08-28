---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedQuerySummary.html
---

# ProtectedQuerySummary
<a name="API_ProtectedQuerySummary"></a>

The protected query summary for the objects listed by the request.

## Contents
<a name="API_ProtectedQuerySummary_Contents"></a>

 ** createTime **   <a name="API-Type-ProtectedQuerySummary-createTime"></a>
The time the protected query was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-ProtectedQuerySummary-id"></a>
The unique ID of the protected query.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-ProtectedQuerySummary-membershipArn"></a>
The unique ARN for the membership that initiated the protected query.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-ProtectedQuerySummary-membershipId"></a>
The unique ID for the membership that initiated the protected query.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** receiverConfigurations **   <a name="API-Type-ProtectedQuerySummary-receiverConfigurations"></a>
 The receiver configuration.
Type: Array of [ReceiverConfiguration](API_ReceiverConfiguration.md) objects
Required: Yes

 ** status **   <a name="API-Type-ProtectedQuerySummary-status"></a>
The status of the protected query.
Type: String
Valid Values: `SUBMITTED | STARTED | CANCELLED | CANCELLING | FAILED | SUCCESS | TIMED_OUT`
Required: Yes

 ** intermediateTableConfiguration **   <a name="API-Type-ProtectedQuerySummary-intermediateTableConfiguration"></a>
The intermediate table configuration, present when the protected query was triggered by a populate operation.
Type: [IntermediateTableOutputConfiguration](API_IntermediateTableOutputConfiguration.md) object
Required: No

 ** queryComputePayerAccountId **   <a name="API-Type-ProtectedQuerySummary-queryComputePayerAccountId"></a>
The account ID of the member that pays for the query compute costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: No

## See Also
<a name="API_ProtectedQuerySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedQuerySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedQuerySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedQuerySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

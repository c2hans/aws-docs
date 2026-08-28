---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_ConnectionSummary.html
---

# ConnectionSummary
<a name="API_account_ConnectionSummary"></a>

A summary view of an active connection between partners containing key information.

## Contents
<a name="API_account_ConnectionSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="AWSPartnerCentral-Type-account_ConnectionSummary-Arn"></a>
The Amazon Resource Name (ARN) of the connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:[a-zA-Z0-9-]+:partnercentral:[a-z0-9\-]*::catalog/[a-zA-Z]+/connection/pac-[A-Za-z0-9]{13}`
Required: Yes

 ** Catalog **   <a name="AWSPartnerCentral-Type-account_ConnectionSummary-Catalog"></a>
The catalog identifier where the connection exists.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** ConnectionTypes **   <a name="AWSPartnerCentral-Type-account_ConnectionSummary-ConnectionTypes"></a>
A map of connection types and their summary information for this connection.
Type: String to [ConnectionTypeSummary](API_account_ConnectionTypeSummary.md) object map
Valid Keys: `OPPORTUNITY_COLLABORATION | SUBSIDIARY`
Required: Yes

 ** Id **   <a name="AWSPartnerCentral-Type-account_ConnectionSummary-Id"></a>
The unique identifier of the connection.
Type: String
Pattern: `pac-[A-Za-z0-9]{13}`
Required: Yes

 ** OtherParticipantAccountId **   <a name="AWSPartnerCentral-Type-account_ConnectionSummary-OtherParticipantAccountId"></a>
The AWS account ID of the other participant in the connection.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** UpdatedAt **   <a name="AWSPartnerCentral-Type-account_ConnectionSummary-UpdatedAt"></a>
The timestamp when the connection was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_account_ConnectionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/ConnectionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/ConnectionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/ConnectionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

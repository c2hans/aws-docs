---
source_url: https://docs.aws.amazon.com/connect-outbound/latest/APIReference/API_DialRequest.html
---

# DialRequest
<a name="API_connect-outbound-campaigns_DialRequest"></a>

Contains information about a dial request.

## Contents
<a name="API_connect-outbound-campaigns_DialRequest_Contents"></a>

 ** attributes **   <a name="connect-Type-connect-outbound-campaigns_DialRequest-attributes"></a>
Attributes for a dial request. In addition to the Value Length Constraints listed below, note the Value Pattern: `^.*$`
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 32767.
Key Pattern: `[a-zA-Z0-9\-_]+`
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Value Pattern: `.*`
Required: Yes

 ** clientToken **   <a name="connect-Type-connect-outbound-campaigns_DialRequest-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/). The token is valid for 7 days after creation. If a dial request is already created, the dial request ID is returned.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[a-zA-Z0-9_\-.]*`
Required: Yes

 ** expirationTime **   <a name="connect-Type-connect-outbound-campaigns_DialRequest-expirationTime"></a>
A UTC timestamp in date-time format that specifies when a dial request expires.
Value Constraints: Minimum value of 30 seconds from now. Maximum value of 900 seconds (15 minutes) from now.
Example: 2024-12-05T19:35:00.000Z
Type: Timestamp
Required: Yes

 ** phoneNumber **   <a name="connect-Type-connect-outbound-campaigns_DialRequest-phoneNumber"></a>
The phone number to dial.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Pattern: `[\d\-+]*`
Required: Yes

## See Also
<a name="API_connect-outbound-campaigns_DialRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaigns-2021-01-30/DialRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaigns-2021-01-30/DialRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaigns-2021-01-30/DialRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

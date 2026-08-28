---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactDataRequest.html
---

# ContactDataRequest
<a name="API_ContactDataRequest"></a>

Request object with information to create a contact.

## Contents
<a name="API_ContactDataRequest_Contents"></a>

 ** Attributes **   <a name="connect-Type-ContactDataRequest-Attributes"></a>
List of attributes to be stored in a contact.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** Campaign **   <a name="connect-Type-ContactDataRequest-Campaign"></a>
Structure to store information associated with a campaign.
Type: [Campaign](API_Campaign.md) object
Required: No

 ** CustomerEndpoint **   <a name="connect-Type-ContactDataRequest-CustomerEndpoint"></a>
Endpoint of the customer for which contact will be initiated.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** OutboundStrategy **   <a name="connect-Type-ContactDataRequest-OutboundStrategy"></a>
Information about the outbound strategy.
Type: [OutboundStrategy](API_OutboundStrategy.md) object
Required: No

 ** QueueId **   <a name="connect-Type-ContactDataRequest-QueueId"></a>
The identifier of the queue associated with the Connect Customer instance in which contacts that are created will be queued.
Type: String
Required: No

 ** RequestIdentifier **   <a name="connect-Type-ContactDataRequest-RequestIdentifier"></a>
Identifier to uniquely identify individual requests in the batch.
Type: String
Length Constraints: Maximum length of 80.
Required: No

 ** SystemEndpoint **   <a name="connect-Type-ContactDataRequest-SystemEndpoint"></a>
Endpoint associated with the Connect Customer instance from which outbound contact will be initiated for the campaign.
Type: [Endpoint](API_Endpoint.md) object
Required: No

## See Also
<a name="API_ContactDataRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactDataRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactDataRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactDataRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

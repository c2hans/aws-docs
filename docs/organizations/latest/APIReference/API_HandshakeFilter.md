---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_HandshakeFilter.html
---

# HandshakeFilter
<a name="API_HandshakeFilter"></a>

Contains the filter used to select the handshakes for an operation.

## Contents
<a name="API_HandshakeFilter_Contents"></a>

 ** ActionType **   <a name="organizations-Type-HandshakeFilter-ActionType"></a>
The type of handshake.
If you specify `ActionType`, you cannot also specify `ParentHandshakeId`.
Type: String
Valid Values: `INVITE | ENABLE_ALL_FEATURES | APPROVE_ALL_FEATURES | ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE | TRANSFER_RESPONSIBILITY`
Required: No

 ** ParentHandshakeId **   <a name="organizations-Type-HandshakeFilter-ParentHandshakeId"></a>
The parent handshake. Only used for handshake types that are a child of another type.
If you specify `ParentHandshakeId`, you cannot also specify `ActionType`.
The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID string requires "h-" followed by from 8 to 32 lowercase letters or digits.
Type: String
Length Constraints: Maximum length of 34.
Pattern: `^h-[0-9a-z]{8,32}$`
Required: No

## See Also
<a name="API_HandshakeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/HandshakeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/HandshakeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/HandshakeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

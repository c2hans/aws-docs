---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_InstanceSummary.html
---

# InstanceSummary
<a name="API_InstanceSummary"></a>

Information about the instance.

## Contents
<a name="API_InstanceSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-InstanceSummary-Arn"></a>
The Amazon Resource Name (ARN) of the instance.
Type: String
Required: No

 ** CreatedTime **   <a name="connect-Type-InstanceSummary-CreatedTime"></a>
When the instance was created.
Type: Timestamp
Required: No

 ** Id **   <a name="connect-Type-InstanceSummary-Id"></a>
The identifier of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** IdentityManagementType **   <a name="connect-Type-InstanceSummary-IdentityManagementType"></a>
The identity management type of the instance.
Type: String
Valid Values: `SAML | CONNECT_MANAGED | EXISTING_DIRECTORY`
Required: No

 ** InboundCallsEnabled **   <a name="connect-Type-InstanceSummary-InboundCallsEnabled"></a>
Whether inbound calls are enabled.
Type: Boolean
Required: No

 ** InstanceAccessUrl **   <a name="connect-Type-InstanceSummary-InstanceAccessUrl"></a>
This URL allows contact center users to access the Connect Customer admin website.
Type: String
Required: No

 ** InstanceAlias **   <a name="connect-Type-InstanceSummary-InstanceAlias"></a>
The alias of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 45.
Pattern: `^(?!d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*$`
Required: No

 ** InstanceStatus **   <a name="connect-Type-InstanceSummary-InstanceStatus"></a>
The state of the instance.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | CREATION_FAILED`
Required: No

 ** OutboundCallsEnabled **   <a name="connect-Type-InstanceSummary-OutboundCallsEnabled"></a>
Whether outbound calls are enabled.
Type: Boolean
Required: No

 ** ServiceRole **   <a name="connect-Type-InstanceSummary-ServiceRole"></a>
The service role of the instance.
Type: String
Required: No

## See Also
<a name="API_InstanceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/InstanceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/InstanceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/InstanceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

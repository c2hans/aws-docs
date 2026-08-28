---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlow.html
---

# ContactFlow
<a name="API_ContactFlow"></a>

Contains information about a flow.

## Contents
<a name="API_ContactFlow_Contents"></a>

 ** Arn **   <a name="connect-Type-ContactFlow-Arn"></a>
The Amazon Resource Name (ARN) of the flow.
Type: String
Required: No

 ** Content **   <a name="connect-Type-ContactFlow-Content"></a>
The JSON string that represents the content of the flow. For an example, see [Example flow in Connect Customer Flow language](https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html).
Length Constraints: Minimum length of 1. Maximum length of 256000.
Type: String
Required: No

 ** Description **   <a name="connect-Type-ContactFlow-Description"></a>
The description of the flow.
Type: String
Required: No

 ** FlowContentSha256 **   <a name="connect-Type-ContactFlow-FlowContentSha256"></a>
Indicates the checksum value of the flow content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]{64}$`
Required: No

 ** Id **   <a name="connect-Type-ContactFlow-Id"></a>
The identifier of the flow.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-ContactFlow-LastModifiedRegion"></a>
The region in which the flow was last modified
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-ContactFlow-LastModifiedTime"></a>
The time at which the flow was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-ContactFlow-Name"></a>
The name of the flow.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** State **   <a name="connect-Type-ContactFlow-State"></a>
The type of flow.
Type: String
Valid Values: `ACTIVE | ARCHIVED`
Required: No

 ** Status **   <a name="connect-Type-ContactFlow-Status"></a>
The status of the flow.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** Tags **   <a name="connect-Type-ContactFlow-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** Type **   <a name="connect-Type-ContactFlow-Type"></a>
The type of the flow. For descriptions of the available types, see [Choose a flow type](https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types) in the *Connect Customer Administrator Guide*.
Type: String
Valid Values: `CONTACT_FLOW | CUSTOMER_QUEUE | CUSTOMER_HOLD | CUSTOMER_WHISPER | AGENT_HOLD | AGENT_WHISPER | OUTBOUND_WHISPER | AGENT_TRANSFER | QUEUE_TRANSFER | CAMPAIGN`
Required: No

 ** Version **   <a name="connect-Type-ContactFlow-Version"></a>
The identifier of the flow version.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** VersionDescription **   <a name="connect-Type-ContactFlow-VersionDescription"></a>
The description of the flow version.
Type: String
Required: No

## See Also
<a name="API_ContactFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

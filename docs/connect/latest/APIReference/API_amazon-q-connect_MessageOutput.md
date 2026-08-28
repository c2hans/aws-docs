---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_MessageOutput.html
---

# MessageOutput
<a name="API_amazon-q-connect_MessageOutput"></a>

The message output.

## Contents
<a name="API_amazon-q-connect_MessageOutput_Contents"></a>

 ** messageId **   <a name="connect-Type-amazon-q-connect_MessageOutput-messageId"></a>
The identifier of a message.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** participant **   <a name="connect-Type-amazon-q-connect_MessageOutput-participant"></a>
The participant of a message.
Type: String
Valid Values: `CUSTOMER | AGENT | BOT`
Required: Yes

 ** timestamp **   <a name="connect-Type-amazon-q-connect_MessageOutput-timestamp"></a>
The timestamp of a message.
Type: Timestamp
Required: Yes

 ** value **   <a name="connect-Type-amazon-q-connect_MessageOutput-value"></a>
The value of a message data.
Type: [MessageData](API_amazon-q-connect_MessageData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_amazon-q-connect_MessageOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/MessageOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/MessageOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/MessageOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_SSEDescription.html
---

# SSEDescription
<a name="API_dax_SSEDescription"></a>

The description of the server-side encryption status on the specified DAX cluster.

## Contents
<a name="API_dax_SSEDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Status **   <a name="DDB-Type-dax_SSEDescription-Status"></a>
The current state of server-side encryption:
+  `ENABLING` - Server-side encryption is being enabled.
+  `ENABLED` - Server-side encryption is enabled.
+  `DISABLING` - Server-side encryption is being disabled.
+  `DISABLED` - Server-side encryption is disabled.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED`
Required: No

## See Also
<a name="API_dax_SSEDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/SSEDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/SSEDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/SSEDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

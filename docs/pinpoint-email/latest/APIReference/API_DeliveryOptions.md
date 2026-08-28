---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeliveryOptions.html
---

# DeliveryOptions
<a name="API_DeliveryOptions"></a>

Used to associate a configuration set with a dedicated IP pool.

## Contents
<a name="API_DeliveryOptions_Contents"></a>

 ** SendingPoolName **   <a name="pinpoint-Type-DeliveryOptions-SendingPoolName"></a>
The name of the dedicated IP pool that you want to associate with the configuration set.
Type: String
Required: No

 ** TlsPolicy **   <a name="pinpoint-Type-DeliveryOptions-TlsPolicy"></a>
Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `Require`, messages are only delivered if a TLS connection can be established. If the value is `Optional`, messages can be delivered in plain text if a TLS connection can't be established.
Type: String
Valid Values: `REQUIRE | OPTIONAL`
Required: No

## See Also
<a name="API_DeliveryOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/DeliveryOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/DeliveryOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/DeliveryOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

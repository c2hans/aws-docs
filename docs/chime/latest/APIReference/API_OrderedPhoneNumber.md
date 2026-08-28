---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_OrderedPhoneNumber.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# OrderedPhoneNumber
<a name="API_OrderedPhoneNumber"></a>

A phone number for which an order has been placed.

## Contents
<a name="API_OrderedPhoneNumber_Contents"></a>

 ** E164PhoneNumber **   <a name="chime-Type-OrderedPhoneNumber-E164PhoneNumber"></a>
The phone number, in E.164 format.
Type: String
Pattern: `^\+?[1-9]\d{1,14}$`
Required: No

 ** Status **   <a name="chime-Type-OrderedPhoneNumber-Status"></a>
The phone number status.
Type: String
Valid Values: `Processing | Acquired | Failed`
Required: No

## See Also
<a name="API_OrderedPhoneNumber_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/OrderedPhoneNumber)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/OrderedPhoneNumber)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/OrderedPhoneNumber)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

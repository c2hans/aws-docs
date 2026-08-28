---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdatePhoneNumberRequestItem.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# UpdatePhoneNumberRequestItem
<a name="API_UpdatePhoneNumberRequestItem"></a>

The phone number ID, product type, or calling name fields to update, used with the [BatchUpdatePhoneNumber](API_BatchUpdatePhoneNumber.md) and [UpdatePhoneNumber](API_UpdatePhoneNumber.md) actions.

## Contents
<a name="API_UpdatePhoneNumberRequestItem_Contents"></a>

 ** PhoneNumberId **   <a name="chime-Type-UpdatePhoneNumberRequestItem-PhoneNumberId"></a>
The phone number ID to update.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** CallingName **   <a name="chime-Type-UpdatePhoneNumberRequestItem-CallingName"></a>
The outbound calling name to update.
Type: String
Pattern: `^$|^[a-zA-Z0-9 ]{2,15}$`
Required: No

 ** ProductType **   <a name="chime-Type-UpdatePhoneNumberRequestItem-ProductType"></a>
The product type to update.
Type: String
Valid Values: `BusinessCalling | VoiceConnector | SipMediaApplicationDialIn`
Required: No

## See Also
<a name="API_UpdatePhoneNumberRequestItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/UpdatePhoneNumberRequestItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/UpdatePhoneNumberRequestItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/UpdatePhoneNumberRequestItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

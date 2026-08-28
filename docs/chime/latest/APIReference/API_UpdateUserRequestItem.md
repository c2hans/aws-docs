---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateUserRequestItem.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# UpdateUserRequestItem
<a name="API_UpdateUserRequestItem"></a>

The user ID and user fields to update, used with the [BatchUpdateUser](API_BatchUpdateUser.md) action.

## Contents
<a name="API_UpdateUserRequestItem_Contents"></a>

 ** UserId **   <a name="chime-Type-UpdateUserRequestItem-UserId"></a>
The user ID.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** AlexaForBusinessMetadata **   <a name="chime-Type-UpdateUserRequestItem-AlexaForBusinessMetadata"></a>
The Alexa for Business metadata.
Type: [AlexaForBusinessMetadata](API_AlexaForBusinessMetadata.md) object
Required: No

 ** LicenseType **   <a name="chime-Type-UpdateUserRequestItem-LicenseType"></a>
The user license type.
Type: String
Valid Values: `Basic | Plus | Pro | ProTrial`
Required: No

 ** UserType **   <a name="chime-Type-UpdateUserRequestItem-UserType"></a>
The user type.
Type: String
Valid Values: `PrivateUser | SharedDevice`
Required: No

## See Also
<a name="API_UpdateUserRequestItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/UpdateUserRequestItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/UpdateUserRequestItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/UpdateUserRequestItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

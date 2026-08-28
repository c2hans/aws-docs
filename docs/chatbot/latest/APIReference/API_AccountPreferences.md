---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_AccountPreferences.html
---

# AccountPreferences
<a name="API_AccountPreferences"></a>

Preferences related to Amazon Q Developer usage in the calling AWS account.

## Contents
<a name="API_AccountPreferences_Contents"></a>

 ** TrainingDataCollectionEnabled **   <a name="qdevinchatapps-Type-AccountPreferences-TrainingDataCollectionEnabled"></a>
Turns on training data collection.
This helps improve the Amazon Q Developer experience by allowing Amazon Q Developer to store and use your customer information, such as Amazon Q Developer configurations, notifications, user inputs, Amazon Q Developer generated responses, and interaction data. This data helps us to continuously improve and develop Artificial Intelligence (AI) technologies. Your data is not shared with any third parties and is protected using sophisticated controls to prevent unauthorized access and misuse. Amazon Q Developer does not store or use interactions in chat channels with Amazon Q for training AI technologies for Amazon Q Developer.
Type: Boolean
Required: No

 ** UserAuthorizationRequired **   <a name="qdevinchatapps-Type-AccountPreferences-UserAuthorizationRequired"></a>
Enables use of a user role requirement in your chat configuration.
Type: Boolean
Required: No

## See Also
<a name="API_AccountPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/AccountPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/AccountPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/AccountPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

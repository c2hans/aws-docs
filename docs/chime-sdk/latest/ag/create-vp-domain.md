---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/create-vp-domain.html
---

# Creating voice profile domains
<a name="create-vp-domain"></a>

The steps in this section explain how to create voice profile domains. Remember the following:
+ Domain names can't exceed 256 characters.
+ Domain descriptions can't exceed 512 characters.

The Amazon Chime SDK console displays an error message if you exceed either limit.

**Note**
You must use a symmetric KMS key to encrypt all your domains. For more information, see [Using encryption with voice analytics](analytics-encryption.md). Also, your end users must consent to having their voice recorded before you start a voice analytics session. For more information about consent, see [Understanding the voice analytics consent notice](va-consent-notice.md).

**To create a voice profile domain**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, choose **Voice profile domains**.

1. Choose **Create voice profile domain**.

1. Under **Consent Acknowledgement**, choose **Yes, I agree to the Consent Acknowledgement for Amazon Chime Speaker Search**.

1. Under **Setup**, enter a name and description for the domain, then choose a KMS key.

1. (Optional) Under **Tags**, choose **Add new tag**, then enter a key and optional value. Repeat as needed to add more tags.

1. When finished, choose **Create voice profile domain**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

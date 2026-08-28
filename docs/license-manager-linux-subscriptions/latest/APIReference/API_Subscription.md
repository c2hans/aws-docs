---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_Subscription.html
---

# Subscription
<a name="API_Subscription"></a>

An object which details a discovered Linux subscription.

## Contents
<a name="API_Subscription_Contents"></a>

 ** InstanceCount **   <a name="licensemanagerlinuxsubscriptions-Type-Subscription-InstanceCount"></a>
The total amount of running instances using this subscription.
Type: Long
Required: No

 ** Name **   <a name="licensemanagerlinuxsubscriptions-Type-Subscription-Name"></a>
The name of the subscription.
Type: String
Required: No

 ** Type **   <a name="licensemanagerlinuxsubscriptions-Type-Subscription-Type"></a>
The type of subscription. The type can be subscription-included with Amazon EC2, Bring Your Own Subscription model (BYOS), or from the AWS Marketplace. Certain subscriptions may use licensing from the AWS Marketplace as well as OS licensing from Amazon EC2 or BYOS.
Type: String
Required: No

## See Also
<a name="API_Subscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/Subscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/Subscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/Subscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager Linux Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-linux-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

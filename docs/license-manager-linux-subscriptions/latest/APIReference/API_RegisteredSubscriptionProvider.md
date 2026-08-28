---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_RegisteredSubscriptionProvider.html
---

# RegisteredSubscriptionProvider
<a name="API_RegisteredSubscriptionProvider"></a>

A third-party provider for operating system (OS) platform software and license subscriptions, such as Red Hat. When you register a third-party Linux subscription provider, License Manager can get subscription data from the registered provider.

## Contents
<a name="API_RegisteredSubscriptionProvider_Contents"></a>

 ** LastSuccessfulDataRetrievalTime **   <a name="licensemanagerlinuxsubscriptions-Type-RegisteredSubscriptionProvider-LastSuccessfulDataRetrievalTime"></a>
The timestamp from the last time that License Manager accessed third-party subscription data for your account from your registered Linux subscription provider.
Type: String
Required: No

 ** SecretArn **   <a name="licensemanagerlinuxsubscriptions-Type-RegisteredSubscriptionProvider-SecretArn"></a>
The Amazon Resource Name (ARN) of the Secrets Manager secret that stores your registered Linux subscription provider access token. For RHEL account subscriptions, this is the offline token.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:secretsmanager:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:secret:[^/]{1,1023}`
Required: No

 ** SubscriptionProviderArn **   <a name="licensemanagerlinuxsubscriptions-Type-RegisteredSubscriptionProvider-SubscriptionProviderArn"></a>
The Amazon Resource Name (ARN) of the Linux subscription provider resource that you registered.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,510}/[a-z0-9-\.]{1,510}`
Required: No

 ** SubscriptionProviderSource **   <a name="licensemanagerlinuxsubscriptions-Type-RegisteredSubscriptionProvider-SubscriptionProviderSource"></a>
A supported third-party Linux subscription provider. License Manager currently supports Red Hat subscriptions.
Type: String
Valid Values: `RedHat`
Required: No

 ** SubscriptionProviderStatus **   <a name="licensemanagerlinuxsubscriptions-Type-RegisteredSubscriptionProvider-SubscriptionProviderStatus"></a>
Indicates the status of your registered Linux subscription provider access token from the last time License Manager retrieved subscription data. For RHEL account subscriptions, this is the status of the offline token.
Type: String
Valid Values: `ACTIVE | INVALID | PENDING`
Required: No

 ** SubscriptionProviderStatusMessage **   <a name="licensemanagerlinuxsubscriptions-Type-RegisteredSubscriptionProvider-SubscriptionProviderStatusMessage"></a>
A detailed message that's associated with your BYOL subscription provider token status.
Type: String
Required: No

## See Also
<a name="API_RegisteredSubscriptionProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/RegisteredSubscriptionProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/RegisteredSubscriptionProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/RegisteredSubscriptionProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager Linux Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-linux-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

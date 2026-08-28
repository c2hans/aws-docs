---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_Instance.html
---

# Instance
<a name="API_Instance"></a>

Details discovered information about a running instance using Linux subscriptions.

## Contents
<a name="API_Instance_Contents"></a>

 ** AccountID **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-AccountID"></a>
The account ID which owns the instance.
Type: String
Required: No

 ** AmiId **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-AmiId"></a>
The AMI ID used to launch the instance.
Type: String
Required: No

 ** DualSubscription **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-DualSubscription"></a>
Indicates that you have two different license subscriptions for the same software on your instance.
Type: String
Required: No

 ** InstanceID **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-InstanceID"></a>
The instance ID of the resource.
Type: String
Required: No

 ** InstanceType **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-InstanceType"></a>
The instance type of the resource.
Type: String
Required: No

 ** LastUpdatedTime **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-LastUpdatedTime"></a>
The time in which the last discovery updated the instance details.
Type: String
Required: No

 ** OsVersion **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-OsVersion"></a>
The operating system software version that runs on your instance.
Type: String
Required: No

 ** ProductCode **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-ProductCode"></a>
The product code for the instance. For more information, see [Usage operation values](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-usage-operation.html) in the * AWS License Manager User Guide* .
Type: Array of strings
Required: No

 ** Region **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-Region"></a>
The Region the instance is running in.
Type: String
Required: No

 ** RegisteredWithSubscriptionProvider **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-RegisteredWithSubscriptionProvider"></a>
Indicates that your instance uses a BYOL license subscription from a third-party Linux subscription provider that you've registered with License Manager.
Type: String
Required: No

 ** Status **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-Status"></a>
The status of the instance.
Type: String
Required: No

 ** SubscriptionName **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-SubscriptionName"></a>
The name of the license subscription that the instance uses.
Type: String
Required: No

 ** SubscriptionProviderCreateTime **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-SubscriptionProviderCreateTime"></a>
The timestamp when you registered the third-party Linux subscription provider for the subscription that the instance uses.
Type: String
Required: No

 ** SubscriptionProviderUpdateTime **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-SubscriptionProviderUpdateTime"></a>
The timestamp from the last time that the instance synced with the registered third-party Linux subscription provider.
Type: String
Required: No

 ** UsageOperation **   <a name="licensemanagerlinuxsubscriptions-Type-Instance-UsageOperation"></a>
The usage operation of the instance. For more information, see For more information, see [Usage operation values](https://docs.aws.amazon.com/license-manager/latest/userguide/linux-subscriptions-usage-operation.html) in the * AWS License Manager User Guide*.
Type: String
Required: No

## See Also
<a name="API_Instance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/Instance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/Instance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/Instance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager Linux Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-linux-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

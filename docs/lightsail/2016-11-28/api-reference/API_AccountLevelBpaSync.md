---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AccountLevelBpaSync.html
---

# AccountLevelBpaSync
<a name="API_AccountLevelBpaSync"></a>

Describes the synchronization status of the Amazon Simple Storage Service (Amazon S3) account-level block public access (BPA) feature for your Lightsail buckets.

The account-level BPA feature of Amazon S3 provides centralized controls to limit public access to all Amazon S3 buckets in an account. BPA can make all Amazon S3 buckets in an AWS account private regardless of the individual bucket and object permissions that are configured. Lightsail buckets take into account the Amazon S3 account-level BPA configuration when allowing or denying public access. To do this, Lightsail periodically fetches the account-level BPA configuration from Amazon S3. When the account-level BPA status is `InSync`, the Amazon S3 account-level BPA configuration is synchronized and it applies to your Lightsail buckets. For more information about Amazon Simple Storage Service account-level BPA and how it affects Lightsail buckets, see [Block public access for buckets in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-block-public-access-for-buckets) in the *Amazon Lightsail Developer Guide*.

## Contents
<a name="API_AccountLevelBpaSync_Contents"></a>

 ** bpaImpactsLightsail **   <a name="Lightsail-Type-AccountLevelBpaSync-bpaImpactsLightsail"></a>
A Boolean value that indicates whether account-level block public access is affecting your Lightsail buckets.
Type: Boolean
Required: No

 ** lastSyncedAt **   <a name="Lightsail-Type-AccountLevelBpaSync-lastSyncedAt"></a>
The timestamp of when the account-level BPA configuration was last synchronized. This value is null when the account-level BPA configuration has not been synchronized.
Type: Timestamp
Required: No

 ** message **   <a name="Lightsail-Type-AccountLevelBpaSync-message"></a>
A message that provides a reason for a `Failed` or `Defaulted` synchronization status.
The following messages are possible:
+  `SYNC_ON_HOLD` - The synchronization has not yet happened. This status message occurs immediately after you create your first Lightsail bucket. This status message should change after the first synchronization happens, approximately 1 hour after the first bucket is created.
+  `DEFAULTED_FOR_SLR_MISSING` - The synchronization failed because the required service-linked role is missing from your AWS account. The account-level BPA configuration for your Lightsail buckets is defaulted to *active* until the synchronization can occur. This means that all your buckets are private and not publicly accessible. For more information about how to create the required service-linked role to allow synchronization, see [Using Service-Linked Roles for Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles) in the *Amazon Lightsail Developer Guide*.
+  `DEFAULTED_FOR_SLR_MISSING_ON_HOLD` - The synchronization failed because the required service-linked role is missing from your AWS account. Account-level BPA is not yet configured for your Lightsail buckets. Therefore, only the bucket access permissions and individual object access permissions apply to your Lightsail buckets. For more information about how to create the required service-linked role to allow synchronization, see [Using Service-Linked Roles for Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-using-service-linked-roles) in the *Amazon Lightsail Developer Guide*.
+  `Unknown` - The reason that synchronization failed is unknown. Contact AWS Support for more information.
Type: String
Valid Values: `DEFAULTED_FOR_SLR_MISSING | SYNC_ON_HOLD | DEFAULTED_FOR_SLR_MISSING_ON_HOLD | Unknown`
Required: No

 ** status **   <a name="Lightsail-Type-AccountLevelBpaSync-status"></a>
The status of the account-level BPA synchronization.
The following statuses are possible:
+  `InSync` - Account-level BPA is synchronized. The Amazon S3 account-level BPA configuration applies to your Lightsail buckets.
+  `NeverSynced` - Synchronization has not yet happened. The Amazon S3 account-level BPA configuration does not apply to your Lightsail buckets.
+  `Failed` - Synchronization failed. The Amazon S3 account-level BPA configuration does not apply to your Lightsail buckets.
+  `Defaulted` - Synchronization failed and account-level BPA for your Lightsail buckets is defaulted to *active*.
You might need to complete further actions if the status is `Failed` or `Defaulted`. The `message` parameter provides more information for those statuses.
Type: String
Valid Values: `InSync | Failed | NeverSynced | Defaulted`
Required: No

## See Also
<a name="API_AccountLevelBpaSync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/AccountLevelBpaSync)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/AccountLevelBpaSync)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/AccountLevelBpaSync)

---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_Bucket.html
---

# Bucket
<a name="API_Bucket"></a>

Describes an Amazon Lightsail bucket.

## Contents
<a name="API_Bucket_Contents"></a>

 ** ableToUpdateBundle **   <a name="Lightsail-Type-Bucket-ableToUpdateBundle"></a>
Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle.
You can update a bucket's bundle only one time within a monthly AWS billing cycle.
Use the [UpdateBucketBundle](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html) action to change a bucket's bundle.
Type: Boolean
Required: No

 ** accessLogConfig **   <a name="Lightsail-Type-Bucket-accessLogConfig"></a>
An object that describes the access log configuration for the bucket.
Type: [BucketAccessLogConfig](API_BucketAccessLogConfig.md) object
Required: No

 ** accessRules **   <a name="Lightsail-Type-Bucket-accessRules"></a>
An object that describes the access rules of the bucket.
Type: [AccessRules](API_AccessRules.md) object
Required: No

 ** arn **   <a name="Lightsail-Type-Bucket-arn"></a>
The Amazon Resource Name (ARN) of the bucket.
Type: String
Pattern: `.*\S.*`
Required: No

 ** bundleId **   <a name="Lightsail-Type-Bucket-bundleId"></a>
The ID of the bundle currently applied to the bucket.
A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.
Use the [UpdateBucketBundle](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html) action to change the bundle of a bucket.
Type: String
Pattern: `.*\S.*`
Required: No

 ** cors **   <a name="Lightsail-Type-Bucket-cors"></a>
An array of cross-origin resource sharing (CORS) rules that identify origins and the HTTP methods that can be executed on your bucket. This field is only included in the response when CORS configuration is requested or when updating CORS configuration. For more information, see [Configuring cross-origin resource sharing (CORS)](https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html).
Type: [BucketCorsConfig](API_BucketCorsConfig.md) object
Required: No

 ** createdAt **   <a name="Lightsail-Type-Bucket-createdAt"></a>
The timestamp when the distribution was created.
Type: Timestamp
Required: No

 ** location **   <a name="Lightsail-Type-Bucket-location"></a>
An object that describes the location of the bucket, such as the AWS Region and Availability Zone.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-Bucket-name"></a>
The name of the bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 54.
Pattern: `^[a-z0-9][a-z0-9-]{1,52}[a-z0-9]$`
Required: No

 ** objectVersioning **   <a name="Lightsail-Type-Bucket-objectVersioning"></a>
Indicates whether object versioning is enabled for the bucket.
The following options can be configured:
+  `Enabled` - Object versioning is enabled.
+  `Suspended` - Object versioning was previously enabled but is currently suspended. Existing object versions are retained.
+  `NeverEnabled` - Object versioning has never been enabled.
Type: String
Pattern: `.*\S.*`
Required: No

 ** readonlyAccessAccounts **   <a name="Lightsail-Type-Bucket-readonlyAccessAccounts"></a>
An array of strings that specify the AWS account IDs that have read-only access to the bucket.
Type: Array of strings
Array Members: Maximum number of 10 items.
Pattern: `.*\S.*`
Required: No

 ** resourcesReceivingAccess **   <a name="Lightsail-Type-Bucket-resourcesReceivingAccess"></a>
An array of objects that describe Lightsail instances that have access to the bucket.
Use the [SetResourceAccessForBucket](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetResourceAccessForBucket.html) action to update the instances that have access to a bucket.
Type: Array of [ResourceReceivingAccess](API_ResourceReceivingAccess.md) objects
Required: No

 ** resourceType **   <a name="Lightsail-Type-Bucket-resourceType"></a>
The Lightsail resource type of the bucket.
Type: String
Pattern: `.*\S.*`
Required: No

 ** state **   <a name="Lightsail-Type-Bucket-state"></a>
An object that describes the state of the bucket.
Type: [BucketState](API_BucketState.md) object
Required: No

 ** supportCode **   <a name="Lightsail-Type-Bucket-supportCode"></a>
The support code for a bucket. Include this code in your email to support when you have questions about a Lightsail bucket. This code enables our support team to look up your Lightsail information more easily.
Type: String
Pattern: `.*\S.*`
Required: No

 ** tags **   <a name="Lightsail-Type-Bucket-tags"></a>
The tag keys and optional values for the bucket. For more information, see [Tags in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags) in the *Amazon Lightsail Developer Guide*.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** url **   <a name="Lightsail-Type-Bucket-url"></a>
The URL of the bucket.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Bucket_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/Bucket)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/Bucket)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/Bucket)

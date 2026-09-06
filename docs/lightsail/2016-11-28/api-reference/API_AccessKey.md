---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AccessKey.html
---

# AccessKey
<a name="API_AccessKey"></a>

Describes an access key for an Amazon Lightsail bucket.

Access keys grant full programmatic access to the specified bucket and its objects. You can have a maximum of two access keys per bucket. Use the [CreateBucketAccessKey](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateBucketAccessKey.html) action to create an access key for a specific bucket. For more information about access keys, see [Creating access keys for a bucket in Amazon Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-bucket-access-keys) in the *Amazon Lightsail Developer Guide*.

**Important**
The `secretAccessKey` value is returned only in response to the `CreateBucketAccessKey` action. You can get a secret access key only when you first create an access key; you cannot get the secret access key later. If you lose the secret access key, you must create a new access key.

## Contents
<a name="API_AccessKey_Contents"></a>

 ** accessKeyId **   <a name="Lightsail-Type-AccessKey-accessKeyId"></a>
The ID of the access key.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^[A-Z0-9]{20}$`
Required: No

 ** createdAt **   <a name="Lightsail-Type-AccessKey-createdAt"></a>
The timestamp when the access key was created.
Type: Timestamp
Required: No

 ** lastUsed **   <a name="Lightsail-Type-AccessKey-lastUsed"></a>
An object that describes the last time the access key was used.
This object does not include data in the response of a [CreateBucketAccessKey](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateBucketAccessKey.html) action. If the access key has not been used, the `region` and `serviceName` values are `N/A`, and the `lastUsedDate` value is null.
Type: [AccessKeyLastUsed](API_AccessKeyLastUsed.md) object
Required: No

 ** secretAccessKey **   <a name="Lightsail-Type-AccessKey-secretAccessKey"></a>
The secret access key used to sign requests.
You should store the secret access key in a safe location. We recommend that you delete the access key if the secret access key is compromised.
Type: String
Pattern: `.*\S.*`
Required: No

 ** status **   <a name="Lightsail-Type-AccessKey-status"></a>
The status of the access key.
A status of `Active` means that the key is valid, while `Inactive` means it is not.
Type: String
Valid Values: `Active | Inactive`
Required: No

## See Also
<a name="API_AccessKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/AccessKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/AccessKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/AccessKey)

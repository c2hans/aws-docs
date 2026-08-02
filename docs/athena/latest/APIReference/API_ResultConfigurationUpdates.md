---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ResultConfigurationUpdates.html
---

# ResultConfigurationUpdates
<a name="API_ResultConfigurationUpdates"></a>

The information about the updates in the query results, such as output location and encryption configuration for the query results.

## Contents
<a name="API_ResultConfigurationUpdates_Contents"></a>

 ** AclConfiguration **   <a name="athena-Type-ResultConfigurationUpdates-AclConfiguration"></a>
The ACL configuration for the query results.
Type: [AclConfiguration](API_AclConfiguration.md) object
Required: No

 ** EncryptionConfiguration **   <a name="athena-Type-ResultConfigurationUpdates-EncryptionConfiguration"></a>
The encryption configuration for query and calculation results.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** ExpectedBucketOwner **   <a name="athena-Type-ResultConfigurationUpdates-ExpectedBucketOwner"></a>
The AWS account ID that you expect to be the owner of the Amazon S3 bucket specified by [ResultConfiguration:OutputLocation](API_ResultConfiguration.md#athena-Type-ResultConfiguration-OutputLocation). If set, Athena uses the value for `ExpectedBucketOwner` when it makes Amazon S3 calls to your specified output location. If the `ExpectedBucketOwner` AWS account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error.
If workgroup settings override client-side settings, then the query uses the `ExpectedBucketOwner` setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See [WorkGroupConfiguration:EnforceWorkGroupConfiguration](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration) and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: No

 ** OutputLocation **   <a name="athena-Type-ResultConfigurationUpdates-OutputLocation"></a>
The location in Amazon S3 where your query and calculation results are stored, such as `s3://path/to/query/bucket/`. If workgroup settings override client-side settings, then the query uses the location for the query results and the encryption configuration that are specified for the workgroup. The "workgroup settings override" is specified in `EnforceWorkGroupConfiguration` (true/false) in the `WorkGroupConfiguration`. See [WorkGroupConfiguration:EnforceWorkGroupConfiguration](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration).
Type: String
Required: No

 ** RemoveAclConfiguration **   <a name="athena-Type-ResultConfigurationUpdates-RemoveAclConfiguration"></a>
If set to `true`, indicates that the previously-specified ACL configuration for queries in this workgroup should be ignored and set to null. If set to `false` or not set, and a value is present in the `AclConfiguration` of `ResultConfigurationUpdates`, the `AclConfiguration` in the workgroup's `ResultConfiguration` is updated with the new value. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
Type: Boolean
Required: No

 ** RemoveEncryptionConfiguration **   <a name="athena-Type-ResultConfigurationUpdates-RemoveEncryptionConfiguration"></a>
If set to "true", indicates that the previously-specified encryption configuration (also known as the client-side setting) for queries in this workgroup should be ignored and set to null. If set to "false" or not set, and a value is present in the `EncryptionConfiguration` in `ResultConfigurationUpdates` (the client-side setting), the `EncryptionConfiguration` in the workgroup's `ResultConfiguration` will be updated with the new value. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
Type: Boolean
Required: No

 ** RemoveExpectedBucketOwner **   <a name="athena-Type-ResultConfigurationUpdates-RemoveExpectedBucketOwner"></a>
If set to "true", removes the AWS account ID previously specified for [ResultConfiguration:ExpectedBucketOwner](API_ResultConfiguration.md#athena-Type-ResultConfiguration-ExpectedBucketOwner). If set to "false" or not set, and a value is present in the `ExpectedBucketOwner` in `ResultConfigurationUpdates` (the client-side setting), the `ExpectedBucketOwner` in the workgroup's `ResultConfiguration` is updated with the new value. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
Type: Boolean
Required: No

 ** RemoveOutputLocation **   <a name="athena-Type-ResultConfigurationUpdates-RemoveOutputLocation"></a>
If set to "true", indicates that the previously-specified query results location (also known as a client-side setting) for queries in this workgroup should be ignored and set to null. If set to "false" or not set, and a value is present in the `OutputLocation` in `ResultConfigurationUpdates` (the client-side setting), the `OutputLocation` in the workgroup's `ResultConfiguration` will be updated with the new value. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
Type: Boolean
Required: No

## See Also
<a name="API_ResultConfigurationUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ResultConfigurationUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ResultConfigurationUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ResultConfigurationUpdates)

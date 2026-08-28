---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ResultConfiguration.html
---

# ResultConfiguration
<a name="API_ResultConfiguration"></a>

The location in Amazon S3 where query and calculation results are stored and the encryption option, if any, used for query and calculation results. These are known as "client-side settings". If workgroup settings override client-side settings, then the query uses the workgroup settings.

## Contents
<a name="API_ResultConfiguration_Contents"></a>

 ** AclConfiguration **   <a name="athena-Type-ResultConfiguration-AclConfiguration"></a>
Indicates that an Amazon S3 canned ACL should be set to control ownership of stored query results. Currently the only supported canned ACL is `BUCKET_OWNER_FULL_CONTROL`. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the ACL configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. For more information, see [WorkGroupConfiguration:EnforceWorkGroupConfiguration](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration) and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
Type: [AclConfiguration](API_AclConfiguration.md) object
Required: No

 ** EncryptionConfiguration **   <a name="athena-Type-ResultConfiguration-EncryptionConfiguration"></a>
If query and calculation results are encrypted in Amazon S3, indicates the encryption option used (for example, `SSE_KMS` or `CSE_KMS`) and key information. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See [WorkGroupConfiguration:EnforceWorkGroupConfiguration](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration) and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** ExpectedBucketOwner **   <a name="athena-Type-ResultConfiguration-ExpectedBucketOwner"></a>
The AWS account ID that you expect to be the owner of the Amazon S3 bucket specified by [ResultConfiguration:OutputLocation](#athena-Type-ResultConfiguration-OutputLocation). If set, Athena uses the value for `ExpectedBucketOwner` when it makes Amazon S3 calls to your specified output location. If the `ExpectedBucketOwner` AWS account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error.
This is a client-side setting. If workgroup settings override client-side settings, then the query uses the `ExpectedBucketOwner` setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See [WorkGroupConfiguration:EnforceWorkGroupConfiguration](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration) and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html).
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: No

 ** OutputLocation **   <a name="athena-Type-ResultConfiguration-OutputLocation"></a>
The location in Amazon S3 where your query and calculation results are stored, such as `s3://path/to/query/bucket/`. To run the query, you must specify the query results location using one of the ways: either for individual queries using either this setting (client-side), or in the workgroup, using [WorkGroupConfiguration](API_WorkGroupConfiguration.md). If none of them is set, Athena issues an error that no output location is provided. If workgroup settings override client-side settings, then the query uses the settings specified for the workgroup. See [WorkGroupConfiguration:EnforceWorkGroupConfiguration](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration).
Type: String
Required: No

## See Also
<a name="API_ResultConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ResultConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ResultConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ResultConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

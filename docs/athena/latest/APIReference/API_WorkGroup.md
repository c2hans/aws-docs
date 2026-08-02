---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_WorkGroup.html
---

# WorkGroup
<a name="API_WorkGroup"></a>

A workgroup, which contains a name, description, creation time, state, and other configuration, listed under [WorkGroup:Configuration](#athena-Type-WorkGroup-Configuration). Each workgroup enables you to isolate queries for you or your group of users from other queries in the same account, to configure the query results location and the encryption configuration (known as workgroup settings), to enable sending query metrics to Amazon CloudWatch, and to establish per-query data usage control limits for all queries in a workgroup. The workgroup settings override is specified in `EnforceWorkGroupConfiguration` (true/false) in the `WorkGroupConfiguration`. See [WorkGroupConfiguration:EnforceWorkGroupConfiguration](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration).

## Contents
<a name="API_WorkGroup_Contents"></a>

 ** Name **   <a name="athena-Type-WorkGroup-Name"></a>
The workgroup name.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: Yes

 ** Configuration **   <a name="athena-Type-WorkGroup-Configuration"></a>
The configuration of the workgroup, which includes the location in Amazon S3 where query and calculation results are stored, the encryption configuration, if any, used for query and calculation results; whether the Amazon CloudWatch Metrics are enabled for the workgroup; whether workgroup settings override client-side settings; and the data usage limits for the amount of data scanned per query or per workgroup. The workgroup settings override is specified in `EnforceWorkGroupConfiguration` (true/false) in the `WorkGroupConfiguration`. See [WorkGroupConfiguration:EnforceWorkGroupConfiguration](API_WorkGroupConfiguration.md#athena-Type-WorkGroupConfiguration-EnforceWorkGroupConfiguration).
Type: [WorkGroupConfiguration](API_WorkGroupConfiguration.md) object
Required: No

 ** CreationTime **   <a name="athena-Type-WorkGroup-CreationTime"></a>
The date and time the workgroup was created.
Type: Timestamp
Required: No

 ** Description **   <a name="athena-Type-WorkGroup-Description"></a>
The workgroup description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** IdentityCenterApplicationArn **   <a name="athena-Type-WorkGroup-IdentityCenterApplicationArn"></a>
The ARN of the IAM Identity Center enabled application associated with the workgroup.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}$`
Required: No

 ** State **   <a name="athena-Type-WorkGroup-State"></a>
The state of the workgroup: ENABLED or DISABLED.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_WorkGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/WorkGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/WorkGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/WorkGroup)

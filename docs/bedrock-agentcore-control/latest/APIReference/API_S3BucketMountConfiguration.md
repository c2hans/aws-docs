---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_S3BucketMountConfiguration.html
---

# S3BucketMountConfiguration

Mounts an Amazon S3 bucket in the AgentCore Runtime with Mountpoint for Amazon S3. Files under the mount path map to objects in the bucket.

## Contents
<a name="API_S3BucketMountConfiguration_Contents"></a>

 ** bucket **   <a name="bedrockagentcorecontrol-Type-S3BucketMountConfiguration-bucket"></a>
The name of the S3 bucket to mount. You can specify a general purpose bucket or a directory bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** mountPath **   <a name="bedrockagentcorecontrol-Type-S3BucketMountConfiguration-mountPath"></a>
The mount path for the S3 bucket inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data`).
Type: String
Length Constraints: Minimum length of 6. Maximum length of 200.
Pattern: `/mnt/[a-zA-Z0-9._-]+/?`
Required: Yes

 ** prefix **   <a name="bedrockagentcorecontrol-Type-S3BucketMountConfiguration-prefix"></a>
The key prefix to mount. Only objects under this prefix are visible at the mount path. To give each session its own prefix, include `{runtimeSessionId}` (for example, `data/{runtimeSessionId}/`). If you omit the prefix, the whole bucket is mounted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9{][a-zA-Z0-9!_.*'()/{}-]*`
Required: No

 ** s3BucketOwner **   <a name="bedrockagentcorecontrol-Type-S3BucketMountConfiguration-s3BucketOwner"></a>
The AWS account ID that must own the bucket. If you omit it, the bucket must be owned by the account that owns the AgentCore Runtime.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** s3BucketRegion **   <a name="bedrockagentcorecontrol-Type-S3BucketMountConfiguration-s3BucketRegion"></a>
The AWS Region of the S3 bucket. If you omit it, the bucket must be in the same Region as the AgentCore Runtime.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([a-z]+-){2,3}\d+`
Required: No

## See Also
<a name="API_S3BucketMountConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/S3BucketMountConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/S3BucketMountConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/S3BucketMountConfiguration)

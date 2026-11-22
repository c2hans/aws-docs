---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_S3SourceConfiguration.html
---

# S3SourceConfiguration

The settings of a source that the registry reads from Amazon S3.

## Contents
<a name="API_S3SourceConfiguration_Contents"></a>

 ** bucketOwnerAccountId **   <a name="agentregistrycontrol-Type-S3SourceConfiguration-bucketOwnerAccountId"></a>
The ID of the AWS account that owns the source bucket. The registry checks that the bucket belongs to this account each time it reads the source. If you omit it for a source that uses an IAM role, the registry expects the bucket to be in the role's account. If you omit it for a source that has no credential provider, which the registry reads as a public object, the request fails with a `ValidationException`.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_S3SourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/S3SourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/S3SourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/S3SourceConfiguration)

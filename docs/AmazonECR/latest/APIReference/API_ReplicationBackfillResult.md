---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ReplicationBackfillResult.html
---

# ReplicationBackfillResult
<a name="API_ReplicationBackfillResult"></a>

An object representing the result of a single replication during a replication backfill. Each image and tag combination is replicated as a single replication.

## Contents
<a name="API_ReplicationBackfillResult_Contents"></a>

 ** imageId **   <a name="ECR-Type-ReplicationBackfillResult-imageId"></a>
An object with identifying information for the image.
Type: [ImageIdentifier](API_ImageIdentifier.md) object
Required: Yes

 ** repositoryName **   <a name="ECR-Type-ReplicationBackfillResult-repositoryName"></a>
The name of the repository that contains the image.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: Yes

 ** status **   <a name="ECR-Type-ReplicationBackfillResult-status"></a>
The replication status of the image.
Type: String
Valid Values: `COMPLETE | FAILED`
Required: Yes

 ** failureCode **   <a name="ECR-Type-ReplicationBackfillResult-failureCode"></a>
The failure code for a replication that has failed.
Type: String
Required: No

 ** subImageFailureCodes **   <a name="ECR-Type-ReplicationBackfillResult-subImageFailureCodes"></a>
The distinct failure codes for the images referenced by a manifest list that failed to replicate. Each failure code appears at most once, regardless of how many referenced images failed with that code. This field is present only when the image is a manifest list.
Type: Array of strings
Required: No

## See Also
<a name="API_ReplicationBackfillResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ReplicationBackfillResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ReplicationBackfillResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ReplicationBackfillResult)

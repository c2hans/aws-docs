---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_PostLaunchActions.html
---

# PostLaunchActions
<a name="API_PostLaunchActions"></a>

Post Launch Actions to be executed on the Test or Cutover instance.

## Contents
<a name="API_PostLaunchActions_Contents"></a>

 ** cloudWatchLogGroupName **   <a name="mgn-Type-PostLaunchActions-cloudWatchLogGroupName"></a>
AWS Systems Manager Command's CloudWatch log group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** deployment **   <a name="mgn-Type-PostLaunchActions-deployment"></a>
Deployment type in which AWS Systems Manager Documents will be executed.
Type: String
Valid Values: `TEST_AND_CUTOVER | CUTOVER_ONLY | TEST_ONLY`
Required: No

 ** s3LogBucket **   <a name="mgn-Type-PostLaunchActions-s3LogBucket"></a>
AWS Systems Manager Command's logs S3 log bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: No

 ** s3OutputKeyPrefix **   <a name="mgn-Type-PostLaunchActions-s3OutputKeyPrefix"></a>
AWS Systems Manager Command's logs S3 output key prefix.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** ssmDocuments **   <a name="mgn-Type-PostLaunchActions-ssmDocuments"></a>
AWS Systems Manager Documents.
Type: Array of [SsmDocument](API_SsmDocument.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_PostLaunchActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/PostLaunchActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/PostLaunchActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/PostLaunchActions)

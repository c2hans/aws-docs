---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_JobResource.html
---

# JobResource
<a name="API_JobResource"></a>

Contains information about a resource that was created or updated by an asynchronous job.

## Contents
<a name="API_JobResource_Contents"></a>

 ** resourceArn **   <a name="endusermessaging-Type-JobResource-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `arn:[A-Za-z0-9_:/-]+`
Required: Yes

 ** resourceId **   <a name="endusermessaging-Type-JobResource-resourceId"></a>
The identifier of the resource that the job created or updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** resourceType **   <a name="endusermessaging-Type-JobResource-resourceType"></a>
The type of the resource that the job created or updated.
Type: String
Valid Values: `REGISTRATION | BRAND_PROFILE`
Required: Yes

## See Also
<a name="API_JobResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/JobResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/JobResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/JobResource)

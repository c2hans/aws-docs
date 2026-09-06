---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_messageflow_S3Reference.html
---

# S3Reference
<a name="API_messageflow_S3Reference"></a>

Amazon S3 object representing the updated message content, in MIME format.

**Note**
The region for the S3 bucket containing the S3 object must match the region used for WorkMail operations. Also, for WorkMail to process an S3 object, it must have permission to access that object. For more information, see [ Updating message content with AWS Lambda](https://docs.aws.amazon.com/workmail/latest/adminguide/update-with-lambda.html).

## Contents
<a name="API_messageflow_S3Reference_Contents"></a>

 ** bucket **   <a name="workmail-Type-messageflow_S3Reference-bucket"></a>
The S3 bucket name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-z0-9][a-z0-9\-]*`
Required: Yes

 ** key **   <a name="workmail-Type-messageflow_S3Reference-key"></a>
The S3 key object name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9\-/]*`
Required: Yes

 ** objectVersion **   <a name="workmail-Type-messageflow_S3Reference-objectVersion"></a>
If you enable versioning for the bucket, you can specify the object version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

## See Also
<a name="API_messageflow_S3Reference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmailmessageflow-2019-05-01/S3Reference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmailmessageflow-2019-05-01/S3Reference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmailmessageflow-2019-05-01/S3Reference)

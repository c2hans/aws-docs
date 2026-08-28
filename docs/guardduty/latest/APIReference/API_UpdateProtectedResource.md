---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateProtectedResource.html
---

# UpdateProtectedResource
<a name="API_UpdateProtectedResource"></a>

Information about the protected resource that is associated with the created Malware Protection plan. Presently, `S3Bucket` is the only supported protected resource.

## Contents
<a name="API_UpdateProtectedResource_Contents"></a>

 ** s3Bucket **   <a name="guardduty-Type-UpdateProtectedResource-s3Bucket"></a>
Information about the protected S3 bucket resource.
Type: [UpdateS3BucketResource](API_UpdateS3BucketResource.md) object
Required: No

## See Also
<a name="API_UpdateProtectedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/UpdateProtectedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/UpdateProtectedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/UpdateProtectedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

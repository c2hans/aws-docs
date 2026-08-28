---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Transition.html
---

# Transition
<a name="API_control_Transition"></a>

Specifies when an object transitions to a specified storage class. For more information about Amazon S3 Lifecycle configuration rules, see [ Transitioning objects using Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html) in the *Amazon S3 User Guide*.

## Contents
<a name="API_control_Transition_Contents"></a>

 ** Date **   <a name="AmazonS3-Type-control_Transition-Date"></a>
Indicates when objects are transitioned to the specified storage class. The date value must be in ISO 8601 format. The time is always midnight UTC.
Type: Timestamp
Required: No

 ** Days **   <a name="AmazonS3-Type-control_Transition-Days"></a>
Indicates the number of days after creation when objects are transitioned to the specified storage class. The value must be a positive integer.
Type: Integer
Required: No

 ** StorageClass **   <a name="AmazonS3-Type-control_Transition-StorageClass"></a>
The storage class to which you want the object to transition.
Type: String
Valid Values: `GLACIER | STANDARD_IA | ONEZONE_IA | INTELLIGENT_TIERING | DEEP_ARCHIVE`
Required: No

## See Also
<a name="API_control_Transition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Transition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Transition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Transition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

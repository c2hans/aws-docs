---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_S3Location.html
---

# S3Location
<a name="API_S3Location"></a>

Represents an Amazon S3 location (bucket name, bucket owner, and object key) where DataBrew can read input data, or write output from a job.

## Contents
<a name="API_S3Location_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Bucket **   <a name="databrew-Type-S3Location-Bucket"></a>
The Amazon S3 bucket name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** BucketOwner **   <a name="databrew-Type-S3Location-BucketOwner"></a>
The AWS account ID of the bucket owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: No

 ** Key **   <a name="databrew-Type-S3Location-Key"></a>
The unique name of the object in the bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1280.
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/S3Location)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/S3Location)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/S3Location)

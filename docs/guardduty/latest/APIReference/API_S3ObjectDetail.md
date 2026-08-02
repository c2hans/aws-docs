---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_S3ObjectDetail.html
---

# S3ObjectDetail
<a name="API_S3ObjectDetail"></a>

Information about the S3 object that was scanned

## Contents
<a name="API_S3ObjectDetail_Contents"></a>

 ** eTag **   <a name="guardduty-Type-S3ObjectDetail-eTag"></a>
The entity tag is a hash of the S3 object. The ETag reflects changes only to the contents of an object, and not its metadata.
Type: String
Required: No

 ** hash **   <a name="guardduty-Type-S3ObjectDetail-hash"></a>
Hash of the threat detected in this finding.
Type: String
Required: No

 ** key **   <a name="guardduty-Type-S3ObjectDetail-key"></a>
Key of the S3 object.
Type: String
Required: No

 ** objectArn **   <a name="guardduty-Type-S3ObjectDetail-objectArn"></a>
Amazon Resource Name (ARN) of the S3 object.
Type: String
Required: No

 ** versionId **   <a name="guardduty-Type-S3ObjectDetail-versionId"></a>
Version ID of the object.
Type: String
Required: No

## See Also
<a name="API_S3ObjectDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/S3ObjectDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/S3ObjectDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/S3ObjectDetail)

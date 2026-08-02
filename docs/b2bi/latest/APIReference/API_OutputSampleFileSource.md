---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_OutputSampleFileSource.html
---

# OutputSampleFileSource
<a name="API_OutputSampleFileSource"></a>

Container for the location of a sample file used for outbound transformations.

## Contents
<a name="API_OutputSampleFileSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fileLocation **   <a name="b2bi-Type-OutputSampleFileSource-fileLocation"></a>
Specifies the details for the Amazon S3 file location that is being used with AWS B2B Data Interchange. File locations in Amazon S3 are identified using a combination of the bucket and key.
Type: [S3Location](API_S3Location.md) object
Required: No

## See Also
<a name="API_OutputSampleFileSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/OutputSampleFileSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/OutputSampleFileSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/OutputSampleFileSource)

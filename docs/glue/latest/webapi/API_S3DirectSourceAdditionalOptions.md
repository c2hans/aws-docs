---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3DirectSourceAdditionalOptions.html
---

# S3DirectSourceAdditionalOptions
<a name="API_S3DirectSourceAdditionalOptions"></a>

Specifies additional connection options for the Amazon S3 data store.

## Contents
<a name="API_S3DirectSourceAdditionalOptions_Contents"></a>

 ** BoundedFiles **   <a name="Glue-Type-S3DirectSourceAdditionalOptions-BoundedFiles"></a>
Sets the upper limit for the target number of files that will be processed.
Type: Long
Required: No

 ** BoundedSize **   <a name="Glue-Type-S3DirectSourceAdditionalOptions-BoundedSize"></a>
Sets the upper limit for the target size of the dataset in bytes that will be processed.
Type: Long
Required: No

 ** EnableSamplePath **   <a name="Glue-Type-S3DirectSourceAdditionalOptions-EnableSamplePath"></a>
Sets option to enable a sample path.
Type: Boolean
Required: No

 ** SamplePath **   <a name="Glue-Type-S3DirectSourceAdditionalOptions-SamplePath"></a>
If enabled, specifies the sample path.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_S3DirectSourceAdditionalOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3DirectSourceAdditionalOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3DirectSourceAdditionalOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3DirectSourceAdditionalOptions)

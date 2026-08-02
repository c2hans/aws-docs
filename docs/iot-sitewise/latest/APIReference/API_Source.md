---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Source.html
---

# Source
<a name="API_Source"></a>

The data source for the dataset.

## Contents
<a name="API_Source_Contents"></a>

 ** arn **   <a name="iotsitewise-Type-Source-arn"></a>
Contains the ARN of the dataset. If the source is Kendra, it's the ARN of the Kendra index.
Type: String
Required: No

 ** location **   <a name="iotsitewise-Type-Source-location"></a>
Contains the location information where the cited text is originally stored. For example, if the data source is Kendra, and the text synchronized is from an S3 bucket, then the location refers to an S3 object.
Type: [Location](API_Location.md) object
Required: No

## See Also
<a name="API_Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/Source)

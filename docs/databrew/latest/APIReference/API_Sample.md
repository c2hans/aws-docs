---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_Sample.html
---

# Sample
<a name="API_Sample"></a>

Represents the sample size and sampling type for DataBrew to use for interactive data analysis.

## Contents
<a name="API_Sample_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Type **   <a name="databrew-Type-Sample-Type"></a>
The way in which DataBrew obtains rows from a dataset.
Type: String
Valid Values: `FIRST_N | LAST_N | RANDOM`
Required: Yes

 ** Size **   <a name="databrew-Type-Sample-Size"></a>
The number of rows in the sample.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

## See Also
<a name="API_Sample_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/Sample)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/Sample)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/Sample)

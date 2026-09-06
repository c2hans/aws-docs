---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_JobInputOptions.html
---

# JobInputOptions
<a name="API_JobInputOptions"></a>

Configuration for input data location and format.

**Note**
Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.

## Contents
<a name="API_JobInputOptions_Contents"></a>

 ** Format **   <a name="location-Type-JobInputOptions-Format"></a>
Input data format. Currently only `Parquet` is supported.
Input files have a limitation of 10gb per file, and 1gb per Parquet row-group within the file.
Type: String
Valid Values: `Parquet`
Required: Yes

 ** Location **   <a name="location-Type-JobInputOptions-Location"></a>
S3 ARN or URI where input files are stored.
The Amazon S3 bucket must be created in the same AWS region where you plan to run your job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `(arn:aws(-[a-z]+)*:[a-z0-9-]+:[a-z0-9-]*:(\d{12})?:[\w/+=,.-]+|s3://[a-z0-9][a-z0-9._-]{2,254}(/[^/]+)*/?)`
Required: Yes

## See Also
<a name="API_JobInputOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/JobInputOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/JobInputOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/JobInputOptions)

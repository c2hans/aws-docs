---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geojobs_JobOutputOptions.html
---

# JobOutputOptions
<a name="API_geojobs_JobOutputOptions"></a>

Configuration for output data location and format.

## Contents
<a name="API_geojobs_JobOutputOptions_Contents"></a>

 ** Format **   <a name="location-Type-geojobs_JobOutputOptions-Format"></a>
Output data format. Currently only "Parquet" is supported.
Type: String
Valid Values: `Parquet`
Required: Yes

 ** Location **   <a name="location-Type-geojobs_JobOutputOptions-Location"></a>
S3 ARN or URI where output files will be written.
The Amazon S3 bucket must exist in the same AWS region where you plan to run your job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `(arn:aws(-[a-z]+)*:[a-z0-9-]+:[a-z0-9-]*:(\d{12})?:[\w/+=,.-]+|s3://[a-z0-9][a-z0-9._-]{2,254}(/[^/]+)*/)`
Required: Yes

## See Also
<a name="API_geojobs_JobOutputOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geojobs-2020-11-19/JobOutputOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geojobs-2020-11-19/JobOutputOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geojobs-2020-11-19/JobOutputOptions)

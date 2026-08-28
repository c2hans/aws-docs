---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ListEarthObservationJobOutputConfig.html
---

# ListEarthObservationJobOutputConfig
<a name="API_geospatial_ListEarthObservationJobOutputConfig"></a>

An object containing information about the output file.

## Contents
<a name="API_geospatial_ListEarthObservationJobOutputConfig_Contents"></a>

 ** Arn **   <a name="sagemaker-Type-geospatial_ListEarthObservationJobOutputConfig-Arn"></a>
The Amazon Resource Name (ARN) of the list of the Earth Observation jobs.
Type: String
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-geospatial_ListEarthObservationJobOutputConfig-CreationTime"></a>
The creation time.
Type: Timestamp
Required: Yes

 ** DurationInSeconds **   <a name="sagemaker-Type-geospatial_ListEarthObservationJobOutputConfig-DurationInSeconds"></a>
The duration of the session, in seconds.
Type: Integer
Required: Yes

 ** Name **   <a name="sagemaker-Type-geospatial_ListEarthObservationJobOutputConfig-Name"></a>
The names of the Earth Observation jobs in the list.
Type: String
Required: Yes

 ** OperationType **   <a name="sagemaker-Type-geospatial_ListEarthObservationJobOutputConfig-OperationType"></a>
The operation type for an Earth Observation job.
Type: String
Required: Yes

 ** Status **   <a name="sagemaker-Type-geospatial_ListEarthObservationJobOutputConfig-Status"></a>
The status of the list of the Earth Observation jobs.
Type: String
Valid Values: `INITIALIZING | IN_PROGRESS | STOPPING | COMPLETED | STOPPED | FAILED | DELETING | DELETED`
Required: Yes

 ** Tags **   <a name="sagemaker-Type-geospatial_ListEarthObservationJobOutputConfig-Tags"></a>
Each tag consists of a key and a value.
Type: String to string map
Required: No

## See Also
<a name="API_geospatial_ListEarthObservationJobOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ListEarthObservationJobOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ListEarthObservationJobOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ListEarthObservationJobOutputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

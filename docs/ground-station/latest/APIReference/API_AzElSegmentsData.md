---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElSegmentsData.html
---

# AzElSegmentsData
<a name="API_AzElSegmentsData"></a>

Container for azimuth elevation segment data.

Specify either [AzElSegmentsData:s3Object](#groundstation-Type-AzElSegmentsData-s3Object) to reference data in Amazon S3, or [AzElSegmentsData:azElData](#groundstation-Type-AzElSegmentsData-azElData) to provide data inline.

## Contents
<a name="API_AzElSegmentsData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** azElData **   <a name="groundstation-Type-AzElSegmentsData-azElData"></a>
Azimuth elevation segment data provided directly in the request.
Use this option for smaller datasets or when Amazon S3 access is not available.
Type: [AzElSegments](API_AzElSegments.md) object
Required: No

 ** s3Object **   <a name="groundstation-Type-AzElSegmentsData-s3Object"></a>
The Amazon S3 object containing azimuth elevation segment data.
The Amazon S3 object must contain JSON-formatted azimuth elevation data matching the [AzElSegments](API_AzElSegments.md) structure.
Type: [S3Object](API_S3Object.md) object
Required: No

## See Also
<a name="API_AzElSegmentsData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/AzElSegmentsData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/AzElSegmentsData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/AzElSegmentsData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

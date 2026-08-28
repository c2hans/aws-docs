---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_MultiRegionAccessPointRoute.html
---

# MultiRegionAccessPointRoute
<a name="API_control_MultiRegionAccessPointRoute"></a>

A structure for a Multi-Region Access Point that indicates where Amazon S3 traffic can be routed. Routes can be either active or passive. Active routes can process Amazon S3 requests through the Multi-Region Access Point, but passive routes are not eligible to process Amazon S3 requests.

Each route contains the Amazon S3 bucket name and the AWS Region that the bucket is located in. The route also includes the `TrafficDialPercentage` value, which shows whether the bucket and Region are active (indicated by a value of `100`) or passive (indicated by a value of `0`).

## Contents
<a name="API_control_MultiRegionAccessPointRoute_Contents"></a>

 ** TrafficDialPercentage **   <a name="AmazonS3-Type-control_MultiRegionAccessPointRoute-TrafficDialPercentage"></a>
The traffic state for the specified bucket or AWS Region.
A value of `0` indicates a passive state, which means that no new traffic will be routed to the Region.
A value of `100` indicates an active state, which means that traffic will be routed to the specified Region.
When the routing configuration for a Region is changed from active to passive, any in-progress operations (uploads, copies, deletes, and so on) to the formerly active Region will continue to run to until a final success or failure status is reached.
If all Regions in the routing configuration are designated as passive, you'll receive an `InvalidRequest` error.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: Yes

 ** Bucket **   <a name="AmazonS3-Type-control_MultiRegionAccessPointRoute-Bucket"></a>
The name of the Amazon S3 bucket for which you'll submit a routing configuration change. Either the `Bucket` or the `Region` value must be provided. If both are provided, the bucket must be in the specified Region.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** Region **   <a name="AmazonS3-Type-control_MultiRegionAccessPointRoute-Region"></a>
The AWS Region to which you'll be submitting a routing configuration change. Either the `Bucket` or the `Region` value must be provided. If both are provided, the bucket must be in the specified Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_control_MultiRegionAccessPointRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/MultiRegionAccessPointRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/MultiRegionAccessPointRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/MultiRegionAccessPointRoute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

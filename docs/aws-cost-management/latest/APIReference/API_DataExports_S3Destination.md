---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_S3Destination.html
---

# S3Destination
<a name="API_DataExports_S3Destination"></a>

Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and object keys of a data exports file.

## Contents
<a name="API_DataExports_S3Destination_Contents"></a>

 ** S3Bucket **   <a name="awscostmanagement-Type-DataExports_S3Destination-S3Bucket"></a>
The name of the Amazon S3 bucket used as the destination of a data export file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** S3OutputConfigurations **   <a name="awscostmanagement-Type-DataExports_S3Destination-S3OutputConfigurations"></a>
The output configuration for the data export.
Type: [S3OutputConfigurations](API_DataExports_S3OutputConfigurations.md) object
Required: Yes

 ** S3Prefix **   <a name="awscostmanagement-Type-DataExports_S3Destination-S3Prefix"></a>
The S3 path prefix you want prepended to the name of your data export.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** S3Region **   <a name="awscostmanagement-Type-DataExports_S3Destination-S3Region"></a>
The S3 bucket Region.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

 ** S3BucketOwner **   <a name="awscostmanagement-Type-DataExports_S3Destination-S3BucketOwner"></a>
The Amazon Web Services account ID that owns the S3 bucket used as the destination for the data export.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_DataExports_S3Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/S3Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/S3Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/S3Destination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

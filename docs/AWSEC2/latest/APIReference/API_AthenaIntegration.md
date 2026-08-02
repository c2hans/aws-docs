---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AthenaIntegration.html
---

# AthenaIntegration
<a name="API_AthenaIntegration"></a>

Describes integration options for Amazon Athena.

## Contents
<a name="API_AthenaIntegration_Contents"></a>

 ** IntegrationResultS3DestinationArn **
The location in Amazon S3 to store the generated CloudFormation template.
Type: String
Required: Yes

 ** PartitionLoadFrequency **
The schedule for adding new partitions to the table.
Type: String
Valid Values: `none | daily | weekly | monthly`
Required: Yes

 ** PartitionEndDate **
The end date for the partition.
Type: Timestamp
Required: No

 ** PartitionStartDate **
The start date for the partition.
Type: Timestamp
Required: No

## See Also
<a name="API_AthenaIntegration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AthenaIntegration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AthenaIntegration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AthenaIntegration)

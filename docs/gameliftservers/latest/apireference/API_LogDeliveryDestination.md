---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_LogDeliveryDestination.html
---

# LogDeliveryDestination
<a name="API_LogDeliveryDestination"></a>

A single destination that receives game session placement insight logs for a game session queue.

**Note**
Amazon CloudWatch Logs vended log charges apply to each destination. Amazon S3 and Amazon Data Firehose destinations also incur their own service charges. For more information, see [Amazon CloudWatch Pricing](http://aws.amazon.com/cloudwatch/pricing/).

## Contents
<a name="API_LogDeliveryDestination_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LogDestination **   <a name="gameliftservers-Type-LogDeliveryDestination-LogDestination"></a>
The type of AWS resource that receives the game session placement insight logs. This value is required. Valid values are:
+  `CLOUDWATCH` -- an Amazon CloudWatch Logs log group.
+  `S3` -- an Amazon S3 bucket.
+  `FIREHOSE` -- an Amazon Data Firehose delivery stream.
Type: String
Valid Values: `CLOUDWATCH | S3 | FIREHOSE`
Required: Yes

 ** DestinationArn **   <a name="gameliftservers-Type-LogDeliveryDestination-DestinationArn"></a>
The Amazon Resource Name (ARN) of the resource that receives the game session placement insight logs. This resource must match the type that you specify in `LogDestination`. This value is required for `FIREHOSE` destinations. For `CLOUDWATCH` and `S3`, you can omit this value; Amazon GameLift Servers then creates a destination resource of the specified type on your behalf.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:[a-zA-Z0-9:/*._#-]+$`
Required: No

## See Also
<a name="API_LogDeliveryDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/LogDeliveryDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/LogDeliveryDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/LogDeliveryDestination)

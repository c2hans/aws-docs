---
source_url: https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/creating-a-decoder-lambda-function.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Creating a decoder Lambda function
<a name="creating-a-decoder-lambda-function"></a>

 The primary purpose of the Lambda decoder function is to intercept the incoming LoRaWAN bytes encoded in base64, and to convert them into a data format that is meaningful to downstream applications. In this solution, the Lambda function performs this conversion, reconstructs the river level reading from each of the respective bytes, and publishes this datapoint along with a timestamp as a JSON document. This data is published to the chosen topic in AWS IoT Core using MQTT, from where any number of rules and actions can be configured to forward the data to the required AWS service.

1.  First, create an AWS rule for the destination under **Act > Rules**.
![Screen showing creating an AWS IoT rule](https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/creating-iot-core-rule.png)

    This rule has an action to invoke the Lambda function, called (for the purpose of this paper) `myLoRaDecoderFunction`.

    The Lambda function uses the `base64` Python module to handle the conversion of the payload, before repackaging the necessary data as a JSON object. This is then published by the function to an MQTT topic using the `boto3` module.

1.  Configure the Lambda function with an [execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) with permissions to publish to the designated MQTT topic. The AWS IoT Core Developer Guide contains [example permissions](https://docs.aws.amazon.com/iot/latest/developerguide/pub-sub-policy.html) required to interact with the service.

    For example, the following IAM policy, when attached to the execution role of the Lambda function, allows the message to be published to the `myTopic/*` topic.

------
#### [ JSON ]

****

   ```
   {
       "Version":"2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "logs:CreateLogGroup",
               "Resource": "arn:aws:logs:{{eu-west-1}}:{{111111111111}}:*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "logs:CreateLogStream",
                   "logs:PutLogEvents"
               ],
               "Resource": [
                   "arn:aws:logs:{{eu-west-1}}:{{111111111111}}:log-group:/aws/lambda/myLoRaDecoderFunction:*"
               ]
           },
           {
               "Effect": "Allow",
               "Action": [
                   "iot:Publish"
               ],
               "Resource": [
                   "arn:aws:iot:{{eu-west-1}}:{{111111111111}}:topic/myTopic/*"
               ]
           }
       ]
   }
   ```

------
**Note**
 AWS account number `{{111111111111}}` is used for demonstration purposes only. This value must be replaced with the account number of the actual AWS account in use. It is also necessary to modify the Region specified in this example policy, if the deployment is not in `{{eu-west-1}}`.

    By monitoring this topic using the AWS IoT console under **Test**, you can see the expected data being published in JSON format.
![Screen showing confirming the receipt of decoded data](https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/images/confirm-receipt-of-decoded-data.png)

 From here, you can configure rules to implement any number of out-of-the-box AWS IoT actions to forward this data to the intended AWS service.

 For example, for a river level monitoring system, it might be beneficial for this data to be considered an input to a detector model in AWS IoT Events, so that the measurements can be interpreted and actioned in the context of predefined states. Alternatively, this data could populate a data lake in [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3), a time-series database in [Amazon Timestream](https://aws.amazon.com/timestream/), or a key-value table in [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). All of this is possible through built-in integrations via an AWS IoT rule and action.

---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/process-from-lexv2.html
---

# Processing messages from Amazon Lex V2 for Amazon Chime SDK messaging
<a name="process-from-lexv2"></a>

When sending messages to Amazon Lex V2, Amazon Chime SDK Messaging populates the `CHIME.channel.arn` and `CHIME.sender.arn` with the channel and sender’s ARN information as request attributes. You can use the attributes to determine who sent a message and the channel the sender belongs to. For more information, refer to [ Enabling custom logic with AWS Lambda functions](https://docs.aws.amazon.com/lexv2/latest/dg/lambda.html) in the *Amazon Lex V2 Developer Guide*.

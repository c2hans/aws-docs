---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/lambda-resource-policies.html
---

# AWS Lambda resource policies
<a name="lambda-resource-policies"></a>

## Control objective
<a name="control-objective.edcc3491-57b7-5874-a85d-09ada8f2bccc"></a>

***Identity perimeter**** – Only trusted identities can access my resources*

Control which services can invoke AWS Lambda functions by applying the following resource policy to AWS Lambda functions used with Amazon Bedrock Agents:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowBedrockAgentInvoke",
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock.amazonaws.com"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:bedrock-agent-*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:bedrock:us-east-1:123456789012:agent/*"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **AllowBedrockAgentInvoke** – Allows only Amazon Bedrock Agents service to invoke AWS Lambda functions, with additional conditions to prevent confused deputy attacks. The source account condition ensures the request originates from your account, while the source ARN condition validates the request comes from a legitimateAmazon Bedrock Agent.

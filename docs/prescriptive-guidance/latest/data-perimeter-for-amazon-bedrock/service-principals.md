---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/service-principals.html
---

# Service principals
<a name="service-principals"></a>

## Control Objective
<a name="control-objective.b07d5ff2-fdfe-5f9f-9cb4-79a9be421ad4"></a>

***Resource perimeter**** – My identities can access only trusted resources*

Amazon Bedrock often operates through service principals when integrated with other AWS services. Restrict these service principals to only the necessary actions and resources, and protect against confused deputy attacks using `aws:SourceAccount` and `aws:SourceArn` conditions.

**Bedrock Agents service role:**

Apply this trust policy to the IAM service role used by Amazon Bedrock Agents:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:bedrock:*:123456789012:agent/*"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **Trust policy** – Allows Amazon Bedrock service to assume this role only when the request originates from your account and from a legitimate Amazon Bedrock agent, preventing confused deputy attacks
+ **Confused deputy protection **– The `aws:SourceAccount` and `aws:SourceArn` conditions in the trust policy prevent confused deputy attacks where a malicious actor tricks the service into assuming your role. Always include both conditions when creating service roles.

Apply this permissions policy to the Amazon Bedrock agents service role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BedrockAgentModelAccess",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:*::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0"
      ]
    }
  ]
}
```

**Policy explanation:**
+ **BedrockAgentModelAccess** – Grants the Amazon Bedrock agent service role access to invoke the Claude Sonnet model with streaming capabilities for agent operations

### AWS Lambda integration with Amazon Bedrock
<a name="aws-lambda-integration-with-amazon-bedrock"></a>

Apply these trust policies to Lambda execution roles that need to invoke Bedrock models:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "123456789012"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:lambda:*:123456789012:function:bedrock-*"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **Trust policy** – Allows Lambda to assume this role only for functions with the "bedrock-" prefix in your account, preventing unauthorized Lambda functions from accessing Amazon Bedrockresources

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "LambdaBedrockAccess",
      "Effect": "Allow",
      "Action": "bedrock:InvokeModel",
      "Resource": "arn:aws:bedrock:*::foundation-model/amazon.titan-text-express-v1"
    }
  ]
}
```

**Policy explanation:**
+ **LambdaBedrockAccess** – Grants Lambda functions permission to invoke only the Titan Text Express model, implementing least privilege by restricting access to a single, cost-effective model for Lambda integrations
+ **Confused deputy protection **– The `aws:SourceAccount` and `aws:SourceArn` conditions in the trust policy prevent confused deputy attacks where a malicious actor tricks the service into assuming your role. Always include both conditions when creating service roles.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/layers-cfn.html
---

# Using AWS CloudFormation with layers
<a name="layers-cfn"></a>

You can use CloudFormation to create a layer and associate the layer with your Lambda function. The following example template creates a layer named `my-lambda-layer` and attaches the layer to the Lambda function using the **Layers** property.

In this example, the template specifies the Amazon Resource Name (ARN) of an existing IAM [execution role](lambda-intro-execution-role.md). You can also create a new execution role in the template using the CloudFormation [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html) resource.

Your function doesn't need any special permissions to use layers.

```
---
Description: CloudFormation Template for Lambda Function with Lambda Layer
Resources:
  MyLambdaLayer:
    Type: AWS::Lambda::LayerVersion
    Properties:
      LayerName: my-lambda-layer
      Description: My Lambda Layer
      Content:
        S3Bucket: amzn-s3-demo-bucket
        S3Key: my-layer.zip
      CompatibleRuntimes:
        - python3.9
        - python3.10
        - python3.11

  MyLambdaFunction:
    Type: AWS::Lambda::Function
    Properties:
      FunctionName: my-lambda-function
      Runtime: python3.9
      Handler: index.handler
      Timeout: 10
      Role: arn:aws:iam::{{111122223333}}:role/{{my_lambda_role}}
      Layers:
        - !Ref MyLambdaLayer
```

You can also use AWS Serverless Application Model to manage layers. For more information, see [Using AWS SAM with layers](layers-sam.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

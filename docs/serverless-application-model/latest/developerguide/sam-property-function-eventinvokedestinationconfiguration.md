---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-eventinvokedestinationconfiguration.html
---

# EventInvokeDestinationConfiguration
<a name="sam-property-function-eventinvokedestinationconfiguration"></a>

A configuration object that specifies the destination of an event after Lambda processes it.

## Syntax
<a name="sam-property-function-eventinvokedestinationconfiguration-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-eventinvokedestinationconfiguration-syntax.yaml"></a>

```
  [OnFailure](#sam-function-eventinvokedestinationconfiguration-onfailure): {{OnFailure}}
  [OnSuccess](#sam-function-eventinvokedestinationconfiguration-onsuccess): {{OnSuccess}}
```

## Properties
<a name="sam-property-function-eventinvokedestinationconfiguration-properties"></a>

 `OnFailure`   <a name="sam-function-eventinvokedestinationconfiguration-onfailure"></a>
A destination for events that failed processing.
*Type*: [OnFailure](sam-property-function-onfailure.md)
*Required*: No
*CloudFormation compatibility*: This property is similar to the `[OnFailure](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-onfailure.html)` property of an `AWS::Lambda::EventInvokeConfig` resource. Requires `Type`, an additional SAM-only property.

 `OnSuccess`   <a name="sam-function-eventinvokedestinationconfiguration-onsuccess"></a>
A destination for events that were processed successfully.
*Type*: [OnSuccess](sam-property-function-onsuccess.md)
*Required*: No
*CloudFormation compatibility*: This property is similar to the `[OnSuccess](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventinvokeconfig-onsuccess)` property of an `AWS::Lambda::EventInvokeConfig` resource. Requires `Type`, an additional SAM-only property.

## Examples
<a name="sam-property-function-eventinvokedestinationconfiguration--examples"></a>

### OnSuccess
<a name="sam-property-function-eventinvokedestinationconfiguration--examples--onsuccess"></a>

OnSuccess example

#### YAML
<a name="sam-property-function-eventinvokedestinationconfiguration--examples--onsuccess--yaml"></a>

```
EventInvokeConfig:
  DestinationConfig:
    OnSuccess:
      Type: SQS
      Destination: arn:aws:sqs:us-west-2:012345678901:my-queue
    OnFailure:
      Type: Lambda
      Destination: !GetAtt DestinationLambda.Arn
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

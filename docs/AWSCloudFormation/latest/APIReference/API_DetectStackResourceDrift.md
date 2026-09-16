---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DetectStackResourceDrift.html
---

# DetectStackResourceDrift
<a name="API_DetectStackResourceDrift"></a>

Returns information about whether a resource's actual configuration differs, or has *drifted*, from its expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see [Detect unmanaged configuration changes to stacks and resources with drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html).

Use `DetectStackResourceDrift` to detect drift on individual resources, or [DetectStackDrift](API_DetectStackDrift.md) to detect drift on all resources in a given stack that support drift detection.

Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see [Resource type support for imports and drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html).

## Request Parameters
<a name="API_DetectStackResourceDrift_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** LogicalResourceId **
The logical name of the resource for which to return drift information.
Type: String
Required: Yes

 ** StackName **
The name of the stack to which the resource belongs.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `([a-zA-Z][-a-zA-Z0-9]*)|(arn:\b(aws|aws-us-gov|aws-cn)\b:[-a-zA-Z0-9:/._+]*)`
Required: Yes

## Response Elements
<a name="API_DetectStackResourceDrift_ResponseElements"></a>

The following element is returned by the service.

 ** StackResourceDrift **
Information about whether the resource's actual configuration has drifted from its expected template configuration, including actual and expected property values and any differences detected.
Type: [StackResourceDrift](API_StackResourceDrift.md) object

## Errors
<a name="API_DetectStackResourceDrift_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DetectStackResourceDrift_Examples"></a>

### DetectStackResourceDrift
<a name="API_DetectStackResourceDrift_Example_1"></a>

This example illustrates one usage of DetectStackResourceDrift.

#### Sample Request
<a name="API_DetectStackResourceDrift_Example_1_Request"></a>

```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DetectStackResourceDrift
 &Version=2010-05-15
 &LogicalResourceId=Queue
 &StackName=my-stack-with-resource-drift
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20171211T230005Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response
<a name="API_DetectStackResourceDrift_Example_1_Response"></a>

```
<DetectStackResourceDriftResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DetectStackResourceDriftResult>
    <StackResourceDrift>
      <PropertyDifferences>
        <member>
          <ActualValue>120</ActualValue>
          <ExpectedValue>20</ExpectedValue>
          <DifferenceType>NOT_EQUAL</DifferenceType>
          <PropertyPath>/DelaySeconds</PropertyPath>
        </member>
        <member>
          <ActualValue>12</ActualValue>
          <ExpectedValue>10</ExpectedValue>
          <DifferenceType>NOT_EQUAL</DifferenceType>
          <PropertyPath>/RedrivePolicy/maxReceiveCount</PropertyPath>
        </member>
      </PropertyDifferences>
      <PhysicalResourceId>https://sqs.us-east-1.amazonaws.com/012345678910/my-stack-with-resource-drift-Queue-494PBHCO76H4</PhysicalResourceId>
      <ExpectedProperties>{
        "ReceiveMessageWaitTimeSeconds":0,
        "DelaySeconds":20,
        "RedrivePolicy":{
          "deadLetterTargetArn":"arn:aws:sqs:us-east-1:012345678910:my-stack-with-resource-drift-DLQ-1BCY7HHD5QIM3",
          "maxReceiveCount":10
          },
        "MessageRetentionPeriod":345600,
        "MaximumMessageSize":262144,
        "VisibilityTimeout":60,
        "QueueName":"my-stack-with-resource-drift-Queue-494PBHCO76H4"
        }
      </ExpectedProperties>
      <StackResourceDriftStatus>MODIFIED</StackResourceDriftStatus>
      <StackId>arn:aws:cloudformation:us-east-1:012345678910:stack/my-stack-with-resource-drift/489e5570-df85-11e7-a7d9-503acac5c0fd</StackId>
      <LogicalResourceId>Queue</LogicalResourceId>
      <ActualProperties>{
        "ReceiveMessageWaitTimeSeconds":0,
        "DelaySeconds":120,
        "RedrivePolicy":{
          "deadLetterTargetArn":"arn:aws:sqs:us-east-1:012345678910:my-stack-with-resource-drift-DLQ-1BCY7HHD5QIM3",
          "maxReceiveCount":12
          },
        "MessageRetentionPeriod":345600,
        "MaximumMessageSize":262144,
        "VisibilityTimeout":60,
        "QueueName":"my-stack-with-resource-drift-Queue-494PBHCO76H4"
        }
      </ActualProperties>
      <Timestamp>2017-12-28T23:51:49.616Z</Timestamp>
      <ResourceType>AWS::SQS::Queue</ResourceType>
    </StackResourceDrift>
  </DetectStackResourceDriftResult>
  <ResponseMetadata>
    <RequestId>1229a48a-ec2a-11e7-a8e5-97a4c2fc6398</RequestId>
  </ResponseMetadata>
</DetectStackResourceDriftResponse>
```

## See Also
<a name="API_DetectStackResourceDrift_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DetectStackResourceDrift)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudformation-2010-05-15/DetectStackResourceDrift)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DetectStackResourceDrift)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DetectStackResourceDrift)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DetectStackResourceDrift)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DetectStackResourceDrift)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DetectStackResourceDrift)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DetectStackResourceDrift)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DetectStackResourceDrift)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DetectStackResourceDrift)

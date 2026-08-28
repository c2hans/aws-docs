---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeScalingProcessTypes.html
---

# DescribeScalingProcessTypes
<a name="API_DescribeScalingProcessTypes"></a>

Describes the scaling process types for use with the [ResumeProcesses](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ResumeProcesses.html) and [SuspendProcesses](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SuspendProcesses.html) APIs.

## Response Elements
<a name="API_DescribeScalingProcessTypes_ResponseElements"></a>

The following element is returned by the service.

 **Processes.member.N**
The names of the process types.
Type: Array of [ProcessType](API_ProcessType.md) objects

## Errors
<a name="API_DescribeScalingProcessTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_DescribeScalingProcessTypes_Examples"></a>

### Example
<a name="API_DescribeScalingProcessTypes_Example_1"></a>

This example illustrates one usage of DescribeScalingProcessTypes.

#### Sample Request
<a name="API_DescribeScalingProcessTypes_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=DescribeScalingProcessTypes
&Version=2011-01-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeScalingProcessTypes_Example_1_Response"></a>

```
<DescribeScalingProcessTypesResponse xmlns="https://autoscaling.amazonaws.com/doc/2011-01-01/">
  <DescribeScalingProcessTypesResult>
    <Processes>
      <member>
        <ProcessName>AZRebalance</ProcessName>
      </member>
      <member>
        <ProcessName>AddToLoadBalancer</ProcessName>
      </member>
      <member>
        <ProcessName>AlarmNotification</ProcessName>
      </member>
      <member>
        <ProcessName>HealthCheck</ProcessName>
      </member>
      <member>
        <ProcessName>InstanceRefresh</ProcessName>
      </member>
      <member>
        <ProcessName>Launch</ProcessName>
      </member>
      <member>
        <ProcessName>ReplaceUnhealthy</ProcessName>
      </member>
      <member>
        <ProcessName>ScheduledActions</ProcessName>
      </member>
      <member>
        <ProcessName>Terminate</ProcessName>
      </member>
    </Processes>
  </DescribeScalingProcessTypesResult>
  <ResponseMetadata>
    <RequestId>7c6e177f-f082-11e1-ac58-3714bEXAMPLE</RequestId>
  </ResponseMetadata>
</DescribeScalingProcessTypesResponse>
```

## See Also
<a name="API_DescribeScalingProcessTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/DescribeScalingProcessTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/DescribeScalingProcessTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/DescribeScalingProcessTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/DescribeScalingProcessTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/DescribeScalingProcessTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/DescribeScalingProcessTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/DescribeScalingProcessTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/DescribeScalingProcessTypes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/DescribeScalingProcessTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/DescribeScalingProcessTypes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

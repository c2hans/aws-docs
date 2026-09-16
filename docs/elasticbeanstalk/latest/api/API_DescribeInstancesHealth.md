---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeInstancesHealth.html
---

# DescribeInstancesHealth
<a name="API_DescribeInstancesHealth"></a>

Retrieves detailed information about the health of instances in your AWS Elastic Beanstalk environments. This operation requires [enhanced health reporting](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced.html).

This action only returns information about environments that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three environments. When the user calls this action, the response will only include the one environment that the user has permission to access instead of all three environments. If the user doesn’t have access to any of the environments an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Request Parameters
<a name="API_DescribeInstancesHealth_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AttributeNames.member.N**
Specifies the response elements you wish to receive. To retrieve all attributes, set to `All`. If no attribute names are specified, returns a list of instances.
Type: Array of strings
Valid Values: `HealthStatus | Color | Causes | ApplicationMetrics | RefreshedAt | LaunchedAt | System | Deployment | AvailabilityZone | InstanceType | All`
Required: No

 ** EnvironmentId **
Specify the AWS Elastic Beanstalk environment by ID.
Type: String
Required: No

 ** EnvironmentName **
Specify the AWS Elastic Beanstalk environment by name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** NextToken **
Specify the pagination token returned by a previous call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_DescribeInstancesHealth_ResponseElements"></a>

The following elements are returned by the service.

 **InstanceHealthList.member.N**
Detailed health information about each instance.
The output differs slightly between Linux and Windows environments. There is a difference in the members that are supported under the `<CPUUtilization>` type.
Type: Array of [SingleInstanceHealth](API_SingleInstanceHealth.md) objects

 ** NextToken **
Pagination token for the next page of results, if available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** RefreshedAt **
The date and time that the health information was retrieved.
Type: Timestamp

## Errors
<a name="API_DescribeInstancesHealth_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ElasticBeanstalkService **
A generic service exception has occurred.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InvalidRequest **
One or more input parameters is not valid. Please correct the input parameters and try the operation again.
HTTP Status Code: 400

## Examples
<a name="API_DescribeInstancesHealth_Examples"></a>

### Request a single instance health attribute
<a name="API_DescribeInstancesHealth_Example_1"></a>

This example illustrates one usage of DescribeInstancesHealth.

```
DescribeInstancesHealth
{"EnvironmentName":"test-1","AttributeNames":["HealthStatus"]}

<DescribeInstancesHealthResponse xmlns='http://elasticbeanstalk.amazonaws.com/docs/2010-12-01/'>
  <DescribeInstancesHealthResult>
    <InstanceHealthList>
      <member>
        <HealthStatus>Degraded</HealthStatus>
        <InstanceId>i-dc6ee922</InstanceId>
      </member>
    </InstanceHealthList>
  </DescribeInstancesHealthResult>
  <ResponseMetadata>
    <RequestId>94808e26-3a47-11e5-94eb-3d0f44fb8967</RequestId>
  </ResponseMetadata>
</DescribeInstancesHealthResponse>
```

### Request all instance health attributes for a Linux environment
<a name="API_DescribeInstancesHealth_Example_2"></a>

This example shows the output for a Linux environment.

```
DescribeInstancesHealth
{"EnvironmentName":"test-1","AttributeNames":["All"]}

<DescribeInstancesHealthResponse xmlns='http://elasticbeanstalk.amazonaws.com/docs/2010-12-01/'>
  <DescribeInstancesHealthResult>
    <InstanceHealthList>
      <member>
        <HealthStatus>Degraded</HealthStatus>
        <System>
          <CPUUtilization>
            <Idle>6.9</Idle>
            <System>46.2</System>
            <Privileged>null</Privileged>
            <SoftIRQ>0.6</SoftIRQ>
            <Nice>0.0</Nice>
            <IOWait>0.1</IOWait>
            <User>46.2</User>
            <IRQ>0.0</IRQ>
          </CPUUtilization>
          <LoadAverage>
            <member>3.81</member>
            <member>2.11</member>
            <member>0.93</member>
          </LoadAverage>
        </System>
        <LaunchedAt>2015-07-17T07:58:58Z</LaunchedAt>
        <Color>Red</Color>
        <InstanceId>i-dc6ee922</InstanceId>
        <ApplicationMetrics>
          <Duration>10</Duration>
          <StatusCodes>
            <Status5xx>843</Status5xx>
            <Status4xx>0</Status4xx>
            <Status3xx>0</Status3xx>
            <Status2xx>3391</Status2xx>
          </StatusCodes>
          <Latency>
            <P90>0.002</P90>
            <P999>1.367</P999>
            <P99>0.003</P99>
            <P85>0.002</P85>
            <P50>0.001</P50>
            <P75>0.001</P75>
            <P95>0.002</P95>
            <P10>0.0</P10>
          </Latency>
          <RequestCount>4234</RequestCount>
        </ApplicationMetrics>
        <Causes>
          <member>19.9 % of the requests are failing with HTTP 5xx.</member>
          <member>93 % of CPU is in use.</member>
        </Causes>
      </member>
    </InstanceHealthList>
    <RefreshedAt>2015-08-04T01:24:34Z</RefreshedAt>
  </DescribeInstancesHealthResult>
  <ResponseMetadata>
    <RequestId>94a07242-3a47-11e5-91c3-1f9989a744d4</RequestId>
  </ResponseMetadata>
</DescribeInstancesHealthResponse>
```

### Request all instance health attributes for a Windows environment
<a name="API_DescribeInstancesHealth_Example_3"></a>

In a Windows environment, there are different supported members in the `<CPUUtilization>` type:

```
        ...
          <CPUUtilization>
            <Idle>9.6</Idle>
            <System>null</System>
            <Privileged>45.2</Privileged>
            <SoftIRQ>null</SoftIRQ>
            <Nice>null</Nice>
            <IOWait>null</IOWait>
            <User>45.2</User>
            <IRQ>null</IRQ>
          </CPUUtilization>
        ...
```

## See Also
<a name="API_DescribeInstancesHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeInstancesHealth)

---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentHealth.html
---

# DescribeEnvironmentHealth
<a name="API_DescribeEnvironmentHealth"></a>

Returns information about the overall health of the specified environment. The **DescribeEnvironmentHealth** operation is only available with AWS Elastic Beanstalk Enhanced Health.

This action only returns information about environments that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three environments. When the user calls this action, the response will only include the one environment that the user has permission to access instead of all three environments. If the user doesn’t have access to any of the environments an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Request Parameters
<a name="API_DescribeEnvironmentHealth_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AttributeNames.member.N**
Specify the response elements to return. To retrieve all attributes, set to `All`. If no attribute names are specified, returns the name of the environment.
Type: Array of strings
Valid Values: `Status | Color | Causes | ApplicationMetrics | InstancesHealth | All | HealthStatus | RefreshedAt`
Required: No

 ** EnvironmentId **
Specify the environment by ID.
You must specify either this or an EnvironmentName, or both.
Type: String
Required: No

 ** EnvironmentName **
Specify the environment by name.
You must specify either this or an EnvironmentName, or both.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

## Response Elements
<a name="API_DescribeEnvironmentHealth_ResponseElements"></a>

The following elements are returned by the service.

 ** ApplicationMetrics **
Application request metrics for the environment.
Type: [ApplicationMetrics](API_ApplicationMetrics.md) object

 **Causes.member.N**
Descriptions of the data that contributed to the environment's current health status.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** Color **
The [health color](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html) of the environment.
Type: String

 ** EnvironmentName **
The environment's name.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.

 ** HealthStatus **
The [health status](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-enhanced-status.html) of the environment. For example, `Ok`.
Type: String

 ** InstancesHealth **
Summary health information for the instances in the environment.
Type: [InstanceHealthSummary](API_InstanceHealthSummary.md) object

 ** RefreshedAt **
The date and time that the health information was retrieved.
Type: Timestamp

 ** Status **
The environment's operational status. `Ready`, `Launching`, `Updating`, `Terminating`, or `Terminated`.
Type: String
Valid Values: `Green | Yellow | Red | Grey`

## Errors
<a name="API_DescribeEnvironmentHealth_Errors"></a>

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
<a name="API_DescribeEnvironmentHealth_Examples"></a>

### Request a single environment health attribute
<a name="API_DescribeEnvironmentHealth_Example_1"></a>

This example illustrates one usage of DescribeEnvironmentHealth.

```
DescribeEnvironmentHealth
{"EnvironmentName":"test-1","AttributeNames":["HealthStatus"]}

<DescribeEnvironmentHealthResponse xmlns='http://elasticbeanstalk.amazonaws.com/docs/2010-12-01/'>
  <DescribeEnvironmentHealthResult>
    <HealthStatus>Degraded</HealthStatus>
    <EnvironmentName>test-1</EnvironmentName>
  </DescribeEnvironmentHealthResult>
  <ResponseMetadata>
    <RequestId>93ab63d3-3a47-11e5-94eb-3d0f44fb8967</RequestId>
  </ResponseMetadata>
</DescribeEnvironmentHealthResponse>
```

### Request all environment health attributes
<a name="API_DescribeEnvironmentHealth_Example_2"></a>

This example illustrates one usage of DescribeEnvironmentHealth.

```
DescribeEnvironmentHealth
{"EnvironmentName":"test-1","AttributeNames":["All"]}

<DescribeEnvironmentHealthResponse xmlns='http://elasticbeanstalk.amazonaws.com/docs/2010-12-01/'>
  <DescribeEnvironmentHealthResult>
    <HealthStatus>Degraded</HealthStatus>
    <Color>Red</Color>
    <Status>Ready</Status>
    <EnvironmentName>test-1</EnvironmentName>
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
    <RefreshedAt>2015-08-04T01:24:34Z</RefreshedAt>
    <Causes>
      <member>19.9 % of the requests are failing with HTTP 5xx.</member>
      <member>1 instance online is below Auto Scaling group minimum size 2.</member>
    </Causes>
    <InstancesHealth>
      <Degraded>1</Degraded>
      <Pending>0</Pending>
      <Ok>0</Ok>
      <NoData>0</NoData>
      <Unknown>0</Unknown>
      <Severe>0</Severe>
      <Warning>0</Warning>
      <Info>0</Info>
    </InstancesHealth>
  </DescribeEnvironmentHealthResult>
  <ResponseMetadata>
    <RequestId>9460aa20-3a47-11e5-91c3-1f9989a744d4</RequestId>
  </ResponseMetadata>
</DescribeEnvironmentHealthResponse>
```

## See Also
<a name="API_DescribeEnvironmentHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeEnvironmentHealth)

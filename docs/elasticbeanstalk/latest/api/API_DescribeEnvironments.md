---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html
---

# DescribeEnvironments
<a name="API_DescribeEnvironments"></a>

Returns descriptions for existing environments.

This action only returns information about environments that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three environments. When the user calls the *DescribeEnvironments* action, the response will only include the one environment that the user has permission to access instead of all three environments. If the user doesn’t have access to any of the environments an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Request Parameters
<a name="API_DescribeEnvironments_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 **EnvironmentIds.member.N**
If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified IDs.
Type: Array of strings
Required: No

 **EnvironmentNames.member.N**
If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that have the specified names.
Type: Array of strings
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** IncludedDeletedBackTo **
 If specified when `IncludeDeleted` is set to `true`, then environments deleted after this date are displayed.
Type: Timestamp
Required: No

 ** IncludeDeleted **
Indicates whether to include deleted environments:
 `true`: Environments that have been deleted after `IncludedDeletedBackTo` are displayed.
 `false`: Do not include deleted environments.
Type: Boolean
Required: No

 ** MaxRecords **
For a paginated request. Specify a maximum number of environments to include in each response.
If no `MaxRecords` is specified, all available environments are retrieved in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** NextToken **
For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.
If no `NextToken` is specified, the first page is retrieved.
Type: String
Required: No

 ** VersionLabel **
If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those that are associated with this application version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_DescribeEnvironments_ResponseElements"></a>

The following elements are returned by the service.

 **Environments.member.N**
 Returns an [EnvironmentDescription](API_EnvironmentDescription.md) list.
Type: Array of [EnvironmentDescription](API_EnvironmentDescription.md) objects

 ** NextToken **
In a paginated request, the token that you can pass in a subsequent request to get the next response page.
Type: String

## Errors
<a name="API_DescribeEnvironments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeEnvironments_Examples"></a>

### Example
<a name="API_DescribeEnvironments_Example_1"></a>

This example illustrates one usage of DescribeEnvironments.

#### Sample Request
<a name="API_DescribeEnvironments_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&IncludeDeleted=true
&IncludedDeletedBackTo=2008-11-05T06%3A00%3A00Z
&Operation=DescribeEnvironments
&AuthParams
```

#### Sample Response
<a name="API_DescribeEnvironments_Example_1_Response"></a>

```
<DescribeEnvironmentsResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <DescribeEnvironmentsResult>
    <Environments>
      <member>
        <VersionLabel>Version1</VersionLabel>
        <Status>Available</Status>
        <ApplicationName>SampleApp</ApplicationName>
        <EndpointURL>elasticbeanstalk-SampleApp-1394386994.us-east-1.elb.amazonaws.com</EndpointURL>
        <CNAME>SampleApp-jxb293wg7n.elasticbeanstalk.amazonaws.com</CNAME>
        <Health>Green</Health>
        <EnvironmentId>e-icsgecu3wf</EnvironmentId>
        <DateUpdated>2010-11-17T04:01:40.668Z</DateUpdated>
        <SolutionStackName>32bit Amazon Linux running Tomcat 7</SolutionStackName>
        <Description>EnvDescrip</Description>
        <EnvironmentName>SampleApp</EnvironmentName>
        <DateCreated>2010-11-17T03:59:33.520Z</DateCreated>
      </member>
    </Environments>
  </DescribeEnvironmentsResult>
  <ResponseMetadata>
    <RequestId>44790c68-f260-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DescribeEnvironmentsResponse>
```

## See Also
<a name="API_DescribeEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeEnvironments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeEnvironments)

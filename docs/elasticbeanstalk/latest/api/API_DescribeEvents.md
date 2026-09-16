---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEvents.html
---

# DescribeEvents
<a name="API_DescribeEvents"></a>

Returns list of event descriptions matching criteria up to the last 6 weeks.

This action returns the most recent 1,000 events from the specified `NextToken`.

This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Request Parameters
<a name="API_DescribeEvents_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
If specified, AWS Elastic Beanstalk restricts the returned descriptions to include only those associated with this application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** EndTime **
 If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur up to, but not including, the `EndTime`.
Type: Timestamp
Required: No

 ** EnvironmentId **
If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.
Type: String
Required: No

 ** EnvironmentName **
If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this environment.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** MaxRecords **
Specifies the maximum number of events that can be returned, beginning with the most recent event.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** NextToken **
Pagination token. If specified, the events return the next batch of results.
Type: String
Required: No

 ** PlatformArn **
The ARN of a custom platform version. If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this custom platform version.
Type: String
Required: No

 ** RequestId **
If specified, AWS Elastic Beanstalk restricts the described events to include only those associated with this request ID.
Type: String
Required: No

 ** Severity **
If specified, limits the events returned from this call to include only those with the specified severity or higher.
Type: String
Valid Values: `TRACE | DEBUG | INFO | WARN | ERROR | FATAL`
Required: No

 ** StartTime **
If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that occur on or after this time.
Type: Timestamp
Required: No

 ** TemplateName **
If specified, AWS Elastic Beanstalk restricts the returned descriptions to those that are associated with this environment configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** VersionLabel **
If specified, AWS Elastic Beanstalk restricts the returned descriptions to those associated with this application version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_DescribeEvents_ResponseElements"></a>

The following elements are returned by the service.

 **Events.member.N**
 A list of [EventDescription](API_EventDescription.md).
Type: Array of [EventDescription](API_EventDescription.md) objects

 ** NextToken **
 If returned, this indicates that there are more results to obtain. Use this token in the next [DescribeEvents](#API_DescribeEvents) call to get the next batch of events.
Type: String

## Errors
<a name="API_DescribeEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeEvents_Examples"></a>

### Example
<a name="API_DescribeEvents_Example_1"></a>

This example illustrates one usage of DescribeEvents.

#### Sample Request
<a name="API_DescribeEvents_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&Severity=TRACE
&StartTime=2010-11-17T10%3A26%3A40Z
&Operation=DescribeEvents
&AuthParams
```

#### Sample Response
<a name="API_DescribeEvents_Example_1_Response"></a>

```
          <DescribeEventsResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <DescribeEventsResult>
    <Events>
      <member>
        <Message>Successfully completed createEnvironment activity.</Message>
        <EventDate>2010-11-17T20:25:35.191Z</EventDate>
        <VersionLabel>New Version</VersionLabel>
        <RequestId>bb01fa74-f287-11df-8a78-9f77047e0d0c</RequestId>
        <ApplicationName>SampleApp</ApplicationName>
        <EnvironmentName>SampleAppVersion</EnvironmentName>
        <Severity>INFO</Severity>
      </member>
      <member>
        <Message>Launching a new EC2 instance: i-04a8c569</Message>
        <EventDate>2010-11-17T20:21:30Z</EventDate>
        <VersionLabel>New Version</VersionLabel>
        <ApplicationName>SampleApp</ApplicationName>
        <EnvironmentName>SampleAppVersion</EnvironmentName>
        <Severity>DEBUG</Severity>
      </member>
      <member>
        <Message>At least one EC2 instance has entered the InService lifecycle state.</Message>
        <EventDate>2010-11-17T20:20:32.008Z</EventDate>
        <VersionLabel>New Version</VersionLabel>
        <RequestId>bb01fa74-f287-11df-8a78-9f77047e0d0c</RequestId>
        <ApplicationName>SampleApp</ApplicationName>
        <EnvironmentName>SampleAppVersion</EnvironmentName>
        <Severity>INFO</Severity>
      </member>
      <member>
        <Message>Elastic Load Balancer elasticbeanstalk-SampleAppVersion has failed 0 healthy instances - Environment may not be available.</Message>
        <EventDate>2010-11-17T20:19:28Z</EventDate>
        <VersionLabel>New Version</VersionLabel>
        <ApplicationName>SampleApp</ApplicationName>
        <EnvironmentName>SampleAppVersion</EnvironmentName>
        <Severity>WARN</Severity>
      </member>
    </Events>
  </DescribeEventsResult>
  <ResponseMetadata>
    <RequestId>f10d02dd-f288-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DescribeEventsResponse>
```

## See Also
<a name="API_DescribeEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeEvents)

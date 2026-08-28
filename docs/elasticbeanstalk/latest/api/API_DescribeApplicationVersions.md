---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplicationVersions.html
---

# DescribeApplicationVersions
<a name="API_DescribeApplicationVersions"></a>

Retrieve a list of application versions.

This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Request Parameters
<a name="API_DescribeApplicationVersions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
Specify an application name to show only application versions for that application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** MaxRecords **
For a paginated request. Specify a maximum number of application versions to include in each response.
If no `MaxRecords` is specified, all available application versions are retrieved in a single response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** NextToken **
For a paginated request. Specify a token from a previous response page to retrieve the next response page. All other parameter values must be identical to the ones specified in the initial request.
If no `NextToken` is specified, the first page is retrieved.
Type: String
Required: No

 **VersionLabels.member.N**
Specify a version label to show a specific application version.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_DescribeApplicationVersions_ResponseElements"></a>

The following elements are returned by the service.

 **ApplicationVersions.member.N**
List of `ApplicationVersionDescription` objects sorted in order of creation.
Type: Array of [ApplicationVersionDescription](API_ApplicationVersionDescription.md) objects

 ** NextToken **
In a paginated request, the token that you can pass in a subsequent request to get the next response page.
Type: String

## Errors
<a name="API_DescribeApplicationVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeApplicationVersions_Examples"></a>

### Example
<a name="API_DescribeApplicationVersions_Example_1"></a>

This example illustrates one usage of DescribeApplicationVersions.

#### Sample Request
<a name="API_DescribeApplicationVersions_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&Operation=DescribeApplicationVersions
&AuthParams
```

#### Sample Response
<a name="API_DescribeApplicationVersions_Example_1_Response"></a>

```
<DescribeApplicationVersionsResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <DescribeApplicationVersionsResult>
    <ApplicationVersions>
      <member>
        <SourceBundle>
          <S3Bucket>amazonaws.com</S3Bucket>
          <S3Key>sample.war</S3Key>
        </SourceBundle>
        <VersionLabel>Version1</VersionLabel>
        <Description>description</Description>
        <ApplicationName>SampleApp</ApplicationName>
        <DateCreated>2010-11-17T03:21:59.161Z</DateCreated>
        <DateUpdated>2010-11-17T03:21:59.161Z</DateUpdated>
      </member>
    </ApplicationVersions>
  </DescribeApplicationVersionsResult>
  <ResponseMetadata>
    <RequestId>773cd80a-f26c-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DescribeApplicationVersionsResponse>
```

## See Also
<a name="API_DescribeApplicationVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeApplicationVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeApplicationVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeApplicationVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeApplicationVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeApplicationVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeApplicationVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeApplicationVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeApplicationVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeApplicationVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeApplicationVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

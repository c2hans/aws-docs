---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplications.html
---

# DescribeApplications
<a name="API_DescribeApplications"></a>

Returns the descriptions of existing applications.

This action only returns information about applications that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access two of three applications. When the user calls the *DescribeApplications* action, the response will only include the two applications that the user has permission to access instead of all three applications. If the user doesn’t have access to any of the applications an empty result is returned.

**Note**
The *AWSElasticBeanstalkReadOnly* managed policy allows operators to view information about resources related to Elastic Beanstalk environments. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Request Parameters
<a name="API_DescribeApplications_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ApplicationNames.member.N**
If specified, AWS Elastic Beanstalk restricts the returned descriptions to only include those with the specified names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## Response Elements
<a name="API_DescribeApplications_ResponseElements"></a>

The following element is returned by the service.

 **Applications.member.N**
This parameter contains a list of [ApplicationDescription](API_ApplicationDescription.md).
Type: Array of [ApplicationDescription](API_ApplicationDescription.md) objects

## Errors
<a name="API_DescribeApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeApplications_Examples"></a>

### Example
<a name="API_DescribeApplications_Example_1"></a>

This example illustrates one usage of DescribeApplications.

#### Sample Request
<a name="API_DescribeApplications_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationNames.member.1=SampleApplication
&Operation=DescribeApplications
&AuthParams
```

#### Sample Response
<a name="API_DescribeApplications_Example_1_Response"></a>

```
<DescribeApplicationsResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <DescribeApplicationsResult>
    <Applications>
      <member>
        <Versions/>
        <Description>Sample Description</Description>
        <ApplicationName>SampleApplication</ApplicationName>
        <DateCreated>2010-11-16T20:20:51.974Z</DateCreated>
        <DateUpdated>2010-11-16T20:20:51.974Z</DateUpdated>
        <ConfigurationTemplates>
          <member>Default</member>
        </ConfigurationTemplates>
      </member>
    </Applications>
  </DescribeApplicationsResult>
  <ResponseMetadata>
    <RequestId>577c70ff-f1d7-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DescribeApplicationsResponse>
```

## See Also
<a name="API_DescribeApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeApplications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

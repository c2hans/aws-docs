---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeAccountAttributes.html
---

# DescribeAccountAttributes
<a name="API_DescribeAccountAttributes"></a>

Returns attributes related to AWS Elastic Beanstalk that are associated with the calling AWS account.

The result currently has one set of attributes—resource quotas.

This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Response Elements
<a name="API_DescribeAccountAttributes_ResponseElements"></a>

The following element is returned by the service.

 ** ResourceQuotas **
The Elastic Beanstalk resource quotas associated with the calling AWS account.
Type: [ResourceQuotas](API_ResourceQuotas.md) object

## Errors
<a name="API_DescribeAccountAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

## Examples
<a name="API_DescribeAccountAttributes_Examples"></a>

### Example
<a name="API_DescribeAccountAttributes_Example_1"></a>

This example illustrates one usage of DescribeAccountAttributes.

#### Sample Request
<a name="API_DescribeAccountAttributes_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?Operation=DescribeAccountAttributes
&AuthParams
```

#### Sample Response
<a name="API_DescribeAccountAttributes_Example_1_Response"></a>

```
<DescribeAccountAttributesResponse xmlns="http://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <DescribeAccountAttributesResult>
    <ResourceQuotas>
      <ConfigurationTemplateQuota>
        <Maximum>2000</Maximum>
      </ConfigurationTemplateQuota>
      <ApplicationVersionQuota>
        <Maximum>1000</Maximum>
      </ApplicationVersionQuota>
      <CustomPlatformQuota>
        <Maximum>50</Maximum>
      </CustomPlatformQuota>
      <EnvironmentQuota>
        <Maximum>200</Maximum>
      </EnvironmentQuota>
      <ApplicationQuota>
        <Maximum>75</Maximum>
      </ApplicationQuota>
    </ResourceQuotas>
  </DescribeAccountAttributesResult>
  <ResponseMetadata>
    <RequestId>24fc4d65-1308-49e6-9b85-a0a8838f3b4b</RequestId>
  </ResponseMetadata>
</DescribeAccountAttributesResponse>
```

## See Also
<a name="API_DescribeAccountAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeAccountAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeAccountAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeAccountAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeAccountAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeAccountAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeAccountAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeAccountAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeAccountAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeAccountAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeAccountAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

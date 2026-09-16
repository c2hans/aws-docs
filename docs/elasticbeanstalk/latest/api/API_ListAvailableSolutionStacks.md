---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html
---

# ListAvailableSolutionStacks
<a name="API_ListAvailableSolutionStacks"></a>

Returns a list of the available solution stack names, with the public version first and then in reverse chronological order.

This action only returns information about resources that the calling principle has IAM permissions to access. For example, consider a case where a user only has permission to access one of three resources. When the user calls the this action, the response will only include the one resource that the user has permission to access instead of all three resources. If the user doesn’t have access to any of the resources an empty result is returned.

**Note**
The [AWSElasticBeanstalkReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticBeanstalkReadOnly.html) managed policy allows operators to view information about resources related to Elastic Beanstalk. For more information, see [ Managing Elastic Beanstalk user policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html) in the * AWS Elastic Beanstalk Developer Guide*. For detailed instructions to attach a policy to a user or group, see the section [ Controlling access with managed policies](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.iam.managed-policies.html#iam-userpolicies-managed) in the same topic.

## Response Elements
<a name="API_ListAvailableSolutionStacks_ResponseElements"></a>

The following elements are returned by the service.

 **SolutionStackDetails.member.N**
 A list of available solution stacks and their [SolutionStackDescription](API_SolutionStackDescription.md).
Type: Array of [SolutionStackDescription](API_SolutionStackDescription.md) objects

 **SolutionStacks.member.N**
A list of available solution stacks.
Type: Array of strings

## Errors
<a name="API_ListAvailableSolutionStacks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ListAvailableSolutionStacks_Examples"></a>

### Example
<a name="API_ListAvailableSolutionStacks_Example_1"></a>

This example illustrates one usage of ListAvailableSolutionStacks.

#### Sample Request
<a name="API_ListAvailableSolutionStacks_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?Operation=ListAvailableSolutionStacks
&AuthParams
```

#### Sample Response
<a name="API_ListAvailableSolutionStacks_Example_1_Response"></a>

```
<ListAvailableSolutionStacksResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ListAvailableSolutionStacksResult>
    <SolutionStacks>
      <member>64bit Amazon Linux running Tomcat 6</member>
      <member>32bit Amazon Linux running Tomcat 6</member>
      <member>64bit Amazon Linux running Tomcat 7</member>
      <member>32bit Amazon Linux running Tomcat 7</member>
    </SolutionStacks>
  </ListAvailableSolutionStacksResult>
  <ResponseMetadata>
    <RequestId>f21e2a92-f1fc-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</ListAvailableSolutionStacksResponse>
```

## See Also
<a name="API_ListAvailableSolutionStacks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ListAvailableSolutionStacks)

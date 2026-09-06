---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentResources.html
---

# DescribeEnvironmentResources
<a name="API_DescribeEnvironmentResources"></a>

Returns AWS resources for this environment.

## Request Parameters
<a name="API_DescribeEnvironmentResources_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnvironmentId **
The ID of the environment to retrieve AWS resource usage data.
 Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Required: No

 ** EnvironmentName **
The name of the environment to retrieve AWS resource usage data.
 Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

## Response Elements
<a name="API_DescribeEnvironmentResources_ResponseElements"></a>

The following element is returned by the service.

 ** EnvironmentResources **
 A list of [EnvironmentResourceDescription](API_EnvironmentResourceDescription.md).
Type: [EnvironmentResourceDescription](API_EnvironmentResourceDescription.md) object

## Errors
<a name="API_DescribeEnvironmentResources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

## Examples
<a name="API_DescribeEnvironmentResources_Examples"></a>

### Example
<a name="API_DescribeEnvironmentResources_Example_1"></a>

This example illustrates one usage of DescribeEnvironmentResources.

#### Sample Request
<a name="API_DescribeEnvironmentResources_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?EnvironmentId=e-hc8mvnayrx
&EnvironmentName=SampleAppVersion
&Operation=DescribeEnvironmentResources
&AuthParams
```

#### Sample Response
<a name="API_DescribeEnvironmentResources_Example_1_Response"></a>

```
<DescribeEnvironmentResourcesResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <DescribeEnvironmentResourcesResult>
    <EnvironmentResources>
      <LoadBalancers>
        <member>
          <Name>elasticbeanstalk-SampleAppVersion</Name>
        </member>
      </LoadBalancers>
      <LaunchConfigurations>
        <member>
          <Name>elasticbeanstalk-SampleAppVersion-hbAc8cSZH7</Name>
        </member>
      </LaunchConfigurations>
      <LaunchTemplates>
      </LaunchTemplates>
      <AutoScalingGroups>
        <member>
          <Name>elasticbeanstalk-SampleAppVersion-us-east-1c</Name>
        </member>
      </AutoScalingGroups>
      <EnvironmentName>SampleAppVersion</EnvironmentName>
      <Triggers>
        <member>
          <Name>elasticbeanstalk-SampleAppVersion-us-east-1c</Name>
        </member>
      </Triggers>
      <Instances/>
    </EnvironmentResources>
  </DescribeEnvironmentResourcesResult>
  <ResponseMetadata>
    <RequestId>e1cb7b96-f287-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DescribeEnvironmentResourcesResponse>
```

## See Also
<a name="API_DescribeEnvironmentResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeEnvironmentResources)

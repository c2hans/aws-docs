---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RebuildEnvironment.html
---

# RebuildEnvironment
<a name="API_RebuildEnvironment"></a>

Deletes and recreates all of the AWS resources (for example: the Auto Scaling group, load balancer, etc.) for a specified environment and forces a restart.

## Request Parameters
<a name="API_RebuildEnvironment_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnvironmentId **
The ID of the environment to rebuild.
 Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Required: No

 ** EnvironmentName **
The name of the environment to rebuild.
 Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

## Errors
<a name="API_RebuildEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

## Examples
<a name="API_RebuildEnvironment_Examples"></a>

### Example
<a name="API_RebuildEnvironment_Example_1"></a>

This example illustrates one usage of RebuildEnvironment.

#### Sample Request
<a name="API_RebuildEnvironment_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?EnvironmentId=e-hc8mvnayrx
&EnvironmentName=SampleAppVersion
&Operation=RebuildEnvironment
&AuthParams
```

#### Sample Response
<a name="API_RebuildEnvironment_Example_1_Response"></a>

```
<RebuildEnvironmentResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ResponseMetadata>
    <RequestId>a7d6606e-f289-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</RebuildEnvironmentResponse>
```

## See Also
<a name="API_RebuildEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/RebuildEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/RebuildEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/RebuildEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/RebuildEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/RebuildEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/RebuildEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/RebuildEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/RebuildEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/RebuildEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/RebuildEnvironment)

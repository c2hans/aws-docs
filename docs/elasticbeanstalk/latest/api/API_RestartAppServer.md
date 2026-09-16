---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RestartAppServer.html
---

# RestartAppServer
<a name="API_RestartAppServer"></a>

Causes the environment to restart the application container server running on each Amazon EC2 instance.

## Request Parameters
<a name="API_RestartAppServer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnvironmentId **
The ID of the environment to restart the server for.
 Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Required: No

 ** EnvironmentName **
The name of the environment to restart the server for.
 Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

## Errors
<a name="API_RestartAppServer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RestartAppServer_Examples"></a>

### Example
<a name="API_RestartAppServer_Example_1"></a>

This example illustrates one usage of RestartAppServer.

#### Sample Request
<a name="API_RestartAppServer_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?EnvironmentId=e-hc8mvnayrx
&EnvironmentName=SampleAppVersion
&Operation=RestartAppServer
&AuthParams
```

#### Sample Response
<a name="API_RestartAppServer_Example_1_Response"></a>

```
<RestartAppServerResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ResponseMetadata>
    <RequestId>90e8d1d5-f28a-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</RestartAppServerResponse>
```

## See Also
<a name="API_RestartAppServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/RestartAppServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/RestartAppServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/RestartAppServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/RestartAppServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/RestartAppServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/RestartAppServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/RestartAppServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/RestartAppServer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/RestartAppServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/RestartAppServer)

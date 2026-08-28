---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RequestEnvironmentInfo.html
---

# RequestEnvironmentInfo
<a name="API_RequestEnvironmentInfo"></a>

Initiates a request to compile the specified type of information of the deployed environment.

 Setting the `InfoType` to `tail` compiles the last lines from the application server log files of every Amazon EC2 instance in your environment.

 Setting the `InfoType` to `bundle` compresses the application server log files for every Amazon EC2 instance into a `.zip` file. Legacy and .NET containers do not support bundle logs.

 Use [RetrieveEnvironmentInfo](API_RetrieveEnvironmentInfo.md) to obtain the set of logs.

Related Topics
+  [RetrieveEnvironmentInfo](API_RetrieveEnvironmentInfo.md)

## Request Parameters
<a name="API_RequestEnvironmentInfo_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnvironmentId **
The ID of the environment of the requested data.
If no such environment is found, `RequestEnvironmentInfo` returns an `InvalidParameterValue` error.
Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Required: No

 ** EnvironmentName **
The name of the environment of the requested data.
If no such environment is found, `RequestEnvironmentInfo` returns an `InvalidParameterValue` error.
Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** InfoType **
The type of information to request.
Type: String
Valid Values: `tail | bundle`
Required: Yes

## Errors
<a name="API_RequestEnvironmentInfo_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RequestEnvironmentInfo_Examples"></a>

### Example
<a name="API_RequestEnvironmentInfo_Example_1"></a>

This example illustrates one usage of RequestEnvironmentInfo.

#### Sample Request
<a name="API_RequestEnvironmentInfo_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?EnvironmentId=e-hc8mvnayrx
&EnvironmentName=SampleAppVersion
&InfoType=tail
&Operation=RequestEnvironmentInfo
&AuthParams
```

#### Sample Response
<a name="API_RequestEnvironmentInfo_Example_1_Response"></a>

```
<RequestEnvironmentInfoResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ResponseMetadata>
    <RequestId>126a4ff3-f28a-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</RequestEnvironmentInfoResponse>
```

## See Also
<a name="API_RequestEnvironmentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/RequestEnvironmentInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

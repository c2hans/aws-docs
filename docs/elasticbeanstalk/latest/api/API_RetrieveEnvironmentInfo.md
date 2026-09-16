---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_RetrieveEnvironmentInfo.html
---

# RetrieveEnvironmentInfo
<a name="API_RetrieveEnvironmentInfo"></a>

Retrieves the compiled information from a [RequestEnvironmentInfo](API_RequestEnvironmentInfo.md) request.

Related Topics
+  [RequestEnvironmentInfo](API_RequestEnvironmentInfo.md)

## Request Parameters
<a name="API_RetrieveEnvironmentInfo_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnvironmentId **
The ID of the data's environment.
If no such environment is found, returns an `InvalidParameterValue` error.
Condition: You must specify either this or an EnvironmentName, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Required: No

 ** EnvironmentName **
The name of the data's environment.
 If no such environment is found, returns an `InvalidParameterValue` error.
 Condition: You must specify either this or an EnvironmentId, or both. If you do not specify either, AWS Elastic Beanstalk returns `MissingRequiredParameter` error.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** InfoType **
The type of information to retrieve.
Type: String
Valid Values: `tail | bundle`
Required: Yes

## Response Elements
<a name="API_RetrieveEnvironmentInfo_ResponseElements"></a>

The following element is returned by the service.

 **EnvironmentInfo.member.N**
 The [EnvironmentInfoDescription](API_EnvironmentInfoDescription.md) of the environment.
Type: Array of [EnvironmentInfoDescription](API_EnvironmentInfoDescription.md) objects

## Errors
<a name="API_RetrieveEnvironmentInfo_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_RetrieveEnvironmentInfo_Examples"></a>

### Example
<a name="API_RetrieveEnvironmentInfo_Example_1"></a>

This example illustrates one usage of RetrieveEnvironmentInfo.

#### Sample Request
<a name="API_RetrieveEnvironmentInfo_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?EnvironmentId=e-hc8mvnayrx
&EnvironmentName=SampleAppVersion
&InfoType=tail
&Operation=RetrieveEnvironmentInfo
&AuthParams
```

#### Sample Response
<a name="API_RetrieveEnvironmentInfo_Example_1_Response"></a>

```
<RetrieveEnvironmentInfoResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <RetrieveEnvironmentInfoResult>
    <EnvironmentInfo>
      <member>
        <Message>
         https://elasticbeanstalk.us-east-1.s3.amazonaws.com/environments%2Fa514386a-709f-4888-9683-068c38d744b4%2Flogs%2Fi-92a3ceff%2F278756a8-7d83-4bc1-93db-b1763163705a.log?Expires=1291236023
         &AuthParams
        </Message>
        <SampleTimestamp>2010-11-17T20:40:23.210Z</SampleTimestamp>
        <InfoType>tail</InfoType>
        <Ec2InstanceId>i-92a3ceff</Ec2InstanceId>
      </member>
    </EnvironmentInfo>
  </RetrieveEnvironmentInfoResult>
  <ResponseMetadata>
    <RequestId>e8e785c9-f28a-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</RetrieveEnvironmentInfoResponse>
```

## See Also
<a name="API_RetrieveEnvironmentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/RetrieveEnvironmentInfo)

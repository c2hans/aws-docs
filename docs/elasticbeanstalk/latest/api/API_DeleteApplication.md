---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteApplication.html
---

# DeleteApplication
<a name="API_DeleteApplication"></a>

Deletes the specified application along with all associated versions and configurations. The application versions will not be deleted from your Amazon S3 bucket.

**Note**
You cannot delete an application that has a running environment.

## Request Parameters
<a name="API_DeleteApplication_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** TerminateEnvByForce **
When set to true, running environments will be terminated before deleting the application.
Type: Boolean
Required: No

## Errors
<a name="API_DeleteApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationInProgressFailure **
Unable to perform the specified operation because another operation that effects an element in this activity is already in progress.
HTTP Status Code: 400

## Examples
<a name="API_DeleteApplication_Examples"></a>

### Example
<a name="API_DeleteApplication_Example_1"></a>

This example illustrates one usage of DeleteApplication.

#### Sample Request
<a name="API_DeleteApplication_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&Operation=DeleteApplication
&AuthParams
```

#### Sample Response
<a name="API_DeleteApplication_Example_1_Response"></a>

```
<DeleteApplicationResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ResponseMetadata>
    <RequestId>1f155abd-f1d7-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DeleteApplicationResponse>
```

## See Also
<a name="API_DeleteApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DeleteApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DeleteApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DeleteApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DeleteApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DeleteApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DeleteApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DeleteApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DeleteApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DeleteApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DeleteApplication)

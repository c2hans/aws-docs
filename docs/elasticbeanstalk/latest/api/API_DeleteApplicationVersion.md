---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeleteApplicationVersion.html
---

# DeleteApplicationVersion
<a name="API_DeleteApplicationVersion"></a>

Deletes the specified version from the specified application.

**Note**
You cannot delete an application version that is associated with a running environment.

## Request Parameters
<a name="API_DeleteApplicationVersion_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application to which the version belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** DeleteSourceBundle **
Set to `true` to delete the source bundle from your storage bucket. Otherwise, the application version is deleted only from Elastic Beanstalk and the source bundle remains in Amazon S3.
Type: Boolean
Required: No

 ** VersionLabel **
The label of the version to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Errors
<a name="API_DeleteApplicationVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** OperationInProgressFailure **
Unable to perform the specified operation because another operation that effects an element in this activity is already in progress.
HTTP Status Code: 400

 ** S3LocationNotInServiceRegion **
The specified S3 bucket does not belong to the S3 region in which the service is running. The following regions are supported:
+ IAD/us-east-1
+ PDX/us-west-2
+ DUB/eu-west-1
HTTP Status Code: 400

 ** SourceBundleDeletionFailure **
Unable to delete the Amazon S3 source bundle associated with the application version. The application version was deleted successfully.
HTTP Status Code: 400

## Examples
<a name="API_DeleteApplicationVersion_Examples"></a>

### Example
<a name="API_DeleteApplicationVersion_Example_1"></a>

This example illustrates one usage of DeleteApplicationVersion.

#### Sample Request
<a name="API_DeleteApplicationVersion_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&VersionLabel=First%20Release
&Operation=DeleteApplicationVersion
&AuthParams
```

#### Sample Response
<a name="API_DeleteApplicationVersion_Example_1_Response"></a>

```
<DeleteApplicationVersionResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <ResponseMetadata>
    <RequestId>58dc7339-f272-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</DeleteApplicationVersionResponse>
```

## See Also
<a name="API_DeleteApplicationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DeleteApplicationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DeleteApplicationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DeleteApplicationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DeleteApplicationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DeleteApplicationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DeleteApplicationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DeleteApplicationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DeleteApplicationVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DeleteApplicationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DeleteApplicationVersion)

---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DeletePlatformVersion.html
---

# DeletePlatformVersion
<a name="API_DeletePlatformVersion"></a>

Deletes the specified version of a custom platform.

## Request Parameters
<a name="API_DeletePlatformVersion_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** PlatformArn **
The ARN of the version of the custom platform.
Type: String
Required: No

## Response Elements
<a name="API_DeletePlatformVersion_ResponseElements"></a>

The following element is returned by the service.

 ** PlatformSummary **
Detailed information about the version of the custom platform.
Type: [PlatformSummary](API_PlatformSummary.md) object

## Errors
<a name="API_DeletePlatformVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ElasticBeanstalkService **
A generic service exception has occurred.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** OperationInProgressFailure **
Unable to perform the specified operation because another operation that effects an element in this activity is already in progress.
HTTP Status Code: 400

 ** PlatformVersionStillReferenced **
You cannot delete the platform version because there are still environments running on it.
HTTP Status Code: 400

## See Also
<a name="API_DeletePlatformVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DeletePlatformVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DeletePlatformVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DeletePlatformVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DeletePlatformVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DeletePlatformVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DeletePlatformVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DeletePlatformVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DeletePlatformVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DeletePlatformVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DeletePlatformVersion)

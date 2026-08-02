---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplicationResourceLifecycle.html
---

# UpdateApplicationResourceLifecycle
<a name="API_UpdateApplicationResourceLifecycle"></a>

Modifies lifecycle settings for an application.

## Request Parameters
<a name="API_UpdateApplicationResourceLifecycle_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** ResourceLifecycleConfig **
The lifecycle configuration.
Type: [ApplicationResourceLifecycleConfig](API_ApplicationResourceLifecycleConfig.md) object
Required: Yes

## Response Elements
<a name="API_UpdateApplicationResourceLifecycle_ResponseElements"></a>

The following elements are returned by the service.

 ** ApplicationName **
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** ResourceLifecycleConfig **
The lifecycle configuration.
Type: [ApplicationResourceLifecycleConfig](API_ApplicationResourceLifecycleConfig.md) object

## Errors
<a name="API_UpdateApplicationResourceLifecycle_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

## See Also
<a name="API_UpdateApplicationResourceLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/UpdateApplicationResourceLifecycle)

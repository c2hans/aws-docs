---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplyEnvironmentManagedAction.html
---

# ApplyEnvironmentManagedAction
<a name="API_ApplyEnvironmentManagedAction"></a>

Applies a scheduled managed action immediately. A managed action can be applied only if its status is `Scheduled`. Get the status and action ID of a managed action with [DescribeEnvironmentManagedActions](API_DescribeEnvironmentManagedActions.md).

## Request Parameters
<a name="API_ApplyEnvironmentManagedAction_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ActionId **
The action ID of the scheduled managed action to execute.
Type: String
Required: Yes

 ** EnvironmentId **
The environment ID of the target environment.
Type: String
Required: No

 ** EnvironmentName **
The name of the target environment.
Type: String
Required: No

## Response Elements
<a name="API_ApplyEnvironmentManagedAction_ResponseElements"></a>

The following elements are returned by the service.

 ** ActionDescription **
A description of the managed action.
Type: String

 ** ActionId **
The action ID of the managed action.
Type: String

 ** ActionType **
The type of managed action.
Type: String
Valid Values: `InstanceRefresh | PlatformUpdate | Unknown`

 ** Status **
The status of the managed action.
Type: String

## Errors
<a name="API_ApplyEnvironmentManagedAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ElasticBeanstalkService **
A generic service exception has occurred.
 ** message **
The exception error message.
HTTP Status Code: 400

 ** ManagedActionInvalidState **
Cannot modify the managed action in its current state.
HTTP Status Code: 400

## See Also
<a name="API_ApplyEnvironmentManagedAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ApplyEnvironmentManagedAction)

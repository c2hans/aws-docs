---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironmentManagedActionHistory.html
---

# DescribeEnvironmentManagedActionHistory
<a name="API_DescribeEnvironmentManagedActionHistory"></a>

Lists an environment's completed and failed managed actions.

## Request Parameters
<a name="API_DescribeEnvironmentManagedActionHistory_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EnvironmentId **
The environment ID of the target environment.
Type: String
Required: No

 ** EnvironmentName **
The name of the target environment.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 40.
Required: No

 ** MaxItems **
The maximum number of items to return for a single request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** NextToken **
The pagination token returned by a previous request.
Type: String
Required: No

## Response Elements
<a name="API_DescribeEnvironmentManagedActionHistory_ResponseElements"></a>

The following elements are returned by the service.

 **ManagedActionHistoryItems.member.N**
A list of completed and failed managed actions.
Type: Array of [ManagedActionHistoryItem](API_ManagedActionHistoryItem.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** NextToken **
A pagination token that you pass to [DescribeEnvironmentManagedActionHistory](#API_DescribeEnvironmentManagedActionHistory) to get the next page of results.
Type: String

## Errors
<a name="API_DescribeEnvironmentManagedActionHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ElasticBeanstalkService **
A generic service exception has occurred.
 ** message **
The exception error message.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEnvironmentManagedActionHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/DescribeEnvironmentManagedActionHistory)

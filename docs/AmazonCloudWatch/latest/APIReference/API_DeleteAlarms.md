---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteAlarms.html
---

# DeleteAlarms
<a name="API_DeleteAlarms"></a>

Deletes the specified alarms. You can delete up to 100 alarms in one operation. However, this total can include no more than one composite alarm. For example, you could delete 99 metric alarms and one composite alarms with one operation, but you can't delete two composite alarms with one operation. Log alarms cannot be batch deleted.

 If you specify any incorrect alarm names, the alarms you specify with correct names are still deleted. Other syntax errors might result in no alarms being deleted. To confirm that alarms were deleted successfully, you can use the [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) operation after using `DeleteAlarms`.

**Note**
It is possible to create a loop or cycle of composite alarms, where composite alarm A depends on composite alarm B, and composite alarm B also depends on composite alarm A. In this scenario, you can't delete any composite alarm that is part of the cycle because there is always still a composite alarm that depends on that alarm that you want to delete.
To get out of such a situation, you must break the cycle by changing the rule of one of the composite alarms in the cycle to remove a dependency that creates the cycle. The simplest change to make to break a cycle is to change the `AlarmRule` of one of the alarms to `false`.
Additionally, the evaluation of composite alarms stops if CloudWatch detects a cycle in the evaluation path.

## Request Syntax
<a name="API_DeleteAlarms_RequestSyntax"></a>

```
{
   "AlarmNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DeleteAlarms_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AlarmNames](#API_DeleteAlarms_RequestSyntax) **   <a name="ACW-DeleteAlarms-request-AlarmNames"></a>
The alarms to be deleted. Do not enclose the alarm names in quote marks.
Type: Array of strings
Array Members: Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Elements
<a name="API_DeleteAlarms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAlarms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceConflict **
The operation could not be completed because the request conflicts with the current state of the alarm or its underlying scheduled query resource.
HTTP Status Code: 409

 ** ResourceNotFound **
The named resource does not exist.
 ** message **

HTTP Status Code: 404

## See Also
<a name="API_DeleteAlarms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/DeleteAlarms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteAlarms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/DeleteAlarms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/DeleteAlarms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/DeleteAlarms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/DeleteAlarms)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteAlarms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarms)

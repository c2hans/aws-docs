---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateList.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# UpdateList
<a name="API_UpdateList"></a>

 Updates a list.

## Request Syntax
<a name="API_UpdateList_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "elements": [ "{{string}}" ],
   "name": "{{string}}",
   "updateMode": "{{string}}",
   "variableType": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateList_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_UpdateList_RequestSyntax) **   <a name="FraudDetector-UpdateList-request-description"></a>
 The new description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [elements](#API_UpdateList_RequestSyntax) **   <a name="FraudDetector-UpdateList-request-elements"></a>
 One or more list elements to add or replace. If you are providing the elements, make sure to specify the `updateMode` to use.
If you are deleting all elements from the list, use `REPLACE` for the `updateMode` and provide an empty list (0 elements).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100000 items.
Length Constraints: Minimum length of 1. Maximum length of 320.
Pattern: `^\S+( +\S+)*$`
Required: No

 ** [name](#API_UpdateList_RequestSyntax) **   <a name="FraudDetector-UpdateList-request-name"></a>
 The name of the list to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: Yes

 ** [updateMode](#API_UpdateList_RequestSyntax) **   <a name="FraudDetector-UpdateList-request-updateMode"></a>
 The update mode (type).
+ Use `APPEND` if you are adding elements to the list.
+ Use `REPLACE` if you replacing existing elements in the list.
+ Use `REMOVE` if you are removing elements from the list.
Type: String
Valid Values: `REPLACE | APPEND | REMOVE`
Required: No

 ** [variableType](#API_UpdateList_RequestSyntax) **   <a name="FraudDetector-UpdateList-request-variableType"></a>
 The variable type you want to assign to the list.
You cannot update a variable type of a list that already has a variable type assigned to it. You can assign a variable type to a list only if the list does not already have a variable type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Z_]{1,64}$`
Required: No

## Response Elements
<a name="API_UpdateList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** ConflictException **
An exception indicating there was a conflict during a delete operation.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception indicating the specified resource was not found.
HTTP Status Code: 400

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_UpdateList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/UpdateList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/UpdateList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/UpdateList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/UpdateList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/UpdateList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/UpdateList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/UpdateList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/UpdateList)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/UpdateList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/UpdateList)

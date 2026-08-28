---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_CreateList.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# CreateList
<a name="API_CreateList"></a>

 Creates a list.

List is a set of input data for a variable in your event dataset. You use the input data in a rule that's associated with your detector. For more information, see [Lists](https://docs.aws.amazon.com/frauddetector/latest/ug/lists.html).

## Request Syntax
<a name="API_CreateList_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "elements": [ "{{string}}" ],
   "name": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "variableType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateList_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateList_RequestSyntax) **   <a name="FraudDetector-CreateList-request-description"></a>
 The description of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [elements](#API_CreateList_RequestSyntax) **   <a name="FraudDetector-CreateList-request-elements"></a>
 The names of the elements, if providing. You can also create an empty list and add elements later using the [UpdateList](https://docs.aws.amazon.com/frauddetector/latest/api/API_Updatelist.html) API.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100000 items.
Length Constraints: Minimum length of 1. Maximum length of 320.
Pattern: `^\S+( +\S+)*$`
Required: No

 ** [name](#API_CreateList_RequestSyntax) **   <a name="FraudDetector-CreateList-request-name"></a>
 The name of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_]+$`
Required: Yes

 ** [tags](#API_CreateList_RequestSyntax) **   <a name="FraudDetector-CreateList-request-tags"></a>
 A collection of the key and value pairs.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [variableType](#API_CreateList_RequestSyntax) **   <a name="FraudDetector-CreateList-request-variableType"></a>
 The variable type of the list. You can only assign the variable type with String data type. For more information, see [Variable types](https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Z_]{1,64}$`
Required: No

## Response Elements
<a name="API_CreateList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateList_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An exception indicating Amazon Fraud Detector does not have the needed permissions. This can occur if you submit a request, such as `PutExternalModel`, that specifies a role that is not in your account.
HTTP Status Code: 400

 ** InternalServerException **
An exception indicating an internal server error.
HTTP Status Code: 500

 ** ThrottlingException **
An exception indicating a throttling error.
HTTP Status Code: 400

 ** ValidationException **
An exception indicating a specified value is not allowed.
HTTP Status Code: 400

## See Also
<a name="API_CreateList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/frauddetector-2019-11-15/CreateList)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/frauddetector-2019-11-15/CreateList)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/CreateList)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/frauddetector-2019-11-15/CreateList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/CreateList)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/frauddetector-2019-11-15/CreateList)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/frauddetector-2019-11-15/CreateList)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/frauddetector-2019-11-15/CreateList)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/frauddetector-2019-11-15/CreateList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/CreateList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

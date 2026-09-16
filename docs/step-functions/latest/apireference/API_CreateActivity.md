---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateActivity.html
---

# CreateActivity
<a name="API_CreateActivity"></a>

Creates an activity. An activity is a task that you write in any programming language and host on any machine that has access to AWS Step Functions. Activities must poll Step Functions using the `GetActivityTask` API action and respond using `SendTask*` API actions. This function lets Step Functions know the existence of your activity and returns an identifier for use in a state machine and when polling from the activity.

**Note**
This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

**Note**
 `CreateActivity` is an idempotent API. Subsequent requests won’t create a duplicate resource if it was already created. `CreateActivity`'s idempotency check is based on the activity `name`. If a following request has different `tags` values, Step Functions will ignore these differences and treat it as an idempotent request of the previous. In this case, `tags` will not be updated, even if they are different.

## Request Syntax
<a name="API_CreateActivity_RequestSyntax"></a>

```
{
   "encryptionConfiguration": {
      "kmsDataKeyReusePeriodSeconds": {{number}},
      "kmsKeyId": "{{string}}",
      "type": "{{string}}"
   },
   "name": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateActivity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [encryptionConfiguration](#API_CreateActivity_RequestSyntax) **   <a name="StepFunctions-CreateActivity-request-encryptionConfiguration"></a>
Settings to configure server-side encryption.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [name](#API_CreateActivity_RequestSyntax) **   <a name="StepFunctions-CreateActivity-request-name"></a>
The name of the activity to create. This name must be unique for your AWS account and region.
A name must *not* contain:
+ white space
+ brackets `< > { } [ ]`
+ wildcard characters `? *`
+ special characters `" # % \ ^ | ~ ` $ & , ; : /`
+ control characters (`U+0000-001F`, `U+007F-009F`, `U+FFFE-FFFF`)
+ surrogates (`U+D800-DFFF`)
+ invalid characters (` U+10FFFF`)
To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and \_.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

 ** [tags](#API_CreateActivity_RequestSyntax) **   <a name="StepFunctions-CreateActivity-request-tags"></a>
The list of tags to add to a resource.
An array of key-value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the * AWS Billing and Cost Management User Guide*, and [Controlling Access Using IAM Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html).
Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + - @`.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateActivity_ResponseSyntax"></a>

```
{
   "activityArn": "string",
   "creationDate": number
}
```

## Response Elements
<a name="API_CreateActivity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activityArn](#API_CreateActivity_ResponseSyntax) **   <a name="StepFunctions-CreateActivity-response-activityArn"></a>
The Amazon Resource Name (ARN) that identifies the created activity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [creationDate](#API_CreateActivity_ResponseSyntax) **   <a name="StepFunctions-CreateActivity-response-creationDate"></a>
The date the activity is created.
Type: Timestamp

## Errors
<a name="API_CreateActivity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActivityAlreadyExists **
Activity already exists. `EncryptionConfiguration` may not be updated.
HTTP Status Code: 400

 ** ActivityLimitExceeded **
The maximum number of activities has been reached. Existing activities must be deleted before a new activity can be created.
HTTP Status Code: 400

 ** InvalidEncryptionConfiguration **
Received when `encryptionConfiguration` is specified but various conditions exist which make the configuration invalid. For example, if `type` is set to `CUSTOMER_MANAGED_KMS_KEY`, but `kmsKeyId` is null, or `kmsDataKeyReusePeriodSeconds` is not between 60 and 900, or the AWS KMS key is not symmetric or inactive.
HTTP Status Code: 400

 ** InvalidName **
The provided name is not valid.
HTTP Status Code: 400

 ** KmsAccessDeniedException **
Either your AWS KMS key policy or API caller does not have the required permissions.
HTTP Status Code: 400

 ** KmsThrottlingException **
Received when AWS KMS returns `ThrottlingException` for a AWS KMS call that Step Functions makes on behalf of the caller.
HTTP Status Code: 400

 ** TooManyTags **
You've exceeded the number of tags allowed for a resource. See the [ Limits Topic](https://docs.aws.amazon.com/step-functions/latest/dg/limits.html) in the AWS Step Functions Developer Guide.
HTTP Status Code: 400

## See Also
<a name="API_CreateActivity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/CreateActivity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/CreateActivity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/CreateActivity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/CreateActivity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/CreateActivity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/CreateActivity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/CreateActivity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/CreateActivity)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/CreateActivity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/CreateActivity)

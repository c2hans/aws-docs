---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeActivity.html
---

# DescribeActivity
<a name="API_DescribeActivity"></a>

Describes an activity.

**Note**
This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

## Request Syntax
<a name="API_DescribeActivity_RequestSyntax"></a>

```
{
   "activityArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeActivity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [activityArn](#API_DescribeActivity_RequestSyntax) **   <a name="StepFunctions-DescribeActivity-request-activityArn"></a>
The Amazon Resource Name (ARN) of the activity to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_DescribeActivity_ResponseSyntax"></a>

```
{
   "activityArn": "string",
   "creationDate": number,
   "encryptionConfiguration": {
      "kmsDataKeyReusePeriodSeconds": number,
      "kmsKeyId": "string",
      "type": "string"
   },
   "name": "string"
}
```

## Response Elements
<a name="API_DescribeActivity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activityArn](#API_DescribeActivity_ResponseSyntax) **   <a name="StepFunctions-DescribeActivity-response-activityArn"></a>
The Amazon Resource Name (ARN) that identifies the activity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [creationDate](#API_DescribeActivity_ResponseSyntax) **   <a name="StepFunctions-DescribeActivity-response-creationDate"></a>
The date the activity is created.
Type: Timestamp

 ** [encryptionConfiguration](#API_DescribeActivity_ResponseSyntax) **   <a name="StepFunctions-DescribeActivity-response-encryptionConfiguration"></a>
Settings for configured server-side encryption.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [name](#API_DescribeActivity_ResponseSyntax) **   <a name="StepFunctions-DescribeActivity-response-name"></a>
The name of the activity.
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

## Errors
<a name="API_DescribeActivity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActivityDoesNotExist **
The specified activity does not exist.
HTTP Status Code: 400

 ** InvalidArn **
The provided Amazon Resource Name (ARN) is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeActivity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/DescribeActivity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/DescribeActivity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/DescribeActivity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/DescribeActivity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/DescribeActivity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/DescribeActivity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/DescribeActivity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/DescribeActivity)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/DescribeActivity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/DescribeActivity)

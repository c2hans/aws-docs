---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html
---

# DeleteCanary
<a name="API_DeleteCanary"></a>

Permanently deletes the specified canary.

If the canary's `ProvisionedResourceCleanup` field is set to `AUTOMATIC` or you specify `DeleteLambda` in this operation as `true`, CloudWatch Synthetics also deletes the Lambda functions and layers that are used by the canary.

Other resources used and created by the canary are not automatically deleted. After you delete a canary, you should also delete the following:
+ The CloudWatch alarms created for this canary. These alarms have a name of `Synthetics-Alarm-first-198-characters-of-canary-name-canaryId-alarm number `
+ Amazon S3 objects and buckets, such as the canary's artifact location.
+ IAM roles created for the canary. If they were created in the console, these roles have the name ` role/service-role/CloudWatchSyntheticsRole-First-21-Characters-of-CanaryName `
+ CloudWatch Logs log groups created for the canary. These logs groups have the name `/aws/lambda/cwsyn-First-21-Characters-of-CanaryName `

Before you delete a canary, you might want to use `GetCanary` to display the information about this canary. Make note of the information returned by this operation so that you can delete these resources after you delete the canary.

## Request Syntax
<a name="API_DeleteCanary_RequestSyntax"></a>

```
DELETE /canary/{{name}}?deleteLambda={{DeleteLambda}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCanary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeleteLambda](#API_DeleteCanary_RequestSyntax) **   <a name="synthetics-DeleteCanary-request-uri-DeleteLambda"></a>
Specifies whether to also delete the Lambda functions and layers used by this canary. The default is `false`.
Your setting for this parameter is used only if the canary doesn't have `AUTOMATIC` for its `ProvisionedResourceCleanup` field. If that field is set to `AUTOMATIC`, then the Lambda functions and layers will be deleted when this canary is deleted.
Type: Boolean

 ** [name](#API_DeleteCanary_RequestSyntax) **   <a name="synthetics-DeleteCanary-request-uri-Name"></a>
The name of the canary that you want to delete. To find the names of your canaries, use [DescribeCanaries](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html).
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[0-9a-z_\-]+$`
Required: Yes

## Request Body
<a name="API_DeleteCanary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCanary_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteCanary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteCanary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A conflicting operation is already in progress.
HTTP Status Code: 409

 ** InternalServerException **
An unknown internal error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One of the specified resources was not found.
HTTP Status Code: 404

 ** ValidationException **
A parameter could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_DeleteCanary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/synthetics-2017-10-11/DeleteCanary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/synthetics-2017-10-11/DeleteCanary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/DeleteCanary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/synthetics-2017-10-11/DeleteCanary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/DeleteCanary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/synthetics-2017-10-11/DeleteCanary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/synthetics-2017-10-11/DeleteCanary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/synthetics-2017-10-11/DeleteCanary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/synthetics-2017-10-11/DeleteCanary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/DeleteCanary)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeAttachedFilesConfiguration.html
---

# DescribeAttachedFilesConfiguration
<a name="API_DescribeAttachedFilesConfiguration"></a>

Describes the attached files configuration for the specified Connect Customer instance and attachment scope.

If a custom configuration exists for the specified attachment scope, the custom configuration is returned. If no custom configuration exists, the default configuration values for that attachment scope are returned.

## Request Syntax
<a name="API_DescribeAttachedFilesConfiguration_RequestSyntax"></a>

```
GET /attached-files-configurations/{{InstanceId}}/{{AttachmentScope}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAttachedFilesConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttachmentScope](#API_DescribeAttachedFilesConfiguration_RequestSyntax) **   <a name="connect-DescribeAttachedFilesConfiguration-request-uri-AttachmentScope"></a>
The scope of the attachment. Valid values are `EMAIL`, `CHAT`, `CASE`, and `TASK`.
Valid Values: `EMAIL | CHAT | CASE | TASK`
Required: Yes

 ** [InstanceId](#API_DescribeAttachedFilesConfiguration_RequestSyntax) **   <a name="connect-DescribeAttachedFilesConfiguration-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeAttachedFilesConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAttachedFilesConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AttachedFilesConfiguration": {
      "AttachmentScope": "string",
      "ExtensionConfiguration": {
         "AllowedExtensions": [
            {
               "Extension": "string"
            }
         ]
      },
      "InstanceId": "string",
      "LastModifiedTime": number,
      "MaximumSizeLimitInBytes": number
   }
}
```

## Response Elements
<a name="API_DescribeAttachedFilesConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AttachedFilesConfiguration](#API_DescribeAttachedFilesConfiguration_ResponseSyntax) **   <a name="connect-DescribeAttachedFilesConfiguration-response-AttachedFilesConfiguration"></a>
Information about the attached files configuration.
Type: [AttachedFilesConfiguration](API_AttachedFilesConfiguration.md) object

## Errors
<a name="API_DescribeAttachedFilesConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeAttachedFilesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeAttachedFilesConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeAttachedFilesConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeAttachedFilesConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeAttachedFilesConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeAttachedFilesConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeAttachedFilesConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeAttachedFilesConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeAttachedFilesConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeAttachedFilesConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeAttachedFilesConfiguration)

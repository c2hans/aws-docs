---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDefaultApplicationSetting.html
---

# GetDefaultApplicationSetting
<a name="API_GetDefaultApplicationSetting"></a>

Gets the ARN of the current default application.

 If the default application isn't set, the operation returns a resource not found error.

## Request Syntax
<a name="API_GetDefaultApplicationSetting_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/defaultApplicationSetting HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDefaultApplicationSetting_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetDefaultApplicationSetting_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDefaultApplicationSetting_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string"
}
```

## Response Elements
<a name="API_GetDefaultApplicationSetting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_GetDefaultApplicationSetting_ResponseSyntax) **   <a name="opensearchservice-GetDefaultApplicationSetting-response-applicationArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

## Errors
<a name="API_GetDefaultApplicationSetting_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_GetDefaultApplicationSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetDefaultApplicationSetting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetDefaultApplicationSetting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetDefaultApplicationSetting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetDefaultApplicationSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetDefaultApplicationSetting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetDefaultApplicationSetting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetDefaultApplicationSetting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetDefaultApplicationSetting)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetDefaultApplicationSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetDefaultApplicationSetting)

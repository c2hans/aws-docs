---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PutDefaultApplicationSetting.html
---

# PutDefaultApplicationSetting
<a name="API_PutDefaultApplicationSetting"></a>

Sets the default application to the application with the specified ARN.

 To remove the default application, use the `GetDefaultApplicationSetting` operation to get the current default and then call the `PutDefaultApplicationSetting` with the current applications ARN and the `setAsDefault` parameter set to `false`.

## Request Syntax
<a name="API_PutDefaultApplicationSetting_RequestSyntax"></a>

```
PUT /2021-01-01/opensearch/defaultApplicationSetting HTTP/1.1
Content-type: application/json

{
   "applicationArn": "{{string}}",
   "setAsDefault": {{boolean}}
}
```

## URI Request Parameters
<a name="API_PutDefaultApplicationSetting_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutDefaultApplicationSetting_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [applicationArn](#API_PutDefaultApplicationSetting_RequestSyntax) **   <a name="opensearchservice-PutDefaultApplicationSetting-request-applicationArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: Yes

 ** [setAsDefault](#API_PutDefaultApplicationSetting_RequestSyntax) **   <a name="opensearchservice-PutDefaultApplicationSetting-request-setAsDefault"></a>
Set to true to set the specified ARN as the default application. Set to false to clear the default application.
Type: Boolean
Required: Yes

## Response Syntax
<a name="API_PutDefaultApplicationSetting_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationArn": "string"
}
```

## Response Elements
<a name="API_PutDefaultApplicationSetting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationArn](#API_PutDefaultApplicationSetting_ResponseSyntax) **   <a name="opensearchservice-PutDefaultApplicationSetting-response-applicationArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

## Errors
<a name="API_PutDefaultApplicationSetting_Errors"></a>

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
<a name="API_PutDefaultApplicationSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/PutDefaultApplicationSetting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/PutDefaultApplicationSetting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/PutDefaultApplicationSetting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/PutDefaultApplicationSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/PutDefaultApplicationSetting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/PutDefaultApplicationSetting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/PutDefaultApplicationSetting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/PutDefaultApplicationSetting)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/PutDefaultApplicationSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/PutDefaultApplicationSetting)

---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_ListQuickSetupTypes.html
---

# ListQuickSetupTypes
<a name="API_ListQuickSetupTypes"></a>

Returns the available Quick Setup types.

## Request Syntax
<a name="API_ListQuickSetupTypes_RequestSyntax"></a>

```
GET /listQuickSetupTypes HTTP/1.1
```

## URI Request Parameters
<a name="API_ListQuickSetupTypes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListQuickSetupTypes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListQuickSetupTypes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "QuickSetupTypeList": [
      {
         "LatestVersion": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListQuickSetupTypes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QuickSetupTypeList](#API_ListQuickSetupTypes_ResponseSyntax) **   <a name="quicksetup-ListQuickSetupTypes-response-QuickSetupTypeList"></a>
An array of Quick Setup types.
Type: Array of [QuickSetupTypeOutput](API_QuickSetupTypeOutput.md) objects

## Errors
<a name="API_ListQuickSetupTypes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requester has insufficient permissions to perform the operation.
HTTP Status Code: 403

 ** ConflictException **
Another request is being processed. Wait a few minutes and try again.
HTTP Status Code: 409

 ** InternalServerException **
An error occurred on the server side.
HTTP Status Code: 500

 ** ThrottlingException **
The request or operation exceeds the maximum allowed request rate per AWS account and AWS Region.
HTTP Status Code: 429

## See Also
<a name="API_ListQuickSetupTypes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-quicksetup-2018-05-10/ListQuickSetupTypes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-quicksetup-2018-05-10/ListQuickSetupTypes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/ListQuickSetupTypes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-quicksetup-2018-05-10/ListQuickSetupTypes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/ListQuickSetupTypes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-quicksetup-2018-05-10/ListQuickSetupTypes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-quicksetup-2018-05-10/ListQuickSetupTypes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-quicksetup-2018-05-10/ListQuickSetupTypes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-quicksetup-2018-05-10/ListQuickSetupTypes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/ListQuickSetupTypes)

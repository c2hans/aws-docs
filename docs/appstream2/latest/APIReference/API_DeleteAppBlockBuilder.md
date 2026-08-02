---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DeleteAppBlockBuilder.html
---

# DeleteAppBlockBuilder
<a name="API_DeleteAppBlockBuilder"></a>

Deletes an app block builder.

An app block builder can only be deleted when it has no association with an app block.

## Request Syntax
<a name="API_DeleteAppBlockBuilder_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAppBlockBuilder_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DeleteAppBlockBuilder_RequestSyntax) **   <a name="WorkSpacesApplications-DeleteAppBlockBuilder-request-Name"></a>
The name of the app block builder.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Elements
<a name="API_DeleteAppBlockBuilder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAppBlockBuilder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is in use.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAppBlockBuilder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/DeleteAppBlockBuilder)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/DeleteAppBlockBuilder)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/DeleteAppBlockBuilder)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/DeleteAppBlockBuilder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/DeleteAppBlockBuilder)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/DeleteAppBlockBuilder)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/DeleteAppBlockBuilder)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/DeleteAppBlockBuilder)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/DeleteAppBlockBuilder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/DeleteAppBlockBuilder)

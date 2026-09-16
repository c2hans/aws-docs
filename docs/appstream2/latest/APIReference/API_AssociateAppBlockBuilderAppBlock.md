---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateAppBlockBuilderAppBlock.html
---

# AssociateAppBlockBuilderAppBlock
<a name="API_AssociateAppBlockBuilderAppBlock"></a>

Associates the specified app block builder with the specified app block.

## Request Syntax
<a name="API_AssociateAppBlockBuilderAppBlock_RequestSyntax"></a>

```
{
   "AppBlockArn": "{{string}}",
   "AppBlockBuilderName": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateAppBlockBuilderAppBlock_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppBlockArn](#API_AssociateAppBlockBuilderAppBlock_RequestSyntax) **   <a name="WorkSpacesApplications-AssociateAppBlockBuilderAppBlock-request-AppBlockArn"></a>
The ARN of the app block.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** [AppBlockBuilderName](#API_AssociateAppBlockBuilderAppBlock_RequestSyntax) **   <a name="WorkSpacesApplications-AssociateAppBlockBuilderAppBlock-request-AppBlockBuilderName"></a>
The name of the app block builder.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_AssociateAppBlockBuilderAppBlock_ResponseSyntax"></a>

```
{
   "AppBlockBuilderAppBlockAssociation": {
      "AppBlockArn": "string",
      "AppBlockBuilderName": "string"
   }
}
```

## Response Elements
<a name="API_AssociateAppBlockBuilderAppBlock_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppBlockBuilderAppBlockAssociation](#API_AssociateAppBlockBuilderAppBlock_ResponseSyntax) **   <a name="WorkSpacesApplications-AssociateAppBlockBuilderAppBlock-response-AppBlockBuilderAppBlockAssociation"></a>
The list of app block builders associated with app blocks.
Type: [AppBlockBuilderAppBlockAssociation](API_AppBlockBuilderAppBlockAssociation.md) object

## Errors
<a name="API_AssociateAppBlockBuilderAppBlock_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_AssociateAppBlockBuilderAppBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/AssociateAppBlockBuilderAppBlock)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/AssociateAppBlockBuilderAppBlock)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AssociateAppBlockBuilderAppBlock)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/AssociateAppBlockBuilderAppBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AssociateAppBlockBuilderAppBlock)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/AssociateAppBlockBuilderAppBlock)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/AssociateAppBlockBuilderAppBlock)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/AssociateAppBlockBuilderAppBlock)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/AssociateAppBlockBuilderAppBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AssociateAppBlockBuilderAppBlock)

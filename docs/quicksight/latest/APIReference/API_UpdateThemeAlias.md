---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateThemeAlias.html
---

# UpdateThemeAlias
<a name="API_UpdateThemeAlias"></a>

Updates an alias of a theme.

## Request Syntax
<a name="API_UpdateThemeAlias_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/themes/{{ThemeId}}/aliases/{{AliasName}} HTTP/1.1
Content-type: application/json

{
   "ThemeVersionNumber": {{number}}
}
```

## URI Request Parameters
<a name="API_UpdateThemeAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AliasName](#API_UpdateThemeAlias_RequestSyntax) **   <a name="QS-UpdateThemeAlias-request-uri-AliasName"></a>
The name of the theme alias that you want to update.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)`
Required: Yes

 ** [AwsAccountId](#API_UpdateThemeAlias_RequestSyntax) **   <a name="QS-UpdateThemeAlias-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the theme alias that you're updating.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

 ** [ThemeId](#API_UpdateThemeAlias_RequestSyntax) **   <a name="QS-UpdateThemeAlias-request-uri-ThemeId"></a>
The ID for the theme.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

## Request Body
<a name="API_UpdateThemeAlias_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ThemeVersionNumber](#API_UpdateThemeAlias_RequestSyntax) **   <a name="QS-UpdateThemeAlias-request-ThemeVersionNumber"></a>
The version number of the theme that the alias should reference.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

## Response Syntax
<a name="API_UpdateThemeAlias_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string",
   "ThemeAlias": {
      "AliasName": "string",
      "Arn": "string",
      "ThemeVersionNumber": number
   }
}
```

## Response Elements
<a name="API_UpdateThemeAlias_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateThemeAlias_ResponseSyntax) **   <a name="QS-UpdateThemeAlias-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_UpdateThemeAlias_ResponseSyntax) **   <a name="QS-UpdateThemeAlias-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [ThemeAlias](#API_UpdateThemeAlias_ResponseSyntax) **   <a name="QS-UpdateThemeAlias-response-ThemeAlias"></a>
Information about the theme alias.
Type: [ThemeAlias](API_ThemeAlias.md) object

## Errors
<a name="API_UpdateThemeAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceExistsException **
The resource specified already exists.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateThemeAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateThemeAlias)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateThemeAlias)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateThemeAlias)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateThemeAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateThemeAlias)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateThemeAlias)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateThemeAlias)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateThemeAlias)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateThemeAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateThemeAlias)

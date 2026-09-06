---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateServiceAction.html
---

# UpdateServiceAction
<a name="API_UpdateServiceAction"></a>

Updates a self-service action.

## Request Syntax
<a name="API_UpdateServiceAction_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Definition": {
      "{{string}}" : "{{string}}"
   },
   "Description": "{{string}}",
   "Id": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateServiceAction_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_UpdateServiceAction_RequestSyntax) **   <a name="servicecatalog-UpdateServiceAction-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Definition](#API_UpdateServiceAction_RequestSyntax) **   <a name="servicecatalog-UpdateServiceAction-request-Definition"></a>
A map that defines the self-service action.
Type: String to string map
Map Entries: Maximum number of 100 items.
Valid Keys: `Name | Version | AssumeRole | Parameters`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [Description](#API_UpdateServiceAction_RequestSyntax) **   <a name="servicecatalog-UpdateServiceAction-request-Description"></a>
The self-service action description.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [Id](#API_UpdateServiceAction_RequestSyntax) **   <a name="servicecatalog-UpdateServiceAction-request-Id"></a>
The self-service action identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [Name](#API_UpdateServiceAction_RequestSyntax) **   <a name="servicecatalog-UpdateServiceAction-request-Name"></a>
The self-service action name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_\-.]*`
Required: No

## Response Syntax
<a name="API_UpdateServiceAction_ResponseSyntax"></a>

```
{
   "ServiceActionDetail": {
      "Definition": {
         "string" : "string"
      },
      "ServiceActionSummary": {
         "DefinitionType": "string",
         "Description": "string",
         "Id": "string",
         "Name": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateServiceAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ServiceActionDetail](#API_UpdateServiceAction_ResponseSyntax) **   <a name="servicecatalog-UpdateServiceAction-response-ServiceActionDetail"></a>
Detailed information about the self-service action.
Type: [ServiceActionDetail](API_ServiceActionDetail.md) object

## Errors
<a name="API_UpdateServiceAction_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateServiceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/UpdateServiceAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateServiceAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/UpdateServiceAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateServiceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateServiceAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateServiceAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateServiceAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateServiceAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/UpdateServiceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateServiceAction)

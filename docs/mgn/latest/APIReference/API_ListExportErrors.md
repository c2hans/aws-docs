---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListExportErrors.html
---

# ListExportErrors
<a name="API_ListExportErrors"></a>

List export errors.

## Request Syntax
<a name="API_ListExportErrors_RequestSyntax"></a>

```
POST /ListExportErrors HTTP/1.1
Content-type: application/json

{
   "exportID": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListExportErrors_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListExportErrors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [exportID](#API_ListExportErrors_RequestSyntax) **   <a name="mgn-ListExportErrors-request-exportID"></a>
List export errors request export id.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `export-[0-9a-zA-Z]{17}`
Required: Yes

 ** [maxResults](#API_ListExportErrors_RequestSyntax) **   <a name="mgn-ListExportErrors-request-maxResults"></a>
List export errors request max results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListExportErrors_RequestSyntax) **   <a name="mgn-ListExportErrors-request-nextToken"></a>
List export errors request next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListExportErrors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "errorData": {
            "rawError": "string"
         },
         "errorDateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListExportErrors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListExportErrors_ResponseSyntax) **   <a name="mgn-ListExportErrors-response-items"></a>
List export errors response items.
Type: Array of [ExportTaskError](API_ExportTaskError.md) objects

 ** [nextToken](#API_ListExportErrors_ResponseSyntax) **   <a name="mgn-ListExportErrors-response-nextToken"></a>
List export errors response next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListExportErrors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_ListExportErrors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListExportErrors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListExportErrors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListExportErrors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListExportErrors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListExportErrors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListExportErrors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListExportErrors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListExportErrors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListExportErrors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListExportErrors)

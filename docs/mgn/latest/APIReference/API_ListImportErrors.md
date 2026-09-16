---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListImportErrors.html
---

# ListImportErrors
<a name="API_ListImportErrors"></a>

List import errors.

## Request Syntax
<a name="API_ListImportErrors_RequestSyntax"></a>

```
POST /ListImportErrors HTTP/1.1
Content-type: application/json

{
   "importID": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImportErrors_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImportErrors_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [importID](#API_ListImportErrors_RequestSyntax) **   <a name="mgn-ListImportErrors-request-importID"></a>
List import errors request import id.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `import-[0-9a-zA-Z]{17}`
Required: Yes

 ** [maxResults](#API_ListImportErrors_RequestSyntax) **   <a name="mgn-ListImportErrors-request-maxResults"></a>
List import errors request max results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListImportErrors_RequestSyntax) **   <a name="mgn-ListImportErrors-request-nextToken"></a>
List import errors request next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListImportErrors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "errorData": {
            "accountID": "string",
            "applicationID": "string",
            "ec2LaunchTemplateID": "string",
            "rawError": "string",
            "rowNumber": number,
            "sourceServerID": "string",
            "waveID": "string"
         },
         "errorDateTime": "string",
         "errorType": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListImportErrors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListImportErrors_ResponseSyntax) **   <a name="mgn-ListImportErrors-response-items"></a>
List imports errors response items.
Type: Array of [ImportTaskError](API_ImportTaskError.md) objects

 ** [nextToken](#API_ListImportErrors_ResponseSyntax) **   <a name="mgn-ListImportErrors-response-nextToken"></a>
List imports errors response next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListImportErrors_Errors"></a>

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
<a name="API_ListImportErrors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListImportErrors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListImportErrors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListImportErrors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListImportErrors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListImportErrors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListImportErrors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListImportErrors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListImportErrors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListImportErrors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListImportErrors)

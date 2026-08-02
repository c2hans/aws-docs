---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListImports.html
---

# ListImports
<a name="API_ListImports"></a>

List imports.

## Request Syntax
<a name="API_ListImports_RequestSyntax"></a>

```
POST /ListImports HTTP/1.1
Content-type: application/json

{
   "filters": {
      "importIDs": [ "{{string}}" ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListImports_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListImports_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListImports_RequestSyntax) **   <a name="mgn-ListImports-request-filters"></a>
List imports request filters.
Type: [ListImportsRequestFilters](API_ListImportsRequestFilters.md) object
Required: No

 ** [maxResults](#API_ListImports_RequestSyntax) **   <a name="mgn-ListImports-request-maxResults"></a>
List imports request max results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListImports_RequestSyntax) **   <a name="mgn-ListImports-request-nextToken"></a>
List imports request next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListImports_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "creationDateTime": "string",
         "endDateTime": "string",
         "importID": "string",
         "progressPercentage": number,
         "s3BucketSource": {
            "s3Bucket": "string",
            "s3BucketOwner": "string",
            "s3Key": "string"
         },
         "status": "string",
         "summary": {
            "applications": {
               "createdCount": number,
               "modifiedCount": number
            },
            "servers": {
               "createdCount": number,
               "modifiedCount": number
            },
            "waves": {
               "createdCount": number,
               "modifiedCount": number
            }
         },
         "tags": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListImports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListImports_ResponseSyntax) **   <a name="mgn-ListImports-response-items"></a>
List import response items.
Type: Array of [ImportTask](API_ImportTask.md) objects

 ** [nextToken](#API_ListImports_ResponseSyntax) **   <a name="mgn-ListImports-response-nextToken"></a>
List import response next token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_ListImports_Errors"></a>

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
<a name="API_ListImports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/ListImports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/ListImports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListImports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/ListImports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListImports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/ListImports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/ListImports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/ListImports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/ListImports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListImports)

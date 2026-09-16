---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ListDatasets.html
---

# ListDatasets
<a name="API_ListDatasets"></a>

Lists all of the DataBrew datasets.

## Request Syntax
<a name="API_ListDatasets_RequestSyntax"></a>

```
GET /datasets?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDatasets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListDatasets_RequestSyntax) **   <a name="databrew-ListDatasets-request-uri-MaxResults"></a>
The maximum number of results to return in this request.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListDatasets_RequestSyntax) **   <a name="databrew-ListDatasets-request-uri-NextToken"></a>
The token returned by a previous call to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Request Body
<a name="API_ListDatasets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDatasets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Datasets": [
      {
         "AccountId": "string",
         "CreateDate": number,
         "CreatedBy": "string",
         "Format": "string",
         "FormatOptions": {
            "Csv": {
               "Delimiter": "string",
               "HeaderRow": boolean
            },
            "Excel": {
               "HeaderRow": boolean,
               "SheetIndexes": [ number ],
               "SheetNames": [ "string" ]
            },
            "Json": {
               "MultiLine": boolean
            }
         },
         "Input": {
            "DatabaseInputDefinition": {
               "DatabaseTableName": "string",
               "GlueConnectionName": "string",
               "QueryString": "string",
               "TempDirectory": {
                  "Bucket": "string",
                  "BucketOwner": "string",
                  "Key": "string"
               }
            },
            "DataCatalogInputDefinition": {
               "CatalogId": "string",
               "DatabaseName": "string",
               "TableName": "string",
               "TempDirectory": {
                  "Bucket": "string",
                  "BucketOwner": "string",
                  "Key": "string"
               }
            },
            "Metadata": {
               "SourceArn": "string"
            },
            "S3InputDefinition": {
               "Bucket": "string",
               "BucketOwner": "string",
               "Key": "string"
            }
         },
         "LastModifiedBy": "string",
         "LastModifiedDate": number,
         "Name": "string",
         "PathOptions": {
            "FilesLimit": {
               "MaxFiles": number,
               "Order": "string",
               "OrderedBy": "string"
            },
            "LastModifiedDateCondition": {
               "Expression": "string",
               "ValuesMap": {
                  "string" : "string"
               }
            },
            "Parameters": {
               "string" : {
                  "CreateColumn": boolean,
                  "DatetimeOptions": {
                     "Format": "string",
                     "LocaleCode": "string",
                     "TimezoneOffset": "string"
                  },
                  "Filter": {
                     "Expression": "string",
                     "ValuesMap": {
                        "string" : "string"
                     }
                  },
                  "Name": "string",
                  "Type": "string"
               }
            }
         },
         "ResourceArn": "string",
         "Source": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Datasets](#API_ListDatasets_ResponseSyntax) **   <a name="databrew-ListDatasets-response-Datasets"></a>
A list of datasets that are defined.
Type: Array of [Dataset](API_Dataset.md) objects

 ** [NextToken](#API_ListDatasets_ResponseSyntax) **   <a name="databrew-ListDatasets-response-NextToken"></a>
A token that you can use in a subsequent call to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListDatasets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationException **
The input parameters for this request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListDatasets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/databrew-2017-07-25/ListDatasets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/databrew-2017-07-25/ListDatasets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ListDatasets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/databrew-2017-07-25/ListDatasets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ListDatasets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/databrew-2017-07-25/ListDatasets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/databrew-2017-07-25/ListDatasets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/databrew-2017-07-25/ListDatasets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/databrew-2017-07-25/ListDatasets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ListDatasets)

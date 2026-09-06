---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListDocuments.html
---

# ListDocuments
<a name="API_ListDocuments"></a>

Returns all Systems Manager (SSM) documents in the current AWS account and AWS Region. You can limit the results of this request by using a filter.

## Request Syntax
<a name="API_ListDocuments_RequestSyntax"></a>

```
{
   "DocumentFilterList": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDocuments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DocumentFilterList](#API_ListDocuments_RequestSyntax) **   <a name="systemsmanager-ListDocuments-request-DocumentFilterList"></a>
This data type is deprecated. Instead, use `Filters`.
Type: Array of [DocumentFilter](API_DocumentFilter.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [Filters](#API_ListDocuments_RequestSyntax) **   <a name="systemsmanager-ListDocuments-request-Filters"></a>
One or more `DocumentKeyValuesFilter` objects. Use a filter to return a more specific list of results. For keys, you can specify one or more key-value pair tags that have been applied to a document. Other valid keys include `Owner`, `Name`, `PlatformTypes`, `DocumentType`, and `TargetType`. For example, to return documents you own use `Key=Owner,Values=Self`. To specify a custom key-value pair, use the format `Key=tag:tagName,Values=valueName`.
This API operation only supports filtering documents by using a single tag key and one or more tag values. For example: `Key=tag:tagName,Values=valueName1,valueName2`
Type: Array of [DocumentKeyValuesFilter](API_DocumentKeyValuesFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 6 items.
Required: No

 ** [MaxResults](#API_ListDocuments_RequestSyntax) **   <a name="systemsmanager-ListDocuments-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListDocuments_RequestSyntax) **   <a name="systemsmanager-ListDocuments-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_ListDocuments_ResponseSyntax"></a>

```
{
   "DocumentIdentifiers": [
      {
         "Author": "string",
         "CreatedDate": number,
         "DisplayName": "string",
         "DocumentFormat": "string",
         "DocumentType": "string",
         "DocumentVersion": "string",
         "Name": "string",
         "Owner": "string",
         "PlatformTypes": [ "string" ],
         "Requires": [
            {
               "Name": "string",
               "RequireType": "string",
               "Version": "string",
               "VersionName": "string"
            }
         ],
         "ReviewStatus": "string",
         "SchemaVersion": "string",
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "TargetType": "string",
         "VersionName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDocuments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DocumentIdentifiers](#API_ListDocuments_ResponseSyntax) **   <a name="systemsmanager-ListDocuments-response-DocumentIdentifiers"></a>
The names of the SSM documents.
Type: Array of [DocumentIdentifier](API_DocumentIdentifier.md) objects

 ** [NextToken](#API_ListDocuments_ResponseSyntax) **   <a name="systemsmanager-ListDocuments-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_ListDocuments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilterKey **
The specified key isn't valid.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_ListDocuments_Examples"></a>

### Example
<a name="API_ListDocuments_Example_1"></a>

This example illustrates one usage of ListDocuments.

#### Sample Request
<a name="API_ListDocuments_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.ListDocuments
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T150301Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 97

{
    "Filters": [
        {
            "Key": "Owner",
            "Values": [
                "Self"
            ]
        },
        {
            "Key": "tag:DocUse",
            "Values": [
                "Testing"
            ]
        }
    ]
}
```

#### Sample Response
<a name="API_ListDocuments_Example_1_Response"></a>

```
{
    "DocumentIdentifiers": [
        {
            "CreatedDate": 1486594364.541,
            "DocumentFormat": "YAML",
            "DocumentType": "Automation",
            "DocumentVersion": "1",
            "DisplayName": "ExampleDoc",
            "Name": "Example",
            "Owner": "111122223333",
            "PlatformTypes": [
                "Windows",
                "Linux"
            ],
            "SchemaVersion": "0.3",
            "Tags": [
                {
                    "Key": "DocUse",
                    "Value": "Testing"
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_ListDocuments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/ListDocuments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/ListDocuments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ListDocuments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/ListDocuments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ListDocuments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/ListDocuments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/ListDocuments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/ListDocuments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/ListDocuments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ListDocuments)

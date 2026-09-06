---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_ListDatasourcePackages.html
---

# ListDatasourcePackages
<a name="API_ListDatasourcePackages"></a>

Lists data source packages in the behavior graph.

## Request Syntax
<a name="API_ListDatasourcePackages_RequestSyntax"></a>

```
POST /graph/datasources/list HTTP/1.1
Content-type: application/json

{
   "GraphArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListDatasourcePackages_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDatasourcePackages_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GraphArn](#API_ListDatasourcePackages_RequestSyntax) **   <a name="detective-ListDatasourcePackages-request-GraphArn"></a>
The ARN of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

 ** [MaxResults](#API_ListDatasourcePackages_RequestSyntax) **   <a name="detective-ListDatasourcePackages-request-MaxResults"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_ListDatasourcePackages_RequestSyntax) **   <a name="detective-ListDatasourcePackages-request-NextToken"></a>
For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListDatasourcePackages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DatasourcePackages": {
      "string" : {
         "DatasourcePackageIngestState": "string",
         "LastIngestStateChange": {
            "string" : {
               "Timestamp": "string"
            }
         }
      }
   },
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasourcePackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatasourcePackages](#API_ListDatasourcePackages_ResponseSyntax) **   <a name="detective-ListDatasourcePackages-response-DatasourcePackages"></a>
Details on the data source packages active in the behavior graph.
Type: String to [DatasourcePackageIngestDetail](API_DatasourcePackageIngestDetail.md) object map
Valid Keys: `DETECTIVE_CORE | EKS_AUDIT | ASFF_SECURITYHUB_FINDING`

 ** [NextToken](#API_ListDatasourcePackages_ResponseSyntax) **   <a name="detective-ListDatasourcePackages-response-NextToken"></a>
For requests to get the next page of results, the pagination token that was returned with the previous set of results. The initial request does not include a pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListDatasourcePackages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request refers to a nonexistent resource.
HTTP Status Code: 404

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## Examples
<a name="API_ListDatasourcePackages_Examples"></a>

### Example
<a name="API_ListDatasourcePackages_Example_1"></a>

This example illustrates one usage of ListDatasourcePackages.

#### Sample Request
<a name="API_ListDatasourcePackages_Example_1_Request"></a>

```
POST /graph/datasources/list HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: gzip, deflate, br
Content-Length: 94
Authorization: AUTHPARAMS
X-Amz-Date: 20220511T171741Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33

{
  "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:1a8ef4ba50e74440b4b3c0d4a32ef48b"
}
```

### Example
<a name="API_ListDatasourcePackages_Example_2"></a>

This example illustrates one usage of ListDatasourcePackages.

#### Sample Response
<a name="API_ListDatasourcePackages_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 759
Date: Wed, 11 May 2022 17:17:41 GMT
x-amzn-RequestId: ddce670a-02cf-4993-9bb7-72e05c2d08f1
Connection: Keep-alive

{
   "DatasourcePackages":{
      "DETECTIVE_CORE":{
         "DatasourcePackageIngestState":"STARTED",
         "LastIngestStateChange":{
            "DISABLED":null,
            "STOPPED":null,
            "STARTED":{
               "Timestamp":"2022-01-03T15:25:39.865Z"
            }
         }
      },
      "EKS_AUDIT":{
         "DatasourcePackageIngestState":"STARTED",
         "LastIngestStateChange":{
            "DISABLED":null,
            "STOPPED":{
               "Timestamp":"2022-05-05T14:38:13.959Z"
            },
            "STARTED":{
               "Timestamp":"2022-05-05T14:38:47.379Z"
            }
         },
       "ASFF_SECURITYHUB_FINDING":{
         "DatasourcePackageIngestState":"STARTED",
         "LastIngestStateChange":{
            "DISABLED":null,
            "STOPPED":{
               "Timestamp":"2023-05-15T09:22:10.331Z"
            },
            "STARTED":{
               "Timestamp":"2022-05-15T09:22:55.020Z"
            }
         }
      }
   }
}
```

## See Also
<a name="API_ListDatasourcePackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/ListDatasourcePackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/ListDatasourcePackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/ListDatasourcePackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/ListDatasourcePackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/ListDatasourcePackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/ListDatasourcePackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/ListDatasourcePackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/ListDatasourcePackages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/ListDatasourcePackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/ListDatasourcePackages)

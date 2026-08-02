---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_ListOperations.html
---

# ListOperations
<a name="API_ListOperations"></a>

Lists the operations performed by AWS Systems Manager for SAP.

## Request Syntax
<a name="API_ListOperations_RequestSyntax"></a>

```
POST /list-operations HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}",
   "Filters": [
      {
         "Name": "{{string}}",
         "Operator": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListOperations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListOperations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_ListOperations_RequestSyntax) **   <a name="ssmsap-ListOperations-request-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: Yes

 ** [Filters](#API_ListOperations_RequestSyntax) **   <a name="ssmsap-ListOperations-request-Filters"></a>
The filters of an operation.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [MaxResults](#API_ListOperations_RequestSyntax) **   <a name="ssmsap-ListOperations-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value. If you do not specify a value for MaxResults, the request returns 50 items per page by default.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_ListOperations_RequestSyntax) **   <a name="ssmsap-ListOperations-request-NextToken"></a>
The token for the next page of results.
Type: String
Pattern: `.{16,2048}`
Required: No

## Response Syntax
<a name="API_ListOperations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Operations": [
      {
         "EndTime": number,
         "Id": "string",
         "LastUpdatedTime": number,
         "Properties": {
            "string" : "string"
         },
         "ResourceArn": "string",
         "ResourceId": "string",
         "ResourceType": "string",
         "StartTime": number,
         "Status": "string",
         "StatusMessage": "string",
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListOperations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListOperations_ResponseSyntax) **   <a name="ssmsap-ListOperations-response-NextToken"></a>
The token to use to retrieve the next page of results. This value is null when there are no more results to return.
Type: String
Pattern: `.{16,2048}`

 ** [Operations](#API_ListOperations_ResponseSyntax) **   <a name="ssmsap-ListOperations-response-Operations"></a>
List of operations performed by AWS Systems Manager for SAP.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_ListOperations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListOperations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/ListOperations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/ListOperations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/ListOperations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/ListOperations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/ListOperations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/ListOperations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/ListOperations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/ListOperations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/ListOperations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/ListOperations)

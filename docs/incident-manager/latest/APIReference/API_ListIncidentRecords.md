---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_ListIncidentRecords.html
---

# ListIncidentRecords
<a name="API_ListIncidentRecords"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

Lists all incident records in your account. Use this command to retrieve the Amazon Resource Name (ARN) of the incident record you want to update.

## Request Syntax
<a name="API_ListIncidentRecords_RequestSyntax"></a>

```
POST /listIncidentRecords HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "condition": { ... },
         "key": "{{string}}"
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListIncidentRecords_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListIncidentRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListIncidentRecords_RequestSyntax) **   <a name="IncidentManager-ListIncidentRecords-request-filters"></a>
Filters the list of incident records you want to search through. You can filter on the following keys:
+  `creationTime`
+  `impact`
+  `status`
+  `createdBy`
Note the following when when you use Filters:
+ If you don't specify a Filter, the response includes all incident records.
+ If you specify more than one filter in a single request, the response returns incident records that match all filters.
+ If you specify a filter with more than one value, the response returns incident records that match any of the values provided.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [maxResults](#API_ListIncidentRecords_RequestSyntax) **   <a name="IncidentManager-ListIncidentRecords-request-maxResults"></a>
The maximum number of results per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListIncidentRecords_RequestSyntax) **   <a name="IncidentManager-ListIncidentRecords-request-nextToken"></a>
The pagination token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_ListIncidentRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "incidentRecordSummaries": [
      {
         "arn": "string",
         "creationTime": number,
         "impact": number,
         "incidentRecordSource": {
            "createdBy": "string",
            "invokedBy": "string",
            "resourceArn": "string",
            "source": "string"
         },
         "resolvedTime": number,
         "status": "string",
         "title": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListIncidentRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [incidentRecordSummaries](#API_ListIncidentRecords_ResponseSyntax) **   <a name="IncidentManager-ListIncidentRecords-response-incidentRecordSummaries"></a>
The details of each listed incident record.
Type: Array of [IncidentRecordSummary](API_IncidentRecordSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListIncidentRecords_ResponseSyntax) **   <a name="IncidentManager-ListIncidentRecords-response-nextToken"></a>
The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

## Errors
<a name="API_ListIncidentRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_ListIncidentRecords_Examples"></a>

### Example
<a name="API_ListIncidentRecords_Example_1"></a>

This example illustrates one usage of ListIncidentRecords.

#### Sample Request
<a name="API_ListIncidentRecords_Example_1_Request"></a>

```
POST /listIncidentRecords HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.list-incident-records
X-Amz-Date: 20210811T170938Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210811/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_ListIncidentRecords_Example_1_Response"></a>

```
{
    "incidentRecordSummaries": [
        {
            "arn": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/78bd9919-b9ac-962d-91e0-149960600e3f",
            "creationTime": "2021-08-10T22:33:57.849000+00:00",
            "impact": 5,
            "incidentRecordSource": {
                "createdBy": "arn:aws:sts::111122223333:assumed-role/Admin/exampleUser",
                "invokedBy": "arn:aws:sts::111122223333:assumed-role/Admin/exampleUser",
                "source": "aws.ssm-incidents.custom"
            },
            "status": "OPEN",
            "title": "example-incident"
        }
    ]
}
```

## See Also
<a name="API_ListIncidentRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/ListIncidentRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/ListIncidentRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/ListIncidentRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/ListIncidentRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/ListIncidentRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/ListIncidentRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/ListIncidentRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/ListIncidentRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/ListIncidentRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/ListIncidentRecords)

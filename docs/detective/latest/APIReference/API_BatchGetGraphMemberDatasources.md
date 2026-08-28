---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_BatchGetGraphMemberDatasources.html
---

# BatchGetGraphMemberDatasources
<a name="API_BatchGetGraphMemberDatasources"></a>

Gets data source package information for the behavior graph.

## Request Syntax
<a name="API_BatchGetGraphMemberDatasources_RequestSyntax"></a>

```
POST /graph/datasources/get HTTP/1.1
Content-type: application/json

{
   "AccountIds": [ "{{string}}" ],
   "GraphArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchGetGraphMemberDatasources_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetGraphMemberDatasources_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountIds](#API_BatchGetGraphMemberDatasources_RequestSyntax) **   <a name="detective-BatchGetGraphMemberDatasources-request-AccountIds"></a>
The list of AWS accounts to get data source package information on.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: Yes

 ** [GraphArn](#API_BatchGetGraphMemberDatasources_RequestSyntax) **   <a name="detective-BatchGetGraphMemberDatasources-request-GraphArn"></a>
The ARN of the behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

## Response Syntax
<a name="API_BatchGetGraphMemberDatasources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "MemberDatasources": [
      {
         "AccountId": "string",
         "DatasourcePackageIngestHistory": {
            "string" : {
               "string" : {
                  "Timestamp": "string"
               }
            }
         },
         "GraphArn": "string"
      }
   ],
   "UnprocessedAccounts": [
      {
         "AccountId": "string",
         "Reason": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetGraphMemberDatasources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [MemberDatasources](#API_BatchGetGraphMemberDatasources_ResponseSyntax) **   <a name="detective-BatchGetGraphMemberDatasources-response-MemberDatasources"></a>
Details on the status of data source packages for members of the behavior graph.
Type: Array of [MembershipDatasources](API_MembershipDatasources.md) objects

 ** [UnprocessedAccounts](#API_BatchGetGraphMemberDatasources_ResponseSyntax) **   <a name="detective-BatchGetGraphMemberDatasources-response-UnprocessedAccounts"></a>
Accounts that data source package information could not be retrieved for.
Type: Array of [UnprocessedAccount](API_UnprocessedAccount.md) objects

## Errors
<a name="API_BatchGetGraphMemberDatasources_Errors"></a>

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
<a name="API_BatchGetGraphMemberDatasources_Examples"></a>

### Example
<a name="API_BatchGetGraphMemberDatasources_Example_1"></a>

This example illustrates one usage of BatchGetGraphMemberDatasources.

#### Sample Request
<a name="API_BatchGetGraphMemberDatasources_Example_1_Request"></a>

```
GET /graph/datasources/get HTTP/1.1
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: gzip, deflate, br
Content-Length: 94
Authorization: AUTHPARAMS
X-Amz-Date: 20220511T171741Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33

{
  "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:1a8ef4ba50e74440b4b3c0d4a32ef48b",
  "AccountIds": ["379346275224"]
}
```

### Example
<a name="API_BatchGetGraphMemberDatasources_Example_2"></a>

This example illustrates one usage of BatchGetGraphMemberDatasources.

#### Sample Response
<a name="API_BatchGetGraphMemberDatasources_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 596
Date: Wed, 11 May 2022 17:17:41 GMT
x-amzn-RequestId: ddce670a-02cf-4993-9bb7-72e05c2d08f1
Connection: Keep-alive

{
  "MemberDatasources": [
    {
      "AccountId": "379346275224",
      "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:1a8ef4ba50e74440b4b3c0d4a32ef48b",
      "DatasourcePackageIngestHistory": {
        "DETECTIVE_CORE": {
          "STOPPED": null,
          "STARTED": {
            "Timestamp": "2022-05-05T18:56:33.656Z"
          }
        },
        "EKS_AUDIT": {
          "STOPPED": {
            "Timestamp": "2022-05-05T19:00:12.621Z"
          },
          "STARTED": {
            "Timestamp": "2022-05-05T18:56:33.656Z"
          }
        },
         "ASFF_SECURITYHUB_FINDING": {
          "STOPPED":{
            "Timestamp":"2023-05-15T12:47:23.975Z"
          },
          "STARTED":{
            "Timestamp":"2023-05-15T12:46:11.488Z"
          }
        }
      }
    }
  ],
  "UnprocessedAccounts": []
}
```

## See Also
<a name="API_BatchGetGraphMemberDatasources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/BatchGetGraphMemberDatasources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/BatchGetGraphMemberDatasources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/BatchGetGraphMemberDatasources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/BatchGetGraphMemberDatasources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/BatchGetGraphMemberDatasources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/BatchGetGraphMemberDatasources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/BatchGetGraphMemberDatasources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/BatchGetGraphMemberDatasources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/BatchGetGraphMemberDatasources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/BatchGetGraphMemberDatasources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

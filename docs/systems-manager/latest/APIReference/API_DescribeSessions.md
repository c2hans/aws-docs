---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeSessions.html
---

# DescribeSessions
<a name="API_DescribeSessions"></a>

Retrieves a list of all active sessions (both connected and disconnected) or terminated sessions from the past 30 days.

## Request Syntax
<a name="API_DescribeSessions_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "State": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSessions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeSessions_RequestSyntax) **   <a name="systemsmanager-DescribeSessions-request-Filters"></a>
One or more filters to limit the type of sessions returned by the request.
Type: Array of [SessionFilter](API_SessionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Required: No

 ** [MaxResults](#API_DescribeSessions_RequestSyntax) **   <a name="systemsmanager-DescribeSessions-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** [NextToken](#API_DescribeSessions_RequestSyntax) **   <a name="systemsmanager-DescribeSessions-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [State](#API_DescribeSessions_RequestSyntax) **   <a name="systemsmanager-DescribeSessions-request-State"></a>
The session status to retrieve a list of sessions for. For example, "Active".
Type: String
Valid Values: `Active | History`
Required: Yes

## Response Syntax
<a name="API_DescribeSessions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Sessions": [
      {
         "AccessType": "string",
         "Details": "string",
         "DocumentName": "string",
         "EndDate": number,
         "MaxSessionDuration": "string",
         "OutputUrl": {
            "CloudWatchOutputUrl": "string",
            "S3OutputUrl": "string"
         },
         "Owner": "string",
         "Reason": "string",
         "SessionId": "string",
         "StartDate": number,
         "Status": "string",
         "Target": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSessions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSessions_ResponseSyntax) **   <a name="systemsmanager-DescribeSessions-response-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String

 ** [Sessions](#API_DescribeSessions_ResponseSyntax) **   <a name="systemsmanager-DescribeSessions-response-Sessions"></a>
A list of sessions meeting the request parameters.
Type: Array of [Session](API_Session.md) objects

## Errors
<a name="API_DescribeSessions_Errors"></a>

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
<a name="API_DescribeSessions_Examples"></a>

### Example
<a name="API_DescribeSessions_Example_1"></a>

This example illustrates one usage of DescribeSessions.

#### Sample Request
<a name="API_DescribeSessions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeSessions
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240221T175636Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240221/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 20

{
    "State": "History"
}
```

#### Sample Response
<a name="API_DescribeSessions_Example_1_Response"></a>

```
{
    "Sessions": [
        {
            "EndDate": 1582069847.807,
            "OutputUrl": {
                "S3OutputUrl": "https://us-east-2.console.aws.amazon.com/s3/object/amzn-s3-demo-bucket/session-data/Mary-Major-0ab177d470EXAMPLE.log"
            },
            "Owner": "arn:aws:iam::111122223333:user/Mary-Major",
            "SessionId": "Mary-Major-0ab177d470EXAMPLE",
            "StartDate": 1582068633.188,
            "Status": "Terminated",
            "Target": "i-07782c72faEXAMPLE"
        }
        // There may be more content here
    ]
}
```

## See Also
<a name="API_DescribeSessions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeSessions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeSessions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeSessions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeSessions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeSessions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeSessions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeSessions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeSessions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeSessions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeSessions)

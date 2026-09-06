---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDestinations.html
---

# DescribeDestinations
<a name="API_DescribeDestinations"></a>

Lists all your destinations. The results are ASCII-sorted by destination name.

## Request Syntax
<a name="API_DescribeDestinations_RequestSyntax"></a>

```
{
   "DestinationNamePrefix": "{{string}}",
   "limit": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDestinations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationNamePrefix](#API_DescribeDestinations_RequestSyntax) **   <a name="CWL-DescribeDestinations-request-DestinationNamePrefix"></a>
The prefix to match. If you don't specify a value, no prefix filter is applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** [limit](#API_DescribeDestinations_RequestSyntax) **   <a name="CWL-DescribeDestinations-request-limit"></a>
The maximum number of items returned. If you don't specify a value, the default maximum value of 50 items is used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_DescribeDestinations_RequestSyntax) **   <a name="CWL-DescribeDestinations-request-nextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_DescribeDestinations_ResponseSyntax"></a>

```
{
   "destinations": [
      {
         "accessPolicy": "string",
         "arn": "string",
         "creationTime": number,
         "destinationName": "string",
         "roleArn": "string",
         "targetArn": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeDestinations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destinations](#API_DescribeDestinations_ResponseSyntax) **   <a name="CWL-DescribeDestinations-response-destinations"></a>
The destinations.
Type: Array of [Destination](API_Destination.md) objects

 ** [nextToken](#API_DescribeDestinations_ResponseSyntax) **   <a name="CWL-DescribeDestinations-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_DescribeDestinations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_DescribeDestinations_Examples"></a>

### To list all destinations
<a name="API_DescribeDestinations_Example_1"></a>

The following example lists all the destinations for the account.

#### Sample Request
<a name="API_DescribeDestinations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.DescribeDestinations
{
  "destinationNamePrefix": "my-prefix"
}
```

#### Sample Response
<a name="API_DescribeDestinations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  "destination": [
    {
      "destinationName": "my-destination",
      "targetArn": "arn:aws:kinesis:us-east-1:123456789012:stream/my-kinesis-stream",
      "roleArn": "arn:aws:iam::123456789012:role/my-subscription-role",
      "arn": "arn:aws:logs:us-east-1:123456789012:destination:my-destination",
      "creationTime": 1437584472382
    }
  ]
}
```

## See Also
<a name="API_DescribeDestinations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/DescribeDestinations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/DescribeDestinations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DescribeDestinations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/DescribeDestinations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DescribeDestinations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/DescribeDestinations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/DescribeDestinations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/DescribeDestinations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DescribeDestinations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DescribeDestinations)

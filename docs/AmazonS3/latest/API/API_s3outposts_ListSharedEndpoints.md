---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListSharedEndpoints.html
---

# ListSharedEndpoints
<a name="API_s3outposts_ListSharedEndpoints"></a>

Lists all endpoints associated with an Outpost that has been shared by AWS Resource Access Manager (RAM).

Related actions include:
+  [CreateEndpoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html)
+  [DeleteEndpoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html)

## Request Syntax
<a name="API_s3outposts_ListSharedEndpoints_RequestSyntax"></a>

```
GET /S3Outposts/ListSharedEndpoints?maxResults={{MaxResults}}&nextToken={{NextToken}}&outpostId={{OutpostId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3outposts_ListSharedEndpoints_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_s3outposts_ListSharedEndpoints_RequestSyntax) **   <a name="AmazonS3-s3outposts_ListSharedEndpoints-request-uri-MaxResults"></a>
The maximum number of endpoints that will be returned in the response.
Valid Range: Minimum value of 0. Maximum value of 100.

 ** [NextToken](#API_s3outposts_ListSharedEndpoints_RequestSyntax) **   <a name="AmazonS3-s3outposts_ListSharedEndpoints-request-uri-NextToken"></a>
If a previous response from this operation included a `NextToken` value, you can provide that value here to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`

 ** [OutpostId](#API_s3outposts_ListSharedEndpoints_RequestSyntax) **   <a name="AmazonS3-s3outposts_ListSharedEndpoints-request-uri-OutpostId"></a>
The ID of the AWS Outpost.
Pattern: `^(op-[a-f0-9]{17}|\d{12}|ec2)$`
Required: Yes

## Request Body
<a name="API_s3outposts_ListSharedEndpoints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3outposts_ListSharedEndpoints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Endpoints": [
      {
         "AccessType": "string",
         "CidrBlock": "string",
         "CreationTime": number,
         "CustomerOwnedIpv4Pool": "string",
         "EndpointArn": "string",
         "FailedReason": {
            "ErrorCode": "string",
            "Message": "string"
         },
         "NetworkInterfaces": [
            {
               "NetworkInterfaceId": "string"
            }
         ],
         "OutpostsId": "string",
         "SecurityGroupId": "string",
         "Status": "string",
         "SubnetId": "string",
         "VpcId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_s3outposts_ListSharedEndpoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Endpoints](#API_s3outposts_ListSharedEndpoints_ResponseSyntax) **   <a name="AmazonS3-s3outposts_ListSharedEndpoints-response-Endpoints"></a>
The list of endpoints associated with the specified Outpost that have been shared by AWS Resource Access Manager (RAM).
Type: Array of [Endpoint](API_s3outposts_Endpoint.md) objects

 ** [NextToken](#API_s3outposts_ListSharedEndpoints_ResponseSyntax) **   <a name="AmazonS3-s3outposts_ListSharedEndpoints-response-NextToken"></a>
If the number of endpoints associated with the specified Outpost exceeds `MaxResults`, you can include this value in subsequent calls to this operation to retrieve more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`

## Errors
<a name="API_s3outposts_ListSharedEndpoints_Errors"></a>

 ** AccessDeniedException **
Access was denied for this action.
HTTP Status Code: 403

 ** InternalServerException **
There was an exception with the internal server.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
There was an exception validating this data.
HTTP Status Code: 400

## See Also
<a name="API_s3outposts_ListSharedEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3outposts-2017-07-25/ListSharedEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3outposts-2017-07-25/ListSharedEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/ListSharedEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3outposts-2017-07-25/ListSharedEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/ListSharedEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3outposts-2017-07-25/ListSharedEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3outposts-2017-07-25/ListSharedEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3outposts-2017-07-25/ListSharedEndpoints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3outposts-2017-07-25/ListSharedEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/ListSharedEndpoints)

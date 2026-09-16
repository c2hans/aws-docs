---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileAssociations.html
---

# ListProfileAssociations
<a name="API_route53profiles_ListProfileAssociations"></a>

 Lists all the VPCs that the specified Route 53 Profile is associated with.

## Request Syntax
<a name="API_route53profiles_ListProfileAssociations_RequestSyntax"></a>

```
GET /profileassociations?maxResults={{MaxResults}}&nextToken={{NextToken}}&profileId={{ProfileId}}&resourceId={{ResourceId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53profiles_ListProfileAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_route53profiles_ListProfileAssociations_RequestSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileAssociations-request-uri-MaxResults"></a>
 The maximum number of objects that you want to return for this request. If more objects are available, in the response, a `NextToken` value, which you can use in a subsequent call to get the next batch of objects, is provided.
 If you don't specify a value for `MaxResults`, up to 100 objects are returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_route53profiles_ListProfileAssociations_RequestSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileAssociations-request-uri-NextToken"></a>
 For the first call to this list request, omit this value.
When you request a list of objects, at most the number of objects specified by `MaxResults` is returned. If more objects are available for retrieval, a `NextToken` value is returned in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.

 ** [ProfileId](#API_route53profiles_ListProfileAssociations_RequestSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileAssociations-request-uri-ProfileId"></a>
 ID of the Profile.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [ResourceId](#API_route53profiles_ListProfileAssociations_RequestSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileAssociations-request-uri-ResourceId"></a>
 ID of the VPC.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_route53profiles_ListProfileAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53profiles_ListProfileAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProfileAssociations": [
      {
         "CreationTime": number,
         "Id": "string",
         "ModificationTime": number,
         "Name": "string",
         "OwnerId": "string",
         "ProfileId": "string",
         "ResourceId": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53profiles_ListProfileAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_route53profiles_ListProfileAssociations_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileAssociations-response-NextToken"></a>
 If more than `MaxResults` profile associations match the specified criteria, you can submit another `ListProfileAssociations` request to get the next group of results. In the next request, specify the value of `NextToken` from the previous response.
Type: String

 ** [ProfileAssociations](#API_route53profiles_ListProfileAssociations_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileAssociations-response-ProfileAssociations"></a>
 A complex type that containts settings information about the profile's VPC associations.
Type: Array of [ProfileAssociation](API_route53profiles_ProfileAssociation.md) objects

## Errors
<a name="API_route53profiles_ListProfileAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The current account doesn't have the IAM permissions required to perform the specified operation.
HTTP Status Code: 400

 ** InvalidNextTokenException **
 The `NextToken` you provided isn;t valid.
HTTP Status Code: 400

 ** InvalidParameterException **
 One or more parameters in this request are not valid.
 ** FieldName **
 The parameter field name for the invalid parameter exception.
HTTP Status Code: 400

 ** ThrottlingException **
 The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
 You have provided an invalid command.
HTTP Status Code: 400

## Examples
<a name="API_route53profiles_ListProfileAssociations_Examples"></a>

### ListProfileAssociations Example
<a name="API_route53profiles_ListProfileAssociations_Example_1"></a>

This example illustrates one usage of ListProfileAssociations.

#### Sample Request
<a name="API_route53profiles_ListProfileAssociations_Example_1_Request"></a>

```
GET /profileassociations HTTP/1.1
host:route53profiles.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Date:20240319T231359Z
User-Agent: aws-cli/1.32.63 botocore/1.34.63 Python/3.8.18
Authorization: AWS4-HMAC-SHA256
    Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-1/route53profiles/aws4_request,
    SignedHeaders=host;x-amz-date;x-amz-security-token
    Signature=[calculated-signature]
{} # RequestBody is empty
```

#### Sample Response
<a name="API_route53profiles_ListProfileAssociations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 19 Mar 2024 23:14:00 GMT
Content-Type: application/json
Content-Length: 552
Connection: keep-alive
x-amzn-RequestId: dcd9d91e-1a5a-481f-82b7-bafe7dexample
Access-Control-Allow-Origin: *
x-amz-apigw-id: U5eX0FdmIexample=
X-Amzn-Trace-Id: Root=1-65fa10fe-6e5a93a56a325ab8example
{
    "ProfileAssociations": [
        {
            "CreationTime": 1710887901.139,
            "Id": "rpassoc-489ce212fexample",
            "ModificationTime": 1710887901.139,
            "Name": "test-association",
            "OwnerId": "123456789012",
            "ProfileId": "rp-4987774726example",
            "ResourceId": "vpc-0af3b96b3example",
            "Status": "COMPLETE",
            "StatusMessage": "Created Profile Association"
        }
    ]
}
```

## See Also
<a name="API_route53profiles_ListProfileAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53profiles-2018-05-10/ListProfileAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53profiles-2018-05-10/ListProfileAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/ListProfileAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53profiles-2018-05-10/ListProfileAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/ListProfileAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53profiles-2018-05-10/ListProfileAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53profiles-2018-05-10/ListProfileAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53profiles-2018-05-10/ListProfileAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/route53profiles-2018-05-10/ListProfileAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/ListProfileAssociations)

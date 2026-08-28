---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_ListProfileResourceAssociations.html
---

# ListProfileResourceAssociations
<a name="API_route53profiles_ListProfileResourceAssociations"></a>

 Lists all the resource associations for the specified Route 53 Profile.

## Request Syntax
<a name="API_route53profiles_ListProfileResourceAssociations_RequestSyntax"></a>

```
GET /profileresourceassociations/profileid/{{ProfileId}}?maxResults={{MaxResults}}&nextToken={{NextToken}}&resourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53profiles_ListProfileResourceAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_route53profiles_ListProfileResourceAssociations_RequestSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileResourceAssociations-request-uri-MaxResults"></a>
 The maximum number of objects that you want to return for this request. If more objects are available, in the response, a `NextToken` value, which you can use in a subsequent call to get the next batch of objects, is provided.
 If you don't specify a value for `MaxResults`, up to 100 objects are returned.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_route53profiles_ListProfileResourceAssociations_RequestSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileResourceAssociations-request-uri-NextToken"></a>
 For the first call to this list request, omit this value.
When you request a list of objects, at most the number of objects specified by `MaxResults` is returned. If more objects are available for retrieval, a `NextToken` value is returned in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.

 ** [ProfileId](#API_route53profiles_ListProfileResourceAssociations_RequestSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileResourceAssociations-request-uri-ProfileId"></a>
 The ID of the Profile.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ResourceType](#API_route53profiles_ListProfileResourceAssociations_RequestSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileResourceAssociations-request-uri-ResourceType"></a>
 ID of a resource if you want information on only one type.

## Request Body
<a name="API_route53profiles_ListProfileResourceAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53profiles_ListProfileResourceAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ProfileResourceAssociations": [
      {
         "CreationTime": number,
         "Id": "string",
         "ModificationTime": number,
         "Name": "string",
         "OwnerId": "string",
         "ProfileId": "string",
         "ResourceArn": "string",
         "ResourceProperties": "string",
         "ResourceType": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_route53profiles_ListProfileResourceAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_route53profiles_ListProfileResourceAssociations_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileResourceAssociations-response-NextToken"></a>
 If more than `MaxResults` resource associations match the specified criteria, you can submit another `ListProfileResourceAssociations` request to get the next group of results. In the next request, specify the value of `NextToken` from the previous response.
Type: String

 ** [ProfileResourceAssociations](#API_route53profiles_ListProfileResourceAssociations_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_ListProfileResourceAssociations-response-ProfileResourceAssociations"></a>
 Information about the profile resource association that you specified in a `GetProfileResourceAssociation` request.
Type: Array of [ProfileResourceAssociation](API_route53profiles_ProfileResourceAssociation.md) objects

## Errors
<a name="API_route53profiles_ListProfileResourceAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The current account doesn't have the IAM permissions required to perform the specified operation.
HTTP Status Code: 400

 ** InternalServiceErrorException **
 An internal server error occured. Retry your request.
HTTP Status Code: 400

 ** InvalidNextTokenException **
 The `NextToken` you provided isn;t valid.
HTTP Status Code: 400

 ** InvalidParameterException **
 One or more parameters in this request are not valid.
 ** FieldName **
 The parameter field name for the invalid parameter exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The resource you are associating is not found.
 ** ResourceType **
 The resource type that caused the resource not found exception.
HTTP Status Code: 400

 ** ThrottlingException **
 The request was throttled. Try again in a few minutes.
HTTP Status Code: 400

 ** ValidationException **
 You have provided an invalid command.
HTTP Status Code: 400

## Examples
<a name="API_route53profiles_ListProfileResourceAssociations_Examples"></a>

### ListProfileResourceAssociations Example
<a name="API_route53profiles_ListProfileResourceAssociations_Example_1"></a>

This example illustrates one usage of ListProfileResourceAssociations.

#### Sample Request
<a name="API_route53profiles_ListProfileResourceAssociations_Example_1_Request"></a>

```
GET /profileresourceassociations/profileid/rp-4987774726example HTTP/1.1
host:route53profiles.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Date:20240319T231834Z
User-Agent: aws-cli/1.32.63 botocore/1.34.63 Python/3.8.18
Authorization: AWS4-HMAC-SHA256
    Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-1/route53profiles/aws4_request,
    SignedHeaders=host;x-amz-date;x-amz-security-token
    Signature=[calculated-signature]
{} # RequestBody is empty
```

#### Sample Response
<a name="API_route53profiles_ListProfileResourceAssociations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 19 Mar 2024 23:18:34 GMT
Content-Type: application/json
Content-Length: 520
Connection: keep-alive
x-amzn-RequestId: dcd9d91e-1a5a-481f-82b7-bafe7dexample
Access-Control-Allow-Origin: *
x-amz-apigw-id: U5eX0FdmIexample=
X-Amzn-Trace-Id: Root=1-65fa10fe-6e5a93a56a325ab8example
{
    "ProfileResourceAssociations": [
        {
            "CreationTime": 1710851216.613,
            "Id": "rpr-001913120a7example",
            "ModificationTime": 1710851216.613,
            "Name": "test-resource-association",
            "OwnerId": "123456789012",
            "ProfileId": "rp-4987774726example",
            "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example",
            "ResourceProperties": "{\"priority\":102}",
            "ResourceType": "FIREWALL_RULE_GROUP",
            "Status": "COMPLETE",
            "StatusMessage": "Completed creation of Profile to DNS Firewall rule group association"
        }
    ]
}
```

## See Also
<a name="API_route53profiles_ListProfileResourceAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53profiles-2018-05-10/ListProfileResourceAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53profiles-2018-05-10/ListProfileResourceAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/ListProfileResourceAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53profiles-2018-05-10/ListProfileResourceAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/ListProfileResourceAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53profiles-2018-05-10/ListProfileResourceAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53profiles-2018-05-10/ListProfileResourceAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53profiles-2018-05-10/ListProfileResourceAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53profiles-2018-05-10/ListProfileResourceAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/ListProfileResourceAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

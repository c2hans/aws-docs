---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_GetProfileResourceAssociation.html
---

# GetProfileResourceAssociation
<a name="API_route53profiles_GetProfileResourceAssociation"></a>

 Returns information about a specified Route 53 Profile resource association.

## Request Syntax
<a name="API_route53profiles_GetProfileResourceAssociation_RequestSyntax"></a>

```
GET /profileresourceassociation/{{ProfileResourceAssociationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53profiles_GetProfileResourceAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ProfileResourceAssociationId](#API_route53profiles_GetProfileResourceAssociation_RequestSyntax) **   <a name="Route53Profiles-route53profiles_GetProfileResourceAssociation-request-uri-ProfileResourceAssociationId"></a>
 The ID of the profile resource association that you want to get information about.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_route53profiles_GetProfileResourceAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53profiles_GetProfileResourceAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProfileResourceAssociation": {
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
}
```

## Response Elements
<a name="API_route53profiles_GetProfileResourceAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProfileResourceAssociation](#API_route53profiles_GetProfileResourceAssociation_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_GetProfileResourceAssociation-response-ProfileResourceAssociation"></a>
 Information about the Profile resource association that you specified in a `GetProfileResourceAssociation` request.
Type: [ProfileResourceAssociation](API_route53profiles_ProfileResourceAssociation.md) object

## Errors
<a name="API_route53profiles_GetProfileResourceAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The current account doesn't have the IAM permissions required to perform the specified operation.
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
<a name="API_route53profiles_GetProfileResourceAssociation_Examples"></a>

### GetProfileResourceAssociation Example
<a name="API_route53profiles_GetProfileResourceAssociation_Example_1"></a>

This example illustrates one usage of GetProfileResourceAssociation.

#### Sample Request
<a name="API_route53profiles_GetProfileResourceAssociation_Example_1_Request"></a>

```
GET /profileresourceassociation/rpr-001913120a7example HTTP/1.1
host:route53profiles.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Date:20240319T231134Z
User-Agent: aws-cli/1.32.63 botocore/1.34.63 Python/3.8.18
Authorization: AWS4-HMAC-SHA256
    Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-1/route53profiles/aws4_request,
    SignedHeaders=host;x-amz-date;x-amz-security-token
    Signature=[calculated-signature]
{} # RequestBody is empty
```

#### Sample Response
<a name="API_route53profiles_GetProfileResourceAssociation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 19 Mar 2024 23:11:34 GMT
Content-Type: application/json
Content-Length: 517
Connection: keep-alive
x-amzn-RequestId: dcd9d91e-1a5a-481f-82b7-bafe7dexample
Access-Control-Allow-Origin: *
x-amz-apigw-id: U5eX0FdmIexample=
X-Amzn-Trace-Id: Root=1-65fa10fe-6e5a93a56a325ab8example
{
    "ProfileResourceAssociation": {
        "CreationTime": 1710887901.139,
        "Id": "rpr-001913120a7example",
        "ModificationTime": 1710887901.139,
        "Name": "test-resource-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example",
        "ResourceProperties": "{\"priority\":105}",
        "ResourceType": "FIREWALL_RULE_GROUP",
        "Status": "COMPLETE",
        "StatusMessage": "Completed creation of Profile to DNS Firewall rule group association"
    }
}
```

## See Also
<a name="API_route53profiles_GetProfileResourceAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53profiles-2018-05-10/GetProfileResourceAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53profiles-2018-05-10/GetProfileResourceAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/GetProfileResourceAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53profiles-2018-05-10/GetProfileResourceAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/GetProfileResourceAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53profiles-2018-05-10/GetProfileResourceAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53profiles-2018-05-10/GetProfileResourceAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53profiles-2018-05-10/GetProfileResourceAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53profiles-2018-05-10/GetProfileResourceAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/GetProfileResourceAssociation)

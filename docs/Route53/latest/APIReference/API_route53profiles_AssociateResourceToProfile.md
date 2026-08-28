---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateResourceToProfile.html
---

# AssociateResourceToProfile
<a name="API_route53profiles_AssociateResourceToProfile"></a>

 Associates a DNS resource configuration to a Route 53 Profile.

## Request Syntax
<a name="API_route53profiles_AssociateResourceToProfile_RequestSyntax"></a>

```
POST /profileresourceassociation HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "ProfileId": "{{string}}",
   "ResourceArn": "{{string}}",
   "ResourceProperties": "{{string}}"
}
```

## URI Request Parameters
<a name="API_route53profiles_AssociateResourceToProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_route53profiles_AssociateResourceToProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_route53profiles_AssociateResourceToProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_AssociateResourceToProfile-request-Name"></a>
 Name for the resource association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: Yes

 ** [ProfileId](#API_route53profiles_AssociateResourceToProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_AssociateResourceToProfile-request-ProfileId"></a>
 ID of the Profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ResourceArn](#API_route53profiles_AssociateResourceToProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_AssociateResourceToProfile-request-ResourceArn"></a>
 Amazon resource number, ARN, of the resource to associate. Either a private hosted zone, DNS Firewall rule group, Resolver rule, or an interface VPC endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [ResourceProperties](#API_route53profiles_AssociateResourceToProfile_RequestSyntax) **   <a name="Route53Profiles-route53profiles_AssociateResourceToProfile-request-ResourceProperties"></a>
 If you are adding a DNS Firewall rule group, include also a priority. The priority indicates the processing order for the rule groups, starting with the priority assinged the lowest value.
The allowed values for priority are between 100 and 9900.
Type: String
Required: No

## Response Syntax
<a name="API_route53profiles_AssociateResourceToProfile_ResponseSyntax"></a>

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
<a name="API_route53profiles_AssociateResourceToProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProfileResourceAssociation](#API_route53profiles_AssociateResourceToProfile_ResponseSyntax) **   <a name="Route53Profiles-route53profiles_AssociateResourceToProfile-response-ProfileResourceAssociation"></a>
 Infromation about the `AssociateResourceToProfile`, including a status message.
Type: [ProfileResourceAssociation](API_route53profiles_ProfileResourceAssociation.md) object

## Errors
<a name="API_route53profiles_AssociateResourceToProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The current account doesn't have the IAM permissions required to perform the specified operation.
HTTP Status Code: 400

 ** ConflictException **
 The request you submitted conflicts with an existing request.
HTTP Status Code: 400

 ** InternalServiceErrorException **
 An internal server error occured. Retry your request.
HTTP Status Code: 400

 ** InvalidParameterException **
 One or more parameters in this request are not valid.
 ** FieldName **
 The parameter field name for the invalid parameter exception.
HTTP Status Code: 400

 ** LimitExceededException **
 The request caused one or more limits to be exceeded.
 ** ResourceType **
 The resource type that caused the limits to be exceeded.
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
<a name="API_route53profiles_AssociateResourceToProfile_Examples"></a>

### AssociateResourceToProfile Example
<a name="API_route53profiles_AssociateResourceToProfile_Example_1"></a>

This example illustrates one usage of AssociateResourceToProfile.

#### Sample Request
<a name="API_route53profiles_AssociateResourceToProfile_Example_1_Request"></a>

```
POST /profileresourceassociation HTTP/1.1
host:route53profiles.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 508
X-Amz-Date:20240319T223820Z
User-Agent: aws-cli/1.32.63 botocore/1.34.63 Python/3.8.18
Content-Type: application/json
Authorization: AWS4-HMAC-SHA256
    Credential=AKIAJJ2SONIPEXAMPLE/20181101/us-east-1/route53profiles/aws4_request,
    SignedHeaders=content-type;host;x-amz-date;x-amz-security-token
    Signature=[calculated-signature]
{
    "Name": "test-resource-association",
    "ProfileId": "rp-4987774726example",
    "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example",
    "ResourceProperties": "{\\"priority\\": 102}"
}
```

#### Sample Response
<a name="API_route53profiles_AssociateResourceToProfile_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 19 Mar 2024 22:38:21 GMT
Content-Type: application/json
Content-Length: 508
Connection: keep-alive
x-amzn-RequestId: dcd9d91e-1a5a-481f-82b7-bafe7dexample
Access-Control-Allow-Origin: *
x-amz-apigw-id: U5eX0FdmIexample=
X-Amzn-Trace-Id: Root=1-65fa10fe-6e5a93a56a32afdfsd3example
{
    "ProfileResourceAssociation": {
        "CreationTime": 1710887901.139,
        "Id": "rpr-001913120a7example",
        "ModificationTime": 1710887901.139,
        "Name": "test-resource-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example",
        "ResourceProperties": "{\"priority\":102}",
        "ResourceType": "FIREWALL_RULE_GROUP",
        "Status": "UPDATING",
        "StatusMessage": "Updating the Profile to DNS Firewall rule group association"
    }
}
```

## See Also
<a name="API_route53profiles_AssociateResourceToProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53profiles-2018-05-10/AssociateResourceToProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53profiles-2018-05-10/AssociateResourceToProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53profiles-2018-05-10/AssociateResourceToProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53profiles-2018-05-10/AssociateResourceToProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53profiles-2018-05-10/AssociateResourceToProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53profiles-2018-05-10/AssociateResourceToProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53profiles-2018-05-10/AssociateResourceToProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53profiles-2018-05-10/AssociateResourceToProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53profiles-2018-05-10/AssociateResourceToProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53profiles-2018-05-10/AssociateResourceToProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

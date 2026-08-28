---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_CreateDomainNameAccessAssociation.html
---

# CreateDomainNameAccessAssociation
<a name="API_CreateDomainNameAccessAssociation"></a>

 Creates a domain name access association resource between an access association source and a private custom domain name.

## Request Syntax
<a name="API_CreateDomainNameAccessAssociation_RequestSyntax"></a>

```
POST /domainnameaccessassociations HTTP/1.1
Content-type: application/json

{
   "accessAssociationSource": "{{string}}",
   "accessAssociationSourceType": "{{string}}",
   "domainNameArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDomainNameAccessAssociation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDomainNameAccessAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accessAssociationSource](#API_CreateDomainNameAccessAssociation_RequestSyntax) **   <a name="apigw-CreateDomainNameAccessAssociation-request-accessAssociationSource"></a>
 The identifier of the domain name access association source. For a VPCE, the value is the VPC endpoint ID.
Type: String
Required: Yes

 ** [accessAssociationSourceType](#API_CreateDomainNameAccessAssociation_RequestSyntax) **   <a name="apigw-CreateDomainNameAccessAssociation-request-accessAssociationSourceType"></a>
 The type of the domain name access association source.
Type: String
Valid Values: `VPCE`
Required: Yes

 ** [domainNameArn](#API_CreateDomainNameAccessAssociation_RequestSyntax) **   <a name="apigw-CreateDomainNameAccessAssociation-request-domainNameArn"></a>
 The ARN of the domain name.
Type: String
Required: Yes

 ** [tags](#API_CreateDomainNameAccessAssociation_RequestSyntax) **   <a name="apigw-CreateDomainNameAccessAssociation-request-tags"></a>
The key-value map of strings. The valid character set is [a-zA-Z\+-=.\_:/]. The tag key can be up to 128 characters and must not start with `aws:`. The tag value can be up to 256 characters.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateDomainNameAccessAssociation_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "accessAssociationSource": "string",
   "accessAssociationSourceType": "string",
   "domainNameAccessAssociationArn": "string",
   "domainNameArn": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateDomainNameAccessAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [accessAssociationSource](#API_CreateDomainNameAccessAssociation_ResponseSyntax) **   <a name="apigw-CreateDomainNameAccessAssociation-response-accessAssociationSource"></a>
 The identifier of the domain name access association source. For a VPCE, the value is the VPC endpoint ID.
Type: String

 ** [accessAssociationSourceType](#API_CreateDomainNameAccessAssociation_ResponseSyntax) **   <a name="apigw-CreateDomainNameAccessAssociation-response-accessAssociationSourceType"></a>
 The type of the domain name access association source.
Type: String
Valid Values: `VPCE`

 ** [domainNameAccessAssociationArn](#API_CreateDomainNameAccessAssociation_ResponseSyntax) **   <a name="apigw-CreateDomainNameAccessAssociation-response-domainNameAccessAssociationArn"></a>
The ARN of the domain name access association resource.
Type: String

 ** [domainNameArn](#API_CreateDomainNameAccessAssociation_ResponseSyntax) **   <a name="apigw-CreateDomainNameAccessAssociation-response-domainNameArn"></a>
The ARN of the domain name.
Type: String

 ** [tags](#API_CreateDomainNameAccessAssociation_ResponseSyntax) **   <a name="apigw-CreateDomainNameAccessAssociation-response-tags"></a>
 The collection of tags. Each tag element is associated with a given resource.
Type: String to string map

## Errors
<a name="API_CreateDomainNameAccessAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** ConflictException **
The request configuration has conflicts. For details, see the accompanying error message.
HTTP Status Code: 409

 ** LimitExceededException **
The request exceeded the rate limit. Retry after the specified time period.
HTTP Status Code: 429

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## Examples
<a name="API_CreateDomainNameAccessAssociation_Examples"></a>

### Create a domain name access association
<a name="API_CreateDomainNameAccessAssociation_Example_1"></a>

This example illustrates one usage of CreateDomainNameAccessAssociation.

#### Sample Request
<a name="API_CreateDomainNameAccessAssociation_Example_1_Request"></a>

```
POST /domainnameaccessassociation HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20170223T200249Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
   "accessAssociationSource": "vpce-abcd1234",
   "accessAssociationSourceType": "VPCE",
   "domainNameArn": "arn:aws:apigateway:us-east-1:012345678910:/domainnames/private.a.b.c.com+abcd1234"
}
```

#### Sample Response
<a name="API_CreateDomainNameAccessAssociation_Example_1_Response"></a>

```
{
    "_links": {
        "curies": {
            "href": "http://docs.aws.amazon.com/apigateway/latest/developerguide/domainnameaccessassociation-domainname-{rel}.html",
            "name": "domainnameaccessassociation",
            "templated": true
        },
        "self": {
            "href": "/domainnameaccessassociations?limit=10"
        },
        "domainnameaccessassociation:create": {
            "href": "/domainnameaccessassociations"
        },
        "item": {
            "href": "/domainnameaccessassociations/arn:aws:apigateway:us-east-1:012345678910:/domainnameaccessassociations/domainname/private.a.b.c.com+abcd1234/vpcesource/vpce-abcd1234"
        }
    },
    "_embedded": {
        "item": {
            "_links": {
                "self": {
                    "href": "/domainnameaccessassociations/arn:aws:apigateway:us-east-1:012345678910:/domainnameaccessassociations/domainname/private.a.b.c.com+abcd1234/vpcesource/vpce-abcd1234"
                }
            },
            "accessAssociationSource": "vpce-abcd1234",
            "accessAssociationSourceType": "VPCE",
            "domainNameAccessAssociationArn": "arn:aws:apigateway:us-east-1:012345678910:/domainnameaccessassociations/domainname/private.a.b.c.com+abcd1234/vpcesource/vpce-abcd1234",
            "domainNameArn": "arn:aws:apigateway:us-east-1:012345678910:/domainnames/private.a.b.c.com+abcd1234"
        }
    }
}
```

## See Also
<a name="API_CreateDomainNameAccessAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/CreateDomainNameAccessAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/CreateDomainNameAccessAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/CreateDomainNameAccessAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/CreateDomainNameAccessAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/CreateDomainNameAccessAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/CreateDomainNameAccessAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/CreateDomainNameAccessAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/CreateDomainNameAccessAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/CreateDomainNameAccessAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/CreateDomainNameAccessAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

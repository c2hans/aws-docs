---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetDomainNameAccessAssociations.html
---

# GetDomainNameAccessAssociations
<a name="API_GetDomainNameAccessAssociations"></a>

Represents a collection on DomainNameAccessAssociations resources.

## Request Syntax
<a name="API_GetDomainNameAccessAssociations_RequestSyntax"></a>

```
GET /domainnameaccessassociations?limit={{limit}}&position={{position}}&resourceOwner={{resourceOwner}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDomainNameAccessAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [limit](#API_GetDomainNameAccessAssociations_RequestSyntax) **   <a name="apigw-GetDomainNameAccessAssociations-request-uri-limit"></a>
The maximum number of returned results per page. The default value is 25 and the maximum value is 500.

 ** [position](#API_GetDomainNameAccessAssociations_RequestSyntax) **   <a name="apigw-GetDomainNameAccessAssociations-request-uri-position"></a>
The current pagination position in the paged result set.

 ** [resourceOwner](#API_GetDomainNameAccessAssociations_RequestSyntax) **   <a name="apigw-GetDomainNameAccessAssociations-request-uri-resourceOwner"></a>
 The owner of the domain name access association. Use `SELF` to only list the domain name access associations owned by your own account. Use `OTHER_ACCOUNTS` to list the domain name access associations with your private custom domain names that are owned by other AWS accounts.
Valid Values: `SELF | OTHER_ACCOUNTS`

## Request Body
<a name="API_GetDomainNameAccessAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDomainNameAccessAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "item": [
      {
         "accessAssociationSource": "string",
         "accessAssociationSourceType": "string",
         "domainNameAccessAssociationArn": "string",
         "domainNameArn": "string",
         "tags": {
            "string" : "string"
         }
      }
   ],
   "position": "string"
}
```

## Response Elements
<a name="API_GetDomainNameAccessAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [item](#API_GetDomainNameAccessAssociations_ResponseSyntax) **   <a name="apigw-GetDomainNameAccessAssociations-response-item"></a>
 The current page of elements from this collection.
Type: Array of [DomainNameAccessAssociation](API_DomainNameAccessAssociation.md) objects

 ** [position](#API_GetDomainNameAccessAssociations_ResponseSyntax) **   <a name="apigw-GetDomainNameAccessAssociations-response-position"></a>
The current pagination position in the paged result set.
Type: String

## Errors
<a name="API_GetDomainNameAccessAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource is not found. Make sure that the request URI is correct.
HTTP Status Code: 404

 ** TooManyRequestsException **
The request has reached its throttling limit. Retry after the specified time period.
HTTP Status Code: 429

 ** UnauthorizedException **
The request is denied because the caller has insufficient permissions.
HTTP Status Code: 401

## Examples
<a name="API_GetDomainNameAccessAssociations_Examples"></a>

### Get the domain name access associations for domain name access associations owned by your own account
<a name="API_GetDomainNameAccessAssociations_Example_1"></a>

This example illustrates one usage of GetDomainNameAccessAssociations.

```
GET /domainnameaccessassociations?limit=10&resourceOwner=SELF
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160601T173728Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160601/us-east-1/apigateway/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature={sig4_hash}
```

#### Sample Response
<a name="API_GetDomainNameAccessAssociations_Example_1_Response"></a>

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
<a name="API_GetDomainNameAccessAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetDomainNameAccessAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetDomainNameAccessAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetDomainNameAccessAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetDomainNameAccessAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetDomainNameAccessAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetDomainNameAccessAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetDomainNameAccessAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetDomainNameAccessAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetDomainNameAccessAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetDomainNameAccessAssociations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxEnvironments.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# ListKxEnvironments
<a name="API_ListKxEnvironments"></a>

Returns a list of kdb environments created in an account.

## Request Syntax
<a name="API_ListKxEnvironments_RequestSyntax"></a>

```
GET /kx/environments?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListKxEnvironments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListKxEnvironments_RequestSyntax) **   <a name="finspace-ListKxEnvironments-request-uri-maxResults"></a>
The maximum number of results to return in this request.

 ** [nextToken](#API_ListKxEnvironments_RequestSyntax) **   <a name="finspace-ListKxEnvironments-request-uri-nextToken"></a>
A token that indicates where a results page should begin.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Request Body
<a name="API_ListKxEnvironments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListKxEnvironments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "environments": [
      {
         "availabilityZoneIds": [ "string" ],
         "awsAccountId": "string",
         "certificateAuthorityArn": "string",
         "creationTimestamp": number,
         "customDNSConfiguration": [
            {
               "customDNSServerIP": "string",
               "customDNSServerName": "string"
            }
         ],
         "dedicatedServiceAccountId": "string",
         "description": "string",
         "dnsStatus": "string",
         "environmentArn": "string",
         "environmentId": "string",
         "errorMessage": "string",
         "kmsKeyId": "string",
         "name": "string",
         "status": "string",
         "tgwStatus": "string",
         "transitGatewayConfiguration": {
            "attachmentNetworkAclConfiguration": [
               {
                  "cidrBlock": "string",
                  "icmpTypeCode": {
                     "code": number,
                     "type": number
                  },
                  "portRange": {
                     "from": number,
                     "to": number
                  },
                  "protocol": "string",
                  "ruleAction": "string",
                  "ruleNumber": number
               }
            ],
            "routableCIDRSpace": "string",
            "transitGatewayID": "string"
         },
         "updateTimestamp": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListKxEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environments](#API_ListKxEnvironments_ResponseSyntax) **   <a name="finspace-ListKxEnvironments-response-environments"></a>
A list of environments in an account.
Type: Array of [KxEnvironment](API_KxEnvironment.md) objects

 ** [nextToken](#API_ListKxEnvironments_ResponseSyntax) **   <a name="finspace-ListKxEnvironments-response-nextToken"></a>
A token that indicates where a results page should begin.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `.*`

## Errors
<a name="API_ListKxEnvironments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListKxEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/ListKxEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/ListKxEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/ListKxEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/ListKxEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/ListKxEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/ListKxEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/ListKxEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/ListKxEnvironments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/ListKxEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/ListKxEnvironments)

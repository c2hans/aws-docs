---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListRelatedResourcesForAuditFinding.html
---

# ListRelatedResourcesForAuditFinding
<a name="API_ListRelatedResourcesForAuditFinding"></a>

The related resources of an Audit finding. The following resources can be returned from calling this API:
+ DEVICE\_CERTIFICATE
+ CA\_CERTIFICATE
+ IOT\_POLICY
+ COGNITO\_IDENTITY\_POOL
+ CLIENT\_ID
+ ACCOUNT\_SETTINGS
+ ROLE\_ALIAS
+ IAM\_ROLE
+ ISSUER\_CERTIFICATE

**Note**
This API is similar to DescribeAuditFinding's [RelatedResources](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditFinding.html) but provides pagination and is not limited to 10 resources. When calling [DescribeAuditFinding](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuditFinding.html) for the intermediate CA revoked for active device certificates check, RelatedResources will not be populated. You must use this API, ListRelatedResourcesForAuditFinding, to list the certificates.

## Request Syntax
<a name="API_ListRelatedResourcesForAuditFinding_RequestSyntax"></a>

```
GET /audit/relatedResources?findingId={{findingId}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRelatedResourcesForAuditFinding_RequestParameters"></a>

The request uses the following URI parameters.

 ** [findingId](#API_ListRelatedResourcesForAuditFinding_RequestSyntax) **   <a name="iot-ListRelatedResourcesForAuditFinding-request-uri-findingId"></a>
The finding Id.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [maxResults](#API_ListRelatedResourcesForAuditFinding_RequestSyntax) **   <a name="iot-ListRelatedResourcesForAuditFinding-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListRelatedResourcesForAuditFinding_RequestSyntax) **   <a name="iot-ListRelatedResourcesForAuditFinding-request-uri-nextToken"></a>
A token that can be used to retrieve the next set of results, or `null` if there are no additional results.

## Request Body
<a name="API_ListRelatedResourcesForAuditFinding_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRelatedResourcesForAuditFinding_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "relatedResources": [
      {
         "additionalInfo": {
            "string" : "string"
         },
         "resourceIdentifier": {
            "account": "string",
            "caCertificateId": "string",
            "clientId": "string",
            "cognitoIdentityPoolId": "string",
            "deviceCertificateArn": "string",
            "deviceCertificateId": "string",
            "iamRoleArn": "string",
            "issuerCertificateIdentifier": {
               "issuerCertificateSerialNumber": "string",
               "issuerCertificateSubject": "string",
               "issuerId": "string"
            },
            "policyVersionIdentifier": {
               "policyName": "string",
               "policyVersionId": "string"
            },
            "roleAliasArn": "string"
         },
         "resourceType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRelatedResourcesForAuditFinding_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRelatedResourcesForAuditFinding_ResponseSyntax) **   <a name="iot-ListRelatedResourcesForAuditFinding-response-nextToken"></a>
A token that can be used to retrieve the next set of results, or `null` for the first API call.
Type: String

 ** [relatedResources](#API_ListRelatedResourcesForAuditFinding_ResponseSyntax) **   <a name="iot-ListRelatedResourcesForAuditFinding-response-relatedResources"></a>
The related resources.
Type: Array of [RelatedResource](API_RelatedResource.md) objects

## Errors
<a name="API_ListRelatedResourcesForAuditFinding_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListRelatedResourcesForAuditFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListRelatedResourcesForAuditFinding)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListRelatedResourcesForAuditFinding)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListRelatedResourcesForAuditFinding)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListRelatedResourcesForAuditFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListRelatedResourcesForAuditFinding)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListRelatedResourcesForAuditFinding)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListRelatedResourcesForAuditFinding)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListRelatedResourcesForAuditFinding)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListRelatedResourcesForAuditFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListRelatedResourcesForAuditFinding)

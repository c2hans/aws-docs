---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateCertificate.html
---

# CreateCertificate
<a name="API_CreateCertificate"></a>

Creates an SSL/TLS certificate for an Amazon Lightsail content delivery network (CDN) distribution and a container service.

After the certificate is valid, use the `AttachCertificateToDistribution` action to use the certificate and its domains with your distribution. Or use the `UpdateContainerService` action to use the certificate and its domains with your container service.

**Important**
Only certificates created in the `us-east-1` AWS Region can be attached to Lightsail distributions. Lightsail distributions are global resources that can reference an origin in any AWS Region, and distribute its content globally. However, all distributions are located in the `us-east-1` Region.

## Request Syntax
<a name="API_CreateCertificate_RequestSyntax"></a>

```
{
   "certificateName": "{{string}}",
   "domainName": "{{string}}",
   "subjectAlternativeNames": [ "{{string}}" ],
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCertificate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [certificateName](#API_CreateCertificate_RequestSyntax) **   <a name="Lightsail-CreateCertificate-request-certificateName"></a>
The name for the certificate.
Type: String
Required: Yes

 ** [domainName](#API_CreateCertificate_RequestSyntax) **   <a name="Lightsail-CreateCertificate-request-domainName"></a>
The domain name (`example.com`) for the certificate.
Type: String
Required: Yes

 ** [subjectAlternativeNames](#API_CreateCertificate_RequestSyntax) **   <a name="Lightsail-CreateCertificate-request-subjectAlternativeNames"></a>
An array of strings that specify the alternate domains (`example2.com`) and subdomains (`blog.example.com`) for the certificate.
You can specify a maximum of nine alternate domains (in addition to the primary domain name).
Wildcard domain entries (`*.example.com`) are not supported.
Type: Array of strings
Required: No

 ** [tags](#API_CreateCertificate_RequestSyntax) **   <a name="Lightsail-CreateCertificate-request-tags"></a>
The tag keys and optional values to add to the certificate during create.
Use the `TagResource` action to tag a resource after it's created.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateCertificate_ResponseSyntax"></a>

```
{
   "certificate": {
      "certificateArn": "string",
      "certificateDetail": {
         "arn": "string",
         "createdAt": number,
         "domainName": "string",
         "domainValidationRecords": [
            {
               "dnsRecordCreationState": {
                  "code": "string",
                  "message": "string"
               },
               "domainName": "string",
               "resourceRecord": {
                  "name": "string",
                  "type": "string",
                  "value": "string"
               },
               "validationStatus": "string"
            }
         ],
         "eligibleToRenew": "string",
         "inUseResourceCount": number,
         "issuedAt": number,
         "issuerCA": "string",
         "keyAlgorithm": "string",
         "name": "string",
         "notAfter": number,
         "notBefore": number,
         "renewalSummary": {
            "domainValidationRecords": [
               {
                  "dnsRecordCreationState": {
                     "code": "string",
                     "message": "string"
                  },
                  "domainName": "string",
                  "resourceRecord": {
                     "name": "string",
                     "type": "string",
                     "value": "string"
                  },
                  "validationStatus": "string"
               }
            ],
            "renewalStatus": "string",
            "renewalStatusReason": "string",
            "updatedAt": number
         },
         "requestFailureReason": "string",
         "revocationReason": "string",
         "revokedAt": number,
         "serialNumber": "string",
         "status": "string",
         "subjectAlternativeNames": [ "string" ],
         "supportCode": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      },
      "certificateName": "string",
      "domainName": "string",
      "tags": [
         {
            "key": "string",
            "value": "string"
         }
      ]
   },
   "operations": [
      {
         "createdAt": number,
         "errorCode": "string",
         "errorDetails": "string",
         "id": "string",
         "isTerminal": boolean,
         "location": {
            "availabilityZone": "string",
            "regionName": "string"
         },
         "operationDetails": "string",
         "operationType": "string",
         "resourceName": "string",
         "resourceType": "string",
         "status": "string",
         "statusChangedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_CreateCertificate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificate](#API_CreateCertificate_ResponseSyntax) **   <a name="Lightsail-CreateCertificate-response-certificate"></a>
An object that describes the certificate created.
Type: [CertificateSummary](API_CertificateSummary.md) object

 ** [operations](#API_CreateCertificate_ResponseSyntax) **   <a name="Lightsail-CreateCertificate-response-operations"></a>
An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: Array of [Operation](API_Operation.md) objects

## Errors
<a name="API_CreateCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_CreateCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/CreateCertificate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/CreateCertificate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/CreateCertificate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/CreateCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/CreateCertificate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/CreateCertificate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/CreateCertificate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/CreateCertificate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/CreateCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/CreateCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AttachCertificateToDistribution.html
---

# AttachCertificateToDistribution
<a name="API_AttachCertificateToDistribution"></a>

Attaches an SSL/TLS certificate to your Amazon Lightsail content delivery network (CDN) distribution.

After the certificate is attached, your distribution accepts HTTPS traffic for all of the domains that are associated with the certificate.

Use the `CreateCertificate` action to create a certificate that you can attach to your distribution.

**Important**
Only certificates created in the `us-east-1` AWS Region can be attached to Lightsail distributions. Lightsail distributions are global resources that can reference an origin in any AWS Region, and distribute its content globally. However, all distributions are located in the `us-east-1` Region.

## Request Syntax
<a name="API_AttachCertificateToDistribution_RequestSyntax"></a>

```
{
   "certificateName": "{{string}}",
   "distributionName": "{{string}}"
}
```

## Request Parameters
<a name="API_AttachCertificateToDistribution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [certificateName](#API_AttachCertificateToDistribution_RequestSyntax) **   <a name="Lightsail-AttachCertificateToDistribution-request-certificateName"></a>
The name of the certificate to attach to a distribution.
Only certificates with a status of `ISSUED` can be attached to a distribution.
Use the `GetCertificates` action to get a list of certificate names that you can specify.
This is the name of the certificate resource type and is used only to reference the certificate in other API actions. It can be different than the domain name of the certificate. For example, your certificate name might be `WordPress-Blog-Certificate` and the domain name of the certificate might be `example.com`.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

 ** [distributionName](#API_AttachCertificateToDistribution_RequestSyntax) **   <a name="Lightsail-AttachCertificateToDistribution-request-distributionName"></a>
The name of the distribution that the certificate will be attached to.
Use the `GetDistributions` action to get a list of distribution names that you can specify.
Type: String
Pattern: `\w[\w\-]*\w`
Required: Yes

## Response Syntax
<a name="API_AttachCertificateToDistribution_ResponseSyntax"></a>

```
{
   "operation": {
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
}
```

## Response Elements
<a name="API_AttachCertificateToDistribution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operation](#API_AttachCertificateToDistribution_ResponseSyntax) **   <a name="Lightsail-AttachCertificateToDistribution-response-operation"></a>
An object that describes the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.
Type: [Operation](API_Operation.md) object

## Errors
<a name="API_AttachCertificateToDistribution_Errors"></a>

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

 ** OperationFailureException **
Lightsail throws this exception when an operation fails to execute.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_AttachCertificateToDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/AttachCertificateToDistribution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/AttachCertificateToDistribution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/AttachCertificateToDistribution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/AttachCertificateToDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/AttachCertificateToDistribution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/AttachCertificateToDistribution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/AttachCertificateToDistribution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/AttachCertificateToDistribution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/AttachCertificateToDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/AttachCertificateToDistribution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_AssociateBenefitApplicationResource.html
---

# AssociateBenefitApplicationResource
<a name="API_benefits_AssociateBenefitApplicationResource"></a>

Links an AWS resource to an existing benefit application for tracking and management purposes.

## Request Syntax
<a name="API_benefits_AssociateBenefitApplicationResource_RequestSyntax"></a>

```
{
   "BenefitApplicationIdentifier": "{{string}}",
   "Catalog": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_benefits_AssociateBenefitApplicationResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [BenefitApplicationIdentifier](#API_benefits_AssociateBenefitApplicationResource_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_AssociateBenefitApplicationResource-request-BenefitApplicationIdentifier"></a>
The unique identifier of the benefit application to associate the resource with.
Type: String
Pattern: `(arn:.+|benappl-[0-9a-z]{14})`
Required: Yes

 ** [Catalog](#API_benefits_AssociateBenefitApplicationResource_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_AssociateBenefitApplicationResource-request-Catalog"></a>
The catalog identifier that specifies which benefit catalog the application belongs to.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [ResourceArn](#API_benefits_AssociateBenefitApplicationResource_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_AssociateBenefitApplicationResource-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the AWS resource to associate with the benefit application.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `arn:aws:([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.+)`
Required: Yes

## Response Syntax
<a name="API_benefits_AssociateBenefitApplicationResource_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "Id": "string",
   "Revision": "string"
}
```

## Response Elements
<a name="API_benefits_AssociateBenefitApplicationResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_benefits_AssociateBenefitApplicationResource_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_AssociateBenefitApplicationResource-response-Arn"></a>
The Amazon Resource Name (ARN) of the benefit application after the resource association.
Type: String

 ** [Id](#API_benefits_AssociateBenefitApplicationResource_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_AssociateBenefitApplicationResource-response-Id"></a>
The unique identifier of the benefit application after the resource association.
Type: String
Pattern: `benappl-[0-9a-z]{14}`

 ** [Revision](#API_benefits_AssociateBenefitApplicationResource_ResponseSyntax) **   <a name="AWSPartnerCentral-benefits_AssociateBenefitApplicationResource-response-Revision"></a>
The updated revision number of the benefit application after the resource association.
Type: String

## Errors
<a name="API_benefits_AssociateBenefitApplicationResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Thrown when the caller does not have sufficient permissions to perform the requested operation.
 ** Message **
A message describing the access denial.
HTTP Status Code: 400

 ** ConflictException **
Thrown when the request conflicts with the current state of the resource, such as attempting to modify a resource that has been changed by another process.
 ** Message **
A message describing the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an unexpected error occurs on the server side during request processing.
 ** Message **
A message describing the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when the requested resource cannot be found or does not exist.
 ** Message **
A message describing the resource not found error.
HTTP Status Code: 400

 ** ThrottlingException **
Thrown when the request rate exceeds the allowed limits and the request is being throttled.
 ** Message **
A message describing the throttling error.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the request contains invalid parameters or fails input validation requirements.
 ** FieldList **
A list of fields that failed validation.
 ** Message **
A message describing the validation error.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_benefits_AssociateBenefitApplicationResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-benefits-2018-05-10/AssociateBenefitApplicationResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-benefits-2018-05-10/AssociateBenefitApplicationResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/AssociateBenefitApplicationResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-benefits-2018-05-10/AssociateBenefitApplicationResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/AssociateBenefitApplicationResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-benefits-2018-05-10/AssociateBenefitApplicationResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-benefits-2018-05-10/AssociateBenefitApplicationResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-benefits-2018-05-10/AssociateBenefitApplicationResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-benefits-2018-05-10/AssociateBenefitApplicationResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/AssociateBenefitApplicationResource)

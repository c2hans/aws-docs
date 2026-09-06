---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseConversionTaskForResource.html
---

# CreateLicenseConversionTaskForResource
<a name="API_CreateLicenseConversionTaskForResource"></a>

Creates a new license conversion task.

## Request Syntax
<a name="API_CreateLicenseConversionTaskForResource_RequestSyntax"></a>

```
{
   "DestinationLicenseContext": {
      "ProductCodes": [
         {
            "ProductCodeId": "{{string}}",
            "ProductCodeType": "{{string}}"
         }
      ],
      "UsageOperation": "{{string}}"
   },
   "ResourceArn": "{{string}}",
   "SourceLicenseContext": {
      "ProductCodes": [
         {
            "ProductCodeId": "{{string}}",
            "ProductCodeType": "{{string}}"
         }
      ],
      "UsageOperation": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateLicenseConversionTaskForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DestinationLicenseContext](#API_CreateLicenseConversionTaskForResource_RequestSyntax) **   <a name="licensemanager-CreateLicenseConversionTaskForResource-request-DestinationLicenseContext"></a>
Information that identifies the license type you are converting to. For the structure of the destination license, see [Convert a license type using the AWS CLI](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures.html#conversion-cli) in the * AWS License Manager User Guide*.
Type: [LicenseConversionContext](API_LicenseConversionContext.md) object
Required: Yes

 ** [ResourceArn](#API_CreateLicenseConversionTaskForResource_RequestSyntax) **   <a name="licensemanager-CreateLicenseConversionTaskForResource-request-ResourceArn"></a>
Amazon Resource Name (ARN) of the resource you are converting the license type for.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [SourceLicenseContext](#API_CreateLicenseConversionTaskForResource_RequestSyntax) **   <a name="licensemanager-CreateLicenseConversionTaskForResource-request-SourceLicenseContext"></a>
Information that identifies the license type you are converting from. For the structure of the source license, see [Convert a license type using the AWS CLI](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures.html#conversion-cli) in the * AWS License Manager User Guide*.
Type: [LicenseConversionContext](API_LicenseConversionContext.md) object
Required: Yes

## Response Syntax
<a name="API_CreateLicenseConversionTaskForResource_ResponseSyntax"></a>

```
{
   "LicenseConversionTaskId": "string"
}
```

## Response Elements
<a name="API_CreateLicenseConversionTaskForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseConversionTaskId](#API_CreateLicenseConversionTaskForResource_ResponseSyntax) **   <a name="licensemanager-CreateLicenseConversionTaskForResource-response-LicenseConversionTaskId"></a>
The ID of the created license type conversion task.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^lct-[a-zA-Z0-9]*`

## Errors
<a name="API_CreateLicenseConversionTaskForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_CreateLicenseConversionTaskForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/CreateLicenseConversionTaskForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/CreateLicenseConversionTaskForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/CreateLicenseConversionTaskForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/CreateLicenseConversionTaskForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/CreateLicenseConversionTaskForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/CreateLicenseConversionTaskForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/CreateLicenseConversionTaskForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/CreateLicenseConversionTaskForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/CreateLicenseConversionTaskForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/CreateLicenseConversionTaskForResource)

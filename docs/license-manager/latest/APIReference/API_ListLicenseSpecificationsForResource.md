---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseSpecificationsForResource.html
---

# ListLicenseSpecificationsForResource
<a name="API_ListLicenseSpecificationsForResource"></a>

Describes the license configurations for the specified resource.

## Request Syntax
<a name="API_ListLicenseSpecificationsForResource_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLicenseSpecificationsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListLicenseSpecificationsForResource_RequestSyntax) **   <a name="licensemanager-ListLicenseSpecificationsForResource-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [NextToken](#API_ListLicenseSpecificationsForResource_RequestSyntax) **   <a name="licensemanager-ListLicenseSpecificationsForResource-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

 ** [ResourceArn](#API_ListLicenseSpecificationsForResource_RequestSyntax) **   <a name="licensemanager-ListLicenseSpecificationsForResource-request-ResourceArn"></a>
Amazon Resource Name (ARN) of a resource that has an associated license configuration.
Type: String
Required: Yes

## Response Syntax
<a name="API_ListLicenseSpecificationsForResource_ResponseSyntax"></a>

```
{
   "LicenseSpecifications": [
      {
         "AmiAssociationScope": "string",
         "LicenseConfigurationArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLicenseSpecificationsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseSpecifications](#API_ListLicenseSpecificationsForResource_ResponseSyntax) **   <a name="licensemanager-ListLicenseSpecificationsForResource-response-LicenseSpecifications"></a>
License configurations associated with a resource.
Type: Array of [LicenseSpecification](API_LicenseSpecification.md) objects

 ** [NextToken](#API_ListLicenseSpecificationsForResource_ResponseSyntax) **   <a name="licensemanager-ListLicenseSpecificationsForResource-response-NextToken"></a>
Token for the next set of results.
Type: String

## Errors
<a name="API_ListLicenseSpecificationsForResource_Errors"></a>

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

## See Also
<a name="API_ListLicenseSpecificationsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListLicenseSpecificationsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListLicenseSpecificationsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListLicenseSpecificationsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListLicenseSpecificationsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListLicenseSpecificationsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListLicenseSpecificationsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListLicenseSpecificationsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListLicenseSpecificationsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListLicenseSpecificationsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListLicenseSpecificationsForResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

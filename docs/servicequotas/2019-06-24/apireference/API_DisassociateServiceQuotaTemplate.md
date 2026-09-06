---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_DisassociateServiceQuotaTemplate.html
---

# DisassociateServiceQuotaTemplate
<a name="API_DisassociateServiceQuotaTemplate"></a>

Disables your quota request template. After a template is disabled, the quota increase requests in the template are not applied to new AWS accounts in your organization. Disabling a quota request template does not apply its quota increase requests.

## Response Elements
<a name="API_DisassociateServiceQuotaTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisassociateServiceQuotaTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permission to perform this action.
HTTP Status Code: 400

 ** AWSServiceAccessNotEnabledException **
The action you attempted is not allowed unless Service Access with Service Quotas is enabled in your organization.
HTTP Status Code: 400

 ** DependencyAccessDeniedException **
You can't perform this action because a dependency does not have access.
HTTP Status Code: 400

 ** NoAvailableOrganizationException **
The AWS account making this call is not a member of an organization.
HTTP Status Code: 400

 ** ServiceException **
Something went wrong.
HTTP Status Code: 500

 ** ServiceQuotaTemplateNotInUseException **
The quota request template is not associated with your organization.
HTTP Status Code: 400

 ** TemplatesNotAvailableInRegionException **
The Service Quotas template is not available in this AWS Region.
HTTP Status Code: 400

 ** TooManyRequestsException **
Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateServiceQuotaTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/DisassociateServiceQuotaTemplate)

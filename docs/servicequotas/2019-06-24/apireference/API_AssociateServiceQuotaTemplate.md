---
source_url: https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_AssociateServiceQuotaTemplate.html
---

# AssociateServiceQuotaTemplate
<a name="API_AssociateServiceQuotaTemplate"></a>

Associates your quota request template with your organization. When a new AWS account is created in your organization, the quota increase requests in the template are automatically applied to the account. You can add a quota increase request for any adjustable quota to your template.

**Related Actions**
+  [DisassociateServiceQuotaTemplate](API_DisassociateServiceQuotaTemplate.md)
+  [GetAssociationForServiceQuotaTemplate](API_GetAssociationForServiceQuotaTemplate.md)
+  [PutServiceQuotaIncreaseRequestIntoTemplate](API_PutServiceQuotaIncreaseRequestIntoTemplate.md)

## Response Elements
<a name="API_AssociateServiceQuotaTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateServiceQuotaTemplate_Errors"></a>

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

 ** OrganizationNotInAllFeaturesModeException **
The organization that your AWS account belongs to is not in All Features mode.
HTTP Status Code: 400

 ** ServiceException **
Something went wrong.
HTTP Status Code: 500

 ** TemplatesNotAvailableInRegionException **
The Service Quotas template is not available in this AWS Region.
HTTP Status Code: 400

 ** TooManyRequestsException **
Due to throttling, the request was denied. Slow down the rate of request calls, or request an increase for this quota.
HTTP Status Code: 400

## See Also
<a name="API_AssociateServiceQuotaTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/service-quotas-2019-06-24/AssociateServiceQuotaTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/service-quotas-2019-06-24/AssociateServiceQuotaTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/service-quotas-2019-06-24/AssociateServiceQuotaTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/service-quotas-2019-06-24/AssociateServiceQuotaTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/service-quotas-2019-06-24/AssociateServiceQuotaTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/service-quotas-2019-06-24/AssociateServiceQuotaTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/service-quotas-2019-06-24/AssociateServiceQuotaTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/service-quotas-2019-06-24/AssociateServiceQuotaTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/service-quotas-2019-06-24/AssociateServiceQuotaTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/service-quotas-2019-06-24/AssociateServiceQuotaTemplate)

---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_EnableAWSOrganizationsAccess.html
---

# EnableAWSOrganizationsAccess
<a name="API_EnableAWSOrganizationsAccess"></a>

Enable portfolio sharing feature through AWS Organizations. This API will allow AWS Service Catalog to receive updates on your organization in order to sync your shares with the current structure. This API can only be called by the management account in the organization.

When you call this API, Service Catalog calls `organizations:EnableAWSServiceAccess` on your behalf so that your shares stay in sync with any changes in your AWS Organizations structure.

Note that a delegated administrator is not authorized to invoke `EnableAWSOrganizationsAccess`.

After this operation returns, AWS Service Catalog counts the accounts in your organization before it finishes enabling access. Use [GetAWSOrganizationsAccessStatus](API_GetAWSOrganizationsAccessStatus.md) to check the result. The check usually completes within two hours.
+  `UNDER_CHANGE` - The check is in progress. Wait until the status changes from `UNDER_CHANGE` to `ENABLED` before you share portfolios with organization nodes.
+  `ENABLED` - AWS Organizations access is enabled. Your organization shares are kept in sync with your organization structure.
+  `DISABLED` - Your organization has more than 15,000 accounts, so access was not enabled. To enable access, reduce the organization to 15,000 accounts or fewer and call `EnableAWSOrganizationsAccess` again. Calling it again without reducing the organization repeats the check and returns `DISABLED`.

The 15,000-account quota is checked only when you enable access. An organization that grows past 15,000 accounts after access is enabled keeps AWS Organizations access, and its shares continue to sync. If you then disable access, you cannot enable it again until the organization has 15,000 accounts or fewer. For more information, see [AWS Service Catalog default service quotas](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/limits.html#orgs) in the * AWS Service Catalog Administrator Guide*.

**Important**
If you have previously disabled Organizations access for Service Catalog, and then enable access again, the portfolio access permissions might not sync with the latest changes to the organization structure. Specifically, accounts that you removed from the organization after disabling Service Catalog access, and before you enabled access again, can retain access to the previously shared portfolio. As a result, an account that has been removed from the organization might still be able to create or manage AWS resources when it is no longer authorized to do so. AWS is working to resolve this issue.

## Response Elements
<a name="API_EnableAWSOrganizationsAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_EnableAWSOrganizationsAccess_Errors"></a>

 ** InvalidStateException **
An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.
HTTP Status Code: 400

 ** OperationNotSupportedException **
The operation is not supported.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_EnableAWSOrganizationsAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)

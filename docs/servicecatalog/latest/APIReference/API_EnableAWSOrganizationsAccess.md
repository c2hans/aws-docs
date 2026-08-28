---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_EnableAWSOrganizationsAccess.html
---

# EnableAWSOrganizationsAccess
<a name="API_EnableAWSOrganizationsAccess"></a>

Enable portfolio sharing feature through AWS Organizations. This API will allow AWS Service Catalog to receive updates on your organization in order to sync your shares with the current structure. This API can only be called by the management account in the organization.

When you call this API, Service Catalog calls `organizations:EnableAWSServiceAccess` on your behalf so that your shares stay in sync with any changes in your AWS Organizations structure.

Note that a delegated administrator is not authorized to invoke `EnableAWSOrganizationsAccess`.

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
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/EnableAWSOrganizationsAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_ErrorDetails.html
---

# ErrorDetails
<a name="API_ErrorDetails"></a>

Contains information about an error that occurred during application processing.

## Contents
<a name="API_ErrorDetails_Contents"></a>

 ** code **   <a name="accountaccess-Type-ErrorDetails-code"></a>
The error code that identifies the type of error.
Type: String
Valid Values: `AUTHORIZATION_ERROR | RESOURCE_NOT_FOUND_ERROR | SERVICE_QUOTA_EXCEEDED_ERROR | INTERNAL_SERVICE_ERROR`
Required: Yes

 ** message **   <a name="accountaccess-Type-ErrorDetails-message"></a>
A human-readable message that describes the error.
Type: String
Required: Yes

## See Also
<a name="API_ErrorDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/ErrorDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/ErrorDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/ErrorDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account access manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query account-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

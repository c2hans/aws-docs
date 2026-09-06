---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_ChangeRequest.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# ChangeRequest
<a name="API_ChangeRequest"></a>

A list of change request objects.

## Contents
<a name="API_ChangeRequest_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** changeType **   <a name="finspace-Type-ChangeRequest-changeType"></a>
Defines the type of change request. A `changeType` can have the following values:
+ PUT – Adds or updates files in a database.
+ DELETE – Deletes files in a database.
Type: String
Valid Values: `PUT | DELETE`
Required: Yes

 ** dbPath **   <a name="finspace-Type-ChangeRequest-dbPath"></a>
Defines the path within the database directory.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1025.
Pattern: `^(\*)*[\/\?\*]([^\/]+\/){0,2}[^\/]*$`
Required: Yes

 ** s3Path **   <a name="finspace-Type-ChangeRequest-s3Path"></a>
Defines the S3 path of the source file that is required to add or update files in a database.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 1093.
Pattern: `^s3:\/\/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]\/([^\/]+\/)*[^\/]*$`
Required: No

## See Also
<a name="API_ChangeRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/ChangeRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/ChangeRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/ChangeRequest)

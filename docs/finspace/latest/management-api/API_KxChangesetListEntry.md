---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxChangesetListEntry.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxChangesetListEntry
<a name="API_KxChangesetListEntry"></a>

Details of changeset.

## Contents
<a name="API_KxChangesetListEntry_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** activeFromTimestamp **   <a name="finspace-Type-KxChangesetListEntry-activeFromTimestamp"></a>
Beginning time from which the changeset is active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** changesetId **   <a name="finspace-Type-KxChangesetListEntry-changesetId"></a>
A unique identifier for the changeset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** createdTimestamp **   <a name="finspace-Type-KxChangesetListEntry-createdTimestamp"></a>
The timestamp at which the changeset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** lastModifiedTimestamp **   <a name="finspace-Type-KxChangesetListEntry-lastModifiedTimestamp"></a>
The timestamp at which the changeset was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** status **   <a name="finspace-Type-KxChangesetListEntry-status"></a>
 Status of the changeset.
+ Pending – Changeset creation is pending.
+ Processing – Changeset creation is running.
+ Failed – Changeset creation has failed.
+ Complete – Changeset creation has succeeded.
Type: String
Valid Values: `PENDING | PROCESSING | FAILED | COMPLETED`
Required: No

## See Also
<a name="API_KxChangesetListEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxChangesetListEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxChangesetListEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxChangesetListEntry)

---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_FarmMember.html
---

# FarmMember
<a name="API_FarmMember"></a>

The member of a farm.

## Contents
<a name="API_FarmMember_Contents"></a>

 ** farmId **   <a name="deadlinecloud-Type-FarmMember-farmId"></a>
The farm ID of the farm member.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** identityStoreId **   <a name="deadlinecloud-Type-FarmMember-identityStoreId"></a>
The identity store ID of the farm member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipLevel **   <a name="deadlinecloud-Type-FarmMember-membershipLevel"></a>
The farm member's membership level.
Type: String
Valid Values: `VIEWER | CONTRIBUTOR | OWNER | MANAGER`
Required: Yes

 ** principalId **   <a name="deadlinecloud-Type-FarmMember-principalId"></a>
The principal ID of the farm member.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 47.
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: Yes

 ** principalType **   <a name="deadlinecloud-Type-FarmMember-principalType"></a>
The principal type of the farm member.
Type: String
Valid Values: `USER | GROUP`
Required: Yes

## See Also
<a name="API_FarmMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/FarmMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/FarmMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/FarmMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

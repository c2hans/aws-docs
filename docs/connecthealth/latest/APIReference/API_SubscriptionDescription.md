---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_SubscriptionDescription.html
---

# SubscriptionDescription
<a name="API_SubscriptionDescription"></a>

Complete subscription resource data.

## Contents
<a name="API_SubscriptionDescription_Contents"></a>

 ** arn **   <a name="connecthealth-Type-SubscriptionDescription-arn"></a>

Type: String
Pattern: `arn:aws:health-agent:[a-z0-9-]+:[0-9]{12}:domain/(hai-|dom-)[a-z0-9]+/subscription/sub-[a-zA-Z0-9]{21}`
Required: Yes

 ** createdAt **   <a name="connecthealth-Type-SubscriptionDescription-createdAt"></a>

Type: Timestamp
Required: Yes

 ** domainId **   <a name="connecthealth-Type-SubscriptionDescription-domainId"></a>

Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

 ** lastUpdatedAt **   <a name="connecthealth-Type-SubscriptionDescription-lastUpdatedAt"></a>

Type: Timestamp
Required: Yes

 ** status **   <a name="connecthealth-Type-SubscriptionDescription-status"></a>

Type: String
Valid Values: `ACTIVE | INACTIVE | DELETED`
Required: Yes

 ** subscriptionId **   <a name="connecthealth-Type-SubscriptionDescription-subscriptionId"></a>

Type: String
Length Constraints: Fixed length of 25.
Pattern: `sub-[a-zA-Z0-9]{21}`
Required: Yes

 ** activatedAt **   <a name="connecthealth-Type-SubscriptionDescription-activatedAt"></a>

Type: Timestamp
Required: No

 ** deactivatedAt **   <a name="connecthealth-Type-SubscriptionDescription-deactivatedAt"></a>

Type: Timestamp
Required: No

## See Also
<a name="API_SubscriptionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/SubscriptionDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/SubscriptionDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/SubscriptionDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

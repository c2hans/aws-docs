---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_PublisherSummary.html
---

# PublisherSummary

Summary information about a publisher.

## Contents
<a name="API_PublisherSummary_Contents"></a>

 ** createdAt **   <a name="agentregistrycontrol-Type-PublisherSummary-createdAt"></a>
The date and time that the publisher was created.
Type: Timestamp
Required: Yes

 ** publisherArn **   <a name="agentregistrycontrol-Type-PublisherSummary-publisherArn"></a>
The Amazon Resource Name (ARN) of the publisher.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-z0-9-]+::[0-9]{12}:[a-zA-Z0-9._/-]+`
Required: Yes

 ** status **   <a name="agentregistrycontrol-Type-PublisherSummary-status"></a>
The domain verification status of the publisher. Only an `ACTIVE` publisher accepts new registry record associations. The status is one of the following:
+  `ACTION_REQUIRED` - The registry is waiting to find the Domain Name System (DNS) TXT record described by the publisher's `domainChallenge`, which `GetPublisher` returns.
+  `ACTIVE` - The domain is verified. You can associate registry records with the publisher.
+  `SUSPENDED` - The domain was verified, but a later check found the TXT record missing or changed. The publisher returns to `ACTIVE` when the record is found again, and becomes `FAILED` if the record stays missing.
+  `FAILED` - Verification didn't succeed, for example because the TXT record wasn't found in time or another account verified the domain first. Call `ValidatePublisher` to try again.
+  `DELETING` - A delete is in progress.
Type: String
Valid Values: `ACTION_REQUIRED | ACTIVE | FAILED | SUSPENDED | DELETING`
Required: Yes

 ** value **   <a name="agentregistrycontrol-Type-PublisherSummary-value"></a>
The domain that the publisher represents.
Type: [Identifier](API_Identifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** associationCount **   <a name="agentregistrycontrol-Type-PublisherSummary-associationCount"></a>
The number of registry records associated with the publisher, in any association status. Absent when the count isn't available.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** identifierType **   <a name="agentregistrycontrol-Type-PublisherSummary-identifierType"></a>
The type of the publisher's identifier. `DOMAIN` is the only supported value.
Type: String
Valid Values: `DOMAIN`
Required: No

 ** pendingAssociationApprovalCount **   <a name="agentregistrycontrol-Type-PublisherSummary-pendingAssociationApprovalCount"></a>
The number of the publisher's associations that are `PENDING_APPROVAL`. Absent when the count isn't available.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_PublisherSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/PublisherSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/PublisherSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/PublisherSummary)

---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awsshield.html
---

# Data retrieval APIs for AWS Shield
<a name="awsshield"></a>

AWS Shield provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="shield-DescribeAttack"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeAttack.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeAttack.html) | Get attack details. For getting attack details protected by AWS WAF anti-DDoS managed rule group, this action additionally calls wafv2:DescribeTopContributorsByEvent to retrieve application layer attack contributors, which requires to have wafv2:DescribeTopContributorsByEvent permission in IAM policy | Read |
| <a name="shield-DescribeAttackContributors"></a>[https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html) | Get detailed information about the contributors to a specific DDoS attack | Read |
| <a name="shield-DescribeAttackStatistics"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeAttackStatistics.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeAttackStatistics.html) | Describe information about the number and type of attacks AWS Shield has detected in the last year | Read |
| <a name="shield-DescribeDRTAccess"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeDRTAccess.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeDRTAccess.html) | Describe the current role and list of Amazon S3 log buckets used by the DDoS Response team to access your AWS account while assisting with attack mitigation | Read |
| <a name="shield-DescribeEmergencyContactSettings"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeEmergencyContactSettings.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeEmergencyContactSettings.html) | List the email addresses that the DRT can use to contact you during a suspected attack | Read |
| <a name="shield-DescribeProtection"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeProtection.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeProtection.html) | Get protection details | Read |
| <a name="shield-DescribeProtectionGroup"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeProtectionGroup.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeProtectionGroup.html) | Describe the specification for the specified protection group | Read |
| <a name="shield-DescribeSubscription"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeSubscription.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_DescribeSubscription.html) | Get subscription details, such as start time | Read |
| <a name="shield-GetGlobalThreatData"></a>[https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html) | Retrieve global threat intelligence data and trends from AWS Shield's threat monitoring systems | Read |
| <a name="shield-GetSubscriptionState"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_GetSubscriptionState.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_GetSubscriptionState.html) | Get subscription state | Read |
| <a name="shield-ListAttacks"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListAttacks.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListAttacks.html) | List all existing attacks | List |
| <a name="shield-ListMitigations"></a>[https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsshield.html) | Retrieve a list of mitigation actions that have been applied during DDoS attacks | List |
| <a name="shield-ListProtectionGroups"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListProtectionGroups.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListProtectionGroups.html) | Retrieve the protection groups for the account | List |
| <a name="shield-ListProtections"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListProtections.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListProtections.html) | List all existing protections | List |
| <a name="shield-ListResourcesInProtectionGroup"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListResourcesInProtectionGroup.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListResourcesInProtectionGroup.html) | Retrieve the resources that are included in the protection group | List |
| <a name="shield-ListTagsForResource"></a>[https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListTagsForResource.html](https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ListTagsForResource.html) | Get information about AWS tags for a specified Amazon Resource Name (ARN) in AWS Shield | Read |

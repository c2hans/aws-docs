---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_AccountEntityAggregate.html
---

# AccountEntityAggregate
<a name="API_AccountEntityAggregate"></a>

The number of entities in an account that are impacted by a specific event aggregated by the entity status codes.

## Contents
<a name="API_AccountEntityAggregate_Contents"></a>

 ** accountId **   <a name="AWSHealth-Type-AccountEntityAggregate-accountId"></a>
The 12-digit AWS account numbers that contains the affected entities.
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

 ** count **   <a name="AWSHealth-Type-AccountEntityAggregate-count"></a>
The number of entities that match the filter criteria for the specified events.
Type: Integer
Required: No

 ** statuses **   <a name="AWSHealth-Type-AccountEntityAggregate-statuses"></a>
The number of affected entities aggregated by the entity status codes.
Type: String to integer map
Valid Keys: `IMPAIRED | UNIMPAIRED | UNKNOWN | PENDING | RESOLVED`
Required: No

## See Also
<a name="API_AccountEntityAggregate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/AccountEntityAggregate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/AccountEntityAggregate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/AccountEntityAggregate)

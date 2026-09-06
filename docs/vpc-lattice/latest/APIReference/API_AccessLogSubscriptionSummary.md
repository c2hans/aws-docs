---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_AccessLogSubscriptionSummary.html
---

# AccessLogSubscriptionSummary
<a name="API_AccessLogSubscriptionSummary"></a>

Summary information about an access log subscription.

## Contents
<a name="API_AccessLogSubscriptionSummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-AccessLogSubscriptionSummary-arn"></a>
The Amazon Resource Name (ARN) of the access log subscription
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:accesslogsubscription/als-[0-9a-z]{17}`
Required: Yes

 ** createdAt **   <a name="vpclattice-Type-AccessLogSubscriptionSummary-createdAt"></a>
The date and time that the access log subscription was created, in ISO-8601 format.
Type: Timestamp
Required: Yes

 ** destinationArn **   <a name="vpclattice-Type-AccessLogSubscriptionSummary-destinationArn"></a>
The Amazon Resource Name (ARN) of the destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?`
Required: Yes

 ** id **   <a name="vpclattice-Type-AccessLogSubscriptionSummary-id"></a>
The ID of the access log subscription.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `als-[0-9a-z]{17}`
Required: Yes

 ** lastUpdatedAt **   <a name="vpclattice-Type-AccessLogSubscriptionSummary-lastUpdatedAt"></a>
The date and time that the access log subscription was last updated, in ISO-8601 format.
Type: Timestamp
Required: Yes

 ** resourceArn **   <a name="vpclattice-Type-AccessLogSubscriptionSummary-resourceArn"></a>
The Amazon Resource Name (ARN) of the service or service network.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 200.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc)|(resourceconfiguration/rcfg))-[0-9a-z]{17}`
Required: Yes

 ** resourceId **   <a name="vpclattice-Type-AccessLogSubscriptionSummary-resourceId"></a>
The ID of the service or service network.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 50.
Pattern: `((sn)|(svc))-[0-9a-z]{17}`
Required: Yes

 ** serviceNetworkLogType **   <a name="vpclattice-Type-AccessLogSubscriptionSummary-serviceNetworkLogType"></a>
Log type of the service network.
Type: String
Valid Values: `SERVICE | RESOURCE`
Required: No

## See Also
<a name="API_AccessLogSubscriptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/AccessLogSubscriptionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/AccessLogSubscriptionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/AccessLogSubscriptionSummary)

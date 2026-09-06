---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Finding.html
---

# Finding
<a name="API_Finding"></a>

Contains information about the finding that is generated when abnormal or suspicious activity is detected.

## Contents
<a name="API_Finding_Contents"></a>

 ** accountId **   <a name="guardduty-Type-Finding-accountId"></a>
The ID of the account in which the finding was generated.
Type: String
Required: Yes

 ** arn **   <a name="guardduty-Type-Finding-arn"></a>
The ARN of the finding.
Type: String
Required: Yes

 ** createdAt **   <a name="guardduty-Type-Finding-createdAt"></a>
The time and date when the finding was created.
Type: String
Required: Yes

 ** id **   <a name="guardduty-Type-Finding-id"></a>
The ID of the finding.
Type: String
Required: Yes

 ** region **   <a name="guardduty-Type-Finding-region"></a>
The Region where the finding was generated. For findings generated from [Global Service Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events), the Region value in the finding might differ from the Region where GuardDuty identifies the potential threat. For more information, see [How GuardDuty handles AWS CloudTrail global events](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html#cloudtrail_global) in the *Amazon GuardDuty User Guide*.
Type: String
Required: Yes

 ** resource **   <a name="guardduty-Type-Finding-resource"></a>
Contains information about the AWS resource associated with the activity that prompted GuardDuty to generate a finding.
Type: [Resource](API_Resource.md) object
Required: Yes

 ** schemaVersion **   <a name="guardduty-Type-Finding-schemaVersion"></a>
The version of the schema used for the finding.
Type: String
Required: Yes

 ** severity **   <a name="guardduty-Type-Finding-severity"></a>
The severity of the finding.
Type: Double
Required: Yes

 ** type **   <a name="guardduty-Type-Finding-type"></a>
The type of finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** updatedAt **   <a name="guardduty-Type-Finding-updatedAt"></a>
The time and date when the finding was last updated.
Type: String
Required: Yes

 ** associatedAttackSequenceArn **   <a name="guardduty-Type-Finding-associatedAttackSequenceArn"></a>
Amazon Resource Name (ARN) associated with the attack sequence finding.
Type: String
Required: No

 ** confidence **   <a name="guardduty-Type-Finding-confidence"></a>
The confidence score for the finding.
Type: Double
Required: No

 ** description **   <a name="guardduty-Type-Finding-description"></a>
The description of the finding.
Type: String
Required: No

 ** partition **   <a name="guardduty-Type-Finding-partition"></a>
The partition associated with the finding.
Type: String
Required: No

 ** service **   <a name="guardduty-Type-Finding-service"></a>
Contains additional information about the generated finding.
Type: [Service](API_Service.md) object
Required: No

 ** title **   <a name="guardduty-Type-Finding-title"></a>
The title of the finding.
Type: String
Required: No

## See Also
<a name="API_Finding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Finding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Finding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Finding)

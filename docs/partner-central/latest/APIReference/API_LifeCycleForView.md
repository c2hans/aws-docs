---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_LifeCycleForView.html
---

# LifeCycleForView
<a name="API_LifeCycleForView"></a>

 Provides the lifecycle view of an opportunity resource shared through a snapshot.

## Contents
<a name="API_LifeCycleForView_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** NextSteps **   <a name="AWSPartnerCentral-Type-LifeCycleForView-NextSteps"></a>
 Describes the next steps for the opportunity shared through a snapshot.
Type: String
Pattern: `(?s).{0,255}`
Required: No

 ** ReviewStatus **   <a name="AWSPartnerCentral-Type-LifeCycleForView-ReviewStatus"></a>
 Defines the approval status of the opportunity shared through a snapshot.
Type: String
Valid Values: `Pending Submission | Submitted | In review | Approved | Rejected | Action Required`
Required: No

 ** Stage **   <a name="AWSPartnerCentral-Type-LifeCycleForView-Stage"></a>
 Defines the current stage of the opportunity shared through a snapshot.
Type: String
Valid Values: `Prospect | Qualified | Technical Validation | Business Validation | Committed | Launched | Closed Lost`
Required: No

 ** TargetCloseDate **   <a name="AWSPartnerCentral-Type-LifeCycleForView-TargetCloseDate"></a>
 The projected launch date of the opportunity shared through a snapshot.
Type: String
Pattern: `[1-9][0-9]{3}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])`
Required: No

## See Also
<a name="API_LifeCycleForView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/LifeCycleForView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/LifeCycleForView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/LifeCycleForView)

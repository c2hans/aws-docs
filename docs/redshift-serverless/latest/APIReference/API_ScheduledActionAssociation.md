---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ScheduledActionAssociation.html
---

# ScheduledActionAssociation
<a name="API_ScheduledActionAssociation"></a>

Contains names of objects associated with a scheduled action.

## Contents
<a name="API_ScheduledActionAssociation_Contents"></a>

 ** namespaceName **   <a name="redshiftserverless-Type-ScheduledActionAssociation-namespaceName"></a>
Name of associated Amazon Redshift Serverless namespace.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

 ** scheduledActionName **   <a name="redshiftserverless-Type-ScheduledActionAssociation-scheduledActionName"></a>
Name of associated scheduled action.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 60.
Pattern: `[a-z0-9-]+`
Required: No

## See Also
<a name="API_ScheduledActionAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ScheduledActionAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ScheduledActionAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ScheduledActionAssociation)

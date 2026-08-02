---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AnalyticsDataAssociationResult.html
---

# AnalyticsDataAssociationResult
<a name="API_AnalyticsDataAssociationResult"></a>

This API is in preview release for Connect Customer and is subject to change.

Information about associations that are successfully created: `DataSetId`, `TargetAccountId`, `ResourceShareId`, `ResourceShareArn`.

## Contents
<a name="API_AnalyticsDataAssociationResult_Contents"></a>

 ** DataSetId **   <a name="connect-Type-AnalyticsDataAssociationResult-DataSetId"></a>
The identifier of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** ResourceShareArn **   <a name="connect-Type-AnalyticsDataAssociationResult-ResourceShareArn"></a>
The Amazon Resource Name (ARN) of the AWS Resource Access Manager share.
Type: String
Required: No

 ** ResourceShareId **   <a name="connect-Type-AnalyticsDataAssociationResult-ResourceShareId"></a>
The AWS Resource Access Manager share ID.
Type: String
Required: No

 ** ResourceShareStatus **   <a name="connect-Type-AnalyticsDataAssociationResult-ResourceShareStatus"></a>
The AWS Resource Access Manager status of association.
Type: String
Required: No

 ** TargetAccountId **   <a name="connect-Type-AnalyticsDataAssociationResult-TargetAccountId"></a>
The identifier of the target account.
Type: String
Required: No

## See Also
<a name="API_AnalyticsDataAssociationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AnalyticsDataAssociationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AnalyticsDataAssociationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AnalyticsDataAssociationResult)

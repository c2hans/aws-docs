---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ManagedWorkgroupListItem.html
---

# ManagedWorkgroupListItem
<a name="API_ManagedWorkgroupListItem"></a>

A collection of Amazon Redshift compute resources managed by AWS Glue.

## Contents
<a name="API_ManagedWorkgroupListItem_Contents"></a>

 ** creationDate **   <a name="redshiftserverless-Type-ManagedWorkgroupListItem-creationDate"></a>
The creation date of the managed workgroup.
Type: Timestamp
Required: No

 ** managedWorkgroupId **   <a name="redshiftserverless-Type-ManagedWorkgroupListItem-managedWorkgroupId"></a>
The unique identifier of the managed workgroup.
Type: String
Required: No

 ** managedWorkgroupName **   <a name="redshiftserverless-Type-ManagedWorkgroupListItem-managedWorkgroupName"></a>
The name of the managed workgroup.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_:\-]+`
Required: No

 ** sourceArn **   <a name="redshiftserverless-Type-ManagedWorkgroupListItem-sourceArn"></a>
The Amazon Resource Name (ARN) for the managed workgroup in the AWS Glue Data Catalog.
Type: String
Pattern: `arn:aws[a-z-]*:glue:[a-z0-9-]+:\d+:(database|catalog)[a-z0-9-:]*(?:/[A-Za-z0-9-_]{1,255})*`
Required: No

 ** status **   <a name="redshiftserverless-Type-ManagedWorkgroupListItem-status"></a>
The status of the managed workgroup.
Type: String
Valid Values: `CREATING | DELETING | MODIFYING | AVAILABLE | NOT_AVAILABLE`
Required: No

## See Also
<a name="API_ManagedWorkgroupListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ManagedWorkgroupListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ManagedWorkgroupListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ManagedWorkgroupListItem)

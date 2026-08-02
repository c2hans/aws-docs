---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TimeToLiveDescription.html
---

# TimeToLiveDescription
<a name="API_TimeToLiveDescription"></a>

The description of the Time to Live (TTL) status on the specified table.

## Contents
<a name="API_TimeToLiveDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AttributeName **   <a name="DDB-Type-TimeToLiveDescription-AttributeName"></a>
 The name of the TTL attribute for items in the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** TimeToLiveStatus **   <a name="DDB-Type-TimeToLiveDescription-TimeToLiveStatus"></a>
 The TTL status for the table.
Type: String
Valid Values: `ENABLING | DISABLING | ENABLED | DISABLED`
Required: No

## See Also
<a name="API_TimeToLiveDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/TimeToLiveDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/TimeToLiveDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/TimeToLiveDescription)

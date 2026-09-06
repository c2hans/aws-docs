---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TimeToLiveSpecification.html
---

# TimeToLiveSpecification
<a name="API_TimeToLiveSpecification"></a>

Represents the settings used to enable or disable Time to Live (TTL) for the specified table.

## Contents
<a name="API_TimeToLiveSpecification_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AttributeName **   <a name="DDB-Type-TimeToLiveSpecification-AttributeName"></a>
The name of the TTL attribute used to store the expiration time for items in the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Enabled **   <a name="DDB-Type-TimeToLiveSpecification-Enabled"></a>
Indicates whether TTL is to be enabled (true) or disabled (false) on the table.
Type: Boolean
Required: Yes

## See Also
<a name="API_TimeToLiveSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/TimeToLiveSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/TimeToLiveSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/TimeToLiveSpecification)

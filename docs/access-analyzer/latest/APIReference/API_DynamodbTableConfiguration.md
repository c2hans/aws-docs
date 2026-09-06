---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_DynamodbTableConfiguration.html
---

# DynamodbTableConfiguration
<a name="API_DynamodbTableConfiguration"></a>

The proposed access control configuration for a DynamoDB table or index. You can propose a configuration for a new DynamoDB table or index or an existing DynamoDB table or index that you own by specifying the policy for the DynamoDB table or index. For more information, see [PutResourcePolicy](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutResourcePolicy.html).
+ If the configuration is for an existing DynamoDB table or index and you do not specify the DynamoDB policy, then the access preview uses the existing DynamoDB policy for the table or index.
+ If the access preview is for a new resource and you do not specify the policy, then the access preview assumes a DynamoDB table without a policy.
+ To propose deletion of an existing DynamoDB table or index policy, you can specify an empty string for the DynamoDB policy.

## Contents
<a name="API_DynamodbTableConfiguration_Contents"></a>

 ** tablePolicy **   <a name="accessanalyzer-Type-DynamodbTableConfiguration-tablePolicy"></a>
The proposed resource policy defining who can access or manage the DynamoDB table.
Type: String
Required: No

## See Also
<a name="API_DynamodbTableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/DynamodbTableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/DynamodbTableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/DynamodbTableConfiguration)
